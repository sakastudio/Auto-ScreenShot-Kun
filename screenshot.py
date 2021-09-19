import datetime
import os
import time
import threading
import pyautogui
import diff_img
from plyer import notification

def initSetting(_startX, _startY, _endX, _endY, path):
    global startX
    startX = _startX
    global startY
    startY = _startY
    global endX
    endX = _endX
    global endY
    endY = _endY
    global filePath
    filePath = path

def StartScreenshot():
    thread = threading.Thread(target=screenShotThreading)
    thread.start()


def screenShotThreading():
    screenshot = pyautogui.screenshot(region=(startX, startY, endX-startX, endY-startY))
    screenshot.save(getPath('last_tmp'))
    screenshot.save(getPath('tmp'))
    global isStop
    while not isStop:
        time.sleep(1)
        #スクリーンショットの撮影
        if os.path.exists(getPath('last_tmp')):
            os.remove(getPath('last_tmp'))
        os.rename(getPath('tmp'), getPath('last_tmp'))
        screenshot = pyautogui.screenshot(region=(startX, startY, endX-startX, endY-startY))
        screenshot.save(getPath('tmp'))

        score = diff_img.getdiff_img(getPath('tmp'), getPath('last_tmp'))
        print(score)

        if 0.05 < score:
            dt_now = datetime.datetime.now()
            pngname = getPath(str(dt_now.strftime('%Y-%m-%d- %H-%M-%S')))
            os.rename(getPath('last_tmp'), pngname)
            time.sleep(0.1)

def TakeScreenShot():
    print(filePath)
    dt_now = datetime.datetime.now()
    pngname = getPath(str(dt_now.strftime('%Y-%m-%d %H-%M-%S')))
    screenshot = pyautogui.screenshot(region=(startX, startY, endX-startX, endY-startY))
    screenshot.save(pngname)
    time.sleep(0.2)

def StopScreenshot():
    global isStop
    isStop = True


def getPath(optionText):
    return filePath + '/自動スクショ ' + optionText + '.png'


filePath = ""
isStop = False
startX = -1
startY = -1
endX = -1
endY = -1