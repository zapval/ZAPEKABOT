import command_system
import vkapi
import settings
import random


def salf2():
    salf1 = 'photo-194336319_457239079.photo-194336319_457239080.photo-194336319_457239081.photo-194336319_457239082'
    fff = salf1.count('.')
    salf1 = salf1.rsplit(sep='.')
    salf = salf1[random.randint(0,fff)]

    return salf

