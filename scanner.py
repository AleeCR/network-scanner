import scapy.all as scapy
import socket
import json
from datetime import datetime

def scan_port(ip, port, timeout=1):
    """Escanea un puerto TCP específico en una IP."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return {"port": port, "status": "abierto" if result == 0 else "cerrado"}
    except Exception as e:
        return {"port": port, "status": "error", "error": str(e)}

def scan_ports(ip, port_range=(1, 100)):
    """Escanea un rango de puertos en una IP."""
    results = []
    start_port, end_port = port_range
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        raise ValueError("El rango de puertos debe estar entre 1 y 65535")
    if start_port > end_port:
        raise ValueError("El puerto inicial debe ser menor o igual al puerto final")
    
    for port in range(start_port, end_port + 1):
        result = scan_port(ip, port)
        results.append(result)  # Guardamos todos los resultados, no solo los puertos abiertos
    return results

def arp_scan(network):
    """Escanea la red usando ARP para detectar dispositivos."""
    try:
        arp_request = scapy.ARP(pdst=network)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

        devices = []
        for element in answered_list:
            device = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            devices.append(device)
        return devices
    except Exception as e:
        return [{"error": f"Error en ARP scan: {str(e)}"}]

def generate_report(ip, port_results, devices):
    """Genera un reporte JSON con los resultados."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "target_ip": ip,
        "ports": port_results,
        "devices": devices,
        "alerts": []
    }
    # Ejemplo de alerta: puertos comúnmente vulnerables
    vulnerable_ports = [22, 80, 443, 3389]
    for port in port_results:
        if port["status"] == "open" and port["port"] in vulnerable_ports:
            report["alerts"].append(f"Puerto {port['port']} abierto - potencialmente vulnerable")
    return report

if __name__ == "__main__":
    # Ejemplo de uso (cambiar a tu red y rango de puertos)
    target_ip = "192.168.1.43"  # Cambia a la IP de tu red
    network = "192.168.1.0/24"  # Cambia a tu rango de red
    port_range = (1, 100)  # Escanea los primeros 100 puertos

    try:
        print(f"Escaneando puertos en {target_ip}...")
        port_results = scan_ports(target_ip, port_range)
        print(f"Detectando dispositivos en {network}...")
        devices = arp_scan(network)
        report = generate_report(target_ip, port_results, devices)

        with open("scan_report.json", "w") as f:
            json.dump(report, f, indent=4)
        print("Reporte generado en scan_report.json")
    except Exception as e:
        print(f"Error: {str(e)}")