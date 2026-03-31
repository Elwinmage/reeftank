---
layout: default
title: Elwinmage - Projetos Reef Tech
theme: jekyll-theme-cayman
---


# 🌍 [🇺🇸](index.md) / [🇫🇷](fr.md) / [🇩🇪](de.md) / [🇪🇸](es.md) / [🇮🇹](it.md) / [🇵🇱](pl.md) / [🇵🇹]

# Minhas ferramentas ReefTank

Bem-vindo à documentação dos meus projetos para aquários de recife.

<video src="assets/videos/logo_v1.mp4" 
       poster="image-de-remplacement.jpg"
       autoplay 
       loop 
       muted 
       playsinline 
       style="width:100%; border-radius: 8px;height: 390px;object-fit: cover;">
</video>

---

## <img width="38" height="37" alt="image" src="https://images.icon-icons.com/2107/PNG/512/file_type_homeassistant_icon_130543.png" /> Integrações e cartões Home Assistant

---

### Integrações

#### 🐠 [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component)

**Integração local para o ecossistema Red Sea ReefBeat.**

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reefbeat-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reefbeat-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Gerencie seus dispositivos Red Sea ReefBeat **localmente** (sem cloud): ReefATO+, ReefDose, ReefLed, ReefMat, ReefRun e ReefWave.

> ⚠️ Este não é um repositório oficial da Red Sea. Uso por sua conta e risco.

**Funcionalidades principais:**
- **Controle 100% local** — sem dependência da cloud para a maioria dos dispositivos
- Detecção automática de dispositivos na rede local (com modo manual e suporte a sub-redes)
- Ícones personalizados para todos os dispositivos ReefBeat
- Notificações de atualização de firmware (com Cloud API opcional)
- Modo de atualização de configuração em tempo real
- Suporte multilíngue

**Dispositivos suportados:**

