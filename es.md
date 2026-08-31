---
charset: utf-8
layout: default
title: ReefTech Project Ecosystem
theme: jekyll-theme-cayman
lang: es
---

{% include language-selector.html %}

# Mis herramientas ReefTank

Bienvenido a la documentación de mis proyectos para acuarios de arrecife.

<video src="assets/videos/logo_v1.mp4" 
       poster="image-de-remplacement.jpg"
       autoplay 
       loop 
       muted 
       playsinline 
       style="width:100%; border-radius: 8px;height: 390px;object-fit: cover;">
</video>

{% include toc-generator.html %}

* Table of Contents / Sommaire
{:toc}


---

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Integraciones y tarjetas Home Assistant

---

### Integraciones

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Integración local para el ecosistema Red Sea ReefBeat.**

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Gestiona tus dispositivos Red Sea ReefBeat **localmente** (sin cloud): ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, ReefMat, ReefRun y ReefWave.

> ⚠️ Este no es un repositorio oficial de Red Sea. Uso bajo tu propia responsabilidad.

**Funciones principales:**
- **Control 100% local** — sin dependencia del cloud para la mayoría de dispositivos
- Detección automática de dispositivos en la red local (con modo manual y soporte de subredes)
- Iconos personalizados para todos los dispositivos ReefBeat
- Notificaciones de actualización de firmware (con Cloud API opcional)
- Modo de actualización en tiempo real de la configuración
- Soporte multilingüe

<!-- generated:beat-devices:start -->

**Dispositivos soportados:**

> ✅ Soportado &nbsp;|&nbsp; 🚧 En curso &nbsp;|&nbsp; 🧪 Sin probar (puede funcionar) &nbsp;|&nbsp; ❌ Aún no soportado

| Dispositivo | Modelos | Estado |
|------|------|------|
| **ReefATO+** | RSATO+ | ✅ |
| **ReefControl** | RSCONTROLPRO | ✅ |
| **ReefControl** | RSCONTROLLITE | 🧪 |
| **ReefControl-Power** | RSPOWER6 | ✅ |
| **ReefControl-Power** | RSPOWER8 | 🧪 |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115) | ✅ |
| **ReefLed** | G2 (RSLED170) | 🧪 |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ |
| **ReefRun** | RSRUN | ✅ |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ |

<!-- generated:beat-devices:end -->

**Particularidades de ReefWave:** ReefWave es el único dispositivo vinculado al cloud de ReefBeat. Tres modos de operación están disponibles — Cloud, Local e Híbrido — para que elijas el equilibrio entre control local total y sincronización con la app móvil ReefBeat.

