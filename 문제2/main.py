log_list = []
log_dict = {}

try:
    with open('mission_computer_main.log', 'r', encoding='utf-8') as file:
        print('reading mission_computer_main.log\n\n')
        print(file.read())

        # log파일을 list로 전환
        file.seek(0)
        print('\n---------------------------------------------------------------')
        print('log_list\n')
        next(file)  # 첫 번째 줄(헤더) 건너뛰기
        for line in file:
            parts = line.strip().split(",", 2)  # timestamp, event, message 분리
            if len(parts) == 3:
                timestamp, event, message = parts
                log_list.append([timestamp, event, message])
                print(f'{timestamp}: {event} - {message}')
        log_list.sort(reverse = True)
        print('\n---------------------------------------------------------------')
        print('timestamp 의 역순으로 정렬\n')
        for i in range(0, len(log_list)):
            print(f'{log_list[i][0]}: {log_list[i][1]} - {log_list[i][2]}')
        
        # list를 dict로 전환
        print('\n---------------------------------------------------------------')
        print('log_dict(key = index)\n')
        for i, (timestamp, event, message) in enumerate(log_list):
            log_dict[i] = {
                'timestamp': timestamp,
                'event': event,
                'message': message
            }

        for key in log_dict:
            entry = log_dict[key]
            print(f'{key}: {entry}')
        
        # mission_computer_main.json
        with open('mission_computer_main.json', 'w', encoding='utf-8') as json_file:
            json_file.write('{\n')
            total = len(log_dict)
            for i, key in enumerate(log_dict):
                entry = log_dict[key]
                json_file.write(f'  "{key}": {{\n')
                json_file.write(f'    "timestamp": "{entry["timestamp"]}",\n')
                json_file.write(f'    "event": "{entry["event"]}",\n')
                json_file.write(f'    "message": "{entry["message"]}"\n')
                if i < total - 1:
                    json_file.write('  },\n')
                else:
                    json_file.write('  }\n')
            json_file.write('}\n')
                
        # 보너스 문제 - 특정 문자열로 로그 필터링 출력
        print('\n---------------------------------------------------------------')
        search_keyword = input("검색할 문자열을 입력하세요: ")

        print(f'\n"{search_keyword}"이(가) 포함된 로그 항목:\n')

        found = False
        for key, entry in log_dict.items():
            if (search_keyword in entry["timestamp"] or
                search_keyword in entry["event"] or
                search_keyword in entry["message"]):
                print(f'{key}: {entry}')
                found = True

        if not found:
            print("해당 문자열을 포함한 로그가 없습니다.")
            
except FileNotFoundError:
    print('The file does not exist.')