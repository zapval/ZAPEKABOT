import command_system
from flask import Flask, request, json
import vkapi
import settings
import keyb


def iktv84():
   message = 'Вот список моих команд для ИКТВ-84:\n\nДЗ - ссылка на "актуальное" дз;\nЦСИОС - ссылка на гугл диск где все лабы.'
   attachment = ''
   keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.sil_button(label = 'ДЗ', link = 'https://docs.google.com/spreadsheets/d/1nzrsXfkMMRsaieNcIv1yH5SucXi7YqPeByYx8hVEXUQ/edit?usp=sharing'),
                keyb.sil_button(label = 'ЦСИОС', link = 'https://drive.google.com/drive/folders/1CBMGQ3j1AM1fO15MuJ_L90e9qNRK_ze9')],
                [keyb.sil_button(label = 'СССК', link = 'https://drive.google.com/drive/folders/1zYzePMNYDglP1klm5_vpje-R8eobNpl0'),
                keyb.sil_button(label = 'ОПИСИС', link = 'https://drive.google.com/drive/folders/1CBMGQ3j1AM1fO15MuJ_L90e9qNRK_ze9')]
            ]
            }
   return message, attachment, keyboard

iktv84_command = command_system.Command()

iktv84_command.keys = ['валя иктв-84', 'валя иктв84', 'валя иктв 84', '[club194336319|@zapekabot] валя иктв-84']
iktv84_command.process = iktv84
