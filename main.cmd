: alias
:: Author: Ricardo Torrellas - ricardo.torrejas@gmail.com::
@echo off

set bin=%~dp0bin\
set buscar=%bin%buscar\index.cmd
set copiar=%bin%copiar\index.cmd
set crear=%bin%crear\index.cmd
set descargar=%bin%descargar\index.cmd
set desinstalar=%bin%desinstalar\index.cmd
set editar=%bin%editar\index.cmd
set eliminar=%bin%eliminar\index.cmd
set instalar=%bin%instalar\index.cmd
set listar=%bin%listar\index.cmd
set sincronizar=%bin%sincronizar\index.cmd

call "%buscar%"
call "%copiar%"
call "%crear%"
call "%descargar%"
call "%desinstalar%"
call "%editar%"
call "%editar%"
call "%eliminar%"
call "%instalar%"
call "%listar%"
call "%sincronizar%"
