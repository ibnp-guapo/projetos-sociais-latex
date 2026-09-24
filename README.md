# projetos-sociais-latex

Oficialização e documentação dos projetos de impacto social da **Igreja Batista Nova Primavera (IBNP)** no município de Guapó - GO em LaTeX.

---

## 🏛️ Estrutura e Estilo Institucional (`ibnp-base.sty`)

O repositório disponibiliza o pacote [ibnp-base.sty](ibnp-base.sty) para padronização visual e diagramação dos documentos institucionais.

### Características
- **Padrão ABNT / A4:** Margens configuradas via `geometry` (Superior: 3cm, Esquerda: 3cm, Direita: 2cm, Inferior: 2cm).
- **Idioma e Tipografia:** Suporte ao português brasileiro (`babel`), acentuação UTF-8 (`inputenc`, `fontenc` T1), fontes Latin Modern e títulos em sem-serifa (`helvet`).
- **Espaçamento:** Entrelinhas 1.5 (`setspace`).
- **Cabeçalho & Rodapé (`fancyhdr`):**
  - Cabeçalho: Identificação da IBNP e assunto/projeto.
  - Rodapé: Dados institucionais ("Guapó - GO") e numeração de página ("Página X de Y" via `lastpage`).
- **Caixas de Destaque:** Ambiente `ibnpbox` e comando `\ibnpheaderbox{título}{conteúdo}` estilizados para resumos e metas.

### Paleta de Cores Oficial
| Identificador | HEX | Aplicação |
| :--- | :--- | :--- |
| `ibnpNavy` | `#0B2545` | Cor primária institucional (títulos de seção, destaques fortes) |
| `ibnpBlue` | `#133E87` | Cor secundária (subtítulos e bordas de caixas) |
| `ibnpSky` | `#1D76DB` | Cor de acento (links e elementos ativos) |
| `ibnpDark` | `#2D3748` | Tipografia padrão do corpo do texto |
| `ibnpLight` | `#F7FAFC` | Fundo de caixas de informação e cartões |
| `ibnpBorder` | `#E2E8F0` | Divisórias e linhas de cabeçalho/rodapé |

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

## 🧪 Testes Automatizados

O projeto utiliza **Spec-Driven Development (SDD)** com testes automatizados de compilação TeX e validação de regras de versionamento:

```bash
python -m unittest tests/test_latex.py
```
