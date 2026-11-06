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
       autoplay 
       loop 
       muted 
       playsinline 
       style="width:100%; border-radius: 8px;height: 390px;object-fit: cover;">
</video>

<!-- generated:flower:start -->

{% include ecosystem-flower.html %}

<nav class="eco-flower" aria-label="ReefTech projects" data-open="Open project" data-hint="Eight projects that fit together. Each one also works on its own.">
  <div class="eco-center">
    <strong>ReefTech</strong>
    <span>Eight projects that fit together. Each one also works on its own.</span>
  </div>
  <a class="eco-petal" href="https://github.com/Elwinmage/ha-reef-card" data-repo="ha-reef-card" data-links="ha-reefbeat-component ha-aquamedic-component ha-reef-maintenance-component ha-reeftank-component reefbeatEnergyBackup" style="--a:0deg;--x:50.00%;--y:14.00%;--c:#0f7f47">
    <img src="{{ '/assets/flower/ha-reef-card.webp' | relative_url }}" width="192" height="192" alt="" loading="lazy" />
    <span class="eco-name">Reef Card</span>
    <span class="eco-text"><strong>ha-reef-card</strong><span>Interactive view of every device on your dashboard, and the only way to edit advanced schedules.</span></span>
  </a>
  <a class="eco-petal" href="https://github.com/Elwinmage/ha-reefbeat-component" data-repo="ha-reefbeat-component" data-links="ha-reef-blueprints reefbeatEnergyBackup ha-reef-card" style="--a:45deg;--x:75.46%;--y:24.54%;--c:#1e6bb8">
    <img src="{{ '/assets/flower/ha-reefbeat-component.webp' | relative_url }}" width="192" height="192" alt="" loading="lazy" />
    <span class="eco-name">ReefBeat</span>
    <span class="eco-text"><strong>ha-reefbeat-component</strong><span>Red Sea ReefBeat devices in Home Assistant, controlled locally with no cloud.</span></span>
  </a>
  <a class="eco-petal" href="https://github.com/Elwinmage/ha-aquamedic-component" data-repo="ha-aquamedic-component" data-links="ha-reef-blueprints ha-reef-card" style="--a:90deg;--x:86.00%;--y:50.00%;--c:#1e6bb8">
    <img src="{{ '/assets/flower/ha-aquamedic-component.webp' | relative_url }}" width="192" height="192" alt="" loading="lazy" />
    <span class="eco-name">Aqua Medic</span>
    <span class="eco-text"><strong>ha-aquamedic-component</strong><span>Aqua Medic wavemakers, return and skimmer pumps in Home Assistant, through the Gizwits cloud API.</span></span>
  </a>
  <a class="eco-petal" href="https://github.com/Elwinmage/ha-reef-maintenance-component" data-repo="ha-reef-maintenance-component" data-links="ha-reef-blueprints ha-reef-card" style="--a:135deg;--x:75.46%;--y:75.46%;--c:#1e6bb8">
    <img src="{{ '/assets/flower/ha-reef-maintenance-component.webp' | relative_url }}" width="192" height="192" alt="" loading="lazy" />
    <span class="eco-name">Maintenance</span>
    <span class="eco-text"><strong>ha-reef-maintenance-component</strong><span>Cleaning and wear tracking for the equipment Home Assistant cannot talk to.</span></span>
  </a>
  <a class="eco-petal" href="https://github.com/Elwinmage/ha-reef-blueprints" data-repo="ha-reef-blueprints" data-links="ha-reefbeat-component ha-aquamedic-component ha-reef-maintenance-component" style="--a:180deg;--x:50.00%;--y:86.00%;--c:#a86a00">
    <img src="{{ '/assets/flower/ha-reef-blueprints.webp' | relative_url }}" width="192" height="192" alt="" loading="lazy" />
    <span class="eco-name">Blueprints</span>
    <span class="eco-text"><strong>ha-reef-blueprints</strong><span>Shared automations: alerts for overdue maintenance and unreachable devices, a heater test and a relay watch.</span></span>
  </a>
  <a class="eco-petal" href="https://github.com/Elwinmage/reefbeatEnergyBackup" data-repo="reefbeatEnergyBackup" data-links="ha-reef-card ha-reefbeat-component" style="--a:225deg;--x:24.54%;--y:75.46%;--c:#a86a00">
    <img src="{{ '/assets/flower/reefbeatEnergyBackup.webp' | relative_url }}" width="192" height="192" alt="" loading="lazy" />
    <span class="eco-name">Energy Backup</span>
    <span class="eco-text"><strong>reefbeatEnergyBackup</strong><span>Battery backup for outages, slowing your pumps progressively as the charge drops.</span></span>
  </a>
  <a class="eco-petal" href="https://github.com/Elwinmage/reeftank-catalog" data-repo="reeftank-catalog" data-links="ha-reeftank-component" style="--a:270deg;--x:14.00%;--y:50.00%;--c:#c8431f">
    <img src="{{ '/assets/flower/reeftank-catalog.webp' | relative_url }}" width="192" height="192" alt="" loading="lazy" />
    <span class="eco-name">Catalog</span>
    <span class="eco-text"><strong>reeftank-catalog</strong><span>Fish, corals and textures of the aquarium card, kept up to date automatically.</span></span>
  </a>
  <a class="eco-petal" href="https://github.com/Elwinmage/ha-reeftank-component" data-repo="ha-reeftank-component" data-links="reeftank-catalog ha-reef-card" style="--a:315deg;--x:24.54%;--y:24.54%;--c:#c8431f">
    <img src="{{ '/assets/flower/ha-reeftank-component.webp' | relative_url }}" width="192" height="192" alt="" loading="lazy" />
    <span class="eco-name">ReefTank</span>
    <span class="eco-text"><strong>ha-reeftank-component</strong><span>A living picture of your tank: your photo, your real lamps, animated fish and corals.</span></span>
  </a>