| Dispositivo | Modelos | Estado |
|-------------|---------|--------|
| **ReefATO+** | RSATO+ | ✅ Testado |
| **ReefDose** | RSDOSE2, RSDOSE4 | ✅ Testado |
| **ReefLed** | G1 (RSLED50/90/160), G2 (RSLED60/115/170) | ✅ Testado |
| **ReefMat** | RSMAT250, RSMAT500, RSMAT1200 | ✅ Testado |
| **ReefRun** | RSRUN | ✅ Testado |
| **ReefWave** | RSWAVE25, RSWAVE45 | ✅ / ☑️ |
| **ReefControl** | RSSENSE | ❌ Ainda não — [contacte-me](https://github.com/Elwinmage/ha-reefbeat-component/discussions/8) |

**Especificidades do ReefWave:** O ReefWave é o único dispositivo ligado à cloud ReefBeat. Três modos de operação estão disponíveis — Cloud, Local e Híbrido — para que escolha o equilíbrio entre controle local total e sincronização com a app móvel ReefBeat.

**Instalação:** Disponível diretamente no [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — pesquise "redsea" ou "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Controle de bombas Aqua Medic via Home Assistant através da API cloud Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Controle suas bombas Aqua Medic a partir do Home Assistant via API cloud Gizwits (mesmo backend da app oficial Aqua Medic).

**Dispositivos suportados:**

| Dispositivo | Estado |
|-------------|--------|
| **EcoDrift / SmartDrift x.1 / x.3** (bomba de ondas) | ✅ Suportado |
| **DC Runner x.1 / x.2 / x.3** (bomba de retorno) | 🧪 Não testado |
| **Reefdoser EVO** (bomba doseadora) | ❌ Ainda não — [contacte-me](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (controlador de temperatura) | ❌ Ainda não — [contacte-me](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (iluminação) | ❌ Ainda não — [contacte-me](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

**Funcionalidades EcoDrift / SmartDrift:**
- Ligar/desligar, tipo de onda (Pulso/Maré), modo alimentação, temporizador, modo controle 0-10V
- Modos de onda: Clássica, Sinusoidal, Aleatória, Fluxo constante
- Ligação: Independente, Master, Slave
- Controle de caudal, frequência e duração de alimentação
- Sensores de diagnóstico completos (sobrecorrente, sobretensão, sobreaquecimento, rotor bloqueado, funcionamento a seco, UART)

**Funcionalidades DC Runner:**
- Ligar/desligar, modo alimentação (pausa 10 min), modo controle 0-10V
- Controle de caudal (30–100%)
- Sensores de diagnóstico (funcionamento a seco, rotor bloqueado, tensão)

**Instalação:** No HACS, adicione `https://github.com/Elwinmage/ha-aquamedic-component` como repositório personalizado (Integração), depois pesquise "Aqua Medic".

---

### Cartões

#### 🪸 [ha-reef-card](https://github.com/Elwinmage/ha-reef-card)

**Cartão Lovelace personalizado para painéis de recife.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-card.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-card/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Lit](https://img.shields.io/badge/Lit-3.3-blue?style=flat-square&logo=lit)](https://lit.dev/)

O **Reef Card** para Home Assistant ajuda-o a gerir o seu aquário de recife diretamente a partir do painel. Combinado com [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component), deteta e suporta automaticamente os seus dispositivos Red Sea (ReefBeat).

> Dispositivos não-Redsea também podem ser suportados — [solicite aqui](https://github.com/Elwinmage/ha-reef-card/discussions/2).

**Dispositivos suportados:**

| Dispositivo | Estado | Destaques |
|-------------|--------|-----------|
| **ReefDose** (RSDOSE2/4) | ✅ Implementado | Agendamento completo, dosagem manual, escorva/calibração, gestão de suplementos, rastreamento de uso |
| **ReefMat** (RSMAT250/500/1200) | ✅ Implementado | Estado do rolo animado, avanço manual/auto/agendado, estado do sensor, gráficos semanais/mensais |
| **ReefRun** (RSRUN) | ☑️ Em progresso | Controle de velocidade da bomba, gestão de sobre-espumação |
| **ReefATO+** | ❌ Planeado | [Vote na prioridade](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed** (G1/G2) | ❌ Planeado | [Vote na prioridade](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ Planeado | [Vote na prioridade](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

**Destaques ReefDose:**
- Cartão de 6 zonas: config/WiFi, estados, dosagem manual com atalhos, agendamento por cabeça com progresso circular, gestão de suplementos com imagens de marcas, e fila de próximas doses
- Suporte a fluxos de escorva e calibração
- Biblioteca de suplementos com imagens para Red Sea, Tropic Marin, Quantum, ATI, Aqua Forest e mais

**Destaques ReefMat:**
- Cartão de 7 zonas com fundo animado que muda conforme o uso do rolo (0%–100%)
- Info em tempo real do rolo: comprimento restante, média diária, dias restantes estimados
- Controles de avanço manual, automático e agendado
- Exibição do estado do sensor de nível (conectado, desconectado, sujo)
- Gráficos de consumo semanal e mensal

**Instalação:** Disponível diretamente no [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reef-card&category=plugin) — pesquise "reef-card".

**Configuração:** Sem o parâmetro `device`, o cartão deteta automaticamente todos os dispositivos ReefBeat e permite-lhe escolher. Defina o parâmetro `device` para forçar um dispositivo específico.

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Demo ReefDose" width="300"/></a><br/><em>Demo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Demo ReefMat" width="300"/></a><br/><em>Demo ReefMat</em></td>
</tr>
</table>

---

## 📐 Modelos 3D

### ReefRun DC Skimmer
#### 📦 [*Ferramenta para rotor de skimmer DC Red Sea*](https://www.thingiverse.com/thing:7313258)


<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>

<div style="width: 100%; height: 500px; min-height: 500px; position: relative; margin: 20px 0; background: #eee; border-radius: 10px;">
  <model-viewer id="aquarium-model"
                src="assets/models/redsea-key.glb"
                alt="Chave Red Sea 3D"
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

## 💬 Contacto e suporte

- **Perguntas e pedidos de funcionalidades:** Use a aba [Discussions](https://github.com/Elwinmage/ha-reefbeat-component/discussions) de cada projeto
- **Reportar um bug:** Abra um [Issue](https://github.com/Elwinmage/ha-reefbeat-component/issues) com detalhes
- **Apoiar o projeto:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)
