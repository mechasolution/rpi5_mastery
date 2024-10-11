import time  # 지연 함수(sleep) 사용을 위한 라이브러리 불러오기

import adafruit_pcf8591.pcf8591 as PCF  # ADC/DAC 모듈(PCF8591)을 위한 라이브러리 불러오기
import board  # GPIO를 위한 라이브러리 불러오기
from adafruit_pcf8591.analog_in import AnalogIn  # ADC를 위한 라이브러리 불러오기

i2c = board.I2C()  # 보드의 SDA와 SCL을 사용
pcf = PCF.PCF8591(i2c)

pcf_in_0 = AnalogIn(pcf, PCF.A0)  # 아날로그 입력 0 : 조도 센서(Cds)
pcf_in_1 = AnalogIn(pcf, PCF.A1)  # 아날로그 입력 1 : 온도 센서(써미스터)
pcf_in_3 = AnalogIn(pcf, PCF.A3)  # 아날로그 입력 3 : 가변 저항(포텐쇼미터)

resolution = 65535  # 16 bit 최대값

try:
    while True:  # 무한 반복
        # 16 bit 데이터를 전압으로 변환
        cds_voltage = (pcf_in_0.value / resolution) * pcf_in_0.reference_voltage
        print(f"Pin 0 (CdS) : {round(cds_voltage, 2)} V")
        thermistor_voltage = (pcf_in_1.value / resolution) * pcf_in_1.reference_voltage
        print(f"Pin 1 (Thermistor) : {round(thermistor_voltage, 2)} V")
        potentio_voltage = (pcf_in_3.value / resolution) * pcf_in_3.reference_voltage
        print(f"Pin 3 (Potentiometer) : {round(potentio_voltage, 2)} V")

        time.sleep(1)  # 1초 대기

except KeyboardInterrupt:  # 키보드 인터럽트 예외 처리
    pass

except Exception as e:  # 기타 예외 처리
    print(e)
