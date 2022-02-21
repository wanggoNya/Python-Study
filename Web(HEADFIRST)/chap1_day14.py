from datetime import datetime # 날짜 시간 관련 모듈
import random # 난수 발생 모듈
import time # 정지 시간 모듈

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# odds 변수에 홀수 정의

for num in range(5): # 5 번 반복
    right_this_second = datetime.today().second
    # 현재 시간에 초를 추출

    if right_this_second in odds: # 추출한 초가 홀수인지 확인
        print('This second seems a little odd') # 홀수일 경우 출력
    else: # 홀수가 아닌 경우
        print('Not and odd second.') # 짝수일 경우 출력
    wait_time = random.randint(1, 5) # 1에서 5 사이의 난수 발생
    time.sleep(wait_time) # 다음 반복 전에 정지시킬 초 설정