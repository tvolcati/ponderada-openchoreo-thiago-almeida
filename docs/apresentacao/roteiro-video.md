# Roteiro do Vídeo de Apresentação

Tempo alvo: 4 a 5 minutos.

## 1. Abertura

"Nesta atividade eu precisei criar uma instância local do OpenChoreo, validar o funcionamento da plataforma, acessar a interface web e publicar uma aplicação de exemplo. Neste repositório eu organizei a documentação técnica, as evidências de terminal, as capturas da interface e a análise dos problemas encontrados durante a execução."

## 2. O que é o OpenChoreo

"O OpenChoreo é uma plataforma open source voltada para implantação e gestão de aplicações cloud-native. A proposta da ferramenta é padronizar o processo de entrega em Kubernetes, reduzindo a necessidade de cada time manter scripts, manifests e fluxos operacionais próprios."

"No ciclo de desenvolvimento, ele funciona como uma camada de plataforma. O desenvolvedor publica componentes e interage com ambientes mais padronizados, enquanto o OpenChoreo organiza recursos, exposição de aplicações e parte da governança operacional."

"A plataforma consegue gerenciar diferentes tipos de componentes, como aplicações web, serviços, workers e tarefas agendadas."

## 3. Por que o OpenChoreo é útil para times de desenvolvimento

"O principal valor para times de desenvolvimento é a padronização de deploy. Em vez de cada equipe montar seu próprio fluxo, a plataforma oferece uma estrutura comum."

"Isso reduz trabalho operacional repetitivo, centraliza o gerenciamento das aplicações, melhora governança e observabilidade e acelera a entrega, porque os ambientes e os componentes passam a seguir uma convenção previsível."

## 4. Como foi realizada a instalação

"No meu caso, a máquina atendeu o Caminho A da atividade. O host estava com Windows 11, Docker 29.1.3, 16 GB de memória física e 16 CPUs lógicas. Dentro do ambiente Docker eu observei aproximadamente 7.6 GiB de memória disponível e 16 CPUs, então os requisitos mínimos foram atendidos com folga."

"Eu subi o container oficial do Quick Start do OpenChoreo com a imagem `ghcr.io/openchoreo/quick-start:v1.1.1`. Depois executei o script `install.sh --version v1.1.1` dentro do container."

"O principal problema encontrado foi na primeira tentativa da instalação: eu usei `docker exec` sem definir o usuário, então o script acusou que não podia ser executado como root. A correção foi repetir o comando com `-u openchoreo`. Depois disso, a instalação terminou com sucesso em cerca de 4 minutos e 44 segundos."

## 5. Principais componentes da plataforma

"Durante a instalação e a inspeção do cluster, eu consegui observar os principais conceitos da plataforma."

"Projects são agrupamentos lógicos de componentes. No meu ambiente apareceu o projeto padrão `default`."

"Components são as aplicações implantáveis. O componente principal criado nesta atividade foi o `react-starter`."

"Environments representam os estágios de entrega, como development, staging e production."

"Deployment Tracks representam a trilha de promoção entre esses ambientes."

"Data Planes são os locais onde as cargas realmente executam. No meu caso, o Data Plane padrão foi criado localmente pelo Quick Start."

"Backstage é a interface portal usada pelo OpenChoreo para centralizar o acesso, o catálogo e as operações da plataforma."

## 6. Demonstração da solução

"Aqui eu mostro primeiro a interface do OpenChoreo em execução no endereço `openchoreo.localhost:8080`. O login foi feito com as credenciais padrão do administrador e a home carregou corretamente."

"Depois eu mostro as evidências coletadas no repositório: logs de instalação, validação com `check-status.sh` e `validate-installation.sh`, além das saídas dos comandos `kubectl` para namespaces, data planes, environments, projects, component types e components."

"Na sequência eu demonstro a aplicação de exemplo publicada com o script `deploy-react-starter.sh`. O componente `react-starter` foi criado com sucesso e a aplicação ficou acessível pela URL gerada automaticamente pelo ambiente local."

## 7. Fechamento

"Como conclusão, o OpenChoreo conseguiu ser instalado e validado integralmente no meu ambiente local. Os problemas encontrados foram operacionais, principalmente relacionados à forma de executar comandos dentro do container e à automação das evidências, mas todos foram resolvidos. O resultado final foi uma instância funcional da plataforma e uma aplicação exemplo publicada com sucesso."
