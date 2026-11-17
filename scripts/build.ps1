# Convert draft.md to draft.output.hwp with the bundled md2hwp,
# regardless of the directory this script is run from.
$repoRoot = Split-Path -Parent $PSScriptRoot
Push-Location $repoRoot
try {
    & .\md2hwp\md2hwp.exe draft.md --template template.hwp
    $code = $LASTEXITCODE
} finally {
    Pop-Location
}
exit $code
