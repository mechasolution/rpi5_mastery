import time  # 지연 함수(sleep) 사용을 위한 라이브러리 불러오기

import adafruit_pcf8591.pcf8591 as PCF  # ADC/DAC 모듈(PCF8591)을 위한 라이브러리 불러오기
import board  # GPIO를 위한 라이브러리 불러오기
from adafruit_pcf8591.analog_out import AnalogOut  # DAC를 위한 라이브러리 불러오기

i2c = board.I2C()  # 보드의 SDA와 SCL을 사용
pcf = PCF.PCF8591(i2c)

pcf_out = AnalogOut(pcf, PCF.OUT)  # 아날로그 출력(LED)

resolution = 65535  # 16 bit 최대값

try:
    while True:  # 무한 반복
        for i in range(100):
            if i < 50:
                # LED 밝기를 0 ~ 100% 까지 올리기
                pcf_out.value = int(i * 2 * resolution / 100)

            else:
                # LED 밝기를 100 ~ 0% 까지 내리기
                pcf_out.value = int((100 - i) * 2 * resolution / 100)

            # 16 bit 데이터를 전압으로 변환
            out_voltage = (pcf_out.value / resolution) * 3.3
            print(f"DAC out : {round(out_voltage, 2)} V")

            time.sleep(0.05)  # 0.05초 대기

except KeyboardInterrupt:  # 키보드 인터럽트 예외 처리
    pass

except Exception as e:  # 기타 예외 처리
    print(e)
