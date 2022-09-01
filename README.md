# linver

Stupid `winver` parody for Linux systems

### Dependenacies
- python3
- pip
- python3-tkinter
- PySimpleGUI

### Installation
Make sure you have `python3`, `pip` installed, and `python3-tkinter` installed; and install PySimpleGUI
```
pip3 install PySimpleGUI
``` 
Then in some directory of your choice, clone this repo

```
git clone https://github.com/cicilapetitesorciere/linver
```
Finally add the following lines to the end of your `.bashrc` and change the placeholder paths to the path you cloned `linver` into
```
alias linver="(cd /path/to/linver; python3 linver.py)"
alias winver="(cd /path/to/linver; python3 winver.py)"
```
