import command_system
import vkapi
import settings
import random


def komplimenty2():
    komplimenty1 = 'Ты лучшая!.У тебя все получится.Ты очень милая)'
    fff = komplimenty1.count('.')
    komplimenty1 = komplimenty1.rsplit(sep='.')
    komplimenty = komplimenty1[random.randint(0,fff)]


    return komplimenty
