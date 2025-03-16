import os
import subprocess

def run_analysis(file_path):
    result = subprocess.run(
        ["semgrep", "--config=auto", file_path],
        capture_output=True,
        text=True,
        encoding="utf-8"  # 🔥 Força a saída UTF-8 para evitar erros de encoding no Windows
    )
    return result.stdout

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Arquivo para análise de segurança")
    args = parser.parse_args()
    print(run_analysis(args.file))
