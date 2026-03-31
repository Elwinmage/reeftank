---
layout: default
title: Elwinmage - Projekty Reef Tech
theme: jekyll-theme-cayman
---


# 🌍 [🇺🇸](index.md) / [🇫🇷](fr.md) / [🇩🇪](de.md) / [🇪🇸](es.md) / [🇮🇹](it.md) / [🇵🇱] / [🇵🇹](pt.md)

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

Zarządzaj urządzeniami Red Sea ReefBeat **lokalnie** (bez chmury): ReefATO+, ReefDose, ReefLed, ReefMat, ReefRun i ReefWave.

> ⚠️ To nie jest oficjalne repozytorium Red Sea. Używasz na własne ryzyko.

**Główne funkcje:**
- **100% lokalna kontrola** — brak zależności od chmury dla większości urządzeń
- Automatyczne wykrywanie urządzeń w sieci lokalnej (z trybem ręcznym i obsługą podsieci)
- Niestandardowe ikony dla wszystkich urządzeń ReefBeat
- Powiadomienia o aktualizacji firmware (z opcjonalnym Cloud API)
- Tryb aktualizacji konfiguracji w czasie rzeczywistym
- Obsługa wielu języków

**Obsługiwane urządzenia:**

| Urządzenie | Modele | Status |
|------------|--------|--------|
| **ReefATO+** | RSATO+ | ✅ Przetestowane |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ Przetestowane |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115/170) | ✅ Przetestowane |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ Przetestowane |
| **ReefRun** | RSRUN | ✅ Przetestowane |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ / ☑️ |
| **ReefControl** | RSSENSE | ❌ Jeszcze nie — [skontaktuj się](https://github.com/Elwinmage/ha-reefbeat-component/discussions/8) |

**Specyfika ReefWave:** ReefWave to jedyne urządzenie powiązane z chmurą ReefBeat. Dostępne są trzy tryby pracy — Cloud, Lokalny i Hybrydowy — abyś mógł wybrać równowagę między pełną kontrolą lokalną a synchronizacją z aplikacją mobilną ReefBeat.

**Instalacja:** Dostępne bezpośrednio w [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — szukaj "redsea" lub "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Sterowanie pompami Aqua Medic przez Home Assistant za pomocą API chmury Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Steruj pompami Aqua Medic z Home Assistant za pomocą API chmury Gizwits (ten sam backend co oficjalna aplikacja Aqua Medic).

**Obsługiwane urządzenia:**

| Urządzenie | Status |
|------------|--------|
| **EcoDrift / SmartDrift x.1 / x.3** (falownik) | ✅ Obsługiwane |
| **DC Runner x.1 / x.2 / x.3** (pompa zwrotna) | 🧪 Nieprzetestowane |
| **Reefdoser EVO** (pompa dozująca) | ❌ Jeszcze nie — [skontaktuj się](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (sterownik temperatury) | ❌ Jeszcze nie — [skontaktuj się](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (oświetlenie) | ❌ Jeszcze nie — [skontaktuj się](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

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

**Obsługiwane urządzenia:**

| Urządzenie | Status | Najważniejsze |
|------------|--------|---------------|
| **ReefDose** (RSDOSE2/4) | ✅ Wdrożone | Pełne planowanie, ręczne dozowanie, zalewanie/kalibracja, zarządzanie suplementami, śledzenie zużycia |
| **ReefMat** (RSMAT250/500/1200) | ✅ Wdrożone | Animowany stan rolki, posuw ręczny/auto/zaplanowany, stan czujnika, wykresy tygodniowe/miesięczne |
| **ReefRun** (RSRUN) | ☑️ W trakcie | Sterowanie prędkością pompy, zarządzanie nadmiernym pienieniem |
| **ReefATO+** | ❌ Planowane | [Głosuj na priorytet](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed** (G1/G2) | ❌ Planowane | [Głosuj na priorytet](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ Planowane | [Głosuj na priorytet](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

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

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Demo ReefDose" width="300"/></a><br/><em>Demo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Demo ReefMat" width="300"/></a><br/><em>Demo ReefMat</em></td>
</tr>
</table>

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

---

## 💬 Kontakt i wsparcie

- **Pytania i prośby o funkcje:** Użyj zakładki [Discussions](https://github.com/Elwinmage/ha-reefbeat-component/discussions) każdego projektu
- **Zgłaszanie błędów:** Otwórz [Issue](https://github.com/Elwinmage/ha-reefbeat-component/issues) ze szczegółami
- **Wesprzyj projekt:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
