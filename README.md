# Scriptorium

Scriptorium is a project designed to help you write and manage markdown manuscripts, with built-in tools for counting text, rendering math, and converting the manuscripts to HTML format.

## Project Structure

### Markdown Files
- `title.md`: Potential titles for the manuscript.
- `outline.md`: The structured outline of the writing piece.
- `draft.md`: The actual manuscript draft being written.
- `instruction.md`: **[Writer's Manual]** Detailed guide for manuscript writing workflow and file roles.
- `instruction_writing.md`: Detailed writing conventions (notation, citations, etc.).
- `TODO.md`: Planned features and project roadmap.

### Scripts and Environment
- `scripts/`: Python and PowerShell scripts for processing documents.
- `outputs/`: Generated output files (HTML, DOCX, etc.).

## Writing Workflow

The project follows a structured sequence: **Title -> Outline -> Draft**.  
For a detailed step-by-step guide on the writing process and how to use these files, please refer to [instruction.md](file:///e:/scriptorium/instruction.md).

## Environment Setup

Install Pandoc:

```powershell
scoop install pandoc
```

To run the Python scripts, you should set up a virtual environment and install the requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Tool Overview

### 1. `convert_to_docx.ps1`
Runs Pandoc to convert a given Markdown file into a standalone DOCX file.

**Usage:**
```powershell
.\scripts\convert_to_docx.ps1 [input_file.md]
```
*If no argument is passed, it defaults to using `draft.md`.*

### 2. `convert_to_html.ps1`
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

*Note: This script is typically run automatically by `scripts\convert_to_mathml.ps1`.*

A Python script that parses an HTML file, locates all MathML (`<math>...</math>`) blocks, and saves each of them as individual `.mml` files within a `mathml` subdirectory next to the input file. It cleverly uses the text immediately preceding the math block as the base name for the generated `.mml` file.

**Usage:**
```bash
python scripts/extract_mathml.py <input_html_file>
```

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
