import time  # 지연 함수(sleep) 사용을 위한 라이브러리 불러오기

import board  # GPIO를 위한 라이브러리 불러오기
import digitalio  # 디지털 I/O를 위한 라이브러리 불러오기

# GPIO 22 핀을 입력핀으로 설정 (PIR)
pir = digitalio.DigitalInOut(board.D22)
pir.direction = digitalio.Direction.INPUT

try:
    while True:  # 무한 반복
        if pir.value:  # PIR 센서에 움직임이 감지됨
            print("detected")
            time.sleep(1)  # 센서 중복 감지 방지

except KeyboardInterrupt:  # 키보드 인터럽트 예외 처리
    pass

except Exception as e:  # 기타 예외 처리
    print(e)
