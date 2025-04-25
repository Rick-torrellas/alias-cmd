import sys 
from subprocess import run
from rich.console import Console
from questionary import text


console = Console()

def cortar_video(inicio,final,archivo_origen,archivo_final):
    comando_ejecutar = f"ffmpeg -ss {inicio} -to {final} -i {archivo_origen} -y -c copy {archivo_final}"
    ejecucion = run(
        comando_ejecutar,
    capture_output=True,
    text=True,
    shell=True
    )    
    return ejecucion

inicio = sys.argv[1]
final =  sys.argv[2]
archivo_origen =  sys.argv[3]
archivo_final =  sys.argv[4]

def main_interactivo():
    inicio = text("cual es el punto de inicio para el corte").ask() 
    final = text("cual es el punto final del corte").ask()
    archivo_origen = text("indique el video que se va a cortar")

def main():
    resultado = cortar_video(inicio,final,archivo_origen,archivo_final)
    
    if resultado.returncode == 0:
        print(resultado.stderr)
        console.print(f"✅",f"[green]operacion exitosa[/]: archivo creado [cyan]{archivo_final}[/]")
        sys.exit(0)
    print(resultado.stderr) 
    console.print(f"❎",f"[red]error[/]: ")
    sys.exit(1)

if __name__ == "__main__":
    main()
