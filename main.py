# 15.11.2022 ©Sinus44
# Параметры запуска: {путь к картинке} {ширина в символах} {яркость}
# пример: py main.py photo.jpg 200 1

from PIL import Image
from sys import argv
import os
from colorama import Fore,init
init() # Инициализация Coloram'ы

# Возвращает 1 из 8 цветом взависимости от входного стандратного 24 битного
def getColor(color,brightness):
    c = []
    for a in color:
        c.append(max(0, min(1, round(a/255*brightness))))
        
    s = " ".join(str(x)for x in c)
    if s=="0 0 1": return Fore.BLUE
    elif s=="0 1 0": return Fore.GREEN
    elif s=="0 1 1": return Fore.CYAN
    elif s=="1 0 0": return Fore.RED
    elif s=="1 0 1": return Fore.MAGENTA
    elif s=="1 1 0": return Fore.YELLOW
    elif s=="1 1 1": return Fore.WHITE
    else: return Fore.BLACK

path = argv[1]
width = int(argv[2])
alphabet = " .-:!/r(l1Z4H9W8$@"
brightness = float(argv[3])

file = Image.open(path) # Получаем файл из пути
img = file.load() # получение двухмерного списка с цветами пикселей 

w = file.size[0]-1 # ширина оригинального изо -1
h = file.size[1]-1 # высота оригинального изо -1

symbolRate = 5/2 # соотношение символов
originalRate = w/h # соотношение оригинальное
rate = round(originalRate*symbolRate) # соотношение итоговое
height = round(width/rate) # высчитываем высоту изо в консоли

os.system(f"mode con cols={width} lines={height}")

for y in range(height):
    line = "" # инициализируем пустую строку
    for x in range(width):
    	xOOI = round((x/width) * w) # координата X на оригинальном изо  #OnOriginalImage
    	yOOI = round((y/height) * h) # координата Y на оригинальном изо
		color = img[xOOI,yOOI] # Получаем цвет пикселя в оригинальном изо
		shade = (color[0]+color[1]+color[2])/(255*3) # Преобразуем в значение от 0 до 1
		line += getColor(color,brightness) + alphabet[round(shade*(len(alphabet)-1))] # прибавляем к строке соответсвующий символ
    print(line) # Отображаем строку