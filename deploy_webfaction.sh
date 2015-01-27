#!/bin/sh

echo "---------------------------------------"
echo "TRAYENDO CAMBIOS DEL REPOSITORIO"
git pull

echo "---------------------------------------"
echo "MIGRANDO BASE DE DATOS"
python2.7 manage.py migrate

echo "---------------------------------------"
echo "RECOLECTANDO ARCHIVOS ESTATICOS"
python2.7 manage.py collectstatic

echo "---------------------------------------"
echo "REINICIANDO  SERVIDOR"
../apache2/bin/restart