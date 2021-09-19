# Auto-ScreenShot-Kun
画面内の画像の変化を検知し、自動でスクリーンショットを撮影してくれるソフトです。
# 目次
[基本的な使い方](#基本的な使い方)

[撮影した画像を文字起こしする](#撮影した画像を文字起こしする)

[セットアップ](#セットアップ)

[使い方](#使い方)

[参考にしたサイト](#参考にしたサイト)

[Licence](#Licence)

## 基本的な使い方

1.[このページ](https://github.com/sakastudio/Auto-ScreenShot-Kun/releases/tag/1.0) からzipファイルをダウンロードしてください。
![img](readmeimage/1.png)

2.ダウンロードしたzipファイルを右クリックし、展開してください。

![img](readmeimage/2.png)

3.画面上に授業動画やzoomの画面を用意してください。今回はサンプルとして[こちら](https://www.youtube.com/watch?v=J9H2b5IqPHc) の動画をお借りします。

![img](readmeimage/3.png)

4.auto-screenshot-kun.exeを起動してください。

![img](readmeimage/4.png)

5.「WindowsによってPCが保護されました。」と出る場合は、「詳細情報」をクリックし、実行を押してください。

![img](readmeimage/5.png)
![img](readmeimage/6.png)

6.画面上のどの範囲のスクリーンショットを撮るかをドラッグで選択してください。

![img.png](readmeimage/7.png)
![img.png](readmeimage/8.png)

7.範囲設定が出来たら「はい」を押してください。

![img.png](readmeimage/9.png)

8.スクリーンショットの保存先フォルダを選択してください。

![img.png](readmeimage/10.png)
![img.png](readmeimage/12.png)
![img.png](readmeimage/11.png)

9.「スクショスタート」を押すと自動スクリーンショットが開始されます。範囲内の画像の変化を検知し、変化が起こったら画像を保存します。

![img.png](readmeimage/13.png)
![img.png](readmeimage/14.png)

10.「スクショを撮る」を押すと、その場でスクリーンショットを撮影します。変化が起こったけどスクリーンショットが撮影されなかった等、手動で撮影したいときに使用します。


## 撮影した画像を文字起こしする
撮影した大量のスライドを文字起こしし、Googleドキュメントにまとめます。
### セットアップ
1.[GoogleDrive](https://drive.google.com/drive/u/0/my-drive) を開き、新規>その他>Google Apps Scriptを選択してください。

![img.png](readmeimage/15.png)

![img.png](readmeimage/18.png)

3.「無題のプロジェクト」をクリックして、名前を変更してください。

![img.png](readmeimage/19.png)

![img.png](readmeimage/20.png)

4.[こちら](https://gist.github.com/sakastudio/e3c8de62716010bd6153df360ecd80f7) のソースコードをコピペして貼り付けてください。

![img.png](readmeimage/21.png)

5.DriveAPIを有効化します。サービスを押し、少し下にスクロールしたところにあるDrive APIを選択し、追加を押してください。

![img.png](readmeimage/22.png)

![img.png](readmeimage/23.png)

7.新規>フォルダを押してください。フォルダ名を「OCR」にして作成を押してください。

![img.png](readmeimage/15.png)

![img.png](readmeimage/16.png)

![img.png](readmeimage/17.png)

8.rootフォルダにある「OCRくん」をOCRフォルダに入れてください。

![img.png](readmeimage/25.png)

以上でセットアップは終了となります。

### 使い方

1.撮影した画像をアップロードします。Shiftキーを押してアップロードする画像を複数選択し、GoogleドライブのOCRフォルダにドラッグ＆ドロップしてください。

![img.png](readmeimage/26.png)

2.OCRくんをクリックしてください。

![img.png](readmeimage/27.png)

3.実行を押してください。

![img.png](readmeimage/28.png)

4.初回の実行の際には権限が求められますので、許可をします。

![img.png](readmeimage/29.png)

![img.png](readmeimage/30.png)

![img.png](readmeimage/31.png)

![img.png](readmeimage/32.png)

![img.png](readmeimage/33.png)

5.実行ログに実行完了が表示されれば正常に処理が終了しています。

![img.png](readmeimage/34.png)


## 参考にしたサイト
[画像差分](https://qiita.com/kikuyan8540/items/0c92a8ab47e84ec79652)
[スクリーンショット](https://qiita.com/hisakichi95/items/47f6d37e6f425f29c8a8)
[OCR](http://www.initialsite.com/w01/14488)

## Licence
[MIT](https://github.com/sakastudio/Auto-ScreenShot-Kun/blob/master/LICENSE)