**Instalación:** Disponible directamente en [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — busca "redsea" o "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Control de bombas Aqua Medic vía Home Assistant mediante la API cloud Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Controla tus bombas Aqua Medic desde Home Assistant vía la API cloud Gizwits (mismo backend que la app oficial de Aqua Medic).

<!-- generated:aqua-devices:start -->

**Dispositivos soportados:**

> ✅ Soportado &nbsp;|&nbsp; 🚧 En curso &nbsp;|&nbsp; 🧪 Sin probar (puede funcionar) &nbsp;|&nbsp; ❌ Aún no soportado

| Dispositivo | Estado |
|------|------|
| **EcoDrift / SmartDrift x.1 / x.3** (de movimiento) | ✅ |
| **DC Runner x.1 / x.2 / x.3** (bomba de retorno) | ✅ |
| **DC Runner** (bomba de skimmer) | ✅ |
| **Reefdoser EVO** (bomba dosificadora) | ❌ — [Solicitarlo](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (controlador de temperatura) | ❌ — [Solicitarlo](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (iluminación) | ❌ — [Solicitarlo](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

<!-- generated:aqua-devices:end -->

**Funciones EcoDrift / SmartDrift:**
- Encendido/apagado, tipo de onda (Pulso/Marea), modo alimentación, temporizador, modo control 0-10V
- Modos de onda: Clásico, Sinusoidal, Aleatorio, Flujo constante
- Enlace: Independiente, Maestro, Esclavo
- Control de caudal, frecuencia y duración de alimentación
- Sensores de diagnóstico completos (sobrecorriente, sobretensión, sobretemperatura, rotor bloqueado, marcha en seco, UART)

**Funciones DC Runner:**
- Encendido/apagado, modo alimentación (pausa 10 min), modo control 0-10V
- Control de caudal (30–100%)
- Sensores de diagnóstico (marcha en seco, rotor bloqueado, tensión)

**Instalación:** En HACS, añade `https://github.com/Elwinmage/ha-aquamedic-component` como repositorio personalizado (Integración), luego busca "Aqua Medic".

---

<!-- generated:maintenance:start -->

#### 🧰 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Seguimiento de mantenimiento para equipos que Home Assistant no alcanza.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Bombas de movimiento, bombas de retorno, skimmers, reactores — todo lo que limpia a mano. Una entrada por marca, un dispositivo por equipo, cuatro entidades por tarea: un botón que registra el trabajo, un número para el intervalo, un interruptor para silenciar los avisos y una fecha para retrodatar la última intervención.

**Funciones principales:**

- Preajustes para Tunze, Jebao y equipos genéricos, con los intervalos del fabricante cuando los publica
- Una biblioteca común de 17 tareas, traducida a 8 idiomas
- Retrodatación, para que un equipo nuevo no empiece en «nunca hecho»
- Servicio `reef_maintenance.reset` — pegue una etiqueta NFC en la bomba y escanéela al terminar
- Mismo contrato `reef_role` que las integraciones conectadas: las tareas aparecen en la vista de mantenimiento de la tarjeta

**Instalación:** En HACS, añada `https://github.com/Elwinmage/ha-reef-maintenance-component` como repositorio personalizado (Integración).

<!-- generated:maintenance:end -->

---

### Tarjetas

#### 🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)

**Tarjeta Lovelace personalizada para paneles de arrecife.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Lit](https://img.shields.io/badge/Lit-3.3-blue?style=flat-square&logo=lit)](https://lit.dev/)

La **Reef Card** para Home Assistant te ayuda a gestionar tu acuario de arrecife directamente desde tu panel. Combinada con [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component), detecta y soporta automáticamente tus dispositivos Red Sea (ReefBeat).

> Los dispositivos no-Redsea también pueden ser soportados — [solicítalo aquí](https://github.com/Elwinmage/ha-reef-card/discussions/2).

<!-- generated:card-devices:start -->

**Dispositivos soportados:**

> ✅ Soportado &nbsp;|&nbsp; 🚧 En curso &nbsp;|&nbsp; 🧪 Sin probar (puede funcionar) &nbsp;|&nbsp; ❌ Aún no soportado

| Dispositivo | Estado | Puntos fuertes |
|------|------|------|
| **ReefDose (RSDOSE2/4)** | ✅ | Planificación completa, dosificación manual, cebado y calibración, gestión de suplementos, seguimiento de uso |
| **ReefMat (RSMAT250/500/1200)** | ✅ | Estado del rollo animado, avance manual/automático/programado, estado del sensor, gráficos semanales y mensuales |
| **ReefRun (RSRUN)** | ✅ | Control de velocidad de bomba, editor de programas, gestión del sobreespumado |
| **ReefATO+** | ✅ | Nivel de agua, sonda de fugas, diagnóstico de bomba, gráfico de consumo, zumbador de fuga |
| **ReefControl-Power (RSPOWER6/8)** | 🚧 | Control por toma |
| **ReefControl (RSCONTROLPRO/LITE)** | ❌ | [Votar por prioridad](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed (G1/G2)** | ❌ | [Votar por prioridad](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ | [Votar por prioridad](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic EcoDrift / SmartDrift** | ❌ | [Votar por prioridad](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic DC Runner (return, skimmer)** | ❌ | [Votar por prioridad](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

<!-- generated:card-devices:end -->

**Destacados ReefDose:**
- Tarjeta de 6 zonas: config/WiFi, estados, dosificación manual con atajos, planificación por cabezal con progreso circular, gestión de suplementos con imágenes de marcas, y cola de próximas dosis
- Soporte de flujos de cebado y calibración
- Biblioteca de suplementos con imágenes para Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest y más

**Destacados ReefMat:**
- Tarjeta de 7 zonas con fondo animado que cambia según el uso del rollo (0%–100%)
- Info en tiempo real del rollo: longitud restante, media diaria, días restantes estimados
- Controles de avance manual, automático y programado
- Visualización del estado del sensor de nivel (conectado, desconectado, sucio)
- Gráficos de consumo semanal y mensal

**Instalación:** Disponible directamente en [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) — busca "reef-card".

**Configuración:** Sin el parámetro `device`, la tarjeta detecta automáticamente todos los dispositivos ReefBeat y te permite elegir. Establece el parámetro `device` para forzar un dispositivo específico.

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Demo ReefDose" width="300"/></a><br/><em>Demo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Demo ReefMat" width="300"/></a><br/><em>Demo ReefMat</em></td>
</tr>
</table>

---

## 🔌 Infraestructura

---

#### ⚡ [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup)

**Sistema autónomo de respaldo con batería para acuarios de arrecife Red Sea.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Mantén tus ReefWave, ReefRun y DC Skimmer funcionando durante cortes de luz con una batería LiFePO₄ 24V, una Raspberry Pi y degradación inteligente de bombas.

<img src="https://github.com/Elwinmage/reefbeatEnergyBackup/raw/main/docs/images/power-flow-card.png" />

**Funciones principales:**
- **Monitoreo de batería** vía INA226 (I2C) + cargador Victron BLE opcional
- **Detección instantánea** de cortes mediante relé 230V en GPIO
- **Degradación progresiva** de bombas — niveles SoC calculados desde una autonomía objetivo
- **Failover de red 3 niveles** — Ethernet → Wi-Fi → hotspot espejo autónomo
- **Failover 4G/LTE** — notificaciones y acceso cloud ReefBeat vía módem USB o tethering
- **Notificaciones push** vía [ntfy.sh](https://ntfy.sh) (gratis, sin cuenta)
- **Integración Home Assistant** — auto-discovery MQTT, entidad de actualización, blueprint de test
- **Auto-actualización** — verifica GitHub, botón "Instalar" en HA

**Niveles de hardware:**

| Nivel | Lo que obtienes | Presupuesto |
|-------|----------------|-------------|
| **1 — Básico** | Batería + cables, respaldo pasivo | ~290 € |
| **2 — Normal** *(recomendado)* | + RPi + INA226 + relé, monitoreo & automatización | ~402 € |
| **3 — Avanzado** | + Cargador Victron BLE, disyuntor conectado, módem 4G | ~627 € |

**Instalación:**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

> Funciona independientemente o como complemento de [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) para una gestión de arrecife completamente integrada.

---

<!-- generated:blueprints:start -->

#### 🔔 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Blueprints de notificación para todo el ecosistema.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Le avisa en el móvil de los mantenimientos vencidos, encontrados por el atributo común `reef_role` de modo que todas las integraciones quedan cubiertas, y de los dispositivos que dejaron de responder. Ocho idiomas, un botón de importación cada uno.

**Instalación:** importe desde el repositorio, un botón por idioma.

<!-- generated:blueprints:end -->

---

## 📐 Modelos 3D

### ReefRun DC Skimmer
#### 📦 [*Herramienta para impulsor de skimmer DC Red Sea*](https://www.thingiverse.com/thing:7313258)


<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer id="aquarium-model"
                src="assets/models/redsea-key.glb"
                alt="Llave Red Sea 3D"
                camera-controls
                auto-rotate
                ar
                shadow-intensity="1"
                style="width: 100%; height: 100%; display: block;"
                exposure="1">
  </model-viewer>
</div>

<script>
  const modelViewer = document.querySelector("#aquarium-model");
  modelViewer.addEventListener("load", () => {
    const width = modelViewer.clientWidth;
    const height = modelViewer.clientHeight;
    if (width === 0 || height === 0) {
        modelViewer.style.width = "100%";
        modelViewer.style.height = "500px";
    }
  });
</script>

**Demostración en video:**
<video width="100%" height="auto" controls poster="assets/models/redsea-key.png" style="border-radius: 8px; margin: 20px 0; background: #000;">
  <source src="assets/videos/redsea_skimmer.webm" type="video/webm">
  <source src="assets/videos/logo_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

<!-- generated:contact:start -->

## 💬 Contacto y soporte

- **Preguntas y peticiones de funciones:** abra una discusión en el proyecto correspondiente — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues)
- **Informes de errores:** abra una issue en ese mismo proyecto, con los detalles.
- **Apoyar el proyecto:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)

<!-- generated:contact:end -->
