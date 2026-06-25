# Ponderada OpenChoreo

Entrega individual da atividade de validação local do OpenChoreo com Docker, interface Backstage/OpenChoreo em execução e deploy da aplicação de exemplo.

## Repositório

- Repositório GitHub: https://github.com/tvolcati/ponderada-openchoreo-thiago-almeida
- Branch de trabalho: `feat/openchoreo-entrega`
- Documentação principal: `docs/instalacao-openchoreo.md`
- Roteiro do vídeo: `docs/roteiro-video.md`

## Resultado final

- Instância local do OpenChoreo instalada com sucesso.
- Interface acessível em `http://openchoreo.localhost:8080/`.
- Aplicação exemplo publicada com sucesso.
- Evidências reais armazenadas em `docs/evidencias/`.
- Histórico com commits no padrão Conventional Commits.

## URLs validadas

- OpenChoreo Portal: `http://openchoreo.localhost:8080/`
- OpenChoreo API: `http://api.openchoreo.localhost:8080/`
- Thunder UI: `http://thunder.openchoreo.localhost:8080/console`
- React Starter: `http://http-react-starter-development-default-cde5190f.openchoreoapis.localhost:19080`

## Evidências principais

- Ambiente: `docs/evidencias/01-sistema-operacional.txt` a `04-recursos-docker.txt`
- Quick Start e instalação: `docs/evidencias/05-quick-start-container.txt`, `06-install-openchoreo.txt`, `07-install-openchoreo-corrigido.txt`
- Validação: `docs/evidencias/08-check-status.txt`, `09-validate-installation.txt`
- Interface: `docs/evidencias/11-openchoreo-login-page.png`, `12-thunder-login-page.png`, `13-openchoreo-home.png`
- Aplicação exemplo: `docs/evidencias/15-deploy-react-starter.txt`, `23-react-starter-app.png`
- Recursos Kubernetes/OpenChoreo: `docs/evidencias/16-kubectl-namespaces.txt` a `21-kubectl-components.txt`

## Observação sobre o enunciado

O enunciado original pedia GitLab e Merge Request. Esta execução foi realizada no GitHub por decisão operacional, usando `gh` já autenticado no ambiente. O equivalente entregue aqui é um Pull Request para `main`.
