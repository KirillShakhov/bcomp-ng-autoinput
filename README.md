# bcomp-ng-autoinput
Скрипт, который позволяет вбивать команды в БЭВМ-NG без рутины. 
Команды автоматически преобразуются в двоичный код и вбиваются в БЭВМ-NG с помощью библиотеки pyautogui.

### Установка

* `pip install pyautogui`

### Использование

1. Занести, следуя синтаксису, всё необходимое для команд построчно в файл `input.txt`
2. Подправить вызовы функций в `main.py`
3. Запустить через `python main.py` в консоли.
4. Переключить окно на БЭВМ-NG

### Синтаксис input.txt:
* Первая строчка, после строчки `BEGIN` это адрес с которого будут вбиваться команды.
* Остальные строчки это команды, которые будут вбиваться друг за другом.

Скрипт к регистру не чувствителен.
