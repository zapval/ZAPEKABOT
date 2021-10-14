import command_system
from flask import Flask, request, json
import vkapi
import settings
import keyb
import bagazh

def spisokstud2(text1, chto):
    nomer = ""
    users = [
        {
            "name": "Артамонов",
            "fio": "Артамонов Олег Игоревич",
            'group': 'ИКТВ-84',
            "telephone": "89046022335"
        },
        {
            "name": "Боев",
            "fio": "Боев Артём Владимирович",
            'group': 'ИКТВ-84',
            "telephone": "89500314197"
        },
        {
            "name": "Востриков",
            "fio": "Востриков Дмитрий Андреевич",
            'group': 'ИКТВ-84',
            "telephone": "89371243874"
        },
        {
            "name": "Запека",
            "fio": "Запека Валентин Геннадьевич",
            'group': 'ИКТВ-84',
            'proekt': '1NFORM',
            'dolzhnost': 'Серфер',
            "telephone": "89118155029"
        },
        {
            "name": "Козицын",
            "fio": "Козицын Кирилл Павлович",
            'group': 'ИКТВ-84',
            "telephone": "89118491144"
        },
        {
            "name": "Крицкий",
            "fio": "Крицкий Кирилл Олегович",
            'group': 'ИКТВ-84',
            "telephone": "89811496866"
        },
        {
            "name": "Куликовский",
            "fio": "Куликовский Денис Павлович",
            'group': 'ИКТВ-84',
            "telephone": "89522206394"
        },
        {
            "name": "Лагутин",
            "fio": "Лагутин Алексей Ярославович",
            'group': 'ИКТВ-84',
            "telephone": "89992198403"
        },
        {
            "name": "Магомедов",
            "fio": "Магомедов Шамиль Арсенович",
            'group': 'ИКТВ-84',
            "telephone": "89208300555"
        },
        {
            "name": "Маторыкин",
            "fio": "Маторыкин Александр Олегович",
            'group': 'ИКТВ-84',
            "telephone": "89045278558"
        },
        {
            "name": "Меджидов",
            "fio": "Меджидов Рамазан Мурадович",
            'group': 'ИКТВ-84',
            "telephone": "89898907619"
        },
        {
            "name": "Мирошник",
            "fio": "Мирошник Максим Александрович",
            'dolzhnost': 'ПОДПОЛКОВНИК',
            "telephone": "89062687570"
        },
        {
            "name": "Пальчиков",
            "fio": "Пальчиков Александр Сергеевич",
            'group': 'ИКТВ-84',
            "telephone": "89604798827"
        },
        {
            "name": "Сидоров",
            "fio": "Сидоров Евгений Сергеевич",
            'group': 'ИКТВ-84',
            "telephone": "89153431467"
        },
        {
            "name": "Соцков",
            "fio": "Соцков Александр Андреевич",
            'group': 'ИКТВ-84',
            "telephone": "89006452077"
        },
        {
            "name": "Стехов",
            "fio": "Стехов Олег Александрович",
            'group': 'ИКТВ-84',
            "telephone": "89217947840"
        },
        {
            "name": "Сысак",
            "fio": "Сысак Сергей Сергеевич",
            'group': 'ИКТВ-84',
            "telephone": "89775990181"
        },
        {
            "name": "Токмаков",
            "fio": "Токмаков Сергей Алексеевич",
            'group': 'ИКТВ-84',
            "telephone": "89990417683"
        },
        {
            "name": "Тубольцев",
            "fio": "Тубольцев Дмитрий Владимирович",
            'group': 'ИКТВ-84',
            "telephone": "89523644547"
        },
        {
            "name": "Рудасёв",
            "fio": "Рудасёв Иван Андреевич",
            'group': 'ИКТВ-84',
            "telephone": "89052198678"
        },
        {
            "name": "Бабурин",
            "fio": "Бабурин Евгений Владимирович",
            'proekt': '1NFORM',
            'dolzhnost': 'Серфер',
            "telephone": "89312016545"
        },
        {
            "name": "Диброва",
            "fio": "Диброва Олеся Павловна",
            'proekt': '1NFORM',
            'dolzhnost': 'Серфер',
            "telephone": "89200795813"
        },
        {
            "name": "Конобеевская",
            "fio": "Конобеевская Анна Алексеевна",
            'group': 'ЭМ-82',
            'proekt': '1NFORM',
            'dolzhnost': 'Серфер',
            "telephone": "89500378541"
        },
        {
            "name": "Кожокарь",
            "fio": "Кожокарь Эллина Евгеньевна",
            'proekt': '1NFORM',
            'dolzhnost': 'Ивент',
            "telephone": "89818179960"
        },
        {
            "name": "Шрейдер",
            "fio": "Шрейдер Кристина Ивановна",
            'proekt': '1NFORM',
            'dolzhnost': 'Серфер',
            "telephone": "89119559170"
        }
    ]
    
    if chto == "номер":
        for user in users:
            if "telephone" in user:
                if user["name"] == text1:
                    nomer = user["telephone"]

    if chto == "фио":
        for user in users:
            if "fio" in user:
                if user["name"] == text1:
                    nomer = user["fio"]
                    
    if chto == "группа":
        for user in users:
            if "group" in user:
                if user["name"] == text1:
                    nomer = user["group"]
                    
    if chto == "список":
        n = 1
        text1 = text1.upper()
        if text1 == 'ИНФОРМ':
            text1 = '1NFORM'
        if text1 == 'СЕРФЕРОВ' or text1 == 'СЁРФЕРОВ':
            text1 = 'Серфер'
        if text1 == 'ИВЕНТ':
            text1 = 'Ивент'
        for user in users:
            if "group" in user:
                if user["group"] == text1:
                    nomer = nomer + str(n) + ') ' + user["fio"] + ';\n'
                    n += 1
            if "proekt" in user:
                if user["proekt"] == text1:
                    nomer = nomer + str(n) + ') ' + user["fio"] + ';\n'
                    n += 1
            if "dolzhnost" in user:
                if user["dolzhnost"] == text1:
                    nomer = nomer + str(n) + ') ' + user["fio"] + ';\n'
                    n += 1

    if nomer == '':
        nomer = "Таких данных в базе нет"
        
    return nomer