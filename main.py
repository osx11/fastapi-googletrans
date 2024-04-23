import uvicorn
from fastapi import FastAPI
from googletrans import Translator

from starlette.requests import Request

app = FastAPI()
translator = Translator()


@app.get("/translate")
def translate(request: Request):
    text = request.query_params.get('text')
    target_lang = request.query_params.get('target')

    result = None

    for i in range(10):
        try:
            result = translator.translate(text, dest=target_lang).text
            break
        except:
            print('EXCEPTION!!! retrying...', text, target_lang)

    return {'result': result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="info")
