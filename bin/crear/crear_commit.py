import sys 
from subprocess import run
from rich.console import Console
import questionary

console = Console()

def _add():
    comando_ejecutar = f"git add ."
    ejecucion = run(
        comando_ejecutar,
        capture_output=True,
        text=True,
        shell=True
    )
    __check(ejecucion.returncode,ejecucion,ejecucion.stderr,"git add completado","se creo un error al ejecutar git add") 
    return ejecucion

def _commit(titulo: str|None=None,contenido: str|None=None):
    comando_con_contenido = f"git commit -m {titulo} -m {contenido}"
    comando_sin_contenido = f"git commit -m {titulo}"
    ejecucion = None
    
    if titulo == None:
        __error(1,f"valor de titulo: {titulo}","se debe proporcionar el titulo como minimo")
        sys.exit(1)
    if contenido:
        ejecucion = run(
        comando_con_contenido,
        capture_output=True,
        text=True,
        shell=True
        )
        __check(ejecucion.returncode,ejecucion,ejecucion.stderr,"se creo un commit con titulo y mensaje","se produjo un error al crear el commit")
        return ejecucion
    ejecucion = run(
        comando_sin_contenido,
        capture_output=True,
        text=True,
        shell=True
        )
    __check(ejecucion.returncode,ejecucion,ejecucion.stderr,"se creo un commit con titulo","se produjo un error al crear el commit")
    return ejecucion

def _push():
    comando_ejecutar = f"git push"
    ejecucion = run(
        comando_ejecutar,
        capture_output=True,
        text=True,
        shell=True
        )
    __check(ejecucion.returncode,ejecucion,ejecucion.stderr,"push ejecutado correctamente","se ah producido un error al ejecutar el push")
    return ejecucion

def __check(code,resultado_ok=None,resultado_error=None,mensaje_ok="tarea completada",mensaje_error="se ah producido un error"):
    __error(code,resultado_error,mensaje_error)
    __ok(code,resultado_ok,mensaje_ok)

def __ok(code,resultado,mensaje):
    if code == 0:
        print(f"\n{resultado}")
        console.print(f"\n✅",f"[green]{mensaje}[/]")

def __error(code,error=None,mensaje="se ah producido un error"):
    if code > 0:
        console.print(f"\n{error}")
        console.print(f"\n❌",f"[red]{mensaje}[/]")
        sys.exit(1)
        
def main_con_argumentos():
    titulo = sys.argv[1] if len(sys.argv) > 1 else None
    contenido =  sys.argv[2] if len(sys.argv) > 2 else None
    
    _add()
    _commit(titulo,contenido)
    _push()
    return 0
    
def main_interactivo():
    titulo = questionary.text("cual es el titulo del commit?").ask()
    
    if titulo == None:
        __error(1,f"el valor del titulo es: {titulo}","debe propocionarse un titulo para el commit")
    
    pregunta_contenido = questionary.rawselect(
            "Quieres agregar contenido a tu commit?",
            choices=["No", "Si"],
        ).ask()
    print(pregunta_contenido)
    pass
    
    _add()
    
    if pregunta_contenido == "No" or pregunta_contenido == None:
        _commit(titulo)
        _push()
        return 0
    
    try:
        contenido = questionary.text("cual es el contenido de tu commit?").ask()
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario")
        sys.exit(0)
    _commit(titulo,contenido)
    _push()
    return 0

def main():
    titulo = sys.argv[1] if len(sys.argv) > 1 else None
    
    if titulo:
        main_con_argumentos()
        sys.exit(0)
    
    main_interactivo()
    sys.exit(0)
    
if __name__ == "__main__":
    main()