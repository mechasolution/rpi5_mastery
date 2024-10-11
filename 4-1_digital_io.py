import time  # 지연 함수(sleep) 사용을 위한 라이브러리 불러오기

import board  # GPIO를 위한 라이브러리 불러오기
import digitalio  # 디지털 I/O를 위한 라이브러리 불러오기

# GPIO 17 핀을 입력핀으로 설정 (스위치 버튼)
button = digitalio.DigitalInOut(board.D17)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# GPIO 27 핀을 출력핀으로 설정 (LED)
led = digitalio.DigitalInOut(board.D27)
led.direction = digitalio.Direction.OUTPUT

try:
    while True:  # 무한 반복
        if button.value:  # 스위치 안누름
            print("Input : HIGH")
            led.value = False  # LED 끄기

        else:  # 스위치 누름
            print("Input : LOW")
            led.value = True  # LED 켜기

        time.sleep(0.5)  # 0.5초 대기

except KeyboardInterrupt:  # 키보드 인터럽트 예외 처리
    pass

except Exception as e:  # 기타 예외 처리
    print(e)
