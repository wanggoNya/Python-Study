def search4vowels(word):
    """Return any vowels found in a supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

print(search4vowels('hitch-hiker'))

from flask import Flask # 서버 동작에 필요한 flask 모듈 읽어오기
from vsearch import search4letters

app = Flask(__name__) # Flask 객체 생성하여 app 변수명으로 할당
# 객체 생성시 생성자에 __name__ vkdlTjs dlsxjvmflxjrk
# 제공하는 값, 현재 활성 모듈의 이름을 가진다

# 데코레이터 decorator 장식자
@app.route('/') #사이트 접근 주소

def  hello() -> str:
    return 'Hello world from Flask 김수연'


# @app.route('/search4')
# def do_search() -> str:
#     return str(search4letters('life is the universe and everything','eiru'))

app.run