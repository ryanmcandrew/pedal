$venvPath = ".venv/pedal"
Write-Host $venvPath
if (-not (Test-Path -Path $venvPath -PathType Container))
{
    Write-Host "Creating venv with $venvPath"
    python -m venv $venvPath
}

$cmd = ($venvPath + "/Scripts/Activate.ps1")
$commandInfo = Get-Command $cmd -ErrorAction SilentlyContinue

if ($commandInfo) 
{
    Invoke-Expression $cmd
    pip install -r requirements.txt
    garden install matplotlib
    python src/main.py
} 
else 
{
    Write-Host "The command '$cmd' is not found or cannot be run."
}