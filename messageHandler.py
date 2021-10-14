import vkapi
import os
import importlib
from command_system import command_list
from flask import Flask, request, json
import komplimenty
import salf
import keyb
import random

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("HelloFlask/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(text):
    # Сообщение по умолчанию если распознать не удастся
    message = ''
    attachment = ''
    keyboard = ''
    delimiter = ''
    lat = ''
    long = ''
    textbez1 = text.split()
    textbez = ''.join(textbez1)
    for c in command_list:
        i=0
        k=4
        while k <= len(textbez):
            slovo = (textbez[i:k])
            if slovo in c.keys:
                message, attachment, keyboard = c.process()
                break
            i = i + 1
            k = k + 1
        i=0
        while i <= len(text):
            slovo = (text[0:i])
            if slovo in c.keys:
                message, attachment, keyboard = c.process()
                break
            i = i + 1
    return message, attachment, keyboard

def create_answer(data, token):
    load_modules()
    peer_id = data['message']['peer_id']
    random_id = data['message']['random_id']
    message, attachment, keyboard = get_answer(data['message']['text'].lower())
    keyboard = json.dumps(keyboard, ensure_ascii = False)
    vkapi.send_message(peer_id, token, keyboard, random_id, message, attachment)
    