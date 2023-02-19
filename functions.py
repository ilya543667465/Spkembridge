import asyncio
from aiogram import *
import pandas as pd

async def odd_D192_monday(message: types.Message):
    rasp = pd.read_excel(io='Расписание спк.xlsx',
                         engine='openpyxl',
                         usecols='DW:DZ',
                         header=7,
                         nrows=11)
    rasp = rasp.fillna('')
    rasp.columns = ['', '', '', '']
    rasp.index = ['1', '', '2', '', '3', '', '4', '', '5', '', '6']
    await message.answer(f'{rasp}')



async def odd_D192_tuesday(message: types.Message):
    rasp = pd.read_excel(io='Расписание спк.xlsx',
                         engine='openpyxl',
                         usecols='DW:DZ',
                         header=20,
                         nrows=11)
    rasp = rasp.fillna('')
    rasp.columns = ['Предмет', 'Кабинет', 'Предмет', 'Кабинет']
    rasp.index = ['1', '', '2', '', '3', '', '4', '', '5', '', '6']
    await message.answer(f'{rasp}')

async def odd_D192_wednesday(message: types.Message):
        rasp = pd.read_excel(io='Расписание спк.xlsx',
                             engine='openpyxl',
                             usecols='DW:DZ',
                             header=32,
                             nrows=11)
        rasp = rasp.fillna('')
        rasp.columns = ['', '', '', '']
        rasp.index = ['1', '', '2', '', '3', '', '4', '', '5', '', '6']
        await message.answer(f'{rasp}')


async def odd_D192_thursday(message: types.Message):
        rasp = pd.read_excel(io='Расписание спк.xlsx',
                             engine='openpyxl',
                             usecols='DW:DZ',
                             header=44,
                             nrows=11)
        rasp = rasp.fillna('')
        rasp.columns = ['Предмет', 'Кабинет', 'Предмет', 'Кабинет']
        rasp.index = ['1', '', '2', '', '3', '', '4', '', '5', '', '6']
        await message.answer(f'{rasp}')


async def odd_D192_friday(message: types.Message):
        rasp = pd.read_excel(io='Расписание спк.xlsx',
                             engine='openpyxl',
                             usecols='DW:DZ',
                             header=56,
                             nrows=11)
        rasp = rasp.fillna('')
        rasp.columns = ['Предмет', 'Кабинет', 'Предмет', 'Кабинет']
        rasp.index = ['1', '', '2', '', '3', '', '4', '', '5', '', '6']
        await message.answer(f'{rasp}')


async def odd_D192_saturday(message: types.Message):
        rasp = pd.read_excel(io='Расписание спк.xlsx',
                             engine='openpyxl',
                             usecols='DW:DZ',
                             header=68,
                             nrows=11)
        rasp = rasp.fillna('')
        rasp.columns = ['Предмет', 'Кабинет', 'Предмет', 'Кабинет']
        rasp.index = ['1', '', '2', '', '3', '', '4', '', '5', '', '6']
        await message.answer(f'{rasp}')
