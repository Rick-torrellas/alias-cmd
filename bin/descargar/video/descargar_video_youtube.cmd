rem $1: url del video - $2: resolucion del video - $3: extencion del archivo 
doskey descargar_video_youtube=yt-dlp -f "bestvideo[height<=$2]+bestaudio" --merge-output-format $3 $1
rem $1: url video
doskey descargar_video_youtube720=yt-dlp -f "bestvideo[height<=720]+bestaudio" --merge-output-format mp4 $*
rem $1: url video
doskey descargar_video_youtube1080=yt-dlp -f "bestvideo[height<=1080]+bestaudio" --merge-output-format mp4 $*