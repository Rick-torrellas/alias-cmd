from rich.progress import Progress,TimeElapsedColumn
import subprocess
import time
from datetime import timedelta
from icecream import ic



def exec_process(process: list):
    total_process = len(process)
    incremento = 100 / total_process  # Calcula el avance por comando
    with Progress() as progress: # transient=True para eliminar la barra una vez finalizada
        start_time = time.time()
        tarea = progress.add_task("[red]Ejecutando...", total=100)
        for i,action in enumerate(process):
            action()
            progress.update(tarea, advance=incremento)
        
procesos = [
    lambda: subprocess.run("dir", shell=True),
    lambda: subprocess.run("echo olis", shell=True),
    lambda: subprocess.run("ping google.com", shell=True),
    lambda: subprocess.run("dir", shell=True),
    lambda: subprocess.run("mkdir olis", shell=True),
    lambda: subprocess.run("dir", shell=True)
]
        

exec_process(procesos)