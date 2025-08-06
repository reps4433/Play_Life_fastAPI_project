# main.py

# FastAPIのインポート.
# FastAPIは、APIのすべての機能を提供するPythonクラスです
from fastapi import FastAPI

# FastAPIの「インスタンス」を生成
# このappという名前はuvicornを使ってサーバーを起動する際に参照します。
app = FastAPI()


# パスとHTTPメソッドを指定します
# 直下の関数がリクエストの処理を担当します
@app.get("/")
def root():
    return {"mock": "Hello World"}
