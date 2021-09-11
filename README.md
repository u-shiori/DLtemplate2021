# DLtemplate2021

`PYENV.md`を参考にPythonのバージョンを`3.9.0`にしてください。


```sh
cd DLtemplate2021
pip install -r requirements.txt
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
