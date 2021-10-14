import command_system
from flask import Flask, request, json
import vkapi
import settings
import keyb
import random
import time

def sosi():
    message = 'сам соси'
    attachment = ''
    keyboard = {"buttons":[],"one_time":True}
    return message, attachment, keyboard

sosi_command = command_system.Command()

sosi_command.keys = ['соси']
sosi_command.process = sosi
