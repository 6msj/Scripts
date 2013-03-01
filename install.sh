#!/bin/bash

# cd to working directory
cd `dirname $0`

# start fresh with startMaster.sh_backup
cp astposmac/lib/startMaster.sh_backup astposmac/lib/startMaster.sh
cp auramac/lib/startMaster.sh_backup auramac/lib/startMaster.sh

# (1) get the java_home, edit startMaster.sh and move to newFile
sed "3i\ 
JAVA_HOME=$(/usr/libexec/java_home)" astposmac/lib/startMaster.sh > newFile

# (2) mv newFile to startMaster.sh
mv newFile astposmac/lib/startMaster.sh

# (3) make startMaster.sh executable
chmod +x astposmac/lib/startMaster.sh

# (1)
sed "7i\ 
JAVA_HOME=$(/usr/libexec/java_home)" auramac/lib/startMaster.sh > newFile

# (2)
mv newFile auramac/lib/startMaster.sh

# (3)
chmod +x auramac/lib/startMaster.sh

echo "Setting Java Home"

# copy them to the right directories
cp -r astposmac /usr/local/
cp -r auramac /usr/local/

echo "Copying to /usr/local/"

echo "Done."
