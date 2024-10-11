import time  # 지연 함수(sleep) 사용을 위한 라이브러리 불러오기

import board  # GPIO를 위한 라이브러리 불러오기
import pwmio  # PWM을 위한 라이브러리 불러오기

# GPIO 5 핀을 PWM 출력핀으로 설정 (LED)
led = pwmio.PWMOut(board.D5, frequency=5000, duty_cycle=0)

try:
    while True:  # 무한 반복
        for i in range(100):
            if i < 50:
                # LED 밝기를 0 ~ 100% 까지 올리기
                led.duty_cycle = int(i * 2 * 65535 / 100)

            else:
                # LED 밝기를 100 ~ 0% 까지 내리기
                led.duty_cycle = int((100 - i) * 2 * 65535 / 100)

            time.sleep(0.01)  # 0.01초 대기

except KeyboardInterrupt:  # 키보드 인터럽트 예외 처리
    pass

except Exception as e:  # 기타 예외 처리
    print(e)
