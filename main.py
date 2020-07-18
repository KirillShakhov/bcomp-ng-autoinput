from time import sleep
import pyautogui


def valid_str(str):
    str = bin(int(str, 16))
    str = str[2:len(str)]
    while(len(str) < 16):
        str = "0{}".format(str)
    return str

# Функция записи программы из файла
# file - файл из которого беруться команды
# sleep_time - задержка, чтобы вы могли переключить окно на БЭВМ-NG
def write(file, sleep_time = 3):
    with open(file) as f:
        myList = [ line.split() for line in f ]
    isMain = False
    sleep(sleep_time)
    print("Начало записи: {}".format(file))
    for line in myList:
        if len(line)>0:
            if line[0] == "BEGIN":
                isMain = True
            elif isMain:
                pyautogui.write(valid_str(line[0]))
                pyautogui.press("f4")
                isMain = False
            else:
                pyautogui.write(valid_str(line[0]))
                pyautogui.press("f5")
    print("Запись закончена: {}".format(file))

# Запись одной команды, например для ввода начального адреса
# str - строка, которую надо занести в IR
# sleep_time - задержка, чтобы вы могли переключить окно на БЭВМ-NG
def fast_write(str, sleep_time = 3):
    sleep(sleep_time)
    pyautogui.write(valid_str(str))


# Файл из которого беруться команды, задержка для того чтобы вы успели переключить окно на БЭВМ равна 3
write("input.txt", 3)
# Запись одной команды, например для ввода начального адреса
fast_write("4C6")