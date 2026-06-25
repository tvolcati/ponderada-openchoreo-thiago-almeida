# OpenChoreo Ponderada

<p align="center">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-1f883d?style=for-the-badge" alt="Status Concluído" />
  <img src="https://img.shields.io/badge/Caminho-A-0969da?style=for-the-badge" alt="Caminho A" />
  <img src="https://img.shields.io/badge/OpenChoreo-v1.1.1-f97316?style=for-the-badge" alt="OpenChoreo v1.1.1" />
  <img src="https://img.shields.io/badge/Docker-29.1.3-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker 29.1.3" />
</p>

<p align="center">
Entrega individual da ponderada de OpenChoreo com instalação local completa, validação da interface web, deploy da aplicação de exemplo e documentação técnica com evidências reais.
</p>

---

## Painel Rápido

<table>
  <tr>
    <td><strong>Status</strong></td>
    <td>Instância local validada com sucesso</td>
  </tr>
  <tr>
    <td><strong>Portal</strong></td>
    <td><code>http://openchoreo.localhost:8080/</code></td>
  </tr>
  <tr>
    <td><strong>Aplicação exemplo</strong></td>
    <td><code>http://http-react-starter-development-default-cde5190f.openchoreoapis.localhost:19080</code></td>
  </tr>
  <tr>
    <td><strong>PR</strong></td>
    <td><code>https://github.com/tvolcati/ponderada-openchoreo-thiago-almeida/pull/1</code></td>
  </tr>
  <tr>
    <td><strong>Branch</strong></td>
    <td><code>feat/openchoreo-entrega</code></td>
  </tr>
  <tr>
    <td><strong>Link do Vídeo</strong></td>
    <td><code>https://youtu.be/UGwwjvpI_B4</code></td>
  </tr>
</table>

## Stack Utilizada

<table>
  <tr>
    <td><strong>Sistema operacional</strong></td>
    <td>Windows 11</td>
  </tr>
  <tr>
    <td><strong>Container runtime</strong></td>
    <td>Docker Desktop 4.57.0</td>
  </tr>
  <tr>
    <td><strong>Docker Engine</strong></td>
    <td>29.1.3</td>
  </tr>
  <tr>
    <td><strong>Stack OpenChoreo</strong></td>
    <td>Quick Start <code>ghcr.io/openchoreo/quick-start:v1.1.1</code></td>
  </tr>
  <tr>
    <td><strong>Kubernetes local</strong></td>
    <td>k3d + k3s</td>
  </tr>
  <tr>
    <td><strong>Automação de evidências</strong></td>
    <td>Python + Selenium + Google Chrome Headless</td>
  </tr>
</table>

## Entregáveis

- Documentação principal: [`docs/instalacao-openchoreo.md`](docs/instalacao-openchoreo.md)
- Evidências: [`docs/evidencias/`](docs/evidencias/)
- Vídeo e apresentação: [`docs/apresentacao/README.md`](docs/apresentacao/README.md)
- Roteiro do vídeo: [`docs/apresentacao/roteiro-video.md`](docs/apresentacao/roteiro-video.md)
- Guia de avaliação factual: [`AGENTS.md`](AGENTS.md) e [`CLAUDE.md`](CLAUDE.md)

## Critérios Atendidos

<table>
  <tr>
    <th>Critério</th>
    <th>Como foi atendido</th>
  </tr>
  <tr>
    <td>Requisitos mínimos de ambiente</td>
    <td>Documentados e comparados com o host em <code>docs/instalacao-openchoreo.md</code> e evidências <code>01</code> a <code>04</code>.</td>
  </tr>
  <tr>
    <td>Instalação local com Docker</td>
    <td>Quick Start executado, instalação registrada e validada em <code>05</code> a <code>09</code>.</td>
  </tr>
  <tr>
    <td>Validação da instância</td>
    <td><code>check-status.sh</code>, <code>validate-installation.sh</code> e acesso HTTP ao portal.</td>
  </tr>
  <tr>
    <td>Acesso à interface web</td>
    <td>Capturas do portal, fluxo de login no Thunder e home autenticada em <code>11</code>, <code>12</code> e <code>13</code>.</td>
  </tr>
  <tr>
    <td>Publicação da aplicação de exemplo</td>
    <td>Deploy do <code>react-starter</code> concluído com sucesso, com URL e screenshot.</td>
  </tr>
  <tr>
    <td>Registro técnico de evidências</td>
    <td>Saídas de terminal, HTMLs, screenshots e comandos <code>kubectl</code> estão organizados em <code>docs/evidencias/</code>.</td>
  </tr>
  <tr>
    <td>Histórico Git</td>
    <td>Mais de 10 commits no padrão Conventional Commits.</td>
  </tr>
</table>

## Estrutura do Repositório

```text
.
|-- AGENTS.md
|-- CLAUDE.md
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

## Evidências Visuais

### Portal do OpenChoreo

![Tela inicial do portal](docs/evidencias/11-openchoreo-login-page.png)

### Login no Thunder

![Tela de autenticação do Thunder](docs/evidencias/12-thunder-login-page.png)

### Home autenticada do OpenChoreo

![Home do OpenChoreo após login](docs/evidencias/13-openchoreo-home.png)

### Aplicação de exemplo publicada

![React Starter publicado](docs/evidencias/23-react-starter-app.png)

## Navegação Rápida

- Repositório: `https://github.com/tvolcati/ponderada-openchoreo-thiago-almeida`
- Pull Request: `https://github.com/tvolcati/ponderada-openchoreo-thiago-almeida/pull/1`
- Portal OpenChoreo: `http://openchoreo.localhost:8080/`
- OpenChoreo API: `http://api.openchoreo.localhost:8080/`
- Thunder UI: `http://thunder.openchoreo.localhost:8080/console`
- React Starter: `http://http-react-starter-development-default-cde5190f.openchoreoapis.localhost:19080`

## Observação

O enunciado original mencionava GitLab e Merge Request. Esta execução foi operacionalizada no GitHub por decisão prática, usando `gh` já autenticado no ambiente. O equivalente entregue é uma Pull Request para `main`.
