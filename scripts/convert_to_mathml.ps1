$ErrorActionPreference = "Stop"

# 프로젝트 루트 기준 (이 스크립트가 있는 scripts 폴더의 부모 디렉터리)
$projectRoot = Split-Path -Parent (Split-Path -Parent $PSCommandPath)

# 입력 파일: 기본은 draft.md, 인자가 있으면 첫 번째 인자를 사용
$inputFile = if ($args.Count -ge 1) { $args[0] } else { "draft.md" }

$inputPath  = Join-Path $projectRoot $inputFile
$outputDir  = Join-Path $projectRoot "outputs"
# 파일명이 중복되지 않도록 _mathml 접미사 추가
$outputPath = Join-Path $outputDir ([IO.Path]::GetFileNameWithoutExtension($inputFile) + "_mathml.html")

if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

pandoc $inputPath -o $outputPath --standalone --mathml

Write-Host "Generated HTML with MathML: $outputPath"

Write-Host "Extracting MathML blocks..."
& (Join-Path $projectRoot ".venv\Scripts\Activate.ps1")
python (Join-Path $projectRoot "scripts\extract_mathml.py") $outputPath
