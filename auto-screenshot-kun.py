import sys
import tkinter
from tkinter import messagebox, filedialog
import pyautogui  # 外部ライブラリ
from PIL import Image, ImageTk  # 外部ライブラリ
import screenshot

RESIZE_RETIO = 2 # 縮小倍率の規定

# ドラッグ開始した時のイベント - - - - - - - - - - - - - - - - - - - - - - - - - -
def start_point_get(event):
    global start_x, start_y # グローバル変数に書き込みを行なうため宣言

    canvas1.delete("rect1")  # すでに"rect1"タグの図形があれば削除

    # canvas1上に四角形を描画（rectangleは矩形の意味）
    canvas1.create_rectangle(event.x,
                             event.y,
                             event.x + 1,
                             event.y + 1,
                             outline="red",
                             tag="rect1")
    # グローバル変数に座標を格納
    start_x, start_y = event.x, event.y

# ドラッグ中のイベント - - - - - - - - - - - - - - - - - - - - - - - - - -
def rect_drawing(event):

    # ドラッグ中のマウスポインタが領域外に出た時の処理
    if event.x < 0:
        end_x = 0
    else:
        end_x = min(img_resized.width, event.x)
    if event.y < 0:
        end_y = 0
    else:
        end_y = min(img_resized.height, event.y)

    # "rect1"タグの画像を再描画
    canvas1.coords("rect1", start_x, start_y, end_x, end_y)

# ドラッグを離したときのイベント - - - - - - - - - - - - - - - - - - - - - - - - - -
def release_action(event):

    # "rect1"タグの画像の座標を元の縮尺に戻して取得
    global end_x
    global end_y
    global start_x
    global start_y
    start_x, start_y, end_x, end_y = [
        round(n * RESIZE_RETIO) for n in canvas1.coords("rect1")
    ]
    # 取得した座標を表示
    ret = messagebox.askyesno('範囲の確認', "この範囲を自動スクリーンショットします。よろしいですか？")
    print(start_x, start_y, end_x, end_y)
    if ret:
        tkinter.messagebox.showinfo('保存先フォルダの選択', '保存先フォルダを選択してください。')
        global filePath
        filePath = filedialog.askdirectory()
        while filePath != "" and not messagebox.askyesno('保存先フォルダの確認', "保存先フォルダはこれでよろしいですか？\n"+filePath):
            filePath = filedialog.askdirectory()
        canvas1.destroy()
        root.attributes("-topmost", True)
        root.geometry("300x300")
        tkinter.Label(root,text='スクリーンショット設定').pack()
        startButton.pack()
        takeScreenShotButton.pack()
        screenshot.initSetting(start_x, start_y, end_x, end_y,filePath)

def startScreenshot():
    if startButtonText.get() == "スクショスタート":
        startButtonText.set("スクショストップ")
        screenshot.StartScreenshot()
    else:
        startButtonText.set("スクショスタート")
        screenshot.StopScreenshot()

def takeScreenShot():
    screenshot.TakeScreenShot()

def quit_me():
    print('quit')
    screenshot.StopScreenshot()
    root.quit()
    root.destroy()
    sys.exit(0)



# メイン処理 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__":

    # 表示する画像の取得（スクリーンショット）
    img = pyautogui.screenshot()
    # スクリーンショットした画像は表示しきれないので画像リサイズ
    img_resized = img.resize(size=(int(img.width / RESIZE_RETIO),
                                   int(img.height / RESIZE_RETIO)),
                             resample=Image.BILINEAR)

    root = tkinter.Tk()
    root.protocol("WM_DELETE_WINDOW", quit_me)
    root.title("自動スクリーンショットくん")
    root.attributes("-topmost", True) # tkinterウィンドウを常に最前面に表示

    filePath = ""
    startButtonText = tkinter.StringVar()
    startButtonText.set("スクショスタート")
    startButton = tkinter.Button(root, textvariable=startButtonText, command=startScreenshot)
    takeScreenShotButton = tkinter.Button(root, text="スクショを撮る", command=takeScreenShot)

    # tkinterで表示できるように画像変換
    img_tk = ImageTk.PhotoImage(img_resized)

    tkinter.StringVar()

    # Canvasウィジェットの描画
    canvas1 = tkinter.Canvas(root,
                             bg="black",
                             width=img_resized.width,
                             height=img_resized.height)
    # Canvasウィジェットに取得した画像を描画
    canvas1.create_image(0, 0, image=img_tk, anchor=tkinter.NW)
    # Canvasウィジェットを配置し、各種イベントを設定
    canvas1.pack()
    canvas1.bind("<ButtonPress-1>", start_point_get)
    canvas1.bind("<Button1-Motion>", rect_drawing)
    canvas1.bind("<ButtonRelease-1>", release_action)

    tkinter.messagebox.showinfo('自動スクリーンショットくん', 'スクリーンショットを撮る範囲を選択してください。')
    root.mainloop()