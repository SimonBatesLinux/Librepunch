# Librepunch

Contributers:
Simon Andrew Bates

<h1>Dependencies:</h1>
bash, sh, python3

<h1>Usage Guide:</h1>
<h4>
to exit pin to command line: exit <br/>
start libre punch: ./librepunch -s<br/>
list all users: ./librewolf -l<br/>
remove users: ./librewolf -d {pin}<br/>
add/edit users: ./librepunch -e {pin} {name}<br/>
</h4>

<h1>Install guide:</h1>

run:
<h4>git clone https://github.com/SimonBatesLinux/Librepunch.git<br/>
nano Librepunch/.librepunch/python_files/librepunch.py<br/>

Than in the nano editor find the lines:
<h4>USER_FILE = "$HOME/.librepunch/data_files/user.dat"<br/>
LOG_FILE = "$HOME/.librepunch/data_files/USER.log"</h4>

than replace $HOME with the your home folder.
hit <h4>crtl+o</h4> and enter to save the changes and than hit <h4>ctrl+x</h4> to leave the nano editor.

Than run:
<h4>
cp librepunch $HOME<br/>
chmod u=rwx librepunch<br/>
cp -r .librepunch $HOME<br/>
cd<br/>
echo "./librepunch -s" >> .bashrc<br/>
</h4>
