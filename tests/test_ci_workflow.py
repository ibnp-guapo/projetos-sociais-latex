import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
WORKFLOW_PATH = ROOT_DIR / ".github" / "workflows" / "build-pdf.yml"

class TestCIWorkflow(unittest.TestCase):
    def test_workflow_file_exists(self):
        """Verifica se o arquivo do workflow .github/workflows/build-pdf.yml existe."""
        self.assertTrue(
            WORKFLOW_PATH.exists(),
            f"Arquivo de workflow não encontrado em: {WORKFLOW_PATH}"
        )

    def test_workflow_structure_and_triggers(self):
        """Verifica se o workflow possui os gatilhos e passos obrigatórios definidos na spec."""
        self.assertTrue(WORKFLOW_PATH.exists(), "Workflow inexistente.")
        content = WORKFLOW_PATH.read_text(encoding="utf-8")

        # Gatilhos
        self.assertIn("push:", content, "Gatilho 'push' ausente no workflow.")
        self.assertIn("pull_request:", content, "Gatilho 'pull_request' ausente no workflow.")
        self.assertIn("workflow_dispatch:", content, "Gatilho 'workflow_dispatch' ausente no workflow.")
        self.assertIn("main", content, "Branch 'main' deve estar configurada nos gatilhos.")

        # Passos essenciais de execução
        self.assertIn("actions/checkout", content, "Passo de checkout ausente.")
        self.assertIn("actions/setup-python", content, "Passo de setup do Python ausente.")
        self.assertIn("texlive", content.lower(), "Instalação do TeX Live ausente.")
        self.assertIn("unittest", content, "Execução da suíte de testes ausente.")
        self.assertIn("pdflatex", content, "Compilação via pdflatex ausente.")
        self.assertIn("actions/upload-artifact", content, "Upload de artefatos PDF ausente.")

if __name__ == "__main__":
    unittest.main()
