#!/bin/sh

echo "---------------------------------------"
echo "TRAYENDO CAMBIOS DEL REPOSITORIO"
git checkout

echo "---------------------------------------"
echo "MIGRANDO BASE DE DATOS"
python2.7 manage.py migrate

echo "---------------------------------------"
echo "REINICIANDO  SERVIDOR"
../apache2/bin/restart