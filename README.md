<div align="center">

# 🛡️ DIO Agent · Security Mentor

### Mentor de estudos que agora também ensina **cibersegurança defensiva e AppSec**

*Contexto antes de comandos. Entendimento antes de respostas prontas.*

![Foco](https://img.shields.io/badge/foco-defensivo_%26_educacional-0b7285)
![AppSec](https://img.shields.io/badge/AppSec-OWASP_%7C_CWE-d9480f)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-c92a2a)
![Harness](https://img.shields.io/badge/harness-Claude_Code-8A2BE2)
![Status](https://img.shields.io/badge/status-pronto-2f9e44)

</div>

---

## 📌 Visão geral

O **DIO Agent** nasceu como mentor de estudos da DIO: monta planos de estudo, propõe desafios, explica conceitos, ajuda com portfólio, pesquisa na web e acompanha a Carreira AI Builder.

Nesta evolução, ele ganhou uma **segunda especialização: mentoria em cibersegurança defensiva e AppSec**. Ele conduz o estudante da dúvida até a defesa, passo a passo, sem entregar exploits nem comandos para copiar sem entender.

## 🎯 Especialização e por quê

**Especialização:** mentor de segurança **100% defensivo e educacional**.

**Por que essa especialização:**

- **Segurança é o tipo de assunto em que resposta pronta machuca.** Um comando de firewall colado sem contexto pode derrubar o acesso ao servidor ou dar falsa sensação de proteção. Por isso o agente pergunta primeiro sobre o ambiente.
- **Quem estuda precisa entender o risco, não só aplicar a correção.** O agente mapeia cada fraqueza em padrões de mercado (OWASP, CWE e MITRE ATT&CK), o que prepara o estudante para o dia a dia profissional.
- **O limite ético fica explícito.** O agente explica riscos e orienta correção e validação, mas não fornece exploits ofensivos.

### Regras principais

| Regra | Comportamento |
|---|---|
| 🛡️ Uso exclusivamente defensivo | Explica riscos e mitigações, sem exploits prontos para ataque |
| ❓ Contexto antes de comandos | Em servidor, rede ou infraestrutura, faz **uma pergunta por vez** sobre o ambiente antes de sugerir qualquer comando ou regra |
| 🪜 Escada defensiva | Conduz o estudante de forma gradual em vez de entregar código ou comandos prontos |

## 🧩 A nova skill: `security-mentor`

Roteiro defensivo em **4 etapas**:

1. **Pedir contexto antes de agir:** o que está rodando, o que está exposto e qual o objetivo.
2. **Mapear superfície de ataque e risco** com OWASP, CWE e MITRE ATT&CK.
3. **Conduzir até a defesa** sem dar a resposta pronta.
4. **Validar a mitigação:** confirmar que o risco realmente foi reduzido.

## 🗂️ Arquivos criados e alterados

### Criados

| Arquivo | O que faz |
|---|---|
| `skills/security-mentor/SKILL.md` | **Skill** de mentoria defensiva em AppSec e proteção de ambientes (roteiro de 4 etapas) |
| `agent/knowledge/security-fundamentals.md` | **Conhecimento:** postura ética, conceitos de AppSec (consultas parametrizadas, hash e salt, menor privilégio), tabela de mapeamento OWASP/CWE ↔ MITRE ATT&CK (T1190, T1078, T1110, T1046), princípios de hardening e ciclo de validação |
| `app.py` | Aplicação de exemplo de login com SQLite, usada como laboratório de testes (veja a seção de testes) |

### Alterados

| Arquivo | O que mudou |
|---|---|
| `AGENTS.md` | Registro de `security-fundamentals.md` na **base de conhecimento**; skill **Mentoria em segurança** na tabela de skills; novas regras em *Limites e cuidados*: **Uso exclusivamente defensivo** e **Contexto antes de comandos** |
| `agent/persona.md` | Novo valor **Cautela e contexto**; novas restrições em *O que o DIO Agent não faz*: não fornecer exploits ofensivos e não sugerir comandos às cegas sem entender o cenário |
| `README.md` | Skill registrada na tabela pública de skills e novo modelo de prompt **Mentoria em segurança (AppSec e Hardening)** |
| `docs/glossary.md` | Verbetes didáticos com analogias: AppSec, SQL Injection (SQLi), Consulta Parametrizada, MITRE ATT&CK, Hardening e Superfície de Ataque |

### Estrutura relevante

```
.
├── AGENTS.md                         # regras, skills e base de conhecimento
├── app.py                            # app de laboratório (login + SQLite)
├── agent/
│   ├── persona.md                    # identidade, valores e limites
│   └── knowledge/
│       └── security-fundamentals.md  # conhecimento de segurança defensiva
├── skills/
│   └── security-mentor/
│       └── SKILL.md                  # roteiro defensivo em 4 etapas
└── docs/
    └── glossary.md                   # glossário com analogias
```

## ▶️ Como rodar o agente no harness

```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/NOME-DO-REPO.git
cd NOME-DO-REPO

# 2. Abra o harness na pasta do projeto
#    (ele carrega AGENTS.md, a persona, o conhecimento e as skills)
claude
```

Exemplos de prompt para acionar a skill:

```
> Mentoria em segurança: revise o app.py com foco em AppSec.
> Subi um servidor Ubuntu de laboratório exposto na internet. Quais comandos devo rodar agora?
```

No segundo exemplo, o agente **não responde com comandos**: ele pergunta primeiro o que está rodando e exposto no servidor e qual o objetivo do laboratório.

## 🚀 A melhoria escolhida

**Melhoria:** uma trilha de **mentoria defensiva guiada**, formada por skill, conhecimento e regras de persona que trabalham juntos.

- **Antes:** o agente ajudava nos estudos em geral, sem postura própria para segurança, e poderia responder a um pedido urgente de segurança com uma lista de comandos.
- **Depois:** o agente pede contexto, mapeia o risco em padrões de mercado, conduz o estudante até a mitigação e valida o resultado.
- **Por que escolhi esta:** segurança exige entender o cenário antes de agir, e a melhoria muda justamente esse comportamento.

Como melhoria complementar, atualizei o `README.md` e o `docs/glossary.md` para que a nova capacidade seja descoberta e entendida por quem estuda.

## 🧪 Testes realizados

| # | Teste | Resultado |
|---|---|---|
| 1 | Varredura AppSec no `app.py` **vulnerável** (login concatenando usuário e senha em f-string) | O subagente *AppSec Code Auditor* identificou **SQL Injection (CWE-89 / OWASP A03:2021)**, explicou conceitualmente o bypass de autenticação, mapeou para **T1190** (e **T1078** no impacto) e propôs consulta parametrizada |
| 2 | Nova varredura após a **correção** (`?` em `create_user` e `login`, `pbkdf2_hmac` com salt de 16 bytes e `hmac.compare_digest`) | SQLi (CWE-89 / T1190) **mitigado**; sem falhas críticas ou altas. Restaram só recomendações informativas, como usar 600.000 iterações no PBKDF2 e `getpass` na CLI |
| 3 | Pedido urgente sobre servidor Ubuntu exposto, com o agente carregando `AGENTS.md`, persona, conhecimento e skill | O agente **não sugeriu nenhum comando**, explicou o risco de agir às cegas, definiu hardening em linguagem simples e fez **uma pergunta de contexto** |

> ⚠️ **Limitação:** o Python não estava instalado no ambiente Windows dos testes. A validação do `app.py` foi feita por **inspeção e varredura estática AppSec**, sem execução em runtime.

## 🛣️ Próximos passos

- [ ] Rodar o `app.py` em runtime e adicionar testes automatizados
- [ ] Aplicar as recomendações de hardening (iterações do PBKDF2, `getpass`)
- [ ] Ampliar a skill para revisão de configuração de servidores e redes

## ⚖️ Uso responsável

Este projeto é **educacional e defensivo**. Use-o apenas em ambientes seus ou com autorização explícita.

---

<div align="center">

Feito por **Vinicius** · [GitHub](https://github.com/SEU-USUARIO)

</div>
