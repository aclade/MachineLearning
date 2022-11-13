# doc mau theo toa do da lay
from pynput import keyboard
from pynput import mouse
from PIL import Image, ImageGrab
import xlwt
import time
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
dem = 1

def getHex(rgb):
    return '%02X%02X%02X'%rgb


def checkColor(x,y,ptd):
    bbox = (x,y,x+1,y+1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    if r <= 70 : 
        sheet1.write(dem,ptd, 'BLUE')
    else :
        sheet1.write(dem,ptd, 'RED')

def tam():
    global dem
    time.sleep(0.2) 
    checkColor(1707,498,1)
    checkColor(1602,579,2)
    checkColor(1643,698,3)
    checkColor(1773,699,4)
    checkColor(1810,575,5)   
    dem+=1
    
def onClick(x,y, button, pressed):
	if pressed and button == mouse.Button.left:
		tam()

def onRel(key):
    if key == keyboard.Key.esc:
        wb.save('xlwt example.xls')
        mlstnr.stop()
        return False

if __name__ == '__main__':
    with keyboard.Listener(on_release = onRel) as klstnr:
        with mouse.Listener(on_click = onClick) as mlstnr:
            klstnr.join()
            mlstnr.join()
            
            