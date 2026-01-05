import random
import time
import platform
import os
import json
import threading
import multiprocessing

# DummySensor 클래스
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

# 문제 7에서 완성한 MissionComputer 클래스
class MissionComputer:
    def __init__(self):
        self.sensor = DummySensor()
        self.env_values = {key: None for key in self.sensor.env_values}
        self.history = {key: [] for key in self.env_values}
        self.count = 0

    def print_env_as_json(self):
        print("{")
        for key, value in self.env_values.items():
            print(f'    "{key}": {value},')
        print("}\n")

    def print_5min_average(self):
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
                self.sensor.set_env()
                self.env_values = self.sensor.get_env().copy()

                for key in self.env_values:
                    self.history[key].append(self.env_values[key])

                self.print_env_as_json()
                self.count += 1

                if self.count % 60 == 0:
                    self.print_5min_average()
                    self.history = {key: [] for key in self.env_values}

                time.sleep(5)
        except KeyboardInterrupt:
            print("\nSystem stopped...")

    def get_mission_computer_info(self):
        # 시스템 정보를 JSON 형식으로 출력
        try:
            # setting.txt에서 출력 항목 읽기
            enabled_fields = []
            if os.path.exists("setting.txt"):
                with open("setting.txt", "r") as f:
                    enabled_fields = [line.strip() for line in f if line.strip()]
            else:
                print("Warning: setting.txt not found. Defaulting to all fields.")
                enabled_fields = ["Operating System", "OS Version", "CPU Type", "CPU Core Count", "Memory Size (GB)"]

            # 전체 가능한 정보
            full_info = {
                "Operating System": platform.system(),
                "OS Version": platform.version(),
                "CPU Type": platform.processor(),
                "CPU Core Count": os.cpu_count(),
                "Memory Size (GB)": round(
                    os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024 ** 3), 2
                ) if hasattr(os, 'sysconf') else "Unavailable"
            }

            # 설정에 따라 필터링
            info = {key: full_info[key] for key in enabled_fields if key in full_info}

            print("Mission Computer Info:")
            print(json.dumps(info, indent=4))
        except Exception as e:
            print("Failed to get system info:", e)

    # 미션 컴퓨터의 부하를 가져오는 코드, get_mission_computer_load() 메소드
    def get_mission_computer_load(self):
        # 시스템 부하 출력
        try:
            load = {
                "CPU Load Average (1m)": os.getloadavg()[0] if hasattr(os, 'getloadavg') else "Unavailable",
                "Memory Usage (%)": "Not available without external package"
                # MacOS에서 메모리 사용량은 psutil라이브러리 추가 필요(제약사항과 맞지않음)
            }
            print("Mission Computer Load:")
            print(json.dumps(load, indent=4))
        except Exception as e:
            print("Failed to get system load:", e)


# 20초마다 시스템 정보 출력
def run_info():
    mc = MissionComputer()
    while True:
        mc.get_mission_computer_info()
        time.sleep(20)

# 20초마다 시스템 부하 출력
def run_load():
    mc = MissionComputer()
    while True:
        mc.get_mission_computer_load()
        time.sleep(20)

# 센서 데이터 출력 (5초 주기)
def run_sensor():
    mc = MissionComputer()
    mc.get_sensor_data()

# 멀티 프로세스로 실행
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_info)
    p2 = multiprocessing.Process(target=run_load)
    p3 = multiprocessing.Process(target=run_sensor)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()