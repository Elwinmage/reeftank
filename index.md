---
charset: utf-8
layout: default
title: ReefTech Project Ecosystem
theme: jekyll-theme-cayman
lang: en
---

{% include language-selector.html %}

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

{% include toc-generator.html %}

* Table of Contents / Sommaire
{:toc}


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

Manage your Red Sea ReefBeat devices **locally** (no cloud required): ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, ReefMat, ReefRun and ReefWave.

> ⚠️ This is not an official Red Sea repository. Use at your own risk.

**Key features:**
- **100% local control** — no cloud dependency for most devices
- Auto-detection of devices on local network (with manual mode and subnet support)
- Custom icons for all ReefBeat devices
- Firmware update notifications (with optional Cloud API)
- Live configuration update mode for real-time monitoring
- Multi-language support

<!-- generated:beat-devices:start -->

**Supported devices:**

> ✅ Supported &nbsp;|&nbsp; 🚧 In progress &nbsp;|&nbsp; 🧪 Untested (may work) &nbsp;|&nbsp; ❌ Not yet supported

| Device | Models | Status |
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

**ReefWave specifics:** ReefWave is the only device tied to the ReefBeat cloud. Three operating modes are available — Cloud, Local, and Hybrid — so you can choose your balance between full local control and sync with the ReefBeat mobile app.

