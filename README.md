# 🏥 Sistema de Avaliação de Sarcopenia

<p align="center">
  <a href="https://ufsc.br">
    <img src="https://identidade.ufsc.br/wp-content/themes/brasilGovInterno/img/brasao_site_ufsc.svg?ver=1746558968" alt="UFSC Logo" width="100">
  </a>
</p>

<p align="center">
  <strong>UFSC - Universidade Federal de Santa Catarina</strong><br>
  <strong>Campus Araranguá - Engenharia de Computação</strong>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python"></a>
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-4.2%2B-green" alt="Django"></a>
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-Ready-2496ED" alt="Docker"></a>
  <a href="https://ararangua.ufsc.br/"><img src="https://img.shields.io/badge/UFSC-Ararangu%C3%A1-003366" alt="UFSC"></a>
</p>

## 📋 Informações do Projeto

- **Disciplina**: DEC0013 - Projeto Integrador
- **Semestre**: 2025.2
- **Tipo**: TRABALHO-DISCIPLINA
- **Área**: SOFTWARE / WEB / SAÚDE
- **Tecnologia Principal**: Python, Django, Docker

### 🔗 Links Rápidos

🐳 **[Docker Hub](https://hub.docker.com/r/mfkaner/sarcopenia-pi-25-2)**  • 🔬 **[Protocolo de Avaliação](docs/pdfs/Manual_SBGG.pdf)**

---

## 📖 Visão Geral

Aplicação web desenvolvida com Django para avaliação clínica de sarcopenia em pacientes idosos e obesos. O sistema oferece uma interface completa para profissionais de saúde realizarem avaliações padronizadas, registrarem dados antropométricos e gerarem relatórios diagnósticos baseados em critérios científicos validados.

### Objetivo

Fornecer uma ferramenta digital para profissionais da saúde que facilite:

- Cadastro e gestão de pacientes
- Aplicação de questionários padronizados de triagem
- Registro de medidas antropométricas e testes funcionais
- Cálculo automático de índices diagnósticos
- Geração de relatórios e histórico clínico
- Acompanhamento longitudinal de pacientes

### Contexto Acadêmico

Projeto desenvolvido como trabalho da disciplina de **Projeto Integrador (DEC0013)** no curso de Engenharia de Computação da UFSC Araranguá, integrando conhecimentos de desenvolvimento web, banco de dados e aplicações na área da saúde.

---

## ✨ Funcionalidades

### 1. Gestão de Usuários e Autenticação

#### Sistema de Contas
- ✅ Cadastro de profissionais de saúde
- ✅ Login seguro com autenticação Django
- ✅ Perfis diferenciados (professor coordenador e estudante avaliador)
- ✅ Gestão de permissões por tipo de usuário

### 2. Gestão de Pacientes

#### Cadastro Completo
- **Dados Pessoais**: Nome, CPF, data de nascimento, contato
- **Antropometria**: Peso e altura

#### Busca e Filtros
- Busca por nome
- Visualização em lista
- Exportação de dados para PDF

### 3. Questionários de Avaliação

#### SARC-F
Questionário de triagem com 5 domínios:
- **Força**: Dificuldade em carregar peso
- **Assistência para caminhar**: Necessidade de auxílio
- **Levantar de cadeira**: Capacidade funcional
- **Subir escadas**: Desempenho físico
- **Quedas**: Histórico de quedas no último ano
- **CP**: Circunferência Panturrilha

**Interpretação automática**:
- Score ≥11: Indicativo de sarcopenia (encaminhar para avaliação completa)

### 4. Testes Funcionais e Medidas

#### Testes de Desempenho Físico
- **Velocidade de Marcha**:
  - Teste de caminhada de 4 metros
  - Cálculo automático: velocidade = distância/tempo
  - Classificação por ponto de corte (<0.8 m/s indica sarcopenia)

- **Força de Preensão Manual**:
  - Medição com dinamômetro (kg)
  - Pontos de corte ajustados por sexo e IMC

- **Teste de levantar e sentar**:
  - Realizadas 5 repetições
  - Classificação por ponto de corte (> 15s indica provável sarcopenia)

#### Composição Corporal
- **Bioimpedância**:
  - Massa muscular esquelética apendicular
  
- **Índices Calculados**:
  - **IMMEA** (Índice de massa muscular esquelética apendicular)

### 5. Diagnóstico e Classificação

#### Classificação Automática
- **Provável Sarcopenia**: Força muscular reduzida
- **Sarcopenia Confirmada**: Força + massa muscular reduzida
- **Sarcopenia Grave**: Força + massa + desempenho físico reduzidos

### 6. Relatórios e Acompanhamento

#### Geração de Relatórios
- **Relatório Individual**: Dados completos de uma avaliação
- **Relatório Comparativo**: Evolução temporal do paciente
- **Export**: PDF

---

## 🚀 Acesso Rápido

### Via Docker (Recomendado)

#### Pré-requisitos
- Docker Desktop instalado e em execução
- 4GB de RAM disponível
- Porta 8080 livre

#### Passo 1: Instalar Docker
1. Acesse: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Baixe e instale a versão para seu sistema operacional
3. Abra o **Docker Desktop** e aguarde inicialização completa

#### Passo 2: Baixar Imagem
```bash
docker pull mfkaner/sarcopenia-pi-25-2
```

#### Passo 3: Executar Aplicação
```bash
docker run -d -p 8080:8000 --name sarcopenia-app mfkaner/sarcopenia-pi-25-2
```

**Explicação dos parâmetros:**
- `-d`: Executa em segundo plano (libera o terminal)
- `-p 8080:8000`: Mapeia porta 8080 do host para 8000 do container
- `--name sarcopenia-app`: Define nome do container

#### Passo 4: Acessar Sistema
Abra seu navegador e acesse: **http://localhost:8080**

⚠️ **Nota**: A primeira carga pode levar alguns segundos devido à inicialização das bibliotecas.

#### Comandos Úteis

**Verificar containers em execução:**
```bash
docker ps
```

**Parar aplicação:**
```bash
docker stop sarcopenia-app
```

**Reiniciar aplicação:**
```bash
docker start sarcopenia-app
```

**Ver logs:**
```bash
docker logs sarcopenia-app
```

**Remover container:**
```bash
docker rm -f sarcopenia-app
```

**Atualizar para versão mais recente:**
```bash
docker pull mfkaner/sarcopenia-pi-25-2:latest
docker stop sarcopenia-app
docker rm sarcopenia-app
docker run -d -p 8080:8000 --name sarcopenia-app mfkaner/sarcopenia-pi-25-2:latest
```

---

## 📦 Requisitos de Software

### Ambiente de Desenvolvimento

- **Sistema Operacional**: Windows 10/11, Linux (Ubuntu 20.04+) ou macOS 11+
- **Python**: Versão 3.10 ou superior
- **IDE Recomendada**: VS Code
- **Navegador**: Chrome, Firefox, Safari ou Edge (versão atualizada)
- **Docker**: Para execução em container

### Dependências Python

```txt
# Framework Web
Django>=4.2.0              # Framework web principal
django-crispy-forms>=2.0   # Formulários estilizados
crispy-bootstrap4>=2.0     # Bootstrap 4 para forms

# Autenticação e Segurança
django-allauth>=0.54.0     # Sistema de autenticação completo
django-cors-headers>=4.0   # CORS para APIs

# APIs e Serialização
djangorestframework>=3.14  # REST API framework

# Relatórios e Exportação
weasyprint>=66.0             # Geração de PDFs

```

---

## 📁 Estrutura do Projeto

```
2025.2_DEC0013_AVALIACAO-SARCOPENIA/
│
├── manage.py                      # CLI do Django
├── requirements.txt               # Dependências Python
├── Dockerfile                     # Container Docker
├── .gitignore                    # Arquivos ignorados pelo Git
├── .env.example                  # Exemplo de variáveis de ambiente
├── README.md                     # Este arquivo
│
├── config/                        # ⚙️ Configurações do Projeto
│   ├── __init__.py
│   ├── settings.py               # Configurações principais
│   │   ├── SECRET_KEY           # Chave secreta (produção)
│   │   ├── DEBUG                # Modo debug
│   │   ├── ALLOWED_HOSTS        # Hosts permitidos
│   │   ├── DATABASES            # Configuração do banco
│   │   ├── INSTALLED_APPS       # Apps instalados
│   │   └── MIDDLEWARE           # Middlewares
│   ├── urls.py                   # URLs principais
│   ├── wsgi.py                   # WSGI para produção
│   └── asgi.py                   # ASGI para websockets
│
├── conta/                         # 👤 App de Autenticação
│   ├── models.py                 # Modelo de Usuário customizado
│   │   └── User                 # Perfil, tipo, especialidade
│   ├── views.py                  # Views de login/registro
│   │   ├── LoginView           # Autenticação
│   │   ├── RegisterView        # Cadastro
│   │   ├── ProfileView         # Perfil do usuário
│   │   └── LogoutView          # Logout
│   ├── forms.py                  # Formulários de autenticação
│   ├── urls.py                   # URLs do app
│   └── templates/conta/          # Templates HTML
│       ├── login.html
│       ├── register.html
│       └── profile.html
│
├── questionario/                  # 📝 App de Avaliações
│   ├── models.py                 # Modelos de dados
│   │   ├── Paciente            # Dados do paciente
│   │   ├── Avaliacao           # Avaliação geral
│   │   ├── SARC_F              # Questionário SARC-F
│   │   ├── TesteFuncional      # Testes físicos
│   │   ├── Bioimpedancia       # Composição corporal
│   │   └── Diagnostico         # Classificação final
│   │
│   ├── views.py                  # Lógica de negócio
│   │   ├── PacienteListView    # Lista de pacientes
│   │   ├── PacienteCreateView  # Cadastro
│   │   ├── AvaliacaoView       # Nova avaliação
│   │   ├── SARCFView           # Questionário SARC-F
│   │   ├── TestesView          # Testes funcionais
│   │   ├── DiagnosticoView     # Classificação
│   │   └── RelatorioView       # Geração de relatórios
│   │
│   ├── forms.py                  # Formulários personalizados
│   │   ├── PacienteForm
│   │   ├── SARCFForm
│   │   ├── TestesFuncionaisForm
│   │   └── BioimpedanciaForm
│   │
│   ├── utils.py                  # Funções auxiliares
│   │   ├── calcular_imc()
│   │   ├── calcular_smi()
│   │   ├── classificar_sarcopenia()
│   │   └── gerar_relatorio_pdf()
│   │
│   ├── urls.py                   # Roteamento do app
│   │
│   └── templates/questionario/   # Templates HTML
│       ├── base.html            # Template base
│       ├── paciente_list.html   # Lista de pacientes
│       ├── paciente_form.html   # Formulário de paciente
│       ├── avaliacao_form.html  # Formulário de avaliação
│       ├── sarc_f.html          # SARC-F
│       ├── testes.html          # Testes funcionais
│       ├── diagnostico.html     # Resultado
│       └── relatorio.html       # Relatório completo
│
├── templates/                     # 🎨 Templates Globais
│   ├── base.html                 # Base principal
│   ├── navbar.html               # Barra de navegação
│   ├── footer.html               # Rodapé
│   ├── home.html                 # Página inicial
│   └── 404.html                  # Página de erro
│
├── static/                        # 📦 Arquivos Estáticos
│   ├── css/
│   │   ├── style.css            # Estilos customizados
│   │   └── bootstrap.min.css    # Bootstrap
│   ├── js/
│   │   ├── main.js              # JavaScript principal
│   │   ├── charts.js            # Gráficos (Chart.js)
│   │   └── validation.js        # Validações de formulários
│   └── img/
│       ├── logo.png
│       └── icons/
│
├── media/                         # 📁 Uploads de Usuários
│   ├── pacientes/                # Fotos de pacientes
│   ├── exames/                   # Arquivos de exames
│   └── relatorios/               # PDFs gerados
│
├── docs/                          # 📚 Documentação
│   ├── API.md                    # Documentação da API
│   ├── MANUAL_USUARIO.pdf        # Manual do usuário
│   ├── PROTOCOLO_CLINICO.pdf     # Protocolo de avaliação
│   └── REFERENCIAS.md            # Referências científicas
│
└── tests/                         # 🧪 Testes Automatizados
    ├── test_models.py            # Testes de modelos
    ├── test_views.py             # Testes de views
    ├── test_forms.py             # Testes de formulários
    └── test_utils.py             # Testes de utilitários
```

### Descrição dos Módulos Principais

#### Core do Django

- **manage.py**: Interface de linha de comando do Django
- **config/**: Configurações centralizadas do projeto
- **urls.py**: Sistema de roteamento URL

#### Apps Funcionais

**conta/**
- Autenticação de usuários
- Perfis personalizados por tipo de profissional
- Gerenciamento de permissões

**questionario/**
- Cadastro e gestão de pacientes
- Aplicação de questionários e testes
- Cálculos diagnósticos
- Geração de relatórios

#### Interface e Assets

**templates/**
- HTML com sistema de herança Django
- Componentes reutilizáveis

**static/**
- CSS (Bootstrap + customizações)
- JavaScript (validações, gráficos)
- Imagens e ícones

**media/**
- Uploads de usuários (fotos, exames)
- Relatórios gerados dinamicamente

---

## 🔬 Protocolo de Avaliação

### Fluxo Completo de Avaliação

```

```
---

## 📖 Como Usar

### Fluxo Básico de Uso

**1. Acesso ao Sistema**
- Acesse http://localhost:8080
- Faça login com suas credenciais
- Primeiro acesso: Criar conta de profissional

**2. Cadastro de Paciente**
- Menu: Pacientes → Novo Paciente
- Preencha dados pessoais e clínicos
- Registre medidas antropométricas básicas
- Salve o cadastro

**3. Nova Avaliação**
- Selecione o paciente na lista
- Clique em "Nova Avaliação"
- Preencha data e motivo da avaliação

**4. Aplicar SARC-F**
- Responda as 5 perguntas do questionário
- Sistema calcula score automaticamente
- Score ≥ 4: Continue para avaliação completa
- Score < 4: Orientações de monitoramento

**5. Diagnóstico**
- Sistema gera diagnóstico automático baseado nos dados
- Visualize classificação e recomendações
- Gere relatório em PDF

**6. Acompanhamento**
- Visualize histórico de avaliações do paciente
- Compare evolução de medidas ao longo do tempo
- Exporte dados para análise externa

### Exemplo Prático: Caso Clínico

**Cenário**: Paciente do sexo feminino, 72 anos, com queixa de fraqueza

```
👤 Dados do Paciente:
   Nome: Maria Silva
   Idade: 72 anos
   Sexo: Feminino
   Peso: 58 kg
   Altura: 1.55 m
   IMC: 24.1 kg/m² (Peso normal)

📝 SARC-F:
   Força: 2 pontos (muita dificuldade em carregar 4.5kg)
   Assistência: 0 pontos (caminha sem auxílio)
   Levantar: 1 ponto (alguma dificuldade)
   Subir escadas: 2 pontos (muita dificuldade)
   Quedas: 1 ponto (1-3 quedas no último ano)
   → TOTAL: 6 pontos ⚠️ (Indicativo de sarcopenia)

💪 Testes Funcionais:
   Hand Grip: 14.5 kg (média de 3 tentativas)
   → Abaixo do ponto de corte (16 kg) ❌
   
   Velocidade de Marcha: 0.75 m/s (4m em 5.3s)
   → Abaixo do ponto de corte (0.8 m/s) ❌
   
   SPPB: 7 pontos
   → Abaixo do ponto de corte (8 pontos) ❌

🔬 Bioimpedância:
   Massa Muscular Esquelética: 13.2 kg
   SMI: 5.5 kg/m²
   → No limite inferior (ponto de corte: 5.5 kg/m²) ⚠️

📋 DIAGNÓSTICO:
   ⚠️ SARCOPENIA GRAVE
   
   Critérios atendidos:
   ✓ Força muscular reduzida (força preensão palmar < 16 kg)
   ✓ Massa muscular reduzida (SMI = 5.5 kg/m²)
   ✓ Desempenho físico reduzido (velocidade < 0.8 m/s, SPPB ≤ 8)
   
   Recomendações:
   - Encaminhar para programa de exercícios resistidos
   - Avaliação nutricional para adequação proteica
   - Reavaliação em 3 meses
   - Considerar suplementação de vitamina D
```

---

## 🛠️ Tecnologias Utilizadas

### Backend

- **[Python 3.10+](https://www.python.org/)** - Linguagem de programação principal
- **[Django 4.2+](https://www.djangoproject.com/)** - Framework web de alto nível
- **[Django REST Framework](https://www.django-rest-framework.org/)** - APIs RESTful
- **[MySql](https://www.mysql.com/)** - Banco de dados (desenvolvimento)

### Frontend

- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)** - Estrutura semântica
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)** - Estilização moderna
- **[Bootstrap 4](https://getbootstrap.com/docs/4.6/)** - Framework CSS responsivo
- **[JavaScript ES6+](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** - Interatividade
- **[SweetAlert2](https://sweetalert2.github.io/)** - Alertas

### DevOps e Deployment

- **[Docker](https://www.docker.com/)** - Containerização
- **[Docker Hub](https://hub.docker.com/)** - Registry de imagens
- **[Gunicorn](https://gunicorn.org/)** - WSGI HTTP Server

### Bibliotecas Especializadas

- **[Weasyprint](https://weasyprint.org/)** - Geração de PDFs

### Ferramentas de Desenvolvimento

- **[Git](https://git-scm.com/)** - Controle de versão
- **[GitHub](https://github.com/)** - Hospedagem de código
- **[VS Code](https://code.visualstudio.com/)** - IDE recomendada

---

## 🧪 Validação e Testes

### Metodologia de Validação

O sistema foi validado através de:

1. **Testes Unitários**: Validação de funções de cálculo
2. **Testes de Integração**: Fluxo completo de avaliação
3. **Validação Clínica**: Comparação com casos reais
4. **Testes de Usabilidade**: Feedback de profissionais de saúde

### Casos de Teste

#### Teste 1: Cálculo de IMC

```python
Entrada:
  Peso: 70 kg
  Altura: 1.75 m

Resultado Esperado:
  IMC = 70 / (1.75)² = 22.86 kg/m²
  Classificação: Peso Normal

Resultado do Sistema:
  IMC = 22.86 kg/m² ✓
  Classificação: Peso Normal ✓
```

#### Teste 2: Classificação SARC-F

```python
Entrada:
  Q1 (Força): 2 pontos
  Q2 (Assistência): 0 pontos
  Q3 (Levantar): 1 ponto
  Q4 (Escadas): 2 pontos
  Q5 (Quedas): 0 pontos
  P1 (Circunferência Panturrilha): 32 cm

Resultado Esperado:
  Total: 15 pontos
  Interpretação: Ir para próxima etapa

Resultado do Sistema:
  Total: 15 pontos ✓
  Interpretação: Ir para próxima etapa ✓
```

#### Teste 3: Diagnóstico Completo

```python
Paciente: Sexo Masculino, 75 anos

Dados:
  Força de Preensão Palmar: 25 kg (< 27 kg) → Força Reduzida
  SMI: 6.8 kg/m² (< 7.0 kg/m²) → Massa Reduzida
  Velocidade: 0.9 m/s (> 0.8 m/s) → Desempenho Normal

Resultado Esperado:
  Diagnóstico: Sarcopenia Confirmada
  (força + massa reduzidas, desempenho normal)

Resultado do Sistema:
  Diagnóstico: Sarcopenia Confirmada ✓
```

---

## 👥 Contribuidores

Este projeto foi desenvolvido por estudantes do curso de **Engenharia de Computação** da **UFSC Araranguá** como trabalho da disciplina **DEC0013 - Projeto Integrador**.

### Equipe de Desenvolvimento

- **[Arthur Benedet dos Santos Custodio]**
- **[Kaio Francisco Martinhago]**
- **[Pablo da Rosa Pimentel]** 

### Orientação Acadêmica

- **Prof. [Jim Lau e Olga Yevseyeva]** - Orientadores

---

## 🏛️ Instituição

**Universidade Federal de Santa Catarina**  
**Centro de Ciências, Tecnologias e Saúde**  
**Campus Araranguá**  
**Curso de Engenharia de Computação**

[![Site UFSC](https://img.shields.io/badge/Site-UFSC%20Ararangu%C3%A1-003366?style=for-the-badge)](https://ararangua.ufsc.br/)
[![Curso](https://img.shields.io/badge/Curso-Engenharia%20de%20Computa%C3%A7%C3%A3o-blue?style=for-the-badge)](https://ararangua.ufsc.br/curso-de-engenharia-de-computacao/)

### Contato
             
🌐 Website: [https://ararangua.ufsc.br](https://ararangua.ufsc.br)  
📍 Endereço: Rodovia Governador Jorge Lacerda, 3201 - Araranguá/SC

---

## ❓ Perguntas Frequentes (FAQ)

### Instalação e Configuração

**Q: Preciso instalar o Python na minha máquina para usar o sistema?**  
A: Não, se você usar o Docker. Basta ter o Docker instalado e seguir os passos da seção "Acesso Rápido".

**Q: O sistema funciona offline?**  
A: Atualmente não. É necessária conexão com internet para acessar o sistema hospedado ou para baixar a imagem Docker.

### Uso Clínico

**Q: O sistema substitui a avaliação clínica profissional?**  
A: Não. O sistema é uma ferramenta de apoio. O diagnóstico final deve sempre ser feito por um profissional de saúde qualificado.

**Q: Quais profissionais podem usar o sistema?**  
A: Médicos, fisioterapeutas, enfermeiros e educadores físicos que trabalham com idosos.

**Q: Os dados dos pacientes são seguros?**  
A: Sim. O sistema segue as normas da LGPD, com dados criptografados e acesso restrito por autenticação.

---

## 📸 Capturas de Tela

### Tela de Login
![Login](docs/imgs/login.png)
*Interface de autenticação com suporte a múltiplos tipos de usuário*

### Lista de Pacientes
![Pacientes](docs/imgs/lista_avaliacoes.png)
*Gestão completa com busca e filtros avançados*

### Formulário SARC-F
![SARC-F](docs/imgs/formulario.png)

*Questionário de triagem com cálculo automático*

### Testes Funcionais
<p align="center">
  <img src="docs/imgs/2_etapa.png" alt="Etapa 2" width="80%">
  <br><br>
  <img src="docs/imgs/3_etapa.png" alt="Etapa 3" width="80%">
  <br><br>
  <img src="docs/imgs/4_etapa.png" alt="Etapa 4" width="80%">
</p>

*Interface para registro de testes funcionais*

### Resultado Diagnóstico
![Diagnóstico](docs/imgs/resultado.png)

*Classificação automática com recomendações clínicas*

### Relatório PDF
<p align="center">
  <img src="docs/imgs/exportavel_exemplo_1.png" alt="Relatório página 1" width="45%">
  <img src="docs/imgs/exportavel_exemplo_2.png" alt="Relatório página 2" width="45%">
</p>

*Relatório completo exportável em PDF*
*Relatório completo exportável em PDF*

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no GitHub!**

🔬 **[Protocolo Clínico](docs/pdfs/Manual_SBGG.pdf)**

---

**Desenvolvido com carinho por estudantes de Engenharia de Computação da UFSC Araranguá**