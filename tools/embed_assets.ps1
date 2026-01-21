# FactorLab Asset Embedder
# Embeds local images (<img> tags) as Base64 Data URIs into HTML files
# This fixes "Tainted Canvas" errors when generating PDFs on file:// protocol

$root = "c:\Users\Admin\Desktop\cokarma pitch deck"
$slidesDir = Join-Path $root "faculty_deck\slides"
$assetsDir = Join-Path $root "assets"
$files = Get-ChildItem -Path $slidesDir -Filter "*.html"

Write-Host "Starting Asset Embedding..."
$count = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    $originalContent = $content
    
    # Regex to find img src tags: src="../../assets/filename.ext"
    # We capture the full match and the relative path
    $matches = [regex]::Matches($content, 'src=["''](\.\./\.\./assets/[^"'']+)["'']')
    
    foreach ($match in $matches) {
        $relativePath = $match.Groups[1].Value
        # Resolve path: ../../assets/ -> actual path
        $relPathClean = $relativePath -replace '\.\./\.\./assets/', ''
        $imagePath = Join-Path $assetsDir $relPathClean
        
        if (Test-Path $imagePath) {
            try {
                $bytes = [System.IO.File]::ReadAllBytes($imagePath)
                $b64 = [System.Convert]::ToBase64String($bytes)
                $ext = [System.IO.Path]::GetExtension($imagePath).TrimStart(".")
                if ($ext -eq "svg") { $mime = "image/svg+xml" }
                elseif ($ext -eq "png") { $mime = "image/png" }
                elseif ($ext -eq "jpg" -or $ext -eq "jpeg") { $mime = "image/jpeg" }
                else { $mime = "image/$ext" }
                
                $dataUri = "data:$mime;base64,$b64"
                
                # Replace in content (Simple string replace for safety)
                # Note: This replaces ALL occurrences of this specific path string
                $content = $content.Replace($relativePath, $dataUri)
                Write-Host "  [+] Embedded $relPathClean in $($file.Name)"
            }
            catch {
                Write-Host "  [!] Failed to read $imagePath"
            }
        } else {
            Write-Host "  [?] Image not found: $imagePath"
        }
    }
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Saved $($file.Name)"
        $count++
    }
}

Write-Host "Complete. Updated $count files."
