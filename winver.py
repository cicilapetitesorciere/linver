import PySimpleGUI as sg
import os

sg.Window(title='About Windows',
          layout=[
              [sg.Image('windows.png')],
          ],
          margins=(0, 0)).read()

