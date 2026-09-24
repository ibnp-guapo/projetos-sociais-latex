import os
import subprocess
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
TESTS_DIR = ROOT_DIR / "tests"

class TestIBNPBaseLatex(unittest.TestCase):
    def test_gitignore_exists_and_contains_rules(self):
        """Verifica se .gitignore existe e contém as extensões essenciais do TeX."""
        gitignore_path = ROOT_DIR / ".gitignore"
        self.assertTrue(gitignore_path.exists(), "O arquivo .gitignore não foi encontrado na raiz do projeto.")
        
        content = gitignore_path.read_text(encoding="utf-8")
        essential_patterns = ["*.aux", "*.log", "*.out", "*.toc", "*.synctex.gz", "*.fls", "*.fdb_latexmk"]
        for pattern in essential_patterns:
            self.assertIn(pattern, content, f"Padrão essencial '{pattern}' ausente no .gitignore.")

    def test_ibnp_base_sty_exists(self):
        """Verifica se o pacote ibnp-base.sty existe na raiz do repositório."""
        sty_path = ROOT_DIR / "ibnp-base.sty"
        self.assertTrue(sty_path.exists(), "O pacote ibnp-base.sty não foi encontrado na raiz.")

    def test_official_brand_colors_and_footer(self):
        """Verifica se as cores oficiais e a razão social correta estão no ibnp-base.sty."""
        sty_path = ROOT_DIR / "ibnp-base.sty"
        self.assertTrue(sty_path.exists(), "ibnp-base.sty inexistente.")
        content = sty_path.read_text(encoding="utf-8")

        official_colors = ["F43517", "F36529", "EFA162", "F1D6A9"]
        for color in official_colors:
            self.assertIn(color, content, f"Cor oficial '{color}' ausente no ibnp-base.sty.")

        self.assertIn("Igreja Batista Nacional da Paz de Guapó", content)
        self.assertNotIn("Nova Primavera", content, "Nome incorreto 'Nova Primavera' encontrado no pacote.")

    def test_compile_test_base_pdf(self):
        """Compila tests/test_base.tex e verifica geração do PDF com saída 0."""
        sty_path = ROOT_DIR / "ibnp-base.sty"
        tex_path = TESTS_DIR / "test_base.tex"
        pdf_path = TESTS_DIR / "test_base.pdf"

        # Remove PDF anterior se existir para garantir validação fidedigna
        if pdf_path.exists():
            pdf_path.unlink()

        # Configura ambiente para o LaTeX encontrar arquivos na raiz
        env = os.environ.copy()
        current_texinputs = env.get("TEXINPUTS", "")
        # No Windows/MiKTeX ou TeXLive, o separador pode ser ponto e vírgula
        env["TEXINPUTS"] = f"{ROOT_DIR}{os.pathsep}{TESTS_DIR}{os.pathsep}{current_texinputs}"

        # Executa pdflatex em duas passagens para resolver LastPage e referências cruzadas
        for _ in range(2):
            result = subprocess.run(
                [
                    "pdflatex",
                    "-disable-installer",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    f"-output-directory={TESTS_DIR}",
                    str(tex_path),
                ],
                cwd=str(ROOT_DIR),
                capture_output=True,
                text=True,
                env=env,
            )
            if result.returncode != 0:
                print("STDOUT:", result.stdout)
                print("STDERR:", result.stderr)
            self.assertEqual(result.returncode, 0, f"Falha na compilação do LaTeX: {result.stdout}")

        self.assertTrue(pdf_path.exists(), "O arquivo test_base.pdf não foi gerado.")
        self.assertGreater(pdf_path.stat().st_size, 1000, "O PDF gerado está vazio ou truncado.")

if __name__ == "__main__":
    unittest.main()
