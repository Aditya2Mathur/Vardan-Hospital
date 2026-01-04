
$path = "e:\WebsiteProject(2026)\Vardan\index.html"
$lines = Get-Content $path
# We want to remove lines 885 to 2475 (1-based).
# In 0-based index: 884 to 2474.
# So we keep 0 to 883.
# And 2475 to end.
$newLines = $lines[0..883] + $lines[2475..($lines.Count-1)]
$newLines | Set-Content $path
