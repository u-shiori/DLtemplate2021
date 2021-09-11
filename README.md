# DLtemplate2021

まずは`PYENV.md`でPythonのバージョンを`3.9.0`にしてください。
```sh
cd DLtemplate2021
pip install -r requirements.txt
```

## 目標
画像認識モデル、画像検知モデル、（画像生成モデル）の構造を理解し、下記のコードがある程度理解できるようになること

```sh
cd src
```

- 画像認識モデル
    ```sh
    python resnext.py
    ```

- 画像検知モデル
    ```sh
    python yolov5.py
    ```

- 画像生成モデル
    ```sh
    python dcgan.py
    ```

それぞれ`DLtemplate2021/result/`に結果が保存されます。
