import openai
import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages=[
        {"role": "system", "content": "You are the helpful BuChatBot."},
        {"role": "system", "content": "협업 리딩클래스 백석나비 B조가 만든 gpt 3.5기반의 백석대학교 소개용 챗봇이다."},
        {"role":"system","content":"The headquarters building of Baekseok University is used by several faculties, especially the Department of Computer Science and Engineering and the Department of Tourism."}
     ]

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/post', methods=['POST'])
def post():
    global messages
    name = request.json['message']
    openai.api_key = "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"
    messages.append({
            "role":"assistant",
            "content":f"{name}"
    })  
    res = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages = messages)
    name = res['choices'][0]['message']['content']
    messages.append({
        "role":"user",
        "content":f"{name}"
    })
    result = {'message': f'{name}'}
    return jsonify(result),200, {'Access-Control-Allow-Origin': '*'}
        

if __name__ == '__main__':
    app.run(debug=True)


# API 인증 정보 가져오기

  