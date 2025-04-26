import sys 
from subprocess import run,CalledProcessError,TimeoutExpired
from rich.console import Console
from questionary import text,select
from icecream import ic
from json import loads,JSONDecodeError
import re

def __obtener_resoluciones_disponibles(video_url):
    # Comando para listar formatos en JSON (estructurado)
    comando = [
        "yt-dlp",
        "--list-formats",
        "--skip-download",
        "--dump-json",
        video_url
    ]
    try:
        result = run(comando,capture_output=True,text=True,shell=True)
        json_str = re.search(r'\{.*\}', result.stdout, re.DOTALL).group() # type: ignore
        formats = loads(json_str)["formats"]
        # Ejecutar yt-dlp y capturar la salida JSON
        # Extraer resoluciones únicas (evitando duplicados)
        resolutions = set()
        for f in formats:
            if 'resolution' in f:
                if f['resolution'] not in ['audio only', 'unknown']:  # ⬅️ Comparación directa
                    resolutions.add(f['resolution'])   
            elif 'height' in f:
                resolutions.add(f"{f['height']}p")
        return sorted(resolutions, key=lambda x: int(x.replace('p', '')) if x.endswith('p') else 0)
    except CalledProcessError as e:
        print(f"❌ Error al ejecutar yt-dlp:")
        ic(ic(),e.stderr)
        return []
    except FileNotFoundError:
        print("Error: Comando no encontrado. ¿Está instalado?")
    except JSONDecodeError:
        print("❌ No se pudo parsear la salida de yt-dlp.")
        return []
    except PermissionError:
        print("Error: Permisos denegados.")
    except TimeoutExpired:
        print("⌛ ¡Tiempo de espera agotado!")
    except ValueError:
        print("📛 Argumentos inválidos.")
"""     except Exception as e:  # Captura cualquier otro error inesperado
        print("⚠️ Error inesperado:")
        ic(ic(),f"{type(e).__name__} - {str(e)}") """
        
def __limpiar_resoluciones(resolucion):
    if "x" in resolucion:
        resolucion_limpia = resolucion.split("x")[1]
    if "p" in resolucion:
        resolucion_limpia = resolucion.replace("p", "")
    return resolucion_limpia

def __descargar_video(video_url,resolusion=None):
    comando = f"yt-dlp -f \"bestvideo[height<={resolusion}]+bestaudio\" --merge-output-format mp4 {video_url}"
    ejecucion = run(comando,capture_output=True,text=True,shell=True)
    return ejecucion


def main_interactivo(debug=False):
    video_url = text("indica la url/s del video/s a descargar").ask()
    if video_url == None: exit()
    
    resoluciones = __obtener_resoluciones_disponibles(video_url)
    resolucion = select("inidica la resolucion para descargar:",choices=resoluciones).ask() # type: ignore
    print(resolucion,type(resolucion))
    resolucion_limpia = __limpiar_resoluciones(resolucion)
    descargar_video = __descargar_video(video_url,resolucion_limpia)
    print(descargar_video.stdout)

def main():
    main_interactivo()

if __name__ == "__main__":
    main()