**Installation:** Available directly in [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — search for "redsea" or "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Control for Aqua Medic pumps via Home Assistant through the Gizwits cloud API.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Control your Aqua Medic pumps from Home Assistant via the Gizwits cloud API (same backend as the official Aqua Medic app).

<!-- generated:aqua-devices:start -->

**Supported devices:**

> ✅ Supported &nbsp;|&nbsp; 🚧 In progress &nbsp;|&nbsp; 🧪 Untested (may work) &nbsp;|&nbsp; ❌ Not yet supported

| Device | Status |
|------|------|
| **EcoDrift / SmartDrift x.1 / x.3** (wavemaker) | ✅ |
| **DC Runner x.1 / x.2 / x.3** (return pump) | ✅ |
| **DC Runner** (skimmer pump) | ✅ |
| **Reefdoser EVO** (dosing pump) | ❌ — [Ask for it](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (temperature controller) | ❌ — [Ask for it](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (lighting) | ❌ — [Ask for it](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

<!-- generated:aqua-devices:end -->

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

<!-- generated:maintenance:start -->

#### 🧰 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Maintenance tracking for equipment Home Assistant cannot reach.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Flow pumps, return pumps, skimmers, media reactors — anything you service by hand. One config entry per brand, one device per piece of equipment, four entities per task: a button that records the job, a number for the interval, a switch to mute alerts and a date to backdate the last intervention.

**Key features:**

- Presets for Tunze, Jebao and generic gear, with manufacturer intervals where one is published
- A shared library of 17 tasks, translated in 8 languages
- Backdating, so a new piece of equipment does not start from "never done"
- `reef_maintenance.reset` service — stick an NFC tag on the pump and scan it when you are done
- Same `reef_role` contract as the connected integrations, so tasks land in the card's maintenance view

**Installation:** In HACS, add `https://github.com/Elwinmage/ha-reef-maintenance-component` as a custom repository (Integration).

<!-- generated:maintenance:end -->

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

<!-- generated:card-devices:start -->

**Supported devices:**

> ✅ Supported &nbsp;|&nbsp; 🚧 In progress &nbsp;|&nbsp; 🧪 Untested (may work) &nbsp;|&nbsp; ❌ Not yet supported

| Device | Status | Highlights |
|------|------|------|
| **ReefDose (RSDOSE2/4)** | ✅ | Full scheduling, manual dosing, priming and calibration, supplement management, usage tracking |
| **ReefMat (RSMAT250/500/1200)** | ✅ | Animated roll status, manual/auto/scheduled advance, sensor status, weekly and monthly graphs |
| **ReefRun (RSRUN)** | ✅ | Pump speed control, schedule editor, overskimming management |
| **ReefATO+** | ✅ | Water level, leak probe, pump diagnostics, consumption graph, leak buzzer |
| **ReefControl-Power (RSPOWER6/8)** | 🚧 | Per-socket control |
| **ReefControl (RSCONTROLPRO/LITE)** | ❌ | [Vote for priority](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed (G1/G2)** | ❌ | [Vote for priority](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ | [Vote for priority](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic EcoDrift / SmartDrift** | ❌ | [Vote for priority](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic DC Runner (return, skimmer)** | ❌ | [Vote for priority](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

<!-- generated:card-devices:end -->

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

## 🔌 Infrastructure

---

#### ⚡ [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup)

**Autonomous battery backup system for Red Sea reef aquariums.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Keep your ReefWave, ReefRun and DC Skimmer running during power outages with a 24V LiFePO₄ battery, a Raspberry Pi and smart pump degradation.

<img src="https://github.com/Elwinmage/reefbeatEnergyBackup/raw/main/docs/images/power-flow-card.png" />

**Key features:**
- **Battery monitoring** via INA226 (I2C) + optional Victron BLE charger
- **Instant outage detection** via 230V relay on GPIO
- **Progressive pump degradation** — SoC-based levels computed from a target autonomy
- **3-level network failover** — Ethernet → Wi-Fi → autonomous mirror hotspot
- **4G LTE failover** — notifications and ReefBeat cloud access via USB modem or phone tethering
- **Push notifications** via [ntfy.sh](https://ntfy.sh) (free, no account required)
- **Home Assistant integration** — MQTT auto-discovery, update entity, battery test blueprint
- **Self-update** — checks GitHub for new versions, HA update entity with "Install" button

**Hardware levels:**

| Level | What you get | Budget |
|-------|-------------|--------|
| **1 — Basic** | Battery + cables, passive backup | ~290 € |
| **2 — Normal** *(recommended)* | + RPi + INA226 + relay, full monitoring & automation | ~402 € |
| **3 — Advanced** | + Victron BLE charger, connected breaker, 4G modem | ~627 € |

**Installation:**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

An interactive wizard configures everything: device scan, battery capacity, SoC levels, MQTT, notifications, 4G, scheduled reboot.

> Works standalone or as a complement to [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) for a fully integrated reef management setup.

---

<!-- generated:blueprints:start -->

#### 🔔 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Notification blueprints for the whole ecosystem.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Alerts you on your phone about overdue maintenance, found through the shared `reef_role` attribute so every integration is covered, and about devices that went unreachable. Eight languages, one import button each.

**Installation:** import from the repository, one button per language.

<!-- generated:blueprints:end -->

---

## 📐 3D Models

### ReefRun DC Skimmer
#### 📦 [*Red Sea DC Skimmer impeller tool*](https://www.thingiverse.com/thing:7313258)

<!-- Load model-viewer script -->
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<!-- Container with forced dimensions -->
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

<!-- Fallback script to fix "Zero Size" issue -->
<script>
  const modelViewer = document.querySelector("#aquarium-model");
  modelViewer.addEventListener("load", () => {
    // Force 3D engine to recalculate container size
    const width = modelViewer.clientWidth;
    const height = modelViewer.clientHeight;
    console.log("Model loaded, detected dimensions:", width, "x", height);
    if (width === 0 || height === 0) {
        modelViewer.style.width = "100%";
        modelViewer.style.height = "500px";
    }
  });
</script>

**Video demonstration:**
<video width="100%" height="auto" controls poster="assets/models/redsea-key.png" style="border-radius: 8px; margin: 20px 0; background: #000;">
  <source src="assets/videos/redsea_skimmer.webm" type="video/webm">
  <source src="assets/videos/logo_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

<!-- generated:contact:start -->

## 💬 Contact & Support

- **Questions and feature requests:** open a discussion on the project concerned — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues)
- **Bug reports:** open an issue on that same project, with the details.
- **Support the project:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)

<!-- generated:contact:end -->
