import time  # 지연 함수(sleep) 사용을 위한 라이브러리 불러오기

import adafruit_hcsr04  # 초음파 센서(HC-SR04)를 위한 라이브러리 불러오기
import board  # GPIO를 위한 라이브러리 불러오기

# 현재 라즈베리파이5의 호환성 문제로 인해 pulseio를 사용할 경우 오류가 발생합니다.
# 라이브러리에서 pulseio를 사용하지 않도록 설정합니다.
adafruit_hcsr04._USE_PULSEIO = False

# GPIO 23 핀을 Trigger 핀, GPIO 24 핀을 Echo 핀으로 설정 (HC-SR04)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D23, echo_pin=board.D24)

try:
    while True:  # 무한 반복
        print(sonar.distance)  # 거리 출력
        time.sleep(0.5)  # 0.5초 대기

except KeyboardInterrupt:  # 키보드 인터럽트 예외 처리
    pass

except Exception as e:  # 기타 예외 처리
    print(e)
