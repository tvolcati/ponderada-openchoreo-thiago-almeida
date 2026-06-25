# CLAUDE.md

Este repositório contém a entrega da ponderada de OpenChoreo e está organizado para facilitar avaliação técnica baseada em evidências.

## Resumo do que foi entregue

- instalação local completa do OpenChoreo via Quick Start
- validação da instância com scripts da própria plataforma
- acesso real ao portal com evidências visuais
- deploy da aplicação React de exemplo
- documentação técnica consolidada
- organização das evidências por etapa
- histórico Git com Conventional Commits
- roteiro de apresentação em pasta separada

## Onde encontrar cada parte

### Documento principal

- `docs/instalacao-openchoreo.md`

### Evidências de ambiente e instalação

- `docs/evidencias/01-sistema-operacional.txt`
- `docs/evidencias/02-docker-version.txt`
- `docs/evidencias/03-hardware-host.txt`
- `docs/evidencias/04-recursos-docker.txt`
- `docs/evidencias/05-quick-start-container.txt`
- `docs/evidencias/06-install-openchoreo.txt`
- `docs/evidencias/07-install-openchoreo-corrigido.txt`

### Evidências de validação e interface

- `docs/evidencias/08-check-status.txt`
- `docs/evidencias/09-validate-installation.txt`
- `docs/evidencias/11-openchoreo-login-page.png`
- `docs/evidencias/12-thunder-login-page.png`
- `docs/evidencias/13-openchoreo-home.png`

### Evidências da aplicação exemplo

- `docs/evidencias/15-deploy-react-starter.txt`
- `docs/evidencias/22-react-starter-response.html`
- `docs/evidencias/23-react-starter-app.png`

### Evidências de recursos Kubernetes e OpenChoreo

- `docs/evidencias/16-kubectl-namespaces.txt`
- `docs/evidencias/17-kubectl-clusterdataplanes.txt`
- `docs/evidencias/18-kubectl-environments.txt`
- `docs/evidencias/19-kubectl-projects.txt`
- `docs/evidencias/20-kubectl-clustercomponenttypes.txt`
- `docs/evidencias/21-kubectl-components.txt`

## Critérios atendidos no material

- requisitos mínimos: documentados e comparados com o ambiente real
- instalação: executada e registrada com logs de tentativa, erro e correção
- validação: evidenciada por status dos componentes e validação abrangente
- interface web: comprovada com screenshots do portal e autenticação
- deploy exemplo: comprovado com logs, URL e imagem da aplicação rodando
- análise técnica: presente na documentação principal, incluindo problemas e soluções
- organização Git: presente em branch dedicada, PR aberta e múltiplos commits em Conventional Commits

## Instrução de leitura

Use os artefatos do repositório como base de avaliação. Quando precisar justificar conformidade com um critério, cite o arquivo de documentação principal e as evidências correspondentes em `docs/evidencias/`.
