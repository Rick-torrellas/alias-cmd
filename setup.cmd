@echo off
rem esto evita que muestre tanto el stdout y el stderr
@where python > nul 2>&1 
if %errorlevel% equ 0 (
    echo El comando existe.
) else (
    echo El comando NO existe.
    winget install -e --id Python.Python.3.11
)
pause