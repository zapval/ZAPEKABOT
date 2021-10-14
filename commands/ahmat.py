import command_system
from flask import Flask, request, json
import vkapi
import settings
import keyb
import random

def ahmat():
   # Получаем случайную картинку из паблика
   message = 'нохчи дон'
   attachment = ''
   keyboard = {"buttons":[],"one_time":True}
   return message, attachment, keyboard

ahmat_command = command_system.Command()

ahmat_command.keys = ['ахмат сила']
ahmat_command.process =  ahmat
