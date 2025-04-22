import sys 
import os
from subprocess import run
from rich.console import Console
import json

console = Console()

def iniciar_repositorio_local():
    comando = f"git init"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    if proceso.returncode == 0:
        console.print(proceso.stdout)
        console.print("✅",f"[green]el repositorio local se creo correctamente[/]")
    return proceso
    

def iniciar_repositorio_github(repo_name):
    comando = f"gh repo create --public {repo_name}"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    if proceso.returncode == 0:
        console.print(proceso.stdout)
        console.print("✅",f"[green]el repositorio en github se creo correctamente[/]")
    return proceso

def optener_usuario():
    comando = f"gh api user"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    user_data = json.loads(proceso.stdout)
    return user_data["login"]
    # TODO:  falta poder validad que el proceso se ejecuto correctamente
    

def configurar_repositorios_externos(repositorio):
    remote_repository = "origin"
    usuario = optener_usuario()
    ssh_repositorio = f"git@github.com:{usuario}/{repositorio}.git"
    comando = f"git remote add {remote_repository} {ssh_repositorio}"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    if proceso.returncode == 0:
        console.print("✅",f"[green]el repositorio remoto {remote_repository} se configuro apropiadamente[/]")
        return proceso

def main():
    project_location = os.getcwd()
    project_folder = os.path.basename(project_location) # TODO: se puede usar este valor como por defecto, pero se puede dar la oportunidad al usuario de colocarlo con argumentos.
    #TODO: tambien necesita sanisarse el nombre, por si lleva espacios o caracteres especiales.
    
    iniciar_repositorio_local()
    
    iniciar_repositorio_github(project_folder)
    #TODO: manejar el ecenario donde existe el repositorio en github
    
    configurar_repositorios_externos(project_folder)
    
    #TODO: verificar que la rama principal se llame main, si no cambiarle el nombre a main
    
    #TODO: configurar la ruta remota origin al repositorio ssh en github.
if __name__ == "__main__":
    main()