import command_system
from flask import Flask, request, json
import vkapi
import settings
import keyb
import random



def vsexne():
   message = ''
   attachment = 'doc' + '-194336319' +'_' +'572594542'
   keyboard = {"buttons":[],"one_time":True}
   return message, attachment, keyboard

vsexne_command = command_system.Command()

vsexne_command.keys = ['всех не отчислят']
vsexne_command.process = vsexne
