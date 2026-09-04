---
charset: utf-8
layout: default
title: ReefTech Project Ecosystem
theme: jekyll-theme-cayman
lang: pl
---

{% include language-selector.html %}

# Moje narzędzia ReefTank

Witamy w dokumentacji moich projektów do akwariów rafowych.

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

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Integracje i karty Home Assistant

---

### Integracje

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Lokalna integracja dla ekosystemu Red Sea ReefBeat.**

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Zarządzaj urządzeniami Red Sea ReefBeat **lokalnie** (bez chmury): ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, ReefMat, ReefRun i ReefWave.

> ⚠️ To nie jest oficjalne repozytorium Red Sea. Używasz na własne ryzyko.

**Główne funkcje:**
- **100% lokalna kontrola** — brak zależności od chmury dla większości urządzeń
- Automatyczne wykrywanie urządzeń w sieci lokalnej (z trybem ręcznym i obsługą podsieci)
- Niestandardowe ikony dla wszystkich urządzeń ReefBeat
- Powiadomienia o aktualizacji firmware (z opcjonalnym Cloud API)
- Tryb aktualizacji konfiguracji w czasie rzeczywistym
- Obsługa wielu języków

<!-- generated:beat-devices:start -->

**Obsługiwane urządzenia:**

> ✅ Wspierane &nbsp;|&nbsp; 🚧 W trakcie &nbsp;|&nbsp; 🧪 Nieprzetestowane (może działać) &nbsp;|&nbsp; ❌ Jeszcze niewspierane

| Urządzenie | Modele | Status |
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

**Specyfika ReefWave:** ReefWave to jedyne urządzenie powiązane z chmurą ReefBeat. Dostępne są trzy tryby pracy — Cloud, Lokalny i Hybrydowy — abyś mógł wybrać równowagę między pełną kontrolą lokalną a synchronizacją z aplikacją mobilną ReefBeat.

