# Checklist — Workshop Bot Telegram B3

**Envie este checklist aos alunos 48h antes da aula.**

---

Olá!

No workshop vamos construir um bot de Telegram que consulta cotações da B3 usando o **Agent do Cursor**. Para aproveitar a aula, complete os itens abaixo **antes** de entrar na sala.

## Software

- [ ] [Cursor](https://cursor.com) instalado e logado (conta com **Agent** habilitado)
- [ ] Python 3.11+ instalado — verifique com `python --version`
- [ ] Git instalado — verifique com `git --version`
- [ ] Telegram instalado no celular (para testar o bot ao vivo)

## Contas e tokens

- [ ] **Token do bot Telegram** — crie em [@BotFather](https://t.me/BotFather) com `/newbot`
- [ ] **Token brapi.dev** (recomendado) — cadastre-se em [brapi.dev](https://brapi.dev) e gere o token no dashboard
  - Sem token, só funcionam: PETR4, VALE3, MGLU3, ITUB4
- [ ] **Conta GitHub** — para clonar o repositório

## Setup do projeto

Execute no terminal:

```bash
git clone -b starter git@github.com:mateuscqueiros/telegram-stock-bot.git
cd telegram-stock-bot

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env               # Windows: copy .env.example .env
```

Edite o arquivo **`.env`** (nunca o `.env.example`):

```env
TELEGRAM_TOKEN=seu_token_do_botfather
BRAPI_TOKEN=seu_token_brapi
ALERT_INTERVAL_SECONDS=60
```

## Smoke test

```bash
python -c "import telegram, httpx; print('OK')"
```

Se aparecer `OK`, você está pronto. **Não precisa rodar o bot ainda** — construiremos o código na aula.

## Na aula

1. Abra a pasta clonada no **Cursor**
2. Abra o **Agent** (painel lateral)
3. Tenha o **Telegram** aberto no celular

## Links

- Repositório (branch starter): https://github.com/mateuscqueiros/telegram-stock-bot/tree/starter
- Solução (referência): https://github.com/mateuscqueiros/telegram-stock-bot/tree/main

Qualquer dúvida, responda este e-mail.
