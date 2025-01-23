from ModulesH import *


def audio_callback(indata, frames, time, status):
    """Обработчик аудио входного потока."""
    if status:
        print(f"Error in audio callback: {status}")

    pcm = np.frombuffer(indata, dtype=np.int16)
    for i in range(0, len(pcm), porcupine.frame_length):
        frame = pcm[i:i + porcupine.frame_length]
        if len(frame) == porcupine.frame_length and porcupine.process(frame) >= 0:
            print("Активационная фраза распознана!")
            play_audio("audio/yes.wav")
            process_speech_recognition()

def process_speech_recognition():
    """Обработка речи после активации."""
    
    print("Начинаю распознавание речи...")
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1000)
    stream.start_stream()

    while True:
        data = stream.read(400, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result()).get("text", "")
            print("Распознано:", result)
            if result:
                handle_command(result)
                break
        else:
            print("Промежуточно:", json.loads(recognizer.PartialResult()).get("partial", ""), end="\r")
        
    stream.stop_stream()
    stream.close()
    mic.terminate()

def handle_command(command):
    
    """Обработка команд пользователя."""
    
    if "новый проект" in command:
        command = command.replace("новый проект ", "")
        newProject(command)

  
    if "найди мне" not in command and "открой браузер" in command:
        openingClosingB()
        command = command.replace("открой браузер", "")
        command = command.replace(" и ", "")  
    else:
        command = command.replace("открой браузер", "")
        command = command.replace(" и ", "") 
    
    if "включи прокси" in command:
        startVPN()
        command = command.replace("включи прокси", "")
    if "выключение" in command:
        shutdown()

    if "громкость на" in command:
        volume(words_to_numbers_russian(command.replace("громкость на", "").strip()))

    if "включи музыку" in command:
        command = command.replace("включи музыку", "")

    if "найди мне" in command:
        search(command.replace("найди мне", "").strip())
    
    if "завершение процесса" in command:
        play_audio("audio/Есть.wav")
        os._exit(0)
    if "молодец" in command:
        play_audio("audio/Всегда к вашим услугам сэр.wav")
    
    if "просмотр видео" in command:
        play_audio("audio/down.wav")
        youTube()


if __name__ == "__main__":
    porcupine = pvporcupine.create(access_key="kdQ3MfqR0hE05kGYn0EfDD3B+dQj0Xk2jiXrszZqNLfEonDKgedBPA==", keyword_paths=["audio/jarvis.ppn"])
    recognizer = KaldiRecognizer(Model("vosk-model-ru-0.22"), 16000)
    play_audio("audio/a1.wav")
    print("Готово к работе, слушаю...")
    with sd.InputStream(channels=1, samplerate=porcupine.sample_rate, dtype="int16", blocksize=porcupine.frame_length, callback=audio_callback):
        while True:
            pass
    

    porcupine.delete()


# def handle_command(command):
#     """Обработка команд пользователя с учетом расстояния Левенштейна."""
#     commands = {
#         "открой браузер": openingClosingB,
#         "найди мне": search,
#         "включи музыку эйси диси": playSong,
#         "протокол обхода": startVPN,
#         "выключение": shutdown,
#         "громкость на": volume,
#     }

#     # Выбор команды с минимальным расстоянием Левенштейна
#     closest_command = None
#     min_distance = float('inf')
    
#     for template_command in commands:
#         distance = Levenshtein.distance(command, template_command)
#         if distance < min_distance:
#             min_distance = distance
#             closest_command = template_command
    
#     # Если минимальное расстояние меньше порогового, выполняем команду
#     if min_distance <= 3:  # Пороговое значение, можно изменить в зависимости от потребностей
#         print(f"Исполняем команду: {closest_command}")
#         if closest_command == "найди мне":
#             # Для поиска нужно передать измененную строку
#             commands[closest_command](command.replace("найди мне", "").strip())
#         elif "громкость на" in command:
#             # Для громкости преобразуем строку в число
#             commands[closest_command](words_to_numbers_russian(command.replace("громкость на", "").strip()))
#         else:
#             commands[closest_command]()
#     else:
#         print("Не распознана команда.")





# def levenshtein_distance(s1, s2):
#     """Вычисление расстояния Левенштейна между двумя строками."""
#     len_s1, len_s2 = len(s1), len(s2)
#     dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
#     for i in range(len_s1 + 1):
#         for j in range(len_s2 + 1):
#             if i == 0:
#                 dp[i][j] = j
#             elif j == 0:
#                 dp[i][j] = i
#             elif s1[i - 1] == s2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
#     return dp[len_s1][len_s2]







# def levenshtein_distance(s1, s2):
#     """Вычисление расстояния Левенштейна между двумя строками."""
#     len_s1, len_s2 = len(s1), len(s2)
#     dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

#     for i in range(len_s1 + 1):
#         for j in range(len_s2 + 1):
#             if i == 0:
#                 dp[i][j] = j  # Удаления из s2
#             elif j == 0:
#                 dp[i][j] = i  # Удаления из s1
#             elif s1[i - 1] == s2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]  # Совпадение символов
#             else:
#                 dp[i][j] = 1 + min(dp[i - 1][j],    # Удаление
#                                   dp[i][j - 1],    # Вставка
#                                   dp[i - 1][j - 1]) # Замена
#     return dp[len_s1][len_s2]

# # Примеры использования:
# word1 = "кот"
# word2 = "крот"

# distance = levenshtein_distance(word1, word2)
# print(f"Расстояние Левенштейна между '{word1}' и '{word2}': {distance}")

# # Можно использовать для исправления ошибок в словах:
# input_word = "превед"
# correct_words = ["привет", "проверка", "приветствие"]

# closest_match = min(correct_words, key=lambda w: levenshtein_distance(input_word, w))
# print(f"Возможно, вы имели в виду: {closest_match}")
