import time  # 지연 함수(sleep) 사용을 위한 라이브러리 불러오기

import adafruit_dht  # 온습도 센서(DHT11)를 위한 라이브러리 불러오기
import board  # GPIO를 위한 라이브러리 불러오기

# GPIO 25 핀을 데이터 핀으로 설정 (DHT11)
# 현재 라즈베리파이5의 호환성 문제로 인해 pulseio를 사용할 경우 오류가 발생합니다.
# 라이브러리에서 pulseio를 사용하지 않도록 설정합니다.
dht = adafruit_dht.DHT11(board.D25, use_pulseio=False)

try:
    while True:  # 무한 반복
        temperature = dht.temperature  # 센서로부터 온도값 읽기
        humidity = dht.humidity  # 센서로부터 습도값 읽기

        print("Temp : ", temperature, "C")
        print("Humi : ", humidity, "%")

        time.sleep(2)  # 2초 대기

except RuntimeError as e:  # 런타임 오류 예외 처리
    print(e.args)

except KeyboardInterrupt:  # 키보드 인터럽트 예외 처리
    pass

except Exception as e:  # 기타 예외 처리
    print(e)
