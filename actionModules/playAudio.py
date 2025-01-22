import pygame   
import os
def play_audio(file_path):
    """Функция для воспроизведения звука."""
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"Ошибка воспроизведения аудио: {e}")
    finally:
        pygame.mixer.quit()
