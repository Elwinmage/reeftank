---
layout: default
title: ReefTech Project Ecosystem
theme: jekyll-theme-cayman
lang: pt
---

{% include language-selector.html %}

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

{% include toc-generator.html %}

* Table of Contents / Sommaire
{:toc}


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

Gerencie seus dispositivos Red Sea ReefBeat **localmente** (sem cloud): ReefATO+, ReefControl, ReefControl-Power, ReefDose, ReefLed, ReefMat, ReefRun e ReefWave.

> ⚠️ Este não é um repositório oficial da Red Sea. Uso por sua conta e risco.

**Funcionalidades principais:**
- **Controle 100% local** — sem dependência da cloud para a maioria dos dispositivos
- Detecção automática de dispositivos na rede local (com modo manual e suporte a sub-redes)
- Ícones personalizados para todos os dispositivos ReefBeat
- Notificações de atualização de firmware (com Cloud API opcional)
- Modo de atualização de configuração em tempo real
- Suporte multilíngue

<!-- generated:beat-devices:start -->

**Dispositivos suportados:**

> ✅ Suportado &nbsp;|&nbsp; 🚧 Em curso &nbsp;|&nbsp; 🧪 Não testado (pode funcionar) &nbsp;|&nbsp; ❌ Ainda não suportado

| Aparelho | Modelos | Estado |
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

**Especificidades do ReefWave:** O ReefWave é o único dispositivo ligado à cloud ReefBeat. Três modos de operação estão disponíveis — Cloud, Local e Híbrido — para que escolha o equilíbrio entre controle local total e sincronização com a app móvel ReefBeat.

**Instalação:** Disponível diretamente no [HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=Elwinmage&repository=ha-reefbeat-component&category=integration) — pesquise "redsea" ou "reefbeat".

---

#### 🌊 [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component)

