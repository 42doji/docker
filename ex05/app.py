from flask import Flask, render_template, request, Response
import os
from io import BytesIO
from gtts import gTTS
import logging
from datetime import datetime

app = Flask(__name__, static_folder='static')

ALLOWED_LANGS = ['ko', 'en', 'ja', 'es']

log_file_path = os.path.join(os.path.dirname(__file__), 'input_log.txt')
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        input_text = request.form.get('user_text')
        lang = request.args.get('lang', 'ko') 

        if not input_text:
            raise ValueError("텍스트를 입력해주세요.")
        if lang not in ALLOWED_LANGS:
            raise ValueError(f"지원하지 않는 언어입니다: {lang}")

        logging.info(f"Lang: {lang}, Text: {input_text}")

        tts = gTTS(text=input_text, lang=lang, slow=False)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        return Response(fp.getvalue(), mimetype='audio/mpeg')

    except ValueError as ve:
        logging.error(f"Validation Error: {ve}")
        return Response(str(ve), status=400)
    except Exception as e:
        logging.error(f"gTTS or other error: {e}")
        return Response(f"음성 변환 중 서버 오류 발생: {e}", status=500)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
