# Restore the manuscript templates from main into the repo root,
# regardless of the directory this script is run from.
$repoRoot = Split-Path -Parent $PSScriptRoot
git -C $repoRoot restore -s main -- title.md outline.md draft.md
exit $LASTEXITCODE
