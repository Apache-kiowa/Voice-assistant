import os
import re
import subprocess
from actionModules.playAudio import * 
def newProject(kind):
  
    play_audio("audio/Начинаю автоматическую сборку.wav")
    base_path = os.path.abspath(os.path.join(os.getcwd(), "../"))  

   
    pattern = re.compile(r"project-(\d+)")

   
    existing_folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

   
    project_numbers = []

    for folder in existing_folders:
        match = pattern.match(folder)
        if match:
            project_numbers.append(int(match.group(1)))

  
    if project_numbers:
        next_number = max(project_numbers) + 1
    else:
        next_number = 1  

    new_folder_name = f"project-{next_number}-{kind}"
    new_folder_path = os.path.join(base_path, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)


    requirements_path = os.path.join(new_folder_path, "requirements.txt")


    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    if result.returncode == 0:
        requirements_content = result.stdout
    else:
        requirements_content = "# Ошибка при получении зависимостей\n"

    #requirements.txt
    with open(requirements_path, "w") as file:
        file.write("# Зависимости проекта\n")
        file.write(requirements_content)



    # README.md
    with open(os.path.join(new_folder_path, "README.md"), "w") as file:
        file.write(f"# Проект {new_folder_name}\n")
        file.write("Описание проекта и инструкции по использованию.")

    # LICENSE
    with open(os.path.join(new_folder_path, "LICENSE"), "w") as file:
        file.write("Лицензия проекта. Укажите условия использования.")

    # setup.py
    with open(os.path.join(new_folder_path, "setup.py"), "w") as file:
        file.write("from setuptools import setup, find_packages\n")
        file.write("setup(\n")
        file.write("    name='project',\n")
        file.write("    version='0.1',\n")
        file.write("    packages=find_packages(),\n")
        file.write("    install_requires=[],\n")
        file.write(")\n")

    # main.py (точка входа)
    with open(os.path.join(new_folder_path, "main.py"), "w") as file:
        file.write("def main():\n")
        file.write("    print('Hello, world!')\n")
        file.write("\n")
        file.write("if __name__ == '__main__':\n")
        file.write("    main()\n")

    # Структура для тестов
    test_folder_path = os.path.join(new_folder_path, "tests")
    os.makedirs(test_folder_path, exist_ok=True)
    with open(os.path.join(test_folder_path, "__init__.py"), "w") as file:
        file.write("# Инициализация пакета для тестов\n")

    # Пример теста
    with open(os.path.join(test_folder_path, "test_main.py"), "w") as file:
        file.write("import unittest\n")
        file.write("from main import main\n")
        file.write("\n")
        file.write("class TestMainFunction(unittest.TestCase):\n")
        file.write("    def test_main(self):\n")
        file.write("        self.assertEqual(main(), None)  # Просто пример теста\n")
        file.write("\n")
        file.write("if __name__ == '__main__':\n")
        file.write("    unittest.main()\n")

    # .gitignore
    with open(os.path.join(new_folder_path, ".gitignore"), "w") as file:
        file.write("__pycache__/\n")
        file.write(".venv/\n")
        file.write(".env/\n")
        file.write("*.pyc\n")
        file.write("*.log\n")

    print(f"Проект {new_folder_name} успешно создан с файлами: README.md, LICENSE, setup.py, main.py, requirements.txt, и тестами.")
