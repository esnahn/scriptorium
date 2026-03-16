# Scriptorium

Scriptorium is a project designed to help you write and manage markdown manuscripts, with built-in tools for counting text, rendering math, and converting the manuscripts to HTML format.

## Project Structure

### Markdown Files
- `draft.md`: The base writing template for a single manuscript with basic markdown structural examples (headers, tables, inline/block math).
- `instruction.md`: A general guide for manuscript writing workflow, explaining file structures, directory roles (`outputs/` and `references/`), and project conventions.
- `instruction_writing.md`: A detailed convention guide defining writing rules like notation conventions (languages, numbers, units, law names) and the preferred format for citing books, journals, news articles, and websites.
- `outline.md`: An example essay outline containing the structure of a writing piece.
- `TODO.md`: A list of planned features to improve the project, including conversions to docs, docx, and hwpx.

### Scripts and Environment
- `scripts/`: Python and PowerShell scripts used to process documents, extract MathML, count words, and build HTML versions of the document.
- `outputs/`: The directory where the HTML conversions and specific outputs like `.mml` equations are generated.

## Environment Setup

To run the Python scripts, you should set up a virtual environment and install the requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Tool Overview

### 1. `convert_to_html.ps1`
Runs Pandoc with KaTeX support to convert a given Markdown file into a standalone HTML file.

**Usage:**
```powershell
.\scripts\convert_to_html.ps1 [input_file.md]
```
*If no argument is passed, it defaults to using `draft.md`.*

### 2. `convert_to_mathml.ps1`
Runs Pandoc with MathML support (`--mathml`) to convert a Markdown file into HTML. Then automatically extracts all the math equations.

**Usage:**
```powershell
.\scripts\convert_to_mathml.ps1 [input_file.md]
```

### 3. `extract_mathml.py`
A Python script that parses an HTML file, locates all MathML (`<math>...</math>`) blocks, and saves each of them as individual `.mml` files within a `mathml` subdirectory next to the input file. It cleverly uses the text immediately preceding the math block as the base name for the generated `.mml` file.

**Usage:**
```bash
python scripts/extract_mathml.py <input_html_file>
```
*Note: This script is typically run automatically by `scripts\convert_to_mathml.ps1`.*

### 4. `count_words.py`
Analyzes a text file to calculate document length statistics, which is useful when writing manuscripts with strict character or word limits.

**Usage:**
```bash
python scripts/count_words.py <filename>
```
It outputs:
- Characters (including spaces)
- Characters (excluding spaces)
- Word count
