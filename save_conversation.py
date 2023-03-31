import requests
from env import Env

# ChatGPT API 엔드포인트 URL
chatgpt_url = "https://api.openai.com/v1/chat/completions"

# ChatGPT API 인증 키
api_key = Env.gpt_api

# 대화 기록을 가져오기 위한 prompt 문장
prompt = "내 대화 기록을 가져와."

# ChatGPT API 호출 시 필요한 매개 변수
params = {
    "messages": [{"role": "user", "content": prompt}],
    "model": "gpt-3.5-turbo",
    "max_tokens": 1024,
    "n": 1,
    "stop": "User:",
    "temperature": 0.7
}

# ChatGPT API 호출 헤더에 인증 키 추가
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# ChatGPT API 호출
response = requests.post(chatgpt_url, json=params, headers=headers)

# API 응답에서 대화 기록 추출
# conversation_history = response.json()["choices"][0]["text"]
conversation_history = response.json()["choices"][0]

print(conversation_history)

# 추출된 대화 기록을 블로그에 업로드하는 코드를 작성합니다.
# 이를 위해서는 사용하시는 블로그 플랫폼의 API와 개발 문서를 참조하셔야 합니다.
# 블로그 API 사용 시 필요한 인증 키, 엔드포인트 등을 블로그 플랫폼 문서를 참조하여 작성해 주세요.
