import command_system
from flask import Flask, request, json
import vkapi
import settings



def get_button(label, color, payload = ''):
       return {
               "action": {
                   "type": "text",
                   "payload": {'buttons': '1'},
                   "label": label
               },
               "color": color
           }

def sil_button(label, link, payload = ''):
       return {
               "action": {
                   "type": "open_link",
                   "link": link,
                   "payload": {'buttons': '1'},
                   "label": label
               },
           }
           


