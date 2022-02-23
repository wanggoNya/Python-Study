from flask import Flask, render_template # 서버 동작에 필요한 flask 모듈 읽어오기
from vsearch import search4letters

app = Flask(__name__) # Flask 객체 생성하여 app 변수명으로 할당
# 객체 생성시 생성자에 __name__
# 제공하는 값, 현재 활성 모듈의 이름을 가진다

# 데코레이터 decorator 장식자
@app.route('/') #사이트 접근 주소

def hello() -> str:
    return 'Hello world from Flask 김수연'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life is the universe and everything','eiru'))

@app.route('/entry')
def do_search() -> 'html':
    return render_template(
        'entry.html', 
        the_title = 'Welcom to search4letters on the web!'
        )




app.run()