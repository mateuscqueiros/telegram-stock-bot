# Bot Telegram B3 — Cotações em tempo real

Bot em Python que consulta cotações da B3 via [brapi.dev](https://brapi.dev) e responde no Telegram.

## Funcionalidades

| Comando | Descrição |
|---|---|
| `/start` | Mensagem de boas-vindas |
| `/help` | Lista de comandos |
| `/cotacao PETR4` | Cotação com preço e variação % |
| `/alerta PETR4 35.00` | Alerta quando o preço atinge o limite |

## Stack

- Python 3.11+
- [python-telegram-bot](https://python-telegram-bot.org/) v21+ (com JobQueue)
- [httpx](https://www.python-httpx.org/) — chamadas HTTP async
- [python-dotenv](https://github.com/theskumar/python-dotenv) — variáveis de ambiente

## Pré-requisitos

- Python 3.11+
- Git
- Token do bot via [@BotFather](https://t.me/BotFather) (`/newbot`)
- Token em [brapi.dev](https://brapi.dev) (recomendado — sem token só funcionam PETR4, VALE3, MGLU3, ITUB4)

## Clone e setup

```bash
git clone git@github.com:mateuscqueiros/telegram-stock-bot.git
cd telegram-stock-bot

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env               # Windows: copy .env.example .env
```

Edite o `.env`:

```env
TELEGRAM_TOKEN=seu_token_do_botfather
BRAPI_TOKEN=seu_token_brapi
ALERT_INTERVAL_SECONDS=60
```

Smoke test:

```bash
python -c "import telegram, httpx; print('OK')"
```

## Como rodar

```bash
python -m bot.main
```

Teste no Telegram:

```
/start
/help
/cotacao PETR4
/cotacao VALE3
/alerta PETR4 0.01
```

## Estrutura do projeto

```
bot/
├── config.py          # variáveis de ambiente
├── main.py            # bootstrap + JobQueue
├── quotes.py          # integração com brapi.dev
└── handlers/
    ├── commands.py    # /start, /help, /cotacao
    └── alerts.py      # /alerta + checagem periódica
```

## APIs usadas

### Telegram Bot API

- Gratuita; requer token do [@BotFather](https://t.me/BotFather)
- Polling local — não precisa de servidor público

### brapi.dev (B3)

- Endpoint: `GET https://brapi.dev/api/quote/{TICKER}`
- Header: `Authorization: Bearer {BRAPI_TOKEN}`
- Sem token, apenas estes tickers funcionam: **PETR4**, **VALE3**, **MGLU3**, **ITUB4**

## Troubleshooting

| Problema | Solução |
|---|---|
| `KeyError: TELEGRAM_TOKEN` | Crie `.env` a partir de `.env.example` |
| `InvalidToken` | Token inválido no `.env` (nunca coloque no `.env.example`) |
| Bot não responde | Confirme que `python -m bot.main` está rodando |
| brapi 401 | Adicione `BRAPI_TOKEN` no `.env` ou use tickers gratuitos |
| brapi 429 | Aguarde ou use token autenticado |
| JobQueue desativado | `pip install "python-telegram-bot[job-queue]"` |

## Workshop

Este repositório é usado no workshop **Bot Telegram B3 — 1 hora no Cursor**.

- **Alunos:** clone a branch `starter` e construa o bot na aula com o Agent do Cursor
- **Instrutor:** veja [docs/GUIA_INSTRUTOR.md](docs/GUIA_INSTRUTOR.md) e [docs/CHECKLIST_ALUNOS.md](docs/CHECKLIST_ALUNOS.md)
- **Solução:** esta branch (`main`) contém o código completo

```bash
git clone -b starter git@github.com:mateuscqueiros/telegram-stock-bot.git
```

Leia `AGENTS.md` para as convenções do projeto.
