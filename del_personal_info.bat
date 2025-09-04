@echo off
:: 관리자 권한 체크
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Requesting admin privileges...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

:: 임시 PowerShell 스크립트 경로 설정
set psfile=%TEMP%\wipe_personal_data.ps1

:: PowerShell 스크립트 생성
> "%psfile%" (
echo Write-Host "[*] Wiping Chrome, Edge, Brave, Firefox user data..."
echo Remove-Item "$env:LOCALAPPDATA\Google\Chrome\User Data" -Recurse -Force -ErrorAction SilentlyContinue
echo Remove-Item "$env:LOCALAPPDATA\Microsoft\Edge\User Data" -Recurse -Force -ErrorAction SilentlyContinue
echo Remove-Item "$env:LOCALAPPDATA\BraveSoftware\Brave-Browser\User Data" -Recurse -Force -ErrorAction SilentlyContinue
echo Remove-Item "$env:APPDATA\Mozilla\Firefox" -Recurse -Force -ErrorAction SilentlyContinue
echo Remove-Item "$env:LOCALAPPDATA\Mozilla\Firefox" -Recurse -Force -ErrorAction SilentlyContinue

echo Write-Host "[*] Wiping GitHub CLI tokens..."
echo Remove-Item "$env:APPDATA\GitHub CLI" -Recurse -Force -ErrorAction SilentlyContinue

echo Write-Host "[*] Removing credentials from Windows Credential Manager..."
echo $targets = cmd /c "cmdkey /list" ^| Where-Object {$_ -match '^ *Target:' } ^| ForEach-Object { ($_ -replace '^ *Target:','').Trim() }
echo foreach ($t in $targets) {
echo     cmd /c "cmdkey /delete:`"$t`"" ^> $null
echo }

echo Write-Host "[OK] All personal data wiped."
)

:: PowerShell로 실행
powershell -NoProfile -ExecutionPolicy Bypass -File "%psfile%"

:: 임시 파일 삭제
del "%psfile%" >nul 2>&1
pause
