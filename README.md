# RiskSec AI - Analisador Inteligente de Segurança de Aplicações

## 📌 Descrição
RiskSec AI é uma ferramenta open-source que automatiza a **análise de segurança de aplicações** usando **modelos de IA open-source** como CodeLlama, DeepSeek-Coder e ScanAPI. 

O sistema realiza:
- **Análise de código-fonte** para encontrar vulnerabilidades.
- **Geração de cenários de risco** simulando ataques reais.
- **Cálculo de notas de risco residual** após mitigação.
- **Geração de relatórios completos** para integração com DevSecOps.

## 🚀 Tecnologias Utilizadas
- **Linguagem**: Python 3.10+
- **Modelos de IA**: CodeLlama, DeepSeek-Coder, ScanAPI
- **Análise de Código**: CodeQL, Semgrep, Bandit
- **Framework Web**: FastAPI (para API e integração com CI/CD)
- **Infraestrutura**: Docker, GitHub Actions, Grafana (para dashboards)

## 📂 Estrutura do Projeto
```
RiskSecAI/
│── models/               # Modelos de IA (CodeLlama, DeepSeek, etc.)
│── scanners/             # Ferramentas de análise (CodeQL, Semgrep, Bandit)
│── api/                  # FastAPI para expor os resultados
│── tests/                # Casos de teste e exemplos de código vulnerável
│── config/               # Configurações do projeto (YAML, JSON)
│── docs/                 # Documentação (como instalar, usar, etc.)
│── scripts/              # Scripts auxiliares (deploy, setup)
│── requirements.txt      # Dependências do projeto
│── README.md             # Introdução ao projeto
```

## 🔥 Como Usar
### 1️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Rodar a API
```bash
uvicorn api.main:app --reload
```

### 3️⃣ Testar análise de segurança
```bash
python scanners/analyze.py --file teste.py
```

## 📍 Roadmap
✅ Criar estrutura base do projeto
✅ Integrar modelos de IA para análise de código
⏳ Implementar API REST
⏳ Gerar relatórios completos e dashboards
