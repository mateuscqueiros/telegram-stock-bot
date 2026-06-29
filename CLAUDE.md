# Bot Telegram B3 — Workshop Claude Code

## Objetivo do workshop

Ensinar o fluxo **Claude Code**: pedir → revisar diff → validar no terminal.

O aluno **não escreve código manualmente** — usa o CLI `claude` e aprova as edições.

## Estrutura

```
bot/
├── config.py          # variáveis de ambiente (já pronto)
├── main.py            # bootstrap da aplicação
├── quotes.py          # chamada à API brapi
└── handlers/
    ├── commands.py    # /start, /help, /cotacao
    └── alerts.py      # /alerta + JobQueue
```

## Convenções

- Python 3.11+, código **async** (`async def`, `await`)
- Biblioteca: `python-telegram-bot` v21+ com `Application` e `JobQueue`
- HTTP: `httpx` (async)
- Tickers sempre em **MAIÚSCULAS** (ex: `PETR4`, `VALE3`)
- **Nunca** commitar o arquivo `.env`
- Mensagens ao usuário em **português**
- Formato de preço: `R$ 35,42` (vírgula como separador decimal)
- Formato de variação: `+1,23%` ou `-0,45%`
- **Na aula:** Claude Code gera o código; o aluno revisa e testa

## Variáveis de ambiente

| Variável | Obrigatória | Descrição |
|---|---|---|
| `TELEGRAM_TOKEN` | Sim | Token do @BotFather |
| `BRAPI_TOKEN` | Não | Token brapi.dev |
| `ALERT_INTERVAL_SECONDS` | Não | Intervalo do JobQueue (padrão: 60) |

## Como rodar

```bash
python -m venv .venv
pip install -r requirements.txt
cp .env.example .env
python -m bot.main
```

Ative o venv **antes** do `pip install` (escolha conforme seu terminal):

| Terminal | Comando |
|---|---|
| **Git Bash** (Windows) | `source .venv/Scripts/activate` |
| **PowerShell** (Windows) | `.venv\Scripts\Activate.ps1` |
| **CMD** (Windows) | `.venv\Scripts\activate.bat` |
| **Mac / Linux** | `source .venv/bin/activate` |

## API brapi

- Endpoint: `GET https://brapi.dev/api/quote/{TICKER}`
- Header opcional: `Authorization: Bearer {BRAPI_TOKEN}`
- **Sem token**, só funcionam: `PETR4`, `VALE3`, `MGLU3`, `ITUB4`
- Resposta relevante: `results[0].regularMarketPrice`, `regularMarketChangePercent`, `shortName`
