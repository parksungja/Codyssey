import numpy as np

# 파일 경로
file1 = 'mars_base_main_parts-001.csv'
file2 = 'mars_base_main_parts-002.csv'
file3 = 'mars_base_main_parts-003.csv'

try:
    # 파일 읽기
    arr1 = np.genfromtxt(file1, delimiter=',', skip_header=1, dtype=str)
    arr2 = np.genfromtxt(file2, delimiter=',', skip_header=1, dtype=str)
    arr3 = np.genfromtxt(file3, delimiter=',', skip_header=1, dtype=str)

    # vstack()을 이용하여 배열 합치기
    parts = np.vstack((arr1, arr2, arr3))

    # Weight 추출 후, float로 변환
    weights = parts[:, 1].astype(float)

    # 평균 계산
    weight_mean = np.mean(weights)
    
    # 평균값이 50보다 작은 값만 저장
    with open('parts_to_work_on.csv', 'w', encoding="UTF-8") as f:
        f.write('Part,Weight\n')
        for part, weight in zip(parts[:, 0], weights):
            if weight < weight_mean:
                f.write(f'{part},{weight}\n')

    # 보너스 문제
    bonus_file = 'parts_to_work_on.csv'

    parts2 = np.genfromtxt(bonus_file, delimiter=',', skip_header=1, dtype=str)
    
    # 전치 행렬
    parts3 = parts2.T   # 또는 np.transpose(parts2)
    
    print(parts3)
    
except FileNotFoundError:
    print('The file does not exist.')
except IsADirectoryError:
    print('The path is a directory.')
except PermissionError:
    print('Permission denied.')
except Exception as e:
    print(f"An error occurred: {e}")