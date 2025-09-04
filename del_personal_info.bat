@echo off
:: 관리자 권한 체크
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Requesting admin privileges...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

:: 임시 PowerShell 스크립트 생성
set psfile=%TEMP%\wipe_personal_data.ps1

> "%psfile%" (
echo param()
echo function nuke($p^) { if(Test-Path $p^) { Remove-Item $p -Recurse -Force -ErrorAction SilentlyContinue } }
echo Write-Host "Wiping Chrome, Edge, Brave, Firefox user data..."
echo nuke "$env:LOCALAPPDATA\Google\Chrome\User Data"
echo nuke "$env:LOCALAPPDATA\Microsoft\Edge\User Data"
echo nuke "$env:LOCALAPPDATA\BraveSoftware\Brave-Browser\User Data"
echo nuke "$env:APPDATA\Mozilla\Firefox"
echo nuke "$env:LOCALAPPDATA\Mozilla\Firefox"
echo Write-Host "Wiping GitHub CLI tokens..."
echo nuke "$env:APPDATA\GitHub CLI"
echo Write-Host "Removing credentials from Windows Credential Manager..."
echo $list = cmdkey /list ^| Select-String "Target:" ^| ForEach-Object { ($_ -replace '^\s*Target:\s*','').Trim() }
echo foreach ($t in $list^) { cmdkey /delete:$t ^| Out-Null }
echo Write-Host "Done. All personal data wiped."
)

:: PowerShell로 실행
powershell -NoProfile -ExecutionPolicy Bypass -File "%psfile%"

:: 정리
del "%psfile%" >nul 2>&1
pause