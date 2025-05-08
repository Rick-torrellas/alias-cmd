from rich.console import Console

console = Console()

def keyboard_interrupt():
    console.print("❌",f"el usuario detuvo la ejecucion del processo usando \"ctrl + c\" [red]KeyboardInterrupt[/]")
    exit(1)
    
def exito():
    console.print(f"✅ se completo la operacion correctamente")
    exit(0)