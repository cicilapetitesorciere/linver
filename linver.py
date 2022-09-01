import PySimpleGUI as sg
import os

bcolour='#f1f1f1'
os.system('uname -r > version.txt')
version_file=open('version.txt')
version = version_file.read()
version_file.close()

sg.Window(title='About Linux',
          background_color=bcolour,
          size=(500,500),
          layout=[
              [sg.Image('linux.png',background_color=bcolour,)],
              [sg.MLine('GNU Linux\n'+version+'\n\nThe Linux kernel is protected under the GNU General Public Licence in the United States and other countries/regions.',
                            background_color=bcolour,
                            no_scrollbar=True,
                            size=(50,50),
                            disabled=True,
                            text_color='black')
               ],
              [sg.Button('OK')]
          ],
          margins=(100, 50)).read()

