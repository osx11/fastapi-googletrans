from fastapi import FastAPI
from googletrans import Translator

from starlette.requests import Request

app = FastAPI()
translator = Translator()


@app.get("/translate")
def translate(request: Request):
    text = request.query_params.get('text')
    target_lang = request.query_params.get('target')

    return translator.translate(text, dest=target_lang).text


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
