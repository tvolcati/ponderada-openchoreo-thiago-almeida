# Ponderada OpenChoreo

Entrega individual da atividade de validação local do OpenChoreo, com instalação completa via Docker, acesso à interface do portal e publicação da aplicação React de exemplo.

## Visão Geral

- Status: concluído com sucesso
- Caminho executado: `Caminho A`
- Plataforma de versionamento usada na entrega: `GitHub`
- Pull Request: `https://github.com/tvolcati/ponderada-openchoreo-thiago-almeida/pull/1`

## Stack Utilizada

- Sistema operacional: `Windows 11`
- Container runtime: `Docker Desktop 4.57.0`
- Docker Engine: `29.1.3`
- OpenChoreo Quick Start: `ghcr.io/openchoreo/quick-start:v1.1.1`
- Kubernetes local: `k3d` com `k3s`
- Automação de evidências: `Python`, `Selenium`, `Google Chrome Headless`

## Resultados Obtidos

- Instância local do OpenChoreo instalada com sucesso
- Portal acessível em `http://openchoreo.localhost:8080/`
- Validação interna concluída com `check-status.sh` e `validate-installation.sh`
- Aplicação de exemplo `react-starter` publicada com sucesso
- Evidências reais organizadas em `docs/evidencias/`
- Histórico com mais de 10 commits em Conventional Commits

## Links e Acessos

- Repositório: `https://github.com/tvolcati/ponderada-openchoreo-thiago-almeida`
- Pull Request: `https://github.com/tvolcati/ponderada-openchoreo-thiago-almeida/pull/1`
- Portal OpenChoreo: `http://openchoreo.localhost:8080/`
- OpenChoreo API: `http://api.openchoreo.localhost:8080/`
- Thunder UI: `http://thunder.openchoreo.localhost:8080/console`
- React Starter: `http://http-react-starter-development-default-cde5190f.openchoreoapis.localhost:19080`

## Estrutura do Repositório

```text
.
|-- README.md
|-- docs
|   |-- apresentacao
|   |   |-- README.md
|   |   `-- roteiro-video.md
|   |-- evidencias
|   `-- instalacao-openchoreo.md
`-- scripts
    `-- capture_openchoreo.py
```

## Navegação Rápida

- Documentação principal: [`docs/instalacao-openchoreo.md`](docs/instalacao-openchoreo.md)
- Evidências: [`docs/evidencias/`](docs/evidencias/)
- Apresentação e vídeo: [`docs/apresentacao/README.md`](docs/apresentacao/README.md)
- Roteiro do vídeo: [`docs/apresentacao/roteiro-video.md`](docs/apresentacao/roteiro-video.md)

## Evidências Visuais

### Portal do OpenChoreo

![Tela inicial do portal](docs/evidencias/11-openchoreo-login-page.png)

### Login no Thunder

![Tela de autenticação do Thunder](docs/evidencias/12-thunder-login-page.png)

### Home autenticada do OpenChoreo

![Home do OpenChoreo após login](docs/evidencias/13-openchoreo-home.png)

### Aplicação de exemplo publicada

![React Starter publicado](docs/evidencias/23-react-starter-app.png)

## Documentos Principais

- `docs/instalacao-openchoreo.md`
  - ambiente utilizado
  - requisitos e comparação com o host
  - comandos executados
  - problemas encontrados e soluções adotadas
  - recursos da plataforma e interpretação técnica
- `docs/apresentacao/README.md`
  - espaço para o link final do vídeo
  - observação indicando que o roteiro está disponível caso o vídeo apresente erro
- `docs/apresentacao/roteiro-video.md`
  - roteiro completo da apresentação em até 5 minutos

## Observação Sobre o Enunciado

O enunciado original mencionava GitLab e Merge Request. Esta execução foi operacionalizada no GitHub por decisão prática, usando `gh` já autenticado no ambiente. O equivalente entregue é uma Pull Request para `main`.