**Controle de bombas Aqua Medic via Home Assistant através da API cloud Gizwits.**

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://github.com/hacs/hacs)
[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-aquamedic-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-aquamedic-component/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Controle suas bombas Aqua Medic a partir do Home Assistant via API cloud Gizwits (mesmo backend da app oficial Aqua Medic).

<!-- generated:aqua-devices:start -->

**Dispositivos suportados:**

> ✅ Suportado &nbsp;|&nbsp; 🚧 Em curso &nbsp;|&nbsp; 🧪 Não testado (pode funcionar) &nbsp;|&nbsp; ❌ Ainda não suportado

| Aparelho | Estado |
|------|------|
| **EcoDrift / SmartDrift x.1 / x.3** (de circulação) | ✅ |
| **DC Runner x.1 / x.2 / x.3** (bomba de retorno) | ✅ |
| **DC Runner** (bomba do escumador) | ✅ |
| **Reefdoser EVO** (bomba doseadora) | ❌ — [Peça-o](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **T-Controller Twin** (controlador de temperatura) | ❌ — [Peça-o](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |
| **Aquarius / Spectrus** (iluminação) | ❌ — [Peça-o](https://github.com/Elwinmage/ha-aquamedic-component/discussions) |

<!-- generated:aqua-devices:end -->

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

<!-- generated:maintenance:start -->

#### 🧰 [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component)

**Acompanhamento de manutenção para equipamento que o Home Assistant não alcança.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/ha-reef-maintenance-component.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-maintenance-component/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Bombas de circulação, bombas de retorno, escumadores, reatores — tudo o que limpa à mão. Uma entrada por marca, um aparelho por equipamento, quatro entidades por tarefa: um botão que regista o trabalho, um número para o intervalo, um interruptor para silenciar os avisos e uma data para retroagir a última intervenção.

**Funções principais:**

- Predefinições para Tunze, Jebao e equipamento genérico, com os intervalos do fabricante quando publicados
- Uma biblioteca comum de 17 tarefas, traduzida em 8 idiomas
- Retroatividade, para que um equipamento novo não comece em «nunca feito»
- Serviço `reef_maintenance.reset` — cole uma etiqueta NFC na bomba e leia-a quando terminar
- Mesmo contrato `reef_role` das integrações ligadas: as tarefas aparecem na vista de manutenção do cartão

**Instalação:** No HACS, adicione `https://github.com/Elwinmage/ha-reef-maintenance-component` como repositório personalizado (Integração).

<!-- generated:maintenance:end -->

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

<!-- generated:card-devices:start -->

**Dispositivos suportados:**

> ✅ Suportado &nbsp;|&nbsp; 🚧 Em curso &nbsp;|&nbsp; 🧪 Não testado (pode funcionar) &nbsp;|&nbsp; ❌ Ainda não suportado

| Aparelho | Estado | Pontos fortes |
|------|------|------|
| **ReefDose (RSDOSE2/4)** | ✅ | Planeamento completo, doseamento manual, escorvamento e calibração, gestão de suplementos, acompanhamento do consumo |
| **ReefMat (RSMAT250/500/1200)** | ✅ | Estado do rolo animado, avanço manual/automático/programado, estado do sensor, gráficos semanais e mensais |
| **ReefRun (RSRUN)** | ✅ | Controlo da velocidade da bomba, editor de programas, gestão da sobre-escumação |
| **ReefATO+** | ✅ | Nível de água, sonda de fugas, diagnóstico da bomba, gráfico de consumo, buzzer de fuga |
| **ReefControl-Power (RSPOWER6/8)** | 🚧 | Controlo por tomada |
| **ReefControl (RSCONTROLPRO/LITE)** | ❌ | [Votar na prioridade](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefLed (G1/G2)** | ❌ | [Votar na prioridade](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **ReefWave** | ❌ | [Votar na prioridade](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic EcoDrift / SmartDrift** | ❌ | [Votar na prioridade](https://github.com/Elwinmage/ha-reef-card/discussions/22) |
| **Aqua Medic DC Runner (return, skimmer)** | ❌ | [Votar na prioridade](https://github.com/Elwinmage/ha-reef-card/discussions/22) |

<!-- generated:card-devices:end -->

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

<!-- generated:card-videos:start -->

<table>
<tr>
<td><a href="https://www.youtube.com/watch?v=Qee5LH0T9wQ"><img src="https://img.youtube.com/vi/Qee5LH0T9wQ/0.jpg" alt="Demo ReefDose" width="300"/></a><br/><em>Demo ReefDose</em></td>
<td><a href="https://www.youtube.com/watch?v=yyNyUSitb1E"><img src="https://img.youtube.com/vi/yyNyUSitb1E/0.jpg" alt="Demo ReefMat" width="300"/></a><br/><em>Demo ReefMat</em></td>
</tr>
<tr>
<td><a href="https://www.youtube.com/watch?v=Xxv38OPqiGI"><img src="https://img.youtube.com/vi/Xxv38OPqiGI/0.jpg" alt="Demo ReefRun" width="300"/></a><br/><em>Demo ReefRun</em></td>
<td><a href="https://www.youtube.com/watch?v=Ko46fHonOP4"><img src="https://img.youtube.com/vi/Ko46fHonOP4/0.jpg" alt="Demo Manutenção" width="300"/></a><br/><em>Demo Manutenção</em></td>
</tr>
</table>

<!-- generated:card-videos:end -->

---

## 🔌 Infraestrutura

---

#### ⚡ [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup)

**Sistema autónomo de backup com bateria para aquários de recife Red Sea.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/Elwinmage/reefbeatEnergyBackup.svg?style=flat-square)](https://github.com/Elwinmage/reefbeatEnergyBackup/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Mantenha os seus ReefWave, ReefRun e DC Skimmer a funcionar durante cortes de energia com uma bateria LiFePO₄ 24V, um Raspberry Pi e degradação inteligente das bombas.

<img src="https://github.com/Elwinmage/reefbeatEnergyBackup/raw/main/docs/images/power-flow-card.png" />

**Funcionalidades principais:**
- **Monitorização de bateria** via INA226 (I2C) + carregador Victron BLE opcional
- **Deteção instantânea** de cortes via relé 230V no GPIO
- **Degradação progressiva** das bombas — níveis SoC calculados a partir de uma autonomia alvo
- **Failover de rede 3 níveis** — Ethernet → Wi-Fi → hotspot espelho autónomo
- **Failover 4G/LTE** — notificações e acesso cloud ReefBeat via modem USB ou tethering
- **Notificações push** via [ntfy.sh](https://ntfy.sh) (gratuito, sem conta)
- **Integração Home Assistant** — MQTT auto-discovery, entidade de atualização, blueprint de teste de bateria
- **Auto-atualização** — verifica GitHub, botão "Instalar" no HA

**Níveis de hardware:**

| Nível | O que obtém | Orçamento |
|-------|-----------|-----------|
| **1 — Básico** | Bateria + cabos, backup passivo | ~290 € |
| **2 — Normal** *(recomendado)* | + RPi + INA226 + relé, monitorização & automação | ~402 € |
| **3 — Avançado** | + Carregador Victron BLE, disjuntor conectado, modem 4G | ~627 € |

**Instalação:**
```bash
curl -sL https://raw.githubusercontent.com/Elwinmage/reefbeatEnergyBackup/main/install.sh | sudo bash
```

> Funciona sozinho ou como complemento do [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component) para uma gestão de recife totalmente integrada.

---

<!-- generated:blueprints:start -->

#### 🔔 [ha-reef-blueprints](https://github.com/Elwinmage/ha-reef-blueprints)

**Blueprints de notificação para todo o ecossistema.**

[![GH-release](https://img.shields.io/github/v/release/Elwinmage/ha-reef-blueprints.svg?style=flat-square)](https://github.com/Elwinmage/ha-reef-blueprints/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Avisa-o no telemóvel das manutenções em atraso, encontradas pelo atributo comum `reef_role` para que todas as integrações fiquem cobertas, e dos aparelhos que ficaram inacessíveis. Oito idiomas, um botão de importação cada.

**Instalação:** importe do repositório, um botão por idioma.

<!-- generated:blueprints:end -->

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

**Demonstração em vídeo:**
<video width="100%" height="auto" controls poster="assets/models/redsea-key.png" style="border-radius: 8px; margin: 20px 0; background: #000;">
  <source src="assets/videos/redsea_skimmer.webm" type="video/webm">
  <source src="assets/videos/logo_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

<!-- generated:contact:start -->

## 💬 Contacto e suporte

- **Perguntas e pedidos de funcionalidades:** abra uma discussão no projeto em causa — [ha-reefbeat-component](https://github.com/Elwinmage/ha-reefbeat-component/discussions) · [ha-aquamedic-component](https://github.com/Elwinmage/ha-aquamedic-component/discussions) · [ha-reef-card](https://github.com/Elwinmage/ha-reef-card/discussions) · [ha-reef-maintenance-component](https://github.com/Elwinmage/ha-reef-maintenance-component/issues) · [reefbeatEnergyBackup](https://github.com/Elwinmage/reefbeatEnergyBackup/issues)
- **Relatórios de erros:** abra uma issue nesse mesmo projeto, com os detalhes.
- **Apoiar o projeto:** [![BuyMeCoffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=flat-square)](https://paypal.me/Elwinmage)

<!-- generated:contact:end -->
