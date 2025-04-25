from rich.console import Console
import sys 

console = Console()

def __check(code,resultado_ok=None,resultado_error=None,mensaje_ok="tarea completada",mensaje_error="se ah producido un error",exit=True):
    __error(code,resultado_error,mensaje_error,exit)
    __ok(code,resultado_ok,mensaje_ok)

def __ok(code,resultado,mensaje):
    if code == 0:
        print(f"\n{resultado}")
        console.print(f"\n✅",f"[green]{mensaje}[/]")
        
def __warning(mensaje):
    console.print(f"\n❌",f"[red]{mensaje}[/]")
    

def __error(code,error=None,mensaje="se ah producido un error",exit=True):
    if code > 0:
        console.print(f"\n{error}")
        console.print(f"error code: {code}")
        console.print(f"\n❌",f"[red]{mensaje}[/]")
        if exit:
            sys.exit(1)