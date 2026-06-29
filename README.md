# Workshop: Bot Telegram B3 — Claude Code no Cursor

**Você não vai digitar código.** Seu papel é **dirigir o Agent**: colar prompts, aprovar as mudanças que ele propõe, rodar no terminal e testar no Telegram.

## O que você vai aprender

- Usar **Plan mode** para planejar antes de implementar
- Usar **Agent mode** para o AI escrever o código por você
- Dar contexto com **`@AGENTS.md`** e `@arquivo`
- Iterar: Agent → terminal → Telegram → corrigir com novo prompt

O bot de cotações da B3 é o **projeto de prática**, não o foco da aula.

---

## Cursor gratuito — sem assinatura paga

| Pergunta | Resposta |
|---|---|
| Preciso pagar? | **Não.** O plano **Hobby** do Cursor é gratuito e não pede cartão |
| Preciso instalar o Cursor? | **Sim.** É a ferramenta da aula (fork do VS Code com AI integrado) |
| O Agent funciona no gratuito? | **Sim**, com limite mensal de requisições — suficiente para esta aula (~5 prompts) |
| E se bater o limite? | Use o **Chat** do Cursor para pedir o código e cole manualmente, ou acompanhe um colega |
| Tenho e-mail `.edu`? | Cadastre-se — Cursor oferece **1 ano de Pro grátis** para estudantes |

Crie sua conta grátis em [cursor.com](https://cursor.com) antes da aula.

---

## Regra de ouro da aula

```
Você NÃO escreve código → você ESCREVE PROMPTS
Você NÃO decora Python   → você VALIDA no terminal e no Telegram
```

1. Cole o prompt do bloco no **Agent**
2. Revise o diff e clique **Accept** / **Aplicar**
3. Rode `python -m bot.main` no terminal
4. Teste no Telegram
5. Se falhar, cole um prompt de correção — não edite o código à mão (a menos que o limite do Agent acabe)

---

## O que já vem pronto neste repo

| Arquivo | Descrição |
|---|---|
| `AGENTS.md` | **Leia primeiro.** Regras que o Agent segue |
| `bot/config.py` | Leitura do `.env` |
| `requirements.txt` | Dependências |
| `.env.example` | Modelo de configuração |

## O que o Agent constrói na aula (você só orienta)

| Arquivo | Bloco |
|---|---|
| `bot/main.py` | 2 e 4 |
| `bot/handlers/commands.py` | 2 e 3 |
| `bot/quotes.py` | 3 |
| `bot/handlers/alerts.py` | 4 |

---

## Setup (faça antes da aula)

```bash
git clone -b starter git@github.com:mateuscqueiros/telegram-stock-bot.git
cd telegram-stock-bot

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env               # Windows: copy .env.example .env
```

Edite o **`.env`**:

```env
TELEGRAM_TOKEN=seu_token_do_botfather
BRAPI_TOKEN=seu_token_brapi
```

Tokens: [@BotFather](https://t.me/BotFather) (obrigatório) · [brapi.dev](https://brapi.dev) (recomendado)

Smoke test: `python -c "import telegram, httpx; print('OK')"`

---

## Roteiro — copie e cole no Agent

### Bloco 1 (0–5 min) — Abrir o Agent

1. Abra esta pasta no Cursor
2. Abra o painel **Agent** (Ctrl+I ou ícone lateral)
3. Plan mode: *"O que falta para este projeto ter um bot Telegram com /start?"*
4. Agent mode: *"Implemente o que planejamos seguindo @AGENTS.md"*

### Bloco 2 (5–20 min) — Bot vivo

Cole no **Agent mode**:

> Leia @AGENTS.md e @bot/config.py. Crie `bot/handlers/commands.py` com `/start` e `/help` e `bot/main.py` registrando os handlers. Use async, python-telegram-bot v21, token de config. Implemente tudo sem pedir confirmação.

Terminal: `python -m bot.main` → teste `/start` e `/help` no Telegram.

Se der erro, cole:

> O bot falhou com este erro: [cole o erro]. Corrija seguindo @AGENTS.md.

### Bloco 3 (20–40 min) — `/cotacao`

Cole no **Agent mode**:

> Leia @AGENTS.md. Crie `bot/quotes.py` com `get_quote(ticker)` via httpx e brapi.dev. Adicione `/cotacao` em `commands.py` formatando preço (R$) e variação (%). Trate erro 401 e ticker inválido com mensagem em português. Implemente tudo.

Teste: `/cotacao PETR4` · `/cotacao VALE3` · `/cotacao XXXX`

### Bloco 4 (40–55 min) — Alerta

Cole no **Agent mode**:

> Leia @AGENTS.md e @bot/main.py. Crie `bot/handlers/alerts.py` com `/alerta TICKER PRECO` (1 alerta por chat, memória). Use JobQueue a cada 60s; quando preço >= limite, envie mensagem. Registre handler e job em `main.py`. Implemente tudo.

Teste: `/alerta PETR4 0.01`

### Bloco 5 (55–60 min) — Fechamento

Recapitular: **prompt → Agent → terminal → Telegram**

Solução: [branch main](https://github.com/mateuscqueiros/telegram-stock-bot/tree/main)

---

## Troubleshooting

| Problema | Solução |
|---|---|
| Agent não responde / limite atingido | Use Chat do Cursor ou veja a solução na branch `main` |
| `KeyError: TELEGRAM_TOKEN` | Crie `.env` a partir de `.env.example` |
| `InvalidToken` | Token errado no `.env` |
| Bot não responde | `python -m bot.main` precisa estar rodando |
| brapi 401 | Adicione `BRAPI_TOKEN` ou use PETR4/VALE3/MGLU3/ITUB4 |
