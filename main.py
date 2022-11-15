from PIL import Image
from colorama import Fore,init
from sys import argv

args = argv # получаем параметры запуска 
init() # Инициализация Coloram'ы

# Возвращает 1 из 8 цветом взависимости от входного стандратного 24 битного
def getColor(color):
    c = []
    for a in color:
        c.append(round(a/255*1.4))
        
    s = " ".join(str(x)for x in c)
    if s=="0 0 1": return Fore.BLUE
    elif s=="0 1 0": return Fore.GREEN
    elif s=="0 1 1": return Fore.CYAN
    elif s=="1 0 0": return Fore.RED
    elif s=="1 0 1": return Fore.MAGENTA
    elif s=="1 1 0": return Fore.YELLOW
    elif s=="1 1 1": return Fore.WHITE
    else: return Fore.BLACK

def toAscii(path,width,height=0,alphabet=""):
    file = Image.open(path) # Получаем файл из пути
    img = file.load() # получение двухмерного списка с цветами пикселей 
    
    w = file.size[0]-1 # ширина оригинального изо -1
    h = file.size[1]-1 # высота оригинального изо -1

    symbolRate = 5/2 # соотношение символов
    originalRate = w/h # соотношение оригинальное
    rate = round(originalRate*symbolRate) # соотношение итоговое
    
    if height == 0: # если высота не указана
        height = round(width/rate) # высчитываем высоту изо в консоли

    for y in range(height):
        line = "" # инициализируем пустую строку
        for x in range(width):
            #OnOriginalImage
            xOOI = round((x/width) * w) # координата X на оригинальном изо
            yOOI = round((y/height) * h) # координата Y на оригинальном изо

            color = img[xOOI,yOOI] # Получаем цвет пикселя в оригинальном изо
            shade = (color[0]+color[1]+color[2])/(255*3) # Преобразуем в значение от 0 до 1
            line = line + getColor(color) + alphabet[round(shade*len(alphabet)-1)] # прибавляем к строке соответсвующий символ
        print(line) # Отображаем строку
        
toAscii(args[1],int(args[2]), alphabet = " .-:!/r(l1Z4H9W8$@") # вызываем функцию отрисовки
