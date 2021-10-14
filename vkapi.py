import vk
import random
from settings import *
from flask import Flask, request, json
import time
import settings

session = vk.Session()
api = vk.API(session, v = 5.103)

def get_random_wall_hen(owner_id, token):
    max_num = api.video.get(owner_id=owner_id, album_id='1', count=0, access_token=token)['count']
    num = random.randint(1, max_num)
    media_id = api.video.get(owner_id=str(owner_id), album_id='1', count=1, offset=num, access_token=token)['items'][0]['id']
    attachment = 'video' + str(owner_id) + '_' + str(media_id)
    return attachment

def get_random_mult(owner_id, token):
    max_num = api.video.get(owner_id=owner_id, album_id='2', count=0, access_token=token)['count']
    num = random.randint(1, max_num)
    media_id = api.video.get(owner_id=str(owner_id), album_id='2', count=1, offset=num, access_token=token)['items'][0]['id']
    attachment = 'video' + str(owner_id) + '_' + str(media_id)
    return attachment

def get_random_wall_mem(owner_id, token):
    max_num = api.wall.get(owner_id=owner_id, filter = 'all', count=0, access_token=token)['count']
    num = random.randint(1, max_num)
    media_id = api.wall.get(owner_id=str(owner_id), filter = 'all', count=1, offset=num, access_token=token)['items'][0]['id']
    attachment = 'wall' + str(owner_id) + '_' + str(media_id)
    return attachment

def get_name(owner_id, access_token):
    user_get=api.users.get(user_ids = owner_id, access_token = access_token)
    user_get=user_get[0]
    first_name=user_get['first_name']
    last_name=user_get['last_name']
    full_name=first_name+" "+last_name
    return full_name
    
def get_photo(owner_id, access_token):
    user_get=api.users.get(user_ids = (owner_id), fields = 'photo_id', access_token = access_token)
    user_get=user_get[0]
    photo = user_get['photo_id']
    return photo
    
def get_doc22(peer_id, access_token):
    user_get = api.docs.getWallUploadServer(group_id = '194336319', access_token = access_token)
    docc = user_get['upload_url']
    return docc

def save_doc22(access_token, title, file):
    user_get = api.docs.save(access_token = access_token, title = title, file= file)
    user_get=user_get['doc']
    id = user_get['id']
    owner_id = user_get['owner_id']
    return id, owner_id

def get_photo22(access_token):
    user_get = api.photos.getMessagesUploadServer(peer_id = 0, access_token = access_token)
    photo = user_get['upload_url']
    return photo

def save_photo22(access_token, server, photo, hash):
    user_get = api.photos.saveMessagesPhoto(peer_id = 0, access_token = access_token, server = server, photo= photo, hash = hash)
    user_get=user_get[0]
    id = user_get['id']
    owner_id = user_get['owner_id']
    access_key = user_get['access_key']
    return id, owner_id, access_key
    
def make_board(group_id, text, title):
    api.board.addTopic(group_id = group_id, text = text, title = title, from_group = 1,  access_token = "3ded26e9c079879f0941daffd8f467f120ff665992d6f481656760c783f86efda9220ea141bf38f64c926")


def send_message(peer_id, random_id, keyboard, token, message, attachment):
    api.messages.send(access_token = "c8991d8af3905eaf984126a9ac844c559113e881349d7cdf880ddf8f686044e1153bb60c6af779121add4", keyboard = keyboard, random_id = random.randint(1,100), peer_id=str(peer_id), message=message, attachment=attachment)
