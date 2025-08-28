from flask import Flask, render_template, request, jsonify
import re
from scanner import scan_ports, arp_scan, generate_report

app = Flask(__name__)

def validate_ip(ip):
    """Valida que la IP sea correcta."""
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(pattern, ip))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    try:
        target_ip = request.form.get("ip")
        port_start = int(request.form.get("port_start", 1))
        port_end = int(request.form.get("port_end", 100))
        network = request.form.get("network", target_ip + "/24")

        # Validaciones
        if not validate_ip(target_ip):
            return jsonify({"error": "IP inválida"}), 400
        if not (1 <= port_start <= 65535 and 1 <= port_end <= 65535):
            return jsonify({"error": "Los puertos deben estar entre 1 y 65535"}), 400
        if port_start > port_end:
            return jsonify({"error": "El puerto inicial debe ser menor o igual al puerto final"}), 400

        port_results = scan_ports(target_ip, (port_start, port_end))
        devices = arp_scan(network)
        report = generate_report(target_ip, port_results, devices)
        return jsonify(report)
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Error en el escaneo: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)