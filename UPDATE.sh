
#	This file is part of librepunch.

#    librepunch is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    librepunch is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with librepunch.  If not, see <https://www.gnu.org/licenses/>.

#!/bin/sh
echo "Installing prerequisites"
sudo apt upgrade zsh
sudo apt upgrade python3
sudo apt upgrade pip3
sudo pip install pygame
echo "prequisites installed"
echo "install librepunch"
sudo cp librepunch /bin/librepunch
sudo chmod u=rwx /bin/librepunch
sudo chmod g=rx /bin/librepunch
sudo chmod o=rx /bin/librepunch
echo "We suggest you backup $HOME/.librepunch/settings if you want to keep those settings now"
read -rsp $'Press any key to continue...\n' -n 1 key

mkdir -p $HOME/.librepunch/program_files 2> /dev/null
cp .librepunch/main.py $HOME/.librepunch
cp .librepunch/settings.py $HOME/.librepunch
echo "librepunch upgraded"
