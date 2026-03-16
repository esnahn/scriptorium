$ErrorActionPreference = "Stop"

# 프로젝트 루트 기준 (이 스크립트가 있는 scripts 폴더의 부모 디렉터리)
$projectRoot = Split-Path -Parent (Split-Path -Parent $PSCommandPath)

# 입력 파일: 기본은 draft.md, 인자가 있으면 첫 번째 인자를 사용
$inputFile = if ($args.Count -ge 1) { $args[0] } else { "draft.md" }

$inputPath = Join-Path $projectRoot $inputFile
$outputDir = Join-Path $projectRoot "outputs"
$outputPath = Join-Path $outputDir ([IO.Path]::GetFileNameWithoutExtension($inputFile) + ".html")

if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

pandoc $inputPath -o $outputPath --standalone --katex | Out-Null # Wait for pandoc to finish

Write-Host "Generated HTML: $outputPath"

