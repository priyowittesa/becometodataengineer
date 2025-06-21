@echo off
setlocal

:: Dapatkan direktori target
set "target_dir=%~1"
if "%target_dir%"=="" set "target_dir=%cd%"

:: Jalankan Git Bash sebagai Administrator di folder target
powershell -Command "Start-Process 'C:\Program Files\Git\git-bash.exe' -ArgumentList '--cd=%target_dir%' -Verb runAs"
