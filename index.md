---
layout: default
title: Elwinmage - Reef Tech Projects
theme: jekyll-theme-cayman
---


# 🌍 [🇺🇸] / [🇫🇷](fr.md) / [🇩🇪](de.md) / [🇪🇸](es.md) / [🇮🇹](it.md) / [🇵🇱](pl.md) / [🇵🇹](pt.md)

# My ReefTank tools

Welcome to the documentation of my reef tank projects.

<video src="assets/videos/logo_v1.mp4" 
       poster="image-de-remplacement.jpg"
       autoplay 
       loop 
       muted 
       playsinline 
       style="width:100%; border-radius: 8px;height: 390px;object-fit: cover;">
</video>

---

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Home Assistant Integrations and Cards

---

### Integrations

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Local Integration for Red Sea ReefBeat ecosystem.**

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Manage your Red Sea ReefBeat devices **locally** (no cloud required): ReefATO+, ReefDose, ReefLed, ReefMat, ReefRun and ReefWave.

> ⚠️ This is not an official Red Sea repository. Use at your own risk.

**Key features:**
- **100% local control** — no cloud dependency for most devices
- Auto-detection of devices on local network (with manual mode and subnet support)
- Custom icons for all ReefBeat devices
- Firmware update notifications (with optional Cloud API)
- Live configuration update mode for real-time monitoring
- Multi-language support

**Supported devices:**

| Device | Models | Status |
|--------|--------|--------|
| **ReefATO+** | RSATO+ | ✅ Tested |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ Tested |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115/170) | ✅ Tested |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ Tested |
| **ReefRun** | RSRUN | ✅ Tested |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ / ☑️ |
| **ReefControl** | RSSENSE | ❌ Not yet — [contact me](https://github.com/Elwinmage/ha-reefbeat-component/discussions/8) |

**ReefWave specifics:** ReefWave is the only device tied to the ReefBeat cloud. Three operating modes are available — Cloud, Local, and Hybrid — so you can choose your balance between full local control and sync with the ReefBeat mobile app.

**Installation:** Available directly in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — search for "redsea" or "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Control for Aqua Medic pumps via Home Assistant through the Gizwits cloud API.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Control your Aqua Medic pumps from Home Assistant via the Gizwits cloud API (same backend as the official Aqua Medic app).

**Supported devices:**

| Device | Status |
|--------|--------|
| **EcoDrift / SmartDrift x.1 / x.3** (wavemaker) | ✅ Supported |
| **DC Runner x.1 / x.2 / x.3** (return pump) | 🧪 Untested |
| **Reefdoser EVO** (dosing pump) | ❌ Not yet — [contact me](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (temperature controller) | ❌ Not yet — [contact me](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (lighting) | ❌ Not yet — [contact me](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

**EcoDrift / SmartDrift features:**
- Power on/off, wave type (Pulse/Tide), feeding mode, timer, 0-10V control mode
- Wave modes: Classic, Sine, Random, Constant flow
- Linkage: Independent, Master, Slave
- Flow rate, frequency, and feeding duration controls
- Full diagnostic fault sensors (overcurrent, overvoltage, overtemperature, locked rotor, dry run, UART)

**DC Runner features:**
- Power on/off, feeding mode (10 min pause), 0-10V control mode
- Flow rate control (30–100%)
- Diagnostic fault sensors (dry run, locked rotor, voltage)

**Installation:** In HACS, add `https://github.com/Elwinmage/ha-aquamedic-component` as a custom repository (Integration), then search for "Aqua Medic".

---

### Cards

#### 🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)

**Custom Lovelace card for reef dashboards.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Lit](https://img.shields.io/badge/Lit-3.3-blue?style=flat-square&logo=lit)](https://lit.dev/)

The **Reef Card** for Home Assistant helps you manage your reef aquarium directly from your dashboard. Combined with [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component), it automatically detects and supports your Red Sea (ReefBeat) devices.

> Non-Redsea devices can also be supported — [request it here](https://github.com/Elwinmage/ha-reef-card/discussions/2).

**Supported devices:**

| Device | Status | Highlights |
|--------|--------|------------|
| **ReefDose** (RSDOSE2/4) | ✅ Implemented | Full scheduling, manual dosing, priming/calibration, supplement management, usage tracking |
| **ReefMat** (RSMAT250/500/1200) | ✅ Implemented | Animated roll status, manual/auto/scheduled advance, sensor status, weekly/monthly usage graphs |
| **ReefRun** (RSRUN) | ☑️ In progress | Pump speed control, overskimming management |
| **ReefATO+** | ❌ Planned | [Vote for priority](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed** (G1/G2) | ❌ Planned | [Vote for priority](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ Planned | [Vote for priority](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

**ReefDose highlights:**
- 6-zone card: config/WiFi, states, manual dosing with shortcuts, head scheduling with circular progress, supplement management with brand images, and upcoming dose queue
- Supports priming and calibration workflows
- Supplement library with images for Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest, and more

**ReefMat highlights:**
- 7-zone card with animated background that changes based on roll usage (0%–100%)
- Real-time roll info: remaining length, daily average, estimated days left
- Manual, automatic, and scheduled advance controls
- Level sensor status display (connected, disconnected, dirty)
- Weekly and monthly consumption graphs

**Installation:** Available directly in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) — search for "reef-card".

**Configuration:** Without the `device` parameter, the card automatically detects all ReefBeat devices and lets you choose. Set the `device` parameter to force a specific device.

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="ReefDose demo" width="300"/></a><br/><em>ReefDose demo</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="ReefMat demo" width="300"/></a><br/><em>ReefMat demo</em></td>
</tr>
</table>

---

## 📐 3D Models

### ReefRun DC Skimmer
#### 📦 [*Red Sea DC Skimmer impeller tool*](https://www.thingiverse.com/thing:7313258)


<!-- 1. Chargement du script (si pas déjà fait en haut de page) -->
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<!-- 2. Conteneur avec dimensions forcées -->
<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer id="aquarium-model"
                src="assets/models/redsea-key.glb"
                alt="Support Red Sea Key 3D"
                camera-controls
                auto-rotate
                ar
                shadow-intensity="1"
                style="width: 100%; height: 100%; display: block;"
                exposure="1">
  </model-viewer>
</div>

<!-- 3. Script de secours pour corriger le "Zero Size" -->
<script>
  const modelViewer = document.querySelector("#aquarium-model");
  modelViewer.addEventListener("load", () => {
    // Force le moteur 3D à recalculer la taille du conteneur
    const width = modelViewer.clientWidth;
    const height = modelViewer.clientHeight;
    console.log("Modèle chargé, dimensions détectées :", width, "x", height);
    if (width === 0 || height === 0) {
        modelViewer.style.width = "100%";
        modelViewer.style.height = "500px";
    }
  });
</script>

---

## 💬 Contact & Support

- **Questions & feature requests:** Use the [Discussions](https://github.com/Elwinmage/ha-reefbeat-component/discussions) tab on each project
- **Bug reports:** Open an [Issue](https://github.com/Elwinmage/ha-reefbeat-component/issues) with details
- **Support the project:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