</nav>

<!-- generated:flower:end -->

{% include toc-generator.html %}

* Table of Contents / Sommaire
{:toc}


---

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Home Assistant Integrations and Cards

---

> Since Home Assistant 2026.11, HACS is part of Home Assistant as the **Marketplace** (*Settings > Marketplace*). On an older Home Assistant, the same steps work in HACS.

### Integrations

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Local Integration for Red Sea ReefBeat ecosystem.**

[![Marketplace Badge](https://img.shields.io/badge/Marketplace-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
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
- **Dose regulation** for the ReefDose: assisted dosing from your test results, brine regulated on the salinity
- **Poseidon mode** (experimental): a local relay that replaces most of the polling by what the devices push, with the history of the doses and the alarms of the devices as Home Assistant events
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

**Installation:** Available directly in the [Marketplace](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — search for "redsea" or "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Control for Aqua Medic pumps via Home Assistant through the Gizwits cloud API.**

[![Marketplace Badge](https://img.shields.io/badge/Marketplace-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
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

<!-- generated:aqua-devices:end -->

**EcoDrift / SmartDrift features:**
- Power on/off, wave type (Pulse/Tide), feeding mode, timer, 0-10V control mode
- Wave modes: Classic, Sine, Random, Constant flow
- Linkage: Independent, Master, Slave
- Flow rate, frequency, and feeding duration controls
- Time-slot program, up to 48 slots
- Full diagnostic fault sensors (overcurrent, overvoltage, overtemperature, locked rotor, dry run, UART)

**DC Runner features:**
- Power on/off, feeding mode (1–60 min pause), 0-10V control mode
- Flow rate control (30–100%)
- Time-slot program, up to 48 slots
- Diagnostic fault sensors (dry run, locked rotor, voltage, overcurrent, overtemperature, UART)

**Installation:** Search for "Aqua Medic" in *Settings > Marketplace*.

---

<!-- generated:maintenance:start -->

#### 🐙 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Maintenance tracking for equipment Home Assistant cannot reach.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Flow pumps, return pumps, skimmers, media reactors — anything you service by hand. One config entry per brand, one device per piece of equipment, four entities per task: a button that records the job, a number for the interval, a switch to mute alerts and a date to backdate the last intervention.

**Key features:**

- Presets for Tunze, Jebao and generic gear, with manufacturer intervals where one is published
- A shared library of 22 tasks, translated in 8 languages
- Backdating, so a new piece of equipment does not start from "never done"
- `reef_maintenance.reset` service — stick an NFC tag on the pump and scan it when you are done
- Same `reef_role` contract as the connected integrations, so tasks land in the card's maintenance view

**Installation:** Search for "reef-maintenance" in *Settings > Marketplace*.

<!-- generated:maintenance:end -->

---

<!-- generated:reeftank:start -->

#### 🐟 [ha-reeftank-component](https://github.com/Elwinmage/ha-reeftank-component)

**A living picture of your aquarium on the dashboard.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reeftank-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reeftank-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reeftank-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reeftank-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

<p align="center"><img src="https://raw.githubusercontent.com/Elwinmage/ha-reeftank-component/main/doc/img/preview.webp" width="70%" alt="ReefTank"/></p>

The integration behind the aquarium card of ha-reef-card: your photo, the water lit by your real lamps, animated fish and corals, and your devices and entities on it. It stores the aquariums, their pictures and their livestock, and records the feedings.

**Key features:**

- Outline the water, the sand and the rocks on your own photo — or draw the tank with rock and sand textures
- Fish that shoal, cruise, crawl on the sand or peek out of their burrow, and hide behind the rocks at night
- Water tinted by your lamps (ReefLED or any light), corals swaying with the pumps
- Feedings recorded from feeders, shortcuts or a service; fish and coral counts as sensors; pH and ORP watched against the tank's own history
- Species from the [reeftank-catalog](https://github.com/Elwinmage/reeftank-catalog), kept up to date automatically

**Installation:** Search for "ReefTank" in *Settings > Marketplace*, and install ha-reef-card for the card.

<!-- generated:reeftank:end -->

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
| **ReefDose (RSDOSE2/4)** | ✅ | Full scheduling, manual dosing, priming and calibration, supplement management, usage tracking, dose regulation (assisted dosing, brine), dose history |
| **ReefMat (RSMAT250/500/1200)** | ✅ | Animated roll status, manual/auto/scheduled advance, sensor status, weekly and monthly graphs |
| **ReefRun (RSRUN)** | ✅ | Pump speed control, schedule editor, overskimming management |
| **ReefATO+** | ✅ | Water level, leak probe, pump diagnostics, consumption graph, leak buzzer |
| **ReefControl (RSCONTROLPRO)** | ✅ | Probes with level bars, trends and 7-day history, guided pH/EC/ORP/temperature calibration, 12V ports, ATO, buzzer, paired power center |
| **ReefControl (RSCONTROLLITE)** | 🧪 | Probes with level bars, trends and 7-day history, guided pH/EC/ORP/temperature calibration, 12V ports, ATO, buzzer, paired power center |
| **ReefControl-Power (RSPOWER6)** | ✅ | Per-socket control, on/off/schedule/probe modes, linked devices, local temperature probe or ReefControl link |
| **ReefControl-Power (RSPOWER8)** | 🧪 | Per-socket control, on/off/schedule/probe modes, linked devices, local temperature probe or ReefControl link |
| **ReefLed (G1)** | ✅ | Sky with sun and moon, beam with the day's program, intensity/colour or white/blue sliders, program editor (kelvin or white/blue, clouds), weather mode, groups with staggered sunrise, acclimation |
| **ReefLed (G2)** | 🧪 | Sky with sun and moon, beam with the day's program, intensity/colour or white/blue sliders, program editor (kelvin or white/blue, clouds), weather mode, groups with staggered sunrise, acclimation |
| **ReefWave (RSWAVE25/45)** | ✅ | Animated pump view, speed and direction, wave library, schedule editor with time slots, pump groups |
| **Aqua Medic EcoDrift / SmartDrift** | ✅ | Pump speed on the picture, faults, feed pause, time-slot program editor |
| **Aqua Medic DC Runner (return, skimmer)** | ✅ | Return or skimmer pump view following the integration's role, speed, faults, time-slot program editor |
| **Energy Backup (reefbeatEnergyBackup)** | ✅ | Power flows of the mains, the battery and the pumps, drawn with Power Flow Card Plus |
| **VSON fish feeder (hacked, ESPHome)** | ✅ | Live picture of the feeder, feeding slots, reserve warning, feed now |
| **Aquarium view (ha-reeftank-component)** | ✅ | Your tank photo with live devices and entities, water tinted by your lamps, animated fish and corals, seven-tab scene editor |

<!-- generated:card-devices:end -->

**ReefDose highlights:**
- 6-zone card: config/WiFi, states, manual dosing with shortcuts, head scheduling with circular progress, supplement management with brand images, and upcoming dose queue
- Supports priming and calibration workflows
- Dose regulation dialogs: assisted dosing, brine with its salinity chart
- Supplement library with images for Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest, and more

**ReefMat highlights:**
- 7-zone card with animated background that changes based on roll usage (0%–100%)
- Real-time roll info: remaining length, daily average, estimated days left
- Manual, automatic, and scheduled advance controls
- Level sensor status display (connected, disconnected, dirty)
- Weekly and monthly consumption graphs

**Aquarium view:** a second card, `custom:reef-aquarium-card`, shows a living picture of your tank. It needs [ha-reeftank-component](https://github.com/Elwinmage/ha-reeftank-component).

**Installation:** Available directly in the [Marketplace](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) — search for "reef-card".

**Configuration:** Without the `device` parameter, the card automatically detects all ReefBeat devices and lets you choose. Set the `device` parameter to force a specific device.

<!-- generated:card-videos:start -->

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="ReefDose demo" width="300"/></a><br/><em>ReefDose demo</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="ReefMat demo" width="300"/></a><br/><em>ReefMat demo</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=Xxv38OPqiGI"><img src="https://img.youtube.com/vi/Xxv38OPqiGI/0.jpg" alt="ReefRun demo" width="300"/></a><br/><em>ReefRun demo</em></td>
<td><a href="https://www.youtube.com/watch?v=Ko46fHonOP4"><img src="https://img.youtube.com/vi/Ko46fHonOP4/0.jpg" alt="Maintenance demo" width="300"/></a><br/><em>Maintenance demo</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=2R0DHp2eqT4"><img src="https://img.youtube.com/vi/2R0DHp2eqT4/0.jpg" alt="ReefATO+ demo" width="300"/></a><br/><em>ReefATO+ demo</em></td>
<td><a href="https://www.youtube.com/watch?v=voFobfc7Slk"><img src="https://img.youtube.com/vi/voFobfc7Slk/0.jpg" alt="ReefControl & ReefControl-Power demo" width="300"/></a><br/><em>ReefControl & ReefControl-Power demo</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=pA49z8QjTN4"><img src="https://img.youtube.com/vi/pA49z8QjTN4/0.jpg" alt="ReefLed demo" width="300"/></a><br/><em>ReefLed demo</em></td>
<td><a href="https://www.youtube.com/watch?v=sYVeE0zV3eo"><img src="https://img.youtube.com/vi/sYVeE0zV3eo/0.jpg" alt="ReefWave demo" width="300"/></a><br/><em>ReefWave demo</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=9Gh4YE6Ck9g"><img src="https://img.youtube.com/vi/9Gh4YE6Ck9g/0.jpg" alt="Aqua Medic demo" width="300"/></a><br/><em>Aqua Medic demo</em></td>
</tr>
</table>

<!-- generated:card-videos:end -->

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
- **Poseidon mode watchdog** — watches the MQTT relay of ha-reefbeat-component and switches the devices back to normal mode when it dies
- **Self-update** — checks GitHub for new versions, HA update entity with "Install" button

**Hardware levels:**

| Level | What you get | Budget |
|-------|-------------|--------|
| **1 — Basic** | Battery + cables, passive backup | ~290 € |
| **2 — Normal** *(recommended)* | + RPi + INA226 + relay, full monitoring & automation | ~402 € |
| **3 — Advanced** | + Victron BLE charger, connected breaker, 4G modem | ~664 € |

**Installation:**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

An interactive wizard configures everything: device scan, battery capacity, SoC levels, MQTT, notifications, 4G, scheduled reboot.

> Works standalone or as a complement to [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) for a fully integrated reef management setup.

---

<!-- generated:blueprints:start -->

#### 🐬 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Automation blueprints for the whole ecosystem.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Alerts you on your phone about overdue maintenance, found through the shared `reef_role` attribute so every integration is covered, and about devices that went unreachable. Tests your heaters one at a time, and warns you when a relay reads off while its appliance still draws power. Eight languages, one import button each.

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
  Your browser does not support the video tag.
</video>


<!-- generated:skimmer-risers:start -->

#### 📦 [*RedSea DC Skimmer foots*](https://www.thingiverse.com/thing:7420525)

Risers for the feet of the Red Sea DC skimmer, to set its height in the sump. Four versions: 80, 70, 60 and 50 mm.

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer src="assets/models/redsea-skimmer-risers.glb"
                alt="RedSea DC Skimmer foots"
                camera-controls
                auto-rotate
                ar
                shadow-intensity="1"
                style="width: 100%; height: 100%; display: block;"
                exposure="1">
  </model-viewer>
</div>

### Water tests

#### 📦 [*Organizer for Red Sea reef aquarium tests*](https://www.thingiverse.com/thing:7429899)

A storage system for the Red Sea reef water test kits.

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer src="assets/models/redsea-tests-organizer.glb"
                alt="Organizer for Red Sea reef aquarium tests"
                camera-controls
                auto-rotate
                ar
                shadow-intensity="1"
                style="width: 100%; height: 100%; display: block;"
                exposure="1">
  </model-viewer>
</div>

<!-- generated:skimmer-risers:end -->

---

<!-- generated:contact:start -->

## 💬 Contact & Support

- **Questions and feature requests:** open a discussion on the project concerned — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [ha-reeftank-component](https://github.com/Elwinmage/ha-reeftank-component/issues) · [reeftank-catalog](https://github.com/Elwinmage/reeftank-catalog/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues) · [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints/issues)
- **Bug reports:** open an issue on that same project, with the details.
- **Support the project:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)

<!-- generated:contact:end -->
