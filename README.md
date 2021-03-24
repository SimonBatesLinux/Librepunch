# Librepunch

Contributers:
Simon Andrew Bates

<h1>Install guide:</h1>

run:
<h4>git clone https://github.com/SimonBatesLinux/Librepunch.git<br/>
cd Librepunch/.librepunch/python_files/<br/>
nano librepunch.py</h4><br/>

Than in the nano editor find the lines:
<h4>USER_FILE = "$HOME/.librepunch/data_files/user.dat"<br/>
LOG_FILE = "$HOME/.librepunch/data_files/USER.log"</h4>

than replace $HOME with the your home folder.
hit <h4>crtl+o</h4> and enter to save the changes and than hit <h4>ctrl+x</h4> to leave the nano editor.

Than run:
<h4>
cd ../..
cp librepunch $HOME
cp .librepunch $HOME
cd
echo "cd $HOME"
echo "./librepunch -s"
</h4>
