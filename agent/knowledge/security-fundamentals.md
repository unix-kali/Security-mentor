[security-fundamentals.md](https://github.com/user-attachments/files/35384718/security-fundamentals.md)

# Fundamentos de Segurança Defensiva e AppSec

Base de conhecimento para o Agent orientar estudantes em segurança de aplicações (AppSec), proteção de ambientes (hardening) e leitura defensiva de ameaças.

## Postura defensiva e limites éticos

- **Defesa em primeiro lugar:** o papel do agente é ensinar a proteger sistemas, encontrar fraquezas em código próprio ou de estudo e corrigir vulnerabilidades.
- **Ambiente controlado:** explicações sobre como uma falha pode ser explorada devem permanecer no nível conceitual e didático, sem entregar exploits prontos para atacar alvos reais ou de terceiros.
- **Contexto obrigatório:** nunca recomende comandos de infraestrutura, rede ou alterações de segurança sem antes entender o ambiente do estudante (sistema, serviços expostos, forma de acesso e objetivo do laboratório).

## Conceitos essenciais de AppSec

AppSec (*Application Security*) é a prática de construir e revisar software para reduzir falhas desde o código.

- **Separação entre código e dados (contra SQL Injection — CWE-89 / OWASP A03:2021):** nunca concatene ou interpole entrada do usuário diretamente em comandos SQL. Use **consultas parametrizadas** (*prepared statements* / placeholders), nas quais o banco compila a estrutura da consulta separada dos valores.
- **Gestão segura de credenciais (CWE-256 / CWE-916):** senhas nunca devem ser salvas em texto puro. Utilize funções de derivação de chave adequadas com *salt* único por usuário e comparação em tempo constante.
- **Menor privilégio:** aplicações, usuários e contas de banco devem ter apenas as permissões estritamente necessárias para funcionar.
- **Validação de entradas e segredos fora do código:** trate toda entrada externa como não confiável e evite credenciais fixas (*hardcoded*) no código-fonte.

## Mapeamento defensivo: OWASP e MITRE ATT&CK

Enquanto o **OWASP Top 10** e a **CWE** classificam a fraqueza no software, o **MITRE ATT&CK** descreve táticas e técnicas que adversários usam na prática. Usar os dois juntos ajuda o estudante a ligar uma linha de código ou uma porta aberta ao impacto real e ao controle defensivo certo.

| Cenário / Fraqueza | Referência OWASP / CWE | Técnica MITRE ATT&CK | Foco defensivo |
|--------------------|------------------------|----------------------|----------------|
| SQL Injection em formulário ou API | A03:2021 Injection / CWE-89 | **T1190** — *Exploit Public-Facing Application* | Consultas parametrizadas, validação de entrada e menor privilégio no banco |
| Uso de credenciais vazadas, fracas ou padrão | A07:2021 Identification and Authentication Failures / CWE-798 | **T1078** — *Valid Accounts* | Troca de credenciais padrão, chaves SSH em vez de senha, MFA e hash seguro |
| Tentativas repetidas de login (força bruta) | A07:2021 / CWE-307 | **T1110** — *Brute Force* | Limite de tentativas (*rate limiting*), bloqueio temporário, desabilitar login por senha quando aplicável |
| Serviços desnecessários expostos na rede | A05:2021 Security Misconfiguration | **T1046** — *Network Service Discovery* | Reduzir superfície de ataque, fechar portas não usadas e aplicar firewall restritivo |

## Princípios de hardening de servidores e laboratórios

Ao orientar alguém com um servidor de laboratório (como uma VM Ubuntu exposta na internet), guie o raciocínio por pilares antes de falar em comandos específicos:

1. **Entender a exposição:** o que precisa estar acessível na internet e o que deveria ficar apenas local ou atrás de VPN/rede privada?
2. **Controle de acesso:** quem acessa o servidor e por qual método (chave criptográfica vs. senha, conta root direta vs. usuário comum com `sudo`)?
3. **Firewall e superfície mínima:** negar conexões de entrada por padrão e liberar somente as portas estritamente necessárias, além de desativar serviços sem uso.
4. **Manutenção e visibilidade:** manter pacotes de segurança atualizados e saber onde consultar logs de autenticação e acesso para detectar tentativas suspeitas.
5. **Segurança operacional do estudante:** antes de aplicar filtros de rede, garantir que a regra do acesso administrativo atual esteja contemplada para o estudante não se trancar fora do próprio servidor.

## Ciclo de validação

Toda correção de segurança precisa ser verificada depois de aplicada:

1. **Identificar:** localizar o risco no código ou no ambiente.
2. **Mapear:** explicar o impacto e a técnica associada (OWASP / CWE / MITRE ATT&CK).
3. **Mitigar:** conduzir o estudante na aplicação da correção defensiva.
4. **Revalidar:** executar nova varredura ou checagem após a alteração para confirmar que a falha foi mitigada e nenhum novo risco foi introduzido.
