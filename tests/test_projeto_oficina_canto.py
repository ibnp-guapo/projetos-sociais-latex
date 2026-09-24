import os
import subprocess
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PROJETO_DIR = ROOT_DIR / "projetos" / "01-oficina-canto-infantil"
PROJETO_TEX = PROJETO_DIR / "projeto_oficina_canto.tex"

class TestProjetoOficinaCanto(unittest.TestCase):
    def test_project_file_exists(self):
        """Verifica se o arquivo projetos/01-oficina-canto-infantil/projeto_oficina_canto.tex existe."""
        self.assertTrue(
            PROJETO_TEX.exists(),
            f"Arquivo do projeto não encontrado em: {PROJETO_TEX}"
        )

    def test_project_has_official_parameters(self):
        """Verifica a presença dos parâmetros oficiais fixados na Issue #4."""
        self.assertTrue(PROJETO_TEX.exists(), "Documento do projeto inexistente.")
        content = PROJETO_TEX.read_text(encoding="utf-8")

        required_parameters = [
            "Oficina de Canto Infantil",
            "Guapó",
            "8 a 12 anos",
            "30",
            "6 horas",
            "4 encontros",
            "Dezembro",
        ]

        for param in required_parameters:
            self.assertIn(
                param,
                content,
                f"Parâmetro obrigatório '{param}' não encontrado no documento do projeto."
            )

    def test_project_has_required_sections_and_institutional_data(self):
        """Verifica as seções exigidas na Issue #4 e dados cadastrais da IBNP."""
        self.assertTrue(PROJETO_TEX.exists(), "Documento do projeto inexistente.")
        content = PROJETO_TEX.read_text(encoding="utf-8")

        required_sections = [
            "Apresentação",
            "Justificativa",
            "Critérios de Seleção",
            "Apresentação Pública",
            "02.930.019/0001-62",
            "Igreja Batista Nacional da Paz de Guapó",
        ]

        for sec in required_sections:
            self.assertIn(
                sec,
                content,
                f"Elemento/seção obrigatória '{sec}' ausente no documento do projeto."
            )

    def test_compile_project_pdf(self):
        """Compila projeto_oficina_canto.tex e verifica geração do PDF."""
        self.assertTrue(PROJETO_TEX.exists(), "Documento do projeto inexistente para compilação.")

        pdf_path = PROJETO_DIR / "projeto_oficina_canto.pdf"
        if pdf_path.exists():
            pdf_path.unlink()

        env = os.environ.copy()
        current_texinputs = env.get("TEXINPUTS", "")
        env["TEXINPUTS"] = f"{ROOT_DIR}{os.pathsep}{PROJETO_DIR}{os.pathsep}{current_texinputs}"

        for _ in range(2):
            result = subprocess.run(
                [
                    "pdflatex",
                    "-disable-installer",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    f"-output-directory={PROJETO_DIR}",
                    str(PROJETO_TEX),
                ],
                cwd=str(ROOT_DIR),
                capture_output=True,
                text=True,
                env=env,
            )
            self.assertEqual(result.returncode, 0, f"Falha na compilação do projeto: {result.stdout}")

        self.assertTrue(pdf_path.exists(), "PDF do projeto não foi gerado.")
        self.assertGreater(pdf_path.stat().st_size, 5000, "PDF do projeto está vazio ou truncado.")

if __name__ == "__main__":
    unittest.main()
