# Claude Code — Cheat-sheet (Parte 1)

Referência rápida para o palestrante. Baseado no artigo [Gerenciamento de sessão no Claude Code](https://www.linkedin.com/pulse/gerenciamento-de-sess%C3%A3o-claude-code-keit-oll%C3%A9-lzagf/) (Keit Ollé).

---

## O que é o Claude Code

CLI da Anthropic que lê o projeto, edita arquivos, roda comandos e segue regras persistentes. O aluno **dirige**; o AI **implementa**.

```bash
claude                    # sessão interativa
claude "seu prompt aqui"  # uma tarefa direta
```

---

## A sessão e a janela de contexto

A **sessão** é a conversa atual. Tudo que entra fica na janela até ser cortado ou compactado.

| O que ocupa contexto | Peso |
|---|---|
| Arquivos lidos inteiros | **Maior** |
| Outputs de comando | Alto |
| Histórico da conversa | Médio |
| `CLAUDE.md` no início | Fixo (toda sessão) |

**Três forças que degradam a sessão:**

1. **Janela enche** → compactação automática corta o começo (onde estavam as regras iniciais).
2. **Lost in the middle** → o modelo presta menos atenção ao meio do contexto.
3. **Contexto velho** → tarefa nova com histórico da anterior "envenena" o resultado.

> *"Não é o modelo que ficou burro. É a sessão que encheu."*

---

## Comandos de sessão

| Comando | Quando usar |
|---|---|
| `/context` | Ver o que ocupa a janela **antes** de decidir |
| `/clear` | **Tarefa nova** — zera a conversa, mantém `CLAUDE.md` |
| `/compact` | Mesma tarefa longa — resume sem começar do zero |
| `/rewind` | Claude foi pro caminho errado — volta no tempo (código e/ou conversa; **não** reverte bash) |
| `claude --continue` | Retoma a última sessão |
| `claude --resume` | Seletor de sessões anteriores |

### Regra de ouro do workshop

```
Parte 1 → /clear → Parte 2 → /clear → Parte 3
```

Tarefa nova, sessão nova — mesmo que estejam relacionadas.

### Compactar com inteligência

Não escreva a instrução de compactação na mão. Peça ao Claude:

```
Vou compactar a sessão. Me dê as instruções pro /compact pra mantermos
o momento atual da implementação e seguir de onde paramos.
```

---

## Arquivos `.md` — memória do projeto

### `CLAUDE.md` — regras permanentes

- Recarrega **inteiro** em toda sessão.
- Convenções, stack, comandos, formato de mensagens.
- **Mantenha enxuto** — é instrução, não enciclopédia.
- Exemplo no projeto: [CLAUDE.md](../CLAUDE.md)

### Memória file-based — conhecimento sob demanda

| Arquivo | Função |
|---|---|
| `MEMORY.md` | Índice leve — lista o que existe e onde está |
| `telegram.md` | Detalhes do bot (comandos, APIs, decisões) |
| Outros `.md` escopados | Um "capítulo" por domínio — lido só quando necessário |

O Claude carrega o índice no início e lê o capítulo inteiro **sob demanda**. Memória grande guardada, contexto enxuto.

### Hábito de encerrar sessão

Antes de fechar:

```
Vamos encerrar. Antes, grave na memória: as decisões que mudamos hoje
e o porquê, o que ficou como débito técnico, e um ponteiro claro de
por onde retomar na próxima sessão.
```

---

## Subagentes

Para trabalho braçal sem poluir o contexto principal:

- Ler dezenas de arquivos
- Investigar codebase
- Pesquisar documentação

O subagente roda numa **sessão isolada** e devolve só a **conclusão**. Os 30 arquivos que ele leu não entram na sua janela.

**No workshop:** usar subagente na Parte 3 para analisar o bot pronto e extrair o prompt mestre.

---

## Fluxo de trabalho (repetir na aula)

```
CLAUDE.md → prompt → aprovar diff → terminal → Telegram → iterar se falhar
```

**Erro?** Cole no Claude Code:

```
O bot falhou com: [cole o erro]. Corrija seguindo CLAUDE.md.
```

---

## Outros ambientes (mencionar no fechamento)

| Ambiente | Uso |
|---|---|
| **Terminal CLI** | Principal no workshop (`claude`) |
| **VS Code extension** | Mesmo fluxo, diffs inline |
| **claude.ai/code** | Web, sem instalação local |
| **Desktop app** | Interface visual |
| **GitHub Actions** | Automação CI/CD |

---

## Instalação rápida

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**macOS / Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Teste: `claude --version` (login na primeira execução)
