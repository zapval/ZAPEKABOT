import command_system
from flask import Flask, request, json
import vkapi
import settings
import keyb
import vk
from PIL import Image, ImageDraw, ImageFont
import sys
from io import BytesIO
import io
import random
import traceback
import requests



def redphoto():
    data = json.loads(request.data)
    object = data['object']
    message = object['message']
    text = message['text']
    attachments = message['attachments']
    text1 = text.split("\n")
    try:
        text = text1[1]
    except IndexError:
        peer_id =  message['peer_id']
        message = 'бро, напиши текст, который ты хочешь вставить, во второй строчке...\nпо такому типу\n"валя напиши\nпривки"'
        attachment = ''
        random_id = random.randint(1,100)
        token = "e4b9fa2affa7571dd84575f65a9159830f14533b6c2cdf7f981794795b22fb54c1b7b691b845468fd9c27"
        attachment = ''
        keyboard = keyboard = {"buttons":[],"one_time":True}
        keyboard = json.dumps(keyboard, ensure_ascii = False)
        vkapi.send_message(peer_id, token, keyboard, random_id, message, attachment)

    text = text1[1]
    max = 100
    for a in attachments:
        id = a['photo']['id']
    for a in attachments:
        owner_id = a['photo']['owner_id']
    for a in attachments:
        access_key = a['photo']['access_key']
    for a in a['photo']['sizes']:
        if max <= a['height']:
            max = a['height']
            min = a['width']
            url = a['url']
    resp = requests.get(url)
    img = Image.open(BytesIO(resp.content))
    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/home/z/zapval/zapekabot/HelloFlask/Roboto-Regular.ttf", 60, encoding='UTF-8')
    idraw.text((min/2 - (20 * len(text)/2), max/2-30), text, font = font, fill='#1C0606')
    bytes_io = io.BytesIO()
    img.save(bytes_io, format='PNG')
    img.close()
    bytes_io.seek(0)
    files={'photo': ('file.png', bytes_io, 'image/png')}
    url1 = vkapi.get_photo22(settings.access_token)
    response = requests.post(url1 , files=files)
    result = json.loads(response.text)
    server=result["server"]
    photo=result["photo"]
    hash=result["hash"]
    id, owner_id, access_key = vkapi.save_photo22(settings.access_token, server, photo, hash)
    message = 'готово'
    attachment = 'photo' + str(owner_id) + '_' + str(id) + '_' + str(access_key)
    keyboard = {"buttons":[],"one_time":True}
    return message, attachment, keyboard


redphoto_command = command_system.Command()

redphoto_command.keys = ['валя напиши']
redphoto_command.process = redphoto
