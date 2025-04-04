@echo off

rem # descargar

rem ## descargar videos de youtube

rem ### descargar_youtube

rem $1: url del video - $2: resolucion del video - $3: extencion del archivo 
doskey descargar_youtube=yt-dlp -f "bestvideo[height<=$2]+bestaudio" --merge-output-format $3 $1
rem $1: url video
doskey descargar_youtube720=yt-dlp -f "bestvideo[height<=720]+bestaudio" --merge-output-format mp4 $*
rem $1: url video
doskey descargar_youtube1080=yt-dlp -f "bestvideo[height<=1080]+bestaudio" --merge-output-format mp4 $*


rem ## editar videos

rem cortar_audiovisual - $1: punto de inicio - $2: punto final - $3: archivo origen - $4: archivo final
doskey cortar_audiovisual=ffmpeg -ss $1 -to $2 -i $3 -y -c copy $4

rem cambiarFormat_audiovisual - $1: archivo original - $2: archivo con el formato cambiado
doskey cambiarFormat_audiovisual=ffmpeg -i $1 $2

rem 
doskey sincronizar_nube=rclone sync -v $1 $2

rem ## buscar_paquete_winget - $1: nombre del paquete
doskey buscar_paquete_winget=winget search -e --name $1

rem ## buscar_paquete_instalado_winget - $1: nombre del paquete a buscar
doskey buscar_paquete_instalado_winget=winget list --source winget --name "$1"

rem ## listar_paquetes_instalados_winget
doskey listar_paquetes_instalados_winget=winget list --source winget




