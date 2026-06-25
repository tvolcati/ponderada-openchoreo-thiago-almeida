# Roteiro do Vídeo de Apresentação

Tempo alvo: 4 a 5 minutos.

## 1. Abertura

"Nesta atividade eu precisei criar uma instância local do OpenChoreo, validar o funcionamento da plataforma, acessar a interface web e, sempre que possível, publicar uma aplicação de exemplo. Neste repositório eu documentei o ambiente utilizado, os comandos executados, as evidências coletadas e os problemas encontrados durante a instalação." 

## 2. O que é o OpenChoreo

"O OpenChoreo é uma plataforma open source voltada para implantação e gestão de aplicações cloud-native. A ideia central é oferecer uma camada mais padronizada para criar, publicar e operar aplicações em Kubernetes, reduzindo o trabalho manual que normalmente fica espalhado entre scripts, manifests, pipelines e ferramentas de infraestrutura." 

"No ciclo de desenvolvimento, ele atua como uma plataforma de entrega e operação. O desenvolvedor consegue publicar componentes e acompanhar ambientes, enquanto a plataforma organiza os recursos necessários para execução." 

"Ele pode gerenciar diferentes tipos de componentes, como aplicações web, serviços, workers e tarefas agendadas, além de estruturar isso dentro de projetos, ambientes e data planes." 

## 3. Por que o OpenChoreo é útil para times de desenvolvimento

"Para times de desenvolvimento, o OpenChoreo é útil porque padroniza o deploy e reduz o acoplamento entre desenvolvimento e operação. Em vez de cada time manter seu próprio conjunto de scripts e configurações, a plataforma oferece um fluxo mais centralizado." 

"Isso ajuda na redução de atividades operacionais repetitivas, no gerenciamento centralizado de aplicações, em observabilidade e governança, e também acelera o processo de entrega, porque os recursos e ambientes já seguem uma estrutura previsível." 

## 4. Como foi realizada a instalação

"No meu caso, a máquina atendeu o Caminho A da atividade. O host tem Windows 11, Docker 29.1.3, 16 GB de memória física e 16 CPUs lógicas. Dentro do ambiente Docker eu observei cerca de 7.6 GB de memória disponível e 16 CPUs, então os requisitos mínimos foram atendidos." 

"Eu iniciei o container oficial do Quick Start do OpenChoreo com a imagem `ghcr.io/openchoreo/quick-start:v1.1.1`. Depois executei o script `install.sh --version v1.1.1` dentro do container." 

"O principal problema encontrado foi na primeira tentativa da instalação: eu usei `docker exec` sem definir o usuário, então o script acusou que não podia ser executado como root. A correção foi repetir o comando com `-u openchoreo`. Depois disso, a instalação terminou com sucesso em cerca de 4 minutos e 44 segundos." 

## 5. Principais componentes da plataforma

"Durante a instalação e a inspeção do cluster, eu identifiquei os principais conceitos da plataforma." 

"Projects são agrupamentos lógicos de componentes. No meu ambiente apareceu o projeto padrão `default`." 

"Components são as aplicações implantáveis. O componente principal criado nesta atividade foi o `react-starter`." 

"Environments representam os estágios de entrega, como development, staging e production." 

"Deployment Tracks são as trilhas de promoção entre esses ambientes." 

"Data Planes são os locais onde as cargas realmente rodam. No meu caso, o Data Plane padrão foi criado localmente pelo Quick Start." 

"Backstage é a interface portal usada pelo OpenChoreo para centralizar o acesso, catálogo e operações da plataforma." 

## 6. Demonstração da solução

"Aqui eu mostro primeiro a interface do OpenChoreo em execução no endereço `openchoreo.localhost:8080`. O login foi feito com as credenciais padrão do administrador e a home carregou corretamente." 

"Depois eu mostro as evidências coletadas no repositório: logs de instalação, validação com `check-status.sh` e `validate-installation.sh`, além das saídas dos comandos `kubectl` para namespaces, data planes, environments, projects, component types e components." 

"Na sequência eu demonstro a aplicação de exemplo publicada com o script `deploy-react-starter.sh`. O componente `react-starter` foi criado com sucesso e a aplicação ficou acessível pela URL gerada automaticamente pelo ambiente local." 

## 7. Fechamento

"Como conclusão, o OpenChoreo conseguiu ser instalado e validado integralmente no meu ambiente local. Os problemas encontrados foram operacionais, principalmente relacionados à forma de executar comandos dentro do container e à automação das evidências, mas todos foram resolvidos. O resultado final foi uma instância funcional da plataforma e uma aplicação exemplo publicada com sucesso." 
