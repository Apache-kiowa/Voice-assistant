# ВСТРОЕННЫЕ БИБЛИОТЕКИ

# --- Работа с аудио ---
import sounddevice as sd  # Для записи и воспроизведения аудио
import pyaudio            # Для обработки аудиопотока
import Levenshtein         # Для работы с расстоянием Левенштейна (поиск схожести строк)

# --- Распознавание речи ---
from vosk import Model, KaldiRecognizer  # Для оффлайн-распознавания речи

# --- Работа с ключевыми словами ---
import pvporcupine  # Для обнаружения ключевых слов (wake words)

# --- Работа с данными ---
import json         # Для обработки данных в формате JSON
import numpy as np  # Для работы с числовыми массивами

# --- Интерфейс и дополнительные функции ---
import os           # Для работы с операционной системой (путь, директории и т.д.)
import signal       # Для обработки сигналов завершения программы
import sys

import time         # Для работы с временем
import threading    # Для работы с потоками
import asyncio      # Для работы с асинхронностью

# МОИ МОДУЛИ
from actionModules.openingClosingB import *   # Импорт из вашего модуля, работающего с браузером
from actionModules.startVPN import startVPN  # Импорт функции для включения VPN
from actionModules.playSong import playSong  # Закомментированный импорт для музыки
from actionModules.sistem import shutdown    # Импорт функции для выключения системы
from actionModules.volume import volume      # Импорт функции для управления громкостью
from actionModules.newProject import newProject 
from actionModules.youTube import youTube

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

def words_to_numbers_russian(text):
    word_to_number = {
        "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, 
        "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
        "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
        "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19,
        "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50,
        "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90,
        "сто": 100
    }

    words = text.lower().split()
    total = 0

    for word in words:
        if word in word_to_number:
            total += word_to_number[word]
        else:
            raise ValueError(f"Неизвестное число: {word}")

    return total

