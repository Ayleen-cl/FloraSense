<h1 align="center">🌱 FloraSense</h1>
<p align="center"><b>Sistema IoT Inteligente para el Monitoreo y Automatización de Plantas de Interior</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/UNIVERSIDAD_DE_TARAPACA-Arica%2C_Chile-blueviolet?style=for-the-badge" alt="Universidad de Tarapacá">
  <img src="https://img.shields.io/badge/ESTADO-EN_DESARROLLO-success?style=for-the-badge" alt="Estado">
</p>

---

## 🌸 Sobre el Proyecto

**FloraSense** es una solución inteligente basada en Internet de las Cosas (IoT) diseñada para automatizar el cuidado de plantas de interior. El sistema monitorea en tiempo real las condiciones del suelo y del ambiente mediante una **Raspberry Pi 4**, ejecutando riegos automáticos y activando luces de cultivo cuando es necesario. 

Además, cuenta con una aplicación móvil para supervisión y control remoto, y un prototipo virtual interactivo desarrollado en **Unity** y visualizado con **Meta Quest 3** para la validación espacial.

---

## 🛠️ Componentes y Tecnologías

* **Cerebro:** Raspberry Pi 4 Modelo B + Chip MCP3008 (Conversor A/D).
* **Sensores:** Higrómetro capacitivo (suelo), sensor LDR (luz), DHT11 (temperatura y humedad ambiente) y sensor de nivel de agua.
* **Actuadores:** Mini bomba sumergible (5V), módulo relé y luces LED de cultivo.
* **Realidad Virtual:** Entorno 3D interactivo en Unity compatible con Meta Quest 3.

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,unity,raspberrypi,git,github,vscode" alt="Tecnologías FloraSense"/>
</p>

---

## 📊 Estadísticas del Repositorio

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=AyleenHumire&repo=FloraSense&theme=radical&hide_border=true" alt="FloraSense Stats"/>
</p>

---

## 📁 Estructura del Repositorio

```text
FloraSense/
│
├── 📂 hardware/           # Esquemas de circuitos y conexiones
├── 📂 software/           # Código fuente en Python para la Raspberry Pi
├── 📂 virtual_model/      # Escenas y recursos del prototipo en Unity
├── 📂 docs/               # Informes y manuales del proyecto
└── 📄 README.md           # Documentación principal
