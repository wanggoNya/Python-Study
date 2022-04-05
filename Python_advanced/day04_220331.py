import sys                     # 하드웨어 접근 모듈
from PyQt5.QtWidgets import *  # 파이큐티 관련 모듈
from PyQt5 import uic          # ui 관련 모듈
from PyQt5.QtCore import *     # 타이머 관련 모듈
import pybithumb
import pykorbit

form_class = uic.loadUiType("day04_220331.ui")[0]   # pyqt로 만든 ui 폼 불러오기 
tickers = ["BTC","ETH","XRP","ADA"]

class MyWindow(QMainWindow, form_class):     # MyWindow 클래스 를 상속받아서 작성
    def __init__(self):                      # 생성자로 창생성
        super().__init__()                   # 부모의 생성자를 이용
        self.setupUi(self)                   # Ui 창 생성
        # self.pushButton.clicked.connect(self.btn_clicked)  # 단추 클릭시 열결되는 매서드 정의
        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def get_market_infos(self, ticker):
        df = pybithumb.get_ohlc(ticker) # get_ohlcv() 해당 코인의 다양한 정보를 가져온다. 
        ma5 = df['close'].rolling(window=5).mean() # 종가들을 5일씩 평균을 전부 계산
        last_ma5 = ma5[-2]                         # 가장 최근 5일치의 평균만 추출
        price = pybithumb.get_current_price(ticker)# 해당 코인의 현재가

        state = None
        if price > last_ma5:
            state = "UP"
        else:
            state = "DOWN"
        return price, last_ma5, state

    def timeout(self):
        for i, ticker in enumerate(tickers):

            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

            price, last_ma5, state = self.get_market_infos(ticker)

            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(state))
        
#######################################################################
    def __init__(self):                      # 생성자로 창생성
        super().__init__()                   # 부모의 생성자를 이용
        self.setupUi(self)                   # Ui 창 생성
        # self.pushButton.clicked.connect(self.btn_clicked)  # 단추 클릭시 열결되는 매서드 정의
        timer = QTimer(self)
        timer.start(5000)
        timer.timeout2.connect(self.timeout2)

    def get_market_infos2(self, ticker):
        df = pykorbit.get_ohlcv(ticker) # get_ohlcv() 해당 코인의 다양한 정보를 가져온다. 
        ma5 = df['close'].rolling(window=5).mean() # 종가들을 5일씩 평균을 전부 계산
        last_ma5 = ma5[-2]                         # 가장 최근 5일치의 평균만 추출
        price = pykorbit.get_current_price(ticker)# 해당 코인의 현재가

        state = None
        if price > last_ma5:
            state = "UP"
        else:
            state = "DOWN"
        return price, last_ma5, state

    def timeout2(self):
        for i, ticker in enumerate(tickers):

            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

            price, last_ma5, state = self.get_market_infos2(ticker)

            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWidget_2.setItem(i, 3, QTableWidgetItem(state))

app = QApplication(sys.argv)    # 파이썬은 원래 인터프리터 -> 한줄씩 실행후 창이 꺼져야 정상
window = MyWindow()                          # 윈도우 클래스로 객체 생성
window.show()                                # 생성한 객체를 통해 창을 보여주는 
app.exec_()                  
                # 윈도우 창이 열린 상태로 계속 대기 유지