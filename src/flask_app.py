from flask import Flask, request, Response
import requests
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/openai', defaults={'path': ''})
@app.route('/openai/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def openai_proxy(path):
    new_url = f'http://127.0.0.1:8000/{path}'
    logger.info(f"Proxying to URL: {new_url}")
    resp = requests.request(
        method=request.method,
        url=new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        stream=True
    )

    def generate():
        for line in resp.iter_lines():
            if line:
                yield line + b'\n'

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    
    return Response(generate(), resp.status_code, headers)

@app.route('/')
def home():
    return "LiteLLM proxy is running. Use the /openai endpoint to access it."

def run_flask_app():
    app.run(port=5000)