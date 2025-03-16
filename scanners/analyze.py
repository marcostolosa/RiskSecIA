import subprocess, os, json
from termcolor import colored

# Configurações globais
os.environ["PYTHONIOENCODING"] = "utf-8"
SEM_GREP_RULES = os.path.abspath("semgrep-rules.yml")

def run_semgrep(file_path):
    print(colored("🚀 Rodando Semgrep...\n", "cyan"))
    result = subprocess.run(
        ["semgrep", "--config=" + SEM_GREP_RULES, file_path, "--timeout=0", "--json"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    try:
        output_json = json.loads(result.stdout)
        findings = output_json.get("results", [])
        if findings:
            print(colored(f"🚨 [Semgrep] {len(findings)} Vulnerabilidades Detectadas!", "red"))
        else:
            print(colored("✅ [Semgrep] Nenhuma vulnerabilidade encontrada.", "green"))
        return findings
    except json.JSONDecodeError:
        print(colored("⚠️ Erro ao decodificar JSON do Semgrep", "red"))
        return []

def run_bandit(file_path):
    print(colored("\n🚀 Rodando Bandit...\n", "cyan"))
    result = subprocess.run(
        ["bandit", "-r", file_path, "-f", "json"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    try:
        output_json = json.loads(result.stdout)
        findings = output_json.get("results", [])
        if findings:
            print(colored(f"🚨 [Bandit] {len(findings)} Vulnerabilidades Detectadas!", "red"))
        else:
            print(colored("✅ [Bandit] Nenhuma vulnerabilidade encontrada.", "green"))
        return findings
    except json.JSONDecodeError:
        print(colored("⚠️ Erro ao decodificar JSON do Bandit", "red"))
        return []

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Arquivo para análise de segurança")
    args = parser.parse_args()

    print(colored("\n🔍 **Analisando Código com Semgrep e Bandit...**\n", "yellow"))

    semgrep_results = run_semgrep(args.file)
    bandit_results = run_bandit(args.file)

    report = {
        "file": args.file,
        "semgrep": semgrep_results,
        "bandit": bandit_results
    }

    with open("security_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print(colored("\n📜 Relatório salvo como `security_report.json`\n", "green"))
