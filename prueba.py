import subprocess

def olis(mensaje):
    cmd = [
        "echo",
        mensaje
    ]
    cmd2 = f"echo {mensaje}"
    comando = subprocess.run(cmd,capture_output=True,text=True,shell=True)
    return comando

mensaje = input("cualquier vaina: ")

print(olis(mensaje).args)
print(olis(mensaje).stdout)