rem audiovisual

: ## editar audiovisual

: #cortar_audiovisual - $1: punto de inicio - $2: punto final - $3: archivo origen - $4: archivo final
doskey cortar_audiovisual=ffmpeg -ss $1 -to $2 -i $3 -y -c copy $4

: #cambiarFormat_audiovisual - $1: archivo original - $2: archivo con el formato cambiado
doskey cambiarFormat_audiovisual=ffmpeg -i $1 $2