# projetos-sociais-latex

[![Build and Validate PDFs](https://github.com/ibnp-guapo/projetos-sociais-latex/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/ibnp-guapo/projetos-sociais-latex/actions/workflows/build-pdf.yml)

Oficialização e documentação dos projetos de impacto social da **Igreja Batista Nacional da Paz de Guapó (IBNP)** no município de Guapó - GO em LaTeX.

---

## 🏛️ Estrutura e Estilo Institucional (`ibnp-base.sty`)

O repositório disponibiliza o pacote [ibnp-base.sty](ibnp-base.sty) para padronização visual e diagramação dos documentos institucionais.

### Características
- **Padrão ABNT / A4:** Margens configuradas via `geometry` (Superior: 3cm, Esquerda: 3cm, Direita: 2cm, Inferior: 2cm).
- **Idioma e Tipografia:** Suporte ao português brasileiro (`babel`), acentuação UTF-8 (`inputenc`, `fontenc` T1), fontes Latin Modern e títulos em sem-serifa (`helvet`).
- **Espaçamento:** Entrelinhas 1.5 (`setspace`).
- **Cabeçalho & Rodapé (`fancyhdr`):**
  - Cabeçalho: Identificação da IBNP e assunto/projeto.
  - Rodapé: Dados institucionais ("Igreja Batista Nacional da Paz de Guapó") e numeração de página ("Página X de Y" via `lastpage`).
- **Caixas de Destaque:** Ambiente `ibnpbox` e comando `\ibnpheaderbox{título}{conteúdo}` estilizados para resumos e metas.

### Paleta de Cores Oficial
| Identificador | HEX / RGB | Aplicação |
| :--- | :--- | :--- |
| `ibnpPrimary` (`ibnpNavy`) | `#F43517` (R244 G53 B23) | Terracota oficial (títulos principais, cabeçalhos, destaques fortes) |
| `ibnpSecondary` (`ibnpBlue`) | `#F36529` (R243 G101 B41) | Laranja / Coral (subtítulos e bordas institucionais) |
| `ibnpAccent` (`ibnpSky`) | `#EFA162` (R239 G161 B98) | Pêssego / Areia (acentos e elementos visuais) |
| `ibnpLight` | `#F1D6A9` (R241 G214 B169) | Creme claro (fundos de caixas e cartões) |
| `ibnpDark` | `#2D3748` | Tipografia padrão do corpo do texto |
| `ibnpBorder` | `#E2E8F0` | Divisórias e linhas sutis de cabeçalho/rodapé |

---

## 📋 Modelos Oficiais (Templates)

O repositório disponibiliza o modelo padrão reutilizável em [`templates/template_projeto_social.tex`](templates/template_projeto_social.tex), contendo as 9 seções obrigatórias para formalização e submissão a órgãos públicos e editais:
1. **Identificação do Proponente** (com dados cadastrais oficiais da IBNP Guapó, CNPJ 02.930.019/0001-62 e sede)
2. **Apresentação e Diagnóstico Sociocultural do Município**
3. **Justificativa de Impacto Social**
4. **Objetivos Geral e Específicos**
5. **Metodologia de Execução e Público Atendido**
6. **Cronograma Físico de Atividades**
7. **Planilha Orçamentária Detalhada**
8. **Indicadores de Monitoramento e Avaliação**
9. **Termo de Encerramento e Assinaturas dos Responsáveis**

---

## 📁 Projetos Oficiais

- **[Projeto 01] Oficina de Canto Infantil de Guapó:** [`projetos/01-oficina-canto-infantil/projeto_oficina_canto.tex`](projetos/01-oficina-canto-infantil/projeto_oficina_canto.tex)
  - *Público:* Crianças de 8 a 12 anos de Guapó - GO (30 vagas gratuitas)
  - *Carga Horária:* 6 horas (4 encontros presenciais de 1h30 em Dezembro)
  - *Iniciativa:* Escola Social de Guapó / IBNP Guapó

---

## 🚀 Como Usar em Novos Documentos

```latex
\documentclass[12pt,a4paper]{article}
\usepackage{ibnp-base}

\ibnptitle{Nome do Projeto}
\ibnpsubject{Projetos de Impacto Social}
\ibnplocation{Guapó - GO}
\ibnpdate{\today}

\begin{document}

\section{Apresentação}
Texto do projeto oficial...

\ibnpheaderbox{Destaque}{Metas e indicadores prioritários.}

\end{document}
```

---

## 🧪 Testes Automatizados e CI/CD

O projeto adota a metodologia **Spec-Driven Development (SDD)** com testes automatizados executados localmente e na esteira de integração contínua do GitHub Actions:

```bash
python -m unittest discover tests/
```

Os PDFs oficiais gerados nas execuções da branch `main` são disponibilizados como artefatos para download na aba **Actions** do GitHub.
