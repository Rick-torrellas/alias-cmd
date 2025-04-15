: alias
:: Author: Ricardo Torrellas - ricardo.torrejas@gmail.com::
@echo off

set bin=%~dp0bin\

set buscar=%bin%buscar\index.cmd
set comprimir=%bin%comprimir\index.cmd
@REM set copiar=%bin%copiar\index.cmd
set cortar=%bin%cortar\index.cmd
set crear=%bin%crear\index.cmd
set descargar=%bin%descargar\index.cmd
set descomprimir=%bin%descomprimir\index.cmd
@REM set desinstalar=%bin%desinstalar\index.cmd
set editar=%bin%editar\index.cmd
@REM set eliminar=%bin%eliminar\index.cmd
@REM set instalar=%bin%instalar\index.cmd
@REM set listar=%bin%listar\index.cmd
@REM set renombrar=%bin%renombrar\index.cmd
set sync=%bin%sync\index.cmd

call "%buscar%" 
@REM call "%comprimir%"
@REM call "%copiar%"
@REM call "%crear%"
call "%cortar%"
call "%crear%"
call "%descargar%" 
@REM call "%descomprimir%"
@REM call "%desinstalar%"
@REM call "%editar%"
@REM call "%eliminar%"
@REM call "%instalar%"
@REM call "%listar%"
@REM set renombrar=%renombrar%\index.cmd
@REM call "%sync%"