**Instalacja:** Dostępne bezpośrednio w [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — szukaj "redsea" lub "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Sterowanie pompami Aqua Medic przez Home Assistant za pomocą API chmury Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Steruj pompami Aqua Medic z Home Assistant za pomocą API chmury Gizwits (ten sam backend co oficjalna aplikacja Aqua Medic).

<!-- generated:aqua-devices:start -->

**Obsługiwane urządzenia:**

> ✅ Wspierane &nbsp;|&nbsp; 🚧 W trakcie &nbsp;|&nbsp; 🧪 Nieprzetestowane (może działać) &nbsp;|&nbsp; ❌ Jeszcze niewspierane

| Urządzenie | Status |
|------|------|
| **EcoDrift / SmartDrift x.1 / x.3** (cyrkulacyjna) | ✅ |
| **DC Runner x.1 / x.2 / x.3** (pompa obiegowa) | ✅ |
| **DC Runner** (pompa odpieniacza) | ✅ |
| **Reefdoser EVO** (pompa dozująca) | ❌ — [Poproś o to](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (sterownik temperatury) | ❌ — [Poproś o to](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (oświetlenie) | ❌ — [Poproś o to](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

<!-- generated:aqua-devices:end -->

**Funkcje EcoDrift / SmartDrift:**
- Włączanie/wyłączanie, typ fali (Puls/Przypływ), tryb karmienia, timer, tryb sterowania 0-10V
- Tryby fal: Klasyczna, Sinusoidalna, Losowa, Stały przepływ
- Powiązanie: Niezależne, Master, Slave
- Sterowanie przepływem, częstotliwością i czasem karmienia
- Kompletne czujniki diagnostyczne (nadprąd, przepięcie, przegrzanie, zablokowany wirnik, praca na sucho, UART)

**Funkcje DC Runner:**
- Włączanie/wyłączanie, tryb karmienia (pauza 10 min), tryb sterowania 0-10V
- Sterowanie przepływem (30–100%)
- Czujniki diagnostyczne (praca na sucho, zablokowany wirnik, napięcie)

**Instalacja:** W HACS dodaj `https://github.com/Elwinmage/ha-aquamedic-component` jako niestandardowe repozytorium (Integracja), następnie szukaj "Aqua Medic".

---

<!-- generated:maintenance:start -->

#### 🐙 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Śledzenie konserwacji sprzętu, do którego Home Assistant nie ma dostępu.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Pompy cyrkulacyjne, pompy obiegowe, odpieniacze, reaktory — wszystko, co czyścisz ręcznie. Jeden wpis na markę, jedno urządzenie na sprzęt, cztery encje na zadanie: przycisk rejestrujący wykonanie, liczba dla interwału, przełącznik wyciszający powiadomienia i data do wstecznego wpisania ostatniej obsługi.

**Główne funkcje:**

- Ustawienia wstępne dla Tunze, Jebao i sprzętu generycznego, z interwałami producenta tam, gdzie są publikowane
- Wspólna biblioteka 17 zadań, przetłumaczona na 8 języków
- Wsteczne datowanie, aby nowy sprzęt nie zaczynał od „nigdy nie wykonano"
- Usługa `reef_maintenance.reset` — przyklej tag NFC na pompie i zeskanuj go po zakończeniu
- Ten sam kontrakt `reef_role` co integracje podłączone: zadania trafiają do widoku konserwacji karty

**Instalacja:** W HACS dodaj `https://github.com/Elwinmage/ha-reef-maintenance-component` jako niestandardowe repozytorium (Integracja).

<!-- generated:maintenance:end -->

---

### Karty

#### 🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)

**Niestandardowa karta Lovelace dla paneli rafowych.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Lit](https://img.shields.io/badge/Lit-3.3-blue?style=flat-square&logo=lit)](https://lit.dev/)

**Reef Card** dla Home Assistant pomaga zarządzać akwarium rafowym bezpośrednio z panelu. W połączeniu z [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) automatycznie wykrywa i obsługuje urządzenia Red Sea (ReefBeat).

> Urządzenia innych producentów mogą być również obsługiwane — [zgłoś zapotrzebowanie tutaj](https://github.com/Elwinmage/ha-reef-card/discussions/2).

<!-- generated:card-devices:start -->

**Obsługiwane urządzenia:**

> ✅ Wspierane &nbsp;|&nbsp; 🚧 W trakcie &nbsp;|&nbsp; 🧪 Nieprzetestowane (może działać) &nbsp;|&nbsp; ❌ Jeszcze niewspierane

| Urządzenie | Status | Najważniejsze |
|------|------|------|
| **ReefDose (RSDOSE2/4)** | ✅ | Pełne harmonogramowanie, dozowanie ręczne, zalewanie i kalibracja, zarządzanie suplementami, śledzenie zużycia |
| **ReefMat (RSMAT250/500/1200)** | ✅ | Animowany stan rolki, przesuw ręczny/automatyczny/zaplanowany, stan czujnika, wykresy tygodniowe i miesięczne |
| **ReefRun (RSRUN)** | ✅ | Sterowanie prędkością pompy, edytor harmonogramów, zarządzanie nadmiernym odpienianiem |
| **ReefATO+** | ✅ | Poziom wody, sonda wycieku, diagnostyka pompy, wykres zużycia, buzzer wycieku |
| **ReefControl-Power (RSPOWER6/8)** | 🚧 | Sterowanie per gniazdo |
| **ReefControl (RSCONTROLPRO/LITE)** | ❌ | [Zagłosuj na priorytet](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed (G1/G2)** | ❌ | [Zagłosuj na priorytet](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ | [Zagłosuj na priorytet](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic EcoDrift / SmartDrift** | ❌ | [Zagłosuj na priorytet](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic DC Runner (return, skimmer)** | ❌ | [Zagłosuj na priorytet](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

<!-- generated:card-devices:end -->

**Najważniejsze ReefDose:**
- Karta 6-strefowa: config/WiFi, stany, ręczne dozowanie ze skrótami, planowanie na głowicę z kołowym postępem, zarządzanie suplementami z obrazami marek, kolejka nadchodzących dawek
- Obsługa procesów zalewania i kalibracji
- Biblioteka suplementów z obrazami dla Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest i innych

**Najważniejsze ReefMat:**
- Karta 7-strefowa z animowanym tłem zmieniającym się w zależności od zużycia rolki (0%–100%)
- Informacje o rolce w czasie rzeczywistym: pozostała długość, średnia dzienna, szacowane pozostałe dni
- Sterowanie posuwem ręcznym, automatycznym i zaplanowanym
- Wyświetlanie stanu czujnika poziomu (podłączony, odłączony, zabrudzony)
- Wykresy zużycia tygodniowego i miesięcznego

**Instalacja:** Dostępne bezpośrednio w [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) — szukaj "reef-card".

**Konfiguracja:** Bez parametru `device` karta automatycznie wykrywa wszystkie urządzenia ReefBeat i pozwala wybrać. Ustaw parametr `device`, aby wymusić konkretne urządzenie.

<!-- generated:card-videos:start -->

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Demo ReefDose" width="300"/></a><br/><em>Demo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Demo ReefMat" width="300"/></a><br/><em>Demo ReefMat</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=Xxv38OPqiGI"><img src="https://img.youtube.com/vi/Xxv38OPqiGI/0.jpg" alt="Demo ReefRun" width="300"/></a><br/><em>Demo ReefRun</em></td>
<td><a href="https://www.youtube.com/watch?v=Ko46fHonOP4"><img src="https://img.youtube.com/vi/Ko46fHonOP4/0.jpg" alt="Demo Konserwacja" width="300"/></a><br/><em>Demo Konserwacja</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=2R0DHp2eqT4"><img src="https://img.youtube.com/vi/2R0DHp2eqT4/0.jpg" alt="Demo ReefATO+" width="300"/></a><br/><em>Demo ReefATO+</em></td>
</tr>
</table>

<!-- generated:card-videos:end -->

---

## 🔌 Infrastruktura

---

#### ⚡ [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup)

**Autonomiczny system zasilania bateryjnego dla akwariów rafowych Red Sea.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Utrzymuj ReefWave, ReefRun i DC Skimmer w ruchu podczas przerw w zasilaniu dzięki baterii LiFePO₄ 24V, Raspberry Pi i inteligentnej redukcji pomp.

<img src="https://github.com/Elwinmage/reefbeatEnergyBackup/raw/main/docs/images/power-flow-card.png" />

**Główne funkcje:**
- **Monitorowanie baterii** przez INA226 (I2C) + opcjonalna ładowarka Victron BLE
- **Natychmiastowe wykrywanie** przerw w zasilaniu przez przekaźnik 230V na GPIO
- **Progresywna redukcja** pomp — poziomy SoC obliczone z docelowej autonomii
- **3-poziomowy failover sieci** — Ethernet → Wi-Fi → autonomiczny hotspot lustrzany
- **Failover 4G/LTE** — powiadomienia i dostęp do chmury ReefBeat przez modem USB lub tethering
- **Powiadomienia push** przez [ntfy.sh](https://ntfy.sh) (darmowe, bez konta)
- **Integracja Home Assistant** — MQTT auto-discovery, encja aktualizacji, blueprint testu baterii
- **Auto-aktualizacja** — sprawdza GitHub, przycisk "Zainstaluj" w HA

**Poziomy sprzętowe:**

| Poziom | Co otrzymujesz | Budżet |
|--------|---------------|--------|
| **1 — Podstawowy** | Bateria + kable, pasywny backup | ~290 € |
| **2 — Normalny** *(zalecany)* | + RPi + INA226 + przekaźnik, monitoring & automatyzacja | ~402 € |
| **3 — Zaawansowany** | + Ładowarka Victron BLE, inteligentny wyłącznik, modem 4G | ~627 € |

**Instalacja:**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

> Działa samodzielnie lub jako uzupełnienie [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) dla w pełni zintegrowanego zarządzania akwarium.

---

<!-- generated:blueprints:start -->

#### 🐬 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Blueprinty powiadomień dla całego ekosystemu.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Powiadamia na telefonie o zaległych konserwacjach, znajdowanych przez wspólny atrybut `reef_role`, dzięki czemu objęte są wszystkie integracje, oraz o urządzeniach, które przestały odpowiadać. Osiem języków, po jednym przycisku importu.

**Instalacja:** import z repozytorium, jeden przycisk na język.

<!-- generated:blueprints:end -->

---

## 📐 Modele 3D

### ReefRun DC Skimmer
#### 📦 [*Narzędzie do wirnika odpieniacza DC Red Sea*](https://www.thingiverse.com/thing:7313258)


<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer id="aquarium-model"
                src="assets/models/redsea-key.glb"
                alt="Klucz Red Sea 3D"
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

**Demonstracja wideo:**
<video width="100%" height="auto" controls poster="assets/models/redsea-key.png" style="border-radius: 8px; margin: 20px 0; background: #000;">
  <source src="assets/videos/redsea_skimmer.webm" type="video/webm">
  <source src="assets/videos/logo_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

<!-- generated:contact:start -->

## 💬 Kontakt i wsparcie

- **Pytania i propozycje funkcji:** otwórz dyskusję w odpowiednim projekcie — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues)
- **Zgłoszenia błędów:** otwórz issue w tym samym projekcie, ze szczegółami.
- **Wesprzyj projekt:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)

<!-- generated:contact:end -->
