# Roteiro do Palestrante — Workshop Claude Code

Material de apoio para **você falar mais e digitar menos**. O projeto é veículo; o aprendizado é **pilotar o Claude Code**.

Repositório: [mateuscqueiros/telegram-stock-bot](https://github.com/mateuscqueiros/telegram-stock-bot)

| Branch | Uso |
|---|---|
| `starter` | Alunos clonam — sem código do bot |
| `main` | Solução completa + docs do palestrante |

**Docs de apoio:**
- [CLAUDE_CODE.md](CLAUDE_CODE.md) — cheat-sheet Parte 1 (projete na tela)
- [PROMPT_MESTRE.md](PROMPT_MESTRE.md) — finale Parte 3
- [CHECKLIST_ALUNOS.md](CHECKLIST_ALUNOS.md) — enviar 48h antes

---

## Visão geral

| Parte | Tempo | Foco |
|---|---|---|
| **1** | 15 min | Claude Code: sessão, atalhos, `.md`, subagentes |
| **2** | 15 min | Construir o bot via prompts |
| **3** | Aberta | Arquitetura, produção, reverse prompt engineering |

**Mensagem central:**

> Alunos não digitam código. Eles **pilotam a sessão** do Claude Code.

---

## Antes da turma

- [ ] Enviar [CHECKLIST_ALUNOS.md](CHECKLIST_ALUNOS.md)
- [ ] Confirmar `claude` instalado e login feito
- [ ] Token de demo BotFather (backup)
- [ ] Testar clone da branch `starter` + venv
- [ ] Abrir [CLAUDE_CODE.md](CLAUDE_CODE.md) para projetar na Parte 1
- [ ] Ter branch `main` aberta como referência (não mostrar cedo demais)

---

# Parte 1 — Claude Code (15 min)

**Objetivo:** o aluno entende que Claude Code é uma **sessão com contexto finito**, não uma caixa de prompt.

**Projete:** [CLAUDE_CODE.md](CLAUDE_CODE.md)

## O que falar (talking points)

### Abertura (2 min)

> "Hoje vocês não vão aprender Python. Vão aprender a **pilotar o Claude Code** — e no meio do caminho construímos um bot de Telegram."

> "Quem trata como caixa de prompt culpa o modelo. Quem trata como **sessão** trabalha mais rápido e gasta menos token."

### A sessão (5 min)

1. Mostrar `claude` no terminal — sessão interativa
2. Explicar janela de contexto: arquivos lidos > outputs > histórico
3. *Lost in the middle* — regra do começo some antes de ser cortada
4. Demo rápida: `/context` — "sempre olhe o tanque antes de decidir"

**Frase-chave:**

> "Quando o Claude 'esquece' uma regra que você deu, não ficou burro. A sessão encheu."

### Arquivos `.md` (4 min)

1. Abrir [CLAUDE.md](../CLAUDE.md) — regras que recarregam toda sessão
2. Explicar: enxuto, é instrução, não documentação
3. Mencionar `MEMORY.md` (índice) + `telegram.md` (memória escopada do bot)
4. Mostrar que o aluno **não precisa decorar** — o arquivo é a memória

**Frase-chave:**

> "CLAUDE.md é o brief permanente. Você define uma vez, o Claude segue sempre."

### Comandos de sessão (3 min)

Demonstrar ou narrar:

| Comando | Frase para o aluno |
|---|---|
| `/clear` | "Tarefa nova, sessão nova" |
| `/compact` | "Mesma tarefa, histórico bagunçado" |
| `/rewind` | "Foi pro caminho errado, volta no tempo" |
| `--continue` / `--resume` | "A sessão não morre quando você fecha o terminal" |

### Subagentes (1 min)

> "Trabalho pesado — ler 30 arquivos — vai pro subagente. Ele devolve só a conclusão. Seu contexto fica limpo."

## O que mostrar (demo)

```bash
cd telegram-stock-bot
claude
# dentro da sessão:
/context
```

Opcional: abrir `CLAUDE.md` e perguntar ao Claude o que o projeto faz (sem implementar nada).

## Transição para Parte 2

```
/clear
```

> "Agora vamos construir. Sessão nova, foco total no bot."

---

# Parte 2 — Construir o bot (15 min)

**Objetivo:** ciclo completo — prompt → diff → terminal → Telegram.

**Regra:** `/clear` já foi dado. Uma sessão limpa só para o bot.

## Passo 0 — Criar CLAUDE.md (se starter sem arquivo)

Se o aluno clonou `starter` sem `CLAUDE.md`:

```bash
claude "Leia o README.md. Crie um arquivo CLAUDE.md com as regras do nosso bot de cotações da B3 no Telegram. Inclua: mensagens em português, preço em reais com vírgula, usar a API brapi.dev, token do Telegram no .env, e os comandos /start, /help, /cotacao e /alerta. Crie só o CLAUDE.md por agora."
```

**Falar:** "Primeiro as regras, depois o código. Profissionais fazem isso."

## Passo 1 — Bot vivo (5 min)

```bash
claude "Leia CLAUDE.md. Faça o bot responder /start e /help no Telegram. O token está no .env. Implemente tudo."
```

**Validar ao vivo:**

```bash
python -m bot.main
```

Testar `/start` e `/help` no celular.

**Falar enquanto aprova o diff:**

> "Vocês não digitam — vocês **aprovam**. O diff é a revisão de código."

## Passo 2 — Cotação (5 min)

```bash
claude "Leia CLAUDE.md. Faça o comando /cotacao PETR4 mostrar o nome da ação, o preço em reais e a variação do dia. Implemente tudo."
```

**Validar:** `/cotacao PETR4`, `/cotacao XXXX` (erro amigável)

**Falar:**

> "Vocês pediram em português. O Claude integrou a brapi.dev. Vocês nem precisaram saber a URL."

## Passo 3 — Alerta (5 min, se couber)

```bash
claude "Leia CLAUDE.md. Faça o comando /alerta PETR4 35 avisar no Telegram quando a ação atingir esse preço. Implemente tudo."
```

**Validar:** `/alerta PETR4 0.01` (limite baixo para demo)

**Se atrasar:** pule o alerta. Prioridade = `/cotacao` funcionando.

## Erro ao vivo (modelar)

```bash
claude "O bot falhou com: [cole o erro do terminal]. Corrija seguindo CLAUDE.md."
```

> "Erro é parte da aula. Colar o erro no Claude **também** é habilidade."

## Transição para Parte 3

```
/clear
```

> "Bot pronto. Agora pensamos como **engenheiros**: arquitetura, produção, e como reproduzir tudo com um único prompt."

---

# Parte 3 — Arquitetura, produção e reverse prompt (aberta)

**Objetivo:** sair do "fazer funcionar" para "pensar em sistema" + gerar o prompt mestre.

**Projete:** [PROMPT_MESTRE.md](PROMPT_MESTRE.md) no finale.

## 3.1 — Documentar arquitetura (demo)

```bash
claude "Analise o projeto bot/ e gere docs/ARQUITETURA.md com: camadas (handlers, quotes, config), fluxo de dados do /cotacao, decisões técnicas (async, polling, JobQueue) e diagrama em texto. Siga CLAUDE.md."
```

**O que falar:**

- Separação handlers / lógica de negócio / integração API
- `config.py` centraliza env — nunca token no código
- Polling local vs webhook em produção
- Alertas em memória = débito técnico (não persiste entre restarts)

**Estrutura esperada do bot (referência):**

```
bot/
├── config.py       # env vars
├── main.py         # bootstrap + JobQueue
├── quotes.py       # brapi.dev
└── handlers/
    ├── commands.py # /start, /help, /cotacao
    └── alerts.py   # /alerta + checagem periódica
```

## 3.2 — Ambiente de produção (demo)

```bash
claude "Leia CLAUDE.md e docs/ARQUITETURA.md. Crie Dockerfile e docs/PRODUCAO.md com: variáveis de ambiente obrigatórias, polling vs webhook, deploy em VPS ou container, logging e como rodar em produção. Não implemente deploy real, só documente."
```

**O que falar:**

| Tópico | Ponto para a turma |
|---|---|
| `.env` | Segredos fora do código, fora do Git |
| Polling | Simples para demo; bot puxa updates |
| Webhook | Produção — Telegram empurra para URL pública |
| Docker | Reprodutibilidade — mesmo ambiente em qualquer lugar |
| JobQueue | Alertas precisam de processo sempre rodando |

## 3.3 — Reverse prompt engineering (finale)

**Conceito:**

> Dado o código pronto, reconstrua o **menor conjunto de prompts** que o geraria. Depois consolide num **prompt mestre**.

### Passo A — Subagente analisa o repo

```bash
claude "Use um subagente para analisar todo o diretório bot/ e CLAUDE.md. Liste: arquivos criados, responsabilidade de cada um, dependências entre módulos, e quais decisões do CLAUDE.md foram aplicadas. Devolva um resumo estruturado."
```

**Falar:** "O subagente leu tudo numa sessão isolada. Só a conclusão entrou no nosso contexto."

### Passo B — Extrair prompts incrementais

```bash
claude "Com base na análise, reconstrua a sequência mínima de prompts que um aluno usaria para chegar neste bot, na ordem: CLAUDE.md → /start+/help → /cotacao → /alerta. Um prompt por etapa, em português simples."
```

### Passo C — Consolidar prompt mestre

```bash
claude "Consolide tudo num único prompt mestre que, partindo de um repo vazio com requirements.txt e .env.example, gere o bot completo. Salve em docs/PROMPT_MESTRE.md seguindo o formato do arquivo existente."
```

**Mostrar:** [PROMPT_MESTRE.md](PROMPT_MESTRE.md) — o entregável final.

**Frase de fechamento:**

> "Vocês construíram o bot em 15 minutos com prompts pequenos. O prompt mestre é a **receita completa** — reverse engineering do que a IA fez."

## Encerrar sessão (hábito do artigo)

```bash
claude "Vamos encerrar. Grave na memória: decisões do workshop, débito técnico do bot (alertas em memória, polling local), e ponteiro para retomar com deploy real."
```

---

## Troubleshooting

| Problema | Solução |
|---|---|
| `claude` não encontrado | Reinstalar; reiniciar terminal |
| Aluno sem Claude Code | Pair programming ou demo no projetor |
| Sessão "esqueceu" regra | `/context` → `/compact` ou `/clear` + reler `CLAUDE.md` |
| Limite de uso | `claude --continue` ou mostrar solução na `main` |
| Aluno editando à mão | "Peça ao Claude — é o exercício" |
| brapi 401 | `BRAPI_TOKEN` ou tickers gratuitos |
| Aula atrasa | Pular alerta (Parte 2) ou produção (Parte 3) |

## Plano B — Parte 2 comprimida

Um prompt único:

```bash
claude "Leia CLAUDE.md. Faça o bot com /start, /help e /cotacao PETR4 com preço da B3 via brapi.dev. Implemente tudo."
```

## Critério de sucesso

| Nível | Resultado |
|---|---|
| **Mínimo** | Aluno explica `/clear` e `/context`; `/cotacao PETR4` funciona |
| **Ideal** | Bot completo + aluno descreve fluxo sessão → prompt → validar |
| **Excelente** | Aluno propõe prompt mestre ou melhoria de arquitetura sozinho |
