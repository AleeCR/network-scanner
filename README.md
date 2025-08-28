# Network Scanner and Analyzer 🌐🔍

## Descripción 📝

**Network Scanner and Analyzer** es una herramienta desarrollada en **Python** con una interfaz web (usando **Flask**, **HTML**, **CSS**, y **JavaScript**) que permite escanear puertos abiertos en una red y detectar dispositivos conectados mediante ARP. Este proyecto, diseñado con fines educativos y éticos, es ideal para identificar posibles vulnerabilidades (como puertos abiertos) y detectar dispositivos no autorizados (como en entornos IoT o Wi-Fi) 📡. Incluye una interfaz web intuitiva que muestra los resultados en tablas con un mensaje de "Escaneando..." durante el proceso.

Este proyecto fue creado como parte de mi portafolio de último año en Ingeniería de Telecomunicaciones 🎓, con un enfoque en ciberseguridad 🔒. Demuestra habilidades en análisis de redes, programación en Python, desarrollo web y diseño de interfaces seguras.

**⚠️ Disclaimer ético**: Este proyecto debe usarse **solo en redes donde tengas permiso explícito**. Todas las pruebas se realizaron en un entorno controlado y autorizado.

## Funcionalidades ✨

- **Escaneo de puertos TCP** 🔎: Escanea un rango de puertos (1-65535) en una IP específica para identificar puertos abiertos o cerrados.
- **Detección de dispositivos** 📱: Usa ARP para descubrir dispositivos en la red, mostrando sus direcciones IP y MAC.
- **Generación de reportes** 📊: Produce reportes en JSON con información sobre puertos, dispositivos y alertas de seguridad (ej. puertos vulnerables como 22, 80, 443).
- **Interfaz web** 🌐: Una interfaz responsiva (Flask, HTML, CSS, JavaScript) que permite iniciar escaneos y visualizar resultados en tablas, con un mensaje de "Escaneando..." durante el proceso.
- **Validaciones** ✅: Incluye validaciones para IPs y rangos de puertos, con manejo de errores claro en la interfaz.

## Tecnologías utilizadas 🛠️

- **Python**: Scapy (para escaneo de red), Flask (para la API y servidor web), pandas (para análisis de datos).
- **JavaScript**: Manejo dinámico de la interfaz y resultados en el navegador.
- **HTML/CSS**: Diseño responsivo y atractivo para la interfaz web.
- **JSON**: Formato para reportes y comunicación entre el backend y frontend.

## Requisitos 📋

- **Python 3.8+** 
- **Dependencias**: `scapy`, `flask`, `pandas` (instalar con `pip install scapy flask pandas`).
- **Permisos de administrador** 🔑:
  - Linux/Mac: Requiere `sudo` para el escaneo ARP con Scapy.
  - Windows: Requiere Npcap (descargar desde [npcap.com](https://npcap.com/)) y ejecutar como administrador.
- **Entorno de prueba** 🧪: Usa una red autorizada (ej. tu red Wi-Fi) o un laboratorio virtual (VirtualBox, Kali Linux, GNS3).

## Instalación 🚀

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/network-scanner.git
   cd network-scanner
   ```

2. **Instala las dependencias**:
   ```bash
   pip install scapy flask pandas
   ```

3. **(Windows) Instala Npcap**:
   - Descarga e instala Npcap desde [npcap.com](https://npcap.com/) con la opción “WinPcap API-compatible mode”.

4. **Configura el entorno de prueba**:
   - Identifica la IP de tu red (ej. `192.168.1.1` para tu router) y el rango de red (ej. `192.168.1.0/24`).
   - Usa un laboratorio virtual (Kali Linux en VirtualBox) para pruebas seguras.

## Uso 🖥️

### Opción 1: Script independiente (`scanner.py`)
1. Edita `scanner.py` para configurar la IP objetivo y el rango de red:
   ```python
   target_ip = "192.168.1.1"  # Cambia a tu IP objetivo
   network = "192.168.1.0/24"  # Cambia a tu rango de red
   port_range = (1, 100)  # Ajusta el rango de puertos
   ```
2. Ejecuta el script:
   - Linux/Mac: `sudo python3 scanner.py`
   - Windows (como administrador): `python scanner.py`
3. Revisa el reporte generado en `scan_report.json`.

### Opción 2: Interfaz web (`app.py`)
1. Ejecuta la aplicación Flask:
   - Linux/Mac: `sudo python3 app.py`
   - Windows (como administrador): `python app.py`
2. Abre un navegador y ve a `http://localhost:5000` 🌐.
3. Ingresa la IP objetivo (ej. `192.168.1.1`), el rango de puertos (ej. `1` a `100`), y haz clic en “Escanear” 🔍.
4. Observa el mensaje “Escaneando...” y los resultados en tablas (puertos y dispositivos).

## Estructura del proyecto 📂

```
network-scanner/
├── scanner.py           # Lógica de escaneo de puertos y detección de dispositivos
├── app.py              # Servidor Flask con API y renderizado de la interfaz
├── templates/
│   └── index.html      # Interfaz web con formulario y tablas
├── static/
│   └── styles.css      # Estilos CSS para la interfaz
├── scan_report.json    # Reporte generado por scanner.py (opcional)
```

## Ejemplo de resultados 📈

- **Puertos abiertos**:
  ```
  IP: 192.168.1.1, Puerto: 80, Estado: open, Alerta: Puerto 80 abierto - potencialmente vulnerable
  IP: 192.168.1.1, Puerto: 443, Estado: open, Alerta: Puerto 443 abierto - potencialmente vulnerable
  ```
- **Dispositivos detectados**:
  ```
  IP: 192.168.1.100, MAC: 00:14:22:01:23:45
  IP: 192.168.1.101, MAC: 00:16:17:2A:3B:4C
  ```

## Capturas de pantalla 📷

- Formulario de escaneo: ![Formulario](screenshots/formulario.png)
- Mensaje de carga: ![Escaneando](screenshots/escaneando.png)
- Resultados: ![Resultados](screenshots/resultados.png)

## Caso de uso 🌍

Este proyecto fue utilizado para auditar una red Wi-Fi local, identificando puertos abiertos en un router (como 80 y 443) y detectando dispositivos IoT no autorizados. Las alertas generadas ayudaron a recomendar configuraciones seguras, como cerrar puertos innecesarios, fortaleciendo la seguridad de la red.

## Notas importantes ⚠️

- **Uso ético**: Este proyecto está diseñado para fines educativos y debe usarse solo en redes donde tengas permiso explícito. Cualquier uso no autorizado es ilegal.
- **Limitaciones**: El escaneo de puertos grandes (ej. 1-65535) puede ser lento; usa rangos pequeños para pruebas iniciales.
- **Entornos soportados**: Probado en Linux (Ubuntu, Kali) y Windows con Npcap.

## Futuras mejoras 🚧

- Añadir soporte para escaneo de puertos UDP.
- Integrar gráficos interactivos con Chart.js para visualizar estadísticas de red 📊.
- Implementar detección de anomalías (ej. tráfico inusual).
- Generar reportes en PDF con ReportLab 📄.
- Añadir autenticación a la interfaz web con Flask-Login 🔒.

## Contribuir 🤝

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto, por favor sigue estos pasos:
1. Haz un **fork** del repositorio.
2. Crea una nueva rama (`git checkout -b mejora-nueva-funcionalidad`).
3. Realiza tus cambios y haz **commit** (`git commit -m "Añadir nueva funcionalidad"`).
4. Sube tus cambios (`git push origin mejora-nueva-funcionalidad`).
5. Abre un **Pull Request** con una descripción clara de tus mejoras.

