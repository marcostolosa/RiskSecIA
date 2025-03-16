# RiskSec AI - Analisador Inteligente de Segurança de Aplicações

## 📌 Descrição
**RiskSec AI** é uma ferramenta **open-source** que automatiza a **análise de segurança de aplicações** utilizando **Inteligência Artificial** e scanners avançados como **Semgrep**, **Bandit**, **Nuclei**, **CodeQL** e **ScanAPI**.

### 🔍 O que o RiskSec AI faz?
✅ **Análise estática de código-fonte** para encontrar vulnerabilidades.  
✅ **Detecção de falhas comuns** como **SQL Injection, RCE, XSS, Hardcoded Secrets** e mais.  
✅ **Integração com IA** para **recomendar mitigações inteligentes** usando modelos como **Ollama, CodeLlama e DeepSeek-Coder**,.  
✅ **Automatização de relatórios** para integração com **DevSecOps e CI/CD**.  
✅ **Cálculo de risco residual** e **Criação de Cenários de Risco** após avaliação.  
✅ **Monitoramento de tendências de vulnerabilidades** com **dashboards Grafana**.  

---

## 🚀 Tecnologias Utilizadas
| **Tecnologia**   | **Uso no Projeto**  |
|-----------------|--------------------|
| **Python 3.10+** | Backend e automação |
| **FastAPI** | API para análise de código |
| **Semgrep / Bandit / CodeQL / ScanAPI** | Scanners de segurança |
| **Ollama / CodeLlama / DeepSeek-Coder** | Modelos de IA para análise de código |
| **Docker** | Containers e deploy |
| **Grafana / Prometheus** | Dashboards de segurança |
| **GitHub Actions** | CI/CD para análise automatizada |

---

## 📂 Estrutura do Projeto
```
RiskSecAI/
│── models/               # Modelos de IA (Ollama, CodeLlama, DeepSeek)
│── scanners/             # Ferramentas de análise (Semgrep, Bandit, CodeQL, ScanAPI)
│── api/                  # FastAPI para expor os resultados
│── tests/                # Casos de teste e exemplos de código vulnerável
│── config/               # Configurações do projeto (YAML, JSON)
│── dashboards/           # Relatórios de segurança (Grafana)
│── scripts/              # Scripts auxiliares (deploy, setup)
│── requirements.txt      # Dependências do projeto
│── README.md             # Introdução ao projeto
```

---

## 🔥 Como Usar
### 1️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Rodar a API
```bash
uvicorn api.server:app 
```

### 3️⃣ Testar análise de segurança
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@uploads/teste.py'
```

---

## 🔥 Integração com IA (Em Desenvolvimento)
### 📌 Objetivo
Usar **modelos de IA** para **melhorar a análise de segurança**, sugerindo **correções inteligentes** e fornecendo **Insights Estratégicos** com base no código analisado.

### 🔧 Modelos Planejados:
✅ **Ollama** - Detecção de vulnerabilidades e refatoração automática.  
✅ **CodeLlama** - Análise de padrões de segurança no código.  
✅ **DeepSeek-Coder** - Sugestões de mitigação baseadas em **Machine Learning**.  

---

## 📊 Roadmap
✅ Criar estrutura base do projeto  
✅ Implementar API REST com FastAPI  
✅ Processamento em paralelo com **Multiprocessing**  
✅ Integrar Semgrep, Bandit, CodeQL e ScanAPI  
⏳ Adicionar suporte ao **Ollama** para detecção IA  
⏳ Gerar relatórios e dashboards com **Grafana**  
⏳ Criar sistema de pontuação de risco  

---

## 🤝 Contribuição
🔹 Pull requests são muito bem-vindos!  
