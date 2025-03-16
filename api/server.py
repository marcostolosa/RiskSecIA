import os
import json
import subprocess
import multiprocessing
from fastapi import FastAPI, File, UploadFile

# Configuração do FastAPI
app = FastAPI()

# Diretórios e caminhos de ferramentas
UPLOAD_DIR = "uploads"
SEM_GREP_RULES = os.path.abspath("semgrep-rules.yml")
SEM_GREP_PATH = os.path.join(os.getcwd(), "venv", "Scripts", "semgrep")  # Garante o uso do semgrep no venv

# Criar pasta uploads se não existir
os.makedirs(UPLOAD_DIR, exist_ok=True)

def semgrep_worker(file_path, queue):
    """Executa o Semgrep e captura saída"""
    try:
        result = subprocess.run(
            [SEM_GREP_PATH, "scan", "--config=semgrep-rules.yml", file_path, "--json", "--timeout=0", "--force-color"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        try:
            output = json.loads(result.stdout)
            queue.put(output)
        except json.JSONDecodeError:
            queue.put({
                "errors": [
                    {
                        "message": "Semgrep retornou saída inválida.",
                        "stderr": result.stderr,
                        "raw_output": result.stdout
                    }
                ]
            })

    except subprocess.TimeoutExpired:
        queue.put({"errors": [{"message": "Semgrep travou devido ao tempo limite."}]})

    except Exception as e:
        queue.put({"errors": [{"message": f"Erro inesperado no Semgrep: {str(e)}"}]})

def run_semgrep(file_path):
    """Inicia o Semgrep em um subprocesso"""
    multiprocessing.set_start_method("spawn", force=True)  # Garante compatibilidade com Windows
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=semgrep_worker, args=(file_path, queue))
    process.start()
    process.join()

    if not queue.empty():
        return queue.get()
    return {"errors": [{"message": "Semgrep falhou sem resposta válida."}]}

def bandit_worker(file_path, queue):
    """Executa o Bandit e captura saída"""
    try:
        result = subprocess.run(
            ["bandit", "-r", file_path, "-f", "json"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        try:
            queue.put(json.loads(result.stdout))
        except json.JSONDecodeError:
            queue.put({"errors": [{"message": "Bandit retornou saída inválida."}]})

    except subprocess.TimeoutExpired:
        queue.put({"errors": [{"message": "Bandit travou devido ao tempo limite."}]})

    except Exception as e:
        queue.put({"errors": [{"message": f"Erro inesperado no Bandit: {str(e)}"}]})

def run_bandit(file_path):
    """Inicia o Bandit em um subprocesso"""
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=bandit_worker, args=(file_path, queue))
    process.start()
    process.join()

    if not queue.empty():
        return queue.get()
    return {"errors": [{"message": "Bandit falhou sem resposta válida."}]}

@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    """Recebe um arquivo, salva e executa os scanners"""
    
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    
    # Salva o arquivo na pasta uploads
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())

    # Executa as ferramentas de análise
    semgrep_results = run_semgrep(file_location)
    bandit_results = run_bandit(file_location)

    return {
        "semgrep": semgrep_results,
        "bandit": bandit_results
    }
