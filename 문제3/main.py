csv_list = []
flammability_list = []

try:
    with open('Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as csvfile:
        print(csvfile.read())
        
        print('\n---------------------------------------------------------------')
        # csv파일을 list로 전환
        csvfile.seek(0)
        next(csvfile)  # 첫 번째 줄(헤더) 건너뛰기
        for line in csvfile:
            parts = line.strip().split(",", 5)  # timestamp, event, message 분리
            if len(parts) == 5:
                Substance, Weight, Specific_Gravity, Strength, Flammability = parts
                csv_list.append([Substance, Weight, Specific_Gravity, Strength, Flammability])
                print(f'{Substance}, {Weight}, {Specific_Gravity}, {Strength}, {Flammability}')
    
    # csv_list 파일을 인화성이 높은순으로 정렬
    print('\n---------------------------------------------------------------')
    csv_list.sort(key = lambda x: x[4], reverse = True)
    print('sorted by Flammability\n')
    for item in csv_list:
        print(f'{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}')
    
    # 인화성 지수 0.7 이상인 목록만 따로 출력 & 파일에 저장
    with open('Mars_Base_Inventory_danger.csv', 'w', encoding='utf-8') as f:
        f.write('Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability\n')
        print('\n---------------------------------------------------------------')
        print('Flammabilities >= 0.7')
        for item in csv_list:
            if float(item[4]) >= 0.7:
                f.write(f'{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}\n')
                flammability_list.append(f'{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}\n')
                print(f'{item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}')
                
        # 보너스 문제
        # 정렬된 flammability_list를 문자열로 변환하여 이진 파일(Mars_Base_Inventory_List.bin)에 저장
        with open('Mars_Base_Inventory_List.bin', 'wb') as bin_file:
            data_str = repr(flammability_list)  # 리스트를 문자열로 변환
            bin_file.write(data_str.encode('utf-8'))  # UTF-8 인코딩 후 저장
        print("\n---------------------------------------------------------------")
        
        # 저장된 이진 파일을 읽어와서 원래의 리스트로 복원한 후 화면에 출력
        with open('Mars_Base_Inventory_List.bin', 'rb') as bin_file:
            data = bin_file.read()
            data_str = data.decode('utf-8')
            loaded_list = eval(data_str)  # 문자열을 원래의 리스트로 변환
            print('\n---------------------------------------------------------------')
            for item in loaded_list:
                print(item)
                
    # 보너스 문제 - 이진데이터 형식으로 저장하는 부분까지는 모르겠어서
    # .bin파일에 utf-8 인코딩해서 입력하는 부분까지밖에 못했습니다..
    
except FileNotFoundError:
    print('The file does not exist.')