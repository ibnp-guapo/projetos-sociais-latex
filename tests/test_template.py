import os
import subprocess
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT_DIR / "templates"
TEMPLATE_PATH = TEMPLATES_DIR / "template_projeto_social.tex"

class TestSocialProjectTemplate(unittest.TestCase):
    def test_template_file_exists(self):
        """Verifica se o arquivo templates/template_projeto_social.tex existe."""
        self.assertTrue(
            TEMPLATE_PATH.exists(),
            f"Arquivo de template não encontrado em: {TEMPLATE_PATH}"
        )

    def test_template_has_all_nine_sections(self):
        """Verifica a presença das 9 seções obrigatórias no template TeX."""
        self.assertTrue(TEMPLATE_PATH.exists(), "Template inexistente.")
        content = TEMPLATE_PATH.read_text(encoding="utf-8")

        required_sections = [
            "Identificação do Proponente",
            "Apresentação e Diagnóstico Sociocultural",
            "Justificativa de Impacto Social",
            "Objetivos Geral e Específicos",
            "Metodologia de Execução e Público Atendido",
            "Cronograma Físico de Atividades",
            "Planilha Orçamentária Detalhada",
            "Indicadores de Monitoramento e Avaliação",
            "Termo de Encerramento e Assinaturas",
        ]

        for section in required_sections:
            self.assertIn(
                section,
                content,
                f"Seção obrigatória '{section}' não encontrada no template."
            )

    def test_template_has_official_institutional_data(self):
        """Verifica se os dados institucionais oficiais da IBNP constam na Seção 1."""
        self.assertTrue(TEMPLATE_PATH.exists(), "Template inexistente.")
        content = TEMPLATE_PATH.read_text(encoding="utf-8")

        expected_tokens = [
            "02.930.019/0001-62",
            "Igreja Batista Nacional da Paz de Guapó",
            "Rua Presidente Kennedy",
            "contato@ibnpguapo.org.br",
            "(62) 9870-0089",
            "https://ibnpguapo.org.br",
        ]

        for token in expected_tokens:
            self.assertIn(
                token,
                content,
                f"Dado institucional obrigatório '{token}' ausente no template."
            )

    def test_compile_template_pdf(self):
        """Compila templates/template_projeto_social.tex e verifica geração do PDF."""
        self.assertTrue(TEMPLATE_PATH.exists(), "Template inexistente para compilação.")
        
        output_dir = TEMPLATES_DIR
        pdf_path = output_dir / "template_projeto_social.pdf"
        if pdf_path.exists():
            pdf_path.unlink()

        env = os.environ.copy()
        current_texinputs = env.get("TEXINPUTS", "")
        env["TEXINPUTS"] = f"{ROOT_DIR}{os.pathsep}{TEMPLATES_DIR}{os.pathsep}{current_texinputs}"

        for _ in range(2):
            result = subprocess.run(
                [
                    "pdflatex",
                    "-disable-installer",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    f"-output-directory={output_dir}",
                    str(TEMPLATE_PATH),
                ],
                cwd=str(ROOT_DIR),
                capture_output=True,
                text=True,
                env=env,
            )
            self.assertEqual(result.returncode, 0, f"Falha na compilação do template: {result.stdout}")

        self.assertTrue(pdf_path.exists(), "PDF do template não foi gerado.")
        self.assertGreater(pdf_path.stat().st_size, 5000, "PDF do template está vazio ou incompleto.")

if __name__ == "__main__":
    unittest.main()
