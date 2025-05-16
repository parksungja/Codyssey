import random
import time

class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values

class MissionComputer:
    def __init__(self):
        # DummySensor 클래스의 인스턴스를 생성
        self.sensor = DummySensor()
        # 현재 센서 측정값을 저장할 딕셔너리
        self.env_values = {key: None for key in self.sensor.env_values}
        # 평균 계산을 위한 누적값 저장용 딕셔너리
        self.history = {key: [] for key in self.env_values}
        # 측정 횟수 카운터
        self.count = 0

    def print_env_as_json(self):
        # 현재 측정된 환경 정보를 JSON 형식처럼 출력
        print("{")
        for key, value in self.env_values.items():
            print(f'    "{key}": {value},')
        print("}\n")

    def print_5min_average(self):
        # 5분 동안의 측정값 평균을 출력
        print(">>> 5-Minute Average Values")
        print("{")
        for key in self.env_values:
            avg = round(sum(self.history[key]) / len(self.history[key]), 2)
            print(f'    "{key}": {avg},')
        print("}\n")

    def get_sensor_data(self):
        print("Monitoring environment... Press Ctrl+C to stop.\n")
        try:
            while True:
                # 센서로부터 새로운 측정값 생성 및 저장
                self.sensor.set_env()
                self.env_values = self.sensor.get_env().copy()

                # 측정값을 누적 기록
                for key in self.env_values:
                    self.history[key].append(self.env_values[key])

                # 현재 측정값 출력
                self.print_env_as_json()
                self.count += 1

                # 5분(60회 측정)마다 평균값 출력
                if self.count % 60 == 0:
                    self.print_5min_average()
                    # 누적값 초기화
                    self.history = {key: [] for key in self.env_values}

                # 5초 간격으로 측정 반복
                time.sleep(5)
        except KeyboardInterrupt:
            # 사용자가 Ctrl+C를 누르면 시스템 종료 메시지 출력
            print("\nSystem stopped...")

# 실행
RunComputer = MissionComputer()
RunComputer.get_sensor_data()