import random   # random 모듈 import
from datetime import datetime # 보너스문제를 위한 datetime 라이브러리

# DummySensor 클래스 생성
class DummySensor:
    def __init__(self):
        # 사전객체 생성
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }

    # 메소드 생성
    def set_env(self):
        # 랜덤으로 데이터값 생성(각 항목당 범위 설정)
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    # get_env() 생성 및 env_values return
    def get_env(self):
        # 보너스 문제
        
        # 현재 시간 불러오기
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 로그 내용 구성
        log_entry = (
            f"{now}, "
            f"{self.env_values['mars_base_internal_temperature']}, "
            f"{self.env_values['mars_base_external_temperature']}, "
            f"{self.env_values['mars_base_internal_humidity']}, "
            f"{self.env_values['mars_base_external_illuminance']}, "
            f"{self.env_values['mars_base_internal_co2']}, "
            f"{self.env_values['mars_base_internal_oxygen']}\n"
        )

        # 로그 파일 기록
        with open('env_log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(log_entry)
            
        return self.env_values

# ds라는 이름으로 인스턴스 생성
ds = DummySensor()

# 차례로 호출하여 값 확인
ds.set_env()
print(ds.get_env())