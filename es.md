---
layout: default
title: Elwinmage - Proyectos Reef Tech
theme: jekyll-theme-cayman
---


# 🌍 [🇺🇸](index.md) / [🇫🇷](fr.md) / [🇩🇪](de.md) / [🇪🇸] / [🇮🇹](it.md) / [🇵🇱](pl.md) / [🇵🇹](pt.md)

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

Gestiona tus dispositivos Red Sea ReefBeat **localmente** (sin cloud): ReefATO+, ReefDose, ReefLed, ReefMat, ReefRun y ReefWave.

> ⚠️ Este no es un repositorio oficial de Red Sea. Uso bajo tu propia responsabilidad.

**Funciones principales:**
- **Control 100% local** — sin dependencia del cloud para la mayoría de dispositivos
- Detección automática de dispositivos en la red local (con modo manual y soporte de subredes)
- Iconos personalizados para todos los dispositivos ReefBeat
- Notificaciones de actualización de firmware (con Cloud API opcional)
- Modo de actualización en tiempo real de la configuración
- Soporte multilingüe

**Dispositivos soportados:**

| Dispositivo | Modelos | Estado |
|-------------|---------|--------|
| **ReefATO+** | RSATO+ | ✅ Probado |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ Probado |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115/170) | ✅ Probado |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ Probado |
| **ReefRun** | RSRUN | ✅ Probado |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ / ☑️ |
| **ReefControl** | RSSENSE | ❌ Aún no — [contáctame](https://github.com/Elwinmage/ha-reefbeat-component/discussions/8) |

**Particularidades de ReefWave:** ReefWave es el único dispositivo vinculado al cloud de ReefBeat. Tres modos de operación están disponibles — Cloud, Local e Híbrido — para que elijas el equilibrio entre control local total y sincronización con la app móvil ReefBeat.

**Instalación:** Disponible directamente en [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — busca "redsea" o "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Control de bombas Aqua Medic vía Home Assistant mediante la API cloud Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Controla tus bombas Aqua Medic desde Home Assistant vía la API cloud Gizwits (mismo backend que la app oficial de Aqua Medic).

**Dispositivos soportados:**

| Dispositivo | Estado |
|-------------|--------|
| **EcoDrift / SmartDrift x.1 / x.3** (bomba de olas) | ✅ Soportado |
| **DC Runner x.1 / x.2 / x.3** (bomba de retorno) | 🧪 Sin probar |
| **Reefdoser EVO** (bomba dosificadora) | ❌ Aún no — [contáctame](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (controlador de temperatura) | ❌ Aún no — [contáctame](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (iluminación) | ❌ Aún no — [contáctame](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

**Funciones EcoDrift / SmartDrift:**
- Encendido/apagado, tipo de ola (Pulso/Marea), modo alimentación, temporizador, modo control 0-10V
- Modos de ola: Clásico, Sinusoidal, Aleatorio, Flujo constante
- Enlace: Independiente, Maestro, Esclavo
- Control de caudal, frecuencia y duración de alimentación
- Sensores de diagnóstico completos (sobrecorriente, sobretensión, sobretemperatura, rotor bloqueado, marcha en seco, UART)

**Funciones DC Runner:**
- Encendido/apagado, modo alimentación (pausa 10 min), modo control 0-10V
- Control de caudal (30–100%)
- Sensores de diagnóstico (marcha en seco, rotor bloqueado, tensión)

**Instalación:** En HACS, añade `https://github.com/Elwinmage/ha-aquamedic-component` como repositorio personalizado (Integración), luego busca "Aqua Medic".

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

**Dispositivos soportados:**

| Dispositivo | Estado | Destacados |
|-------------|--------|------------|
| **ReefDose** (RSDOSE2/4) | ✅ Implementado | Planificación completa, dosificación manual, cebado/calibración, gestión de suplementos, seguimiento de uso |
| **ReefMat** (RSMAT250/500/1200) | ✅ Implementado | Estado del rollo animado, avance manual/auto/programado, estado del sensor, gráficos semanales/mensuales |
| **ReefRun** (RSRUN) | ☑️ En progreso | Control de velocidad de bomba, gestión de sobreespumado |
| **ReefATO+** | ❌ Planificado | [Votar por prioridad](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed** (G1/G2) | ❌ Planificado | [Votar por prioridad](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ Planificado | [Votar por prioridad](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

**Destacados ReefDose:**
- Tarjeta de 6 zonas: config/WiFi, estados, dosificación manual con atajos, planificación por cabezal con progreso circular, gestión de suplementos con imágenes de marcas, y cola de próximas dosis
- Soporte de flujos de cebado y calibración
- Biblioteca de suplementos con imágenes para Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest y más

**Destacados ReefMat:**
- Tarjeta de 7 zonas con fondo animado que cambia según el uso del rollo (0%–100%)
- Info en tiempo real del rollo: longitud restante, media diaria, días restantes estimados
- Controles de avance manual, automático y programado
- Visualización del estado del sensor de nivel (conectado, desconectado, sucio)
- Gráficos de consumo semanal y mensual

**Instalación:** Disponible directamente en [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) — busca "reef-card".

**Configuración:** Sin el parámetro `device`, la tarjeta detecta automáticamente todos los dispositivos ReefBeat y te permite elegir. Establece el parámetro `device` para forzar un dispositivo específico.

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Demo ReefDose" width="300"/></a><br/><em>Demo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Demo ReefMat" width="300"/></a><br/><em>Demo ReefMat</em></td>
</tr>
</table>

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

---

## 💬 Contacto y soporte

- **Preguntas y solicitudes de funciones:** Usa la pestaña [Discussions](https://github.com/Elwinmage/ha-reefbeat-component/discussions) de cada proyecto
- **Reportar un error:** Abre un [Issue](https://github.com/Elwinmage/ha-reefbeat-component/issues) con detalles
- **Apoyar el proyecto:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
