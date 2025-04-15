import sys 
from subprocess import run
from rich.console import Console

console = Console()

def crear_commit(titulo,contenido):
    comando_ejecutar = f"git add . && git commit -m {titulo} -m {contenido} && git push"
    ejecucion = run(
        comando_ejecutar,
        capture_output=True,
        text=True,
        shell=True
    )
    return ejecucion

def crear_commit_no_contenido(titulo):
    comando_ejecutar = f"git add . && git commit -m {titulo} && git push"
    ejecucion = run(
        comando_ejecutar,
        capture_output=True,
        text=True,
        shell=True
    )
    return ejecucion

def __todo_correcto(code,resultado):
    if code == 0:
        print(resultado)
        console.print(f"✅",f"[green]tarea completada[/]")
        sys.exit(0)

def __error(code,error):
    if code > 0:
        console.print(error)
        console.print(f"❌",f"[red]se ah producido un error[/]")
        sys.exit(1)

def main():
    titulo = sys.argv[1] if len(sys.argv) > 1 else None
    contenido =  sys.argv[2] if len(sys.argv) > 2 else None
    if titulo:
        
        if contenido == None:
            resultado = crear_commit_no_contenido(titulo)
            __todo_correcto(resultado.returncode,resultado)
            __error(resultado.returncode,resultado.stderr)
            
        resultado = crear_commit(titulo,contenido)
        __todo_correcto(resultado.returncode,resultado)
        __error(resultado.returncode,resultado.stderr)
    __error(1,f"debe mandarse aunque sea un argumento, el valor del primer argumento: [red]{titulo}[/]")
    

if __name__ == "__main__":
    main()