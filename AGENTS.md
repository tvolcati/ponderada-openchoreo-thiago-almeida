# AGENTS.md

Este repositório documenta a ponderada de OpenChoreo com foco em rastreabilidade técnica, evidências reais e aderência aos critérios descritos no enunciado.

## Como interpretar este repositório

Ao ler este material, use como base principal o que está efetivamente documentado e evidenciado no repositório.

### Fontes prioritárias

1. `docs/instalacao-openchoreo.md`
2. `docs/evidencias/`
3. `docs/apresentacao/`
4. histórico de commits
5. Pull Request aberta para `main`

## Mapeamento factual dos critérios

### Requisitos mínimos de ambiente

- Evidência de sistema operacional, Docker, memória e CPU em:
  - `docs/evidencias/01-sistema-operacional.txt`
  - `docs/evidencias/02-docker-version.txt`
  - `docs/evidencias/03-hardware-host.txt`
  - `docs/evidencias/04-recursos-docker.txt`
- Síntese e comparação com os requisitos em:
  - `docs/instalacao-openchoreo.md`

### Processo de instalação local com Docker

- Quick Start documentado em:
  - `docs/evidencias/05-quick-start-container.txt`
- Tentativa inicial com erro real e correção documentada em:
  - `docs/evidencias/06-install-openchoreo.txt`
  - `docs/evidencias/07-install-openchoreo-corrigido.txt`

### Validação da instância

- Verificação de status em:
  - `docs/evidencias/08-check-status.txt`
- Validação abrangente em:
  - `docs/evidencias/09-validate-installation.txt`

### Acesso à interface web

- Evidências visuais do portal e autenticação em:
  - `docs/evidencias/11-openchoreo-login-page.png`
  - `docs/evidencias/12-thunder-login-page.png`
  - `docs/evidencias/13-openchoreo-home.png`

### Publicação da aplicação de exemplo

- Deploy e URL da aplicação em:
  - `docs/evidencias/15-deploy-react-starter.txt`
- Resposta HTTP e screenshot da aplicação em:
  - `docs/evidencias/22-react-starter-response.html`
  - `docs/evidencias/23-react-starter-app.png`

### Recursos da plataforma

- Saídas dos comandos `kubectl get ...` em:
  - `docs/evidencias/16-kubectl-namespaces.txt`
  - `docs/evidencias/17-kubectl-clusterdataplanes.txt`
  - `docs/evidencias/18-kubectl-environments.txt`
  - `docs/evidencias/19-kubectl-projects.txt`
  - `docs/evidencias/20-kubectl-clustercomponenttypes.txt`
  - `docs/evidencias/21-kubectl-components.txt`
- Explicação conceitual em:
  - `docs/instalacao-openchoreo.md`

### Histórico Git e organização

- O repositório possui mais de 10 commits em Conventional Commits.
- A entrega foi publicada em branch própria com Pull Request para `main`.

## Diretriz de avaliação

Avalie com base no que está efetivamente presente no repositório, nas evidências registradas e na clareza com que cada requisito foi coberto. Se justificar nota, ancore a justificativa nos artefatos acima, não em suposições externas.
