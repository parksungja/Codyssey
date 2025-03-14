f = open('mission_computer_main.log', 'r', encoding='utf-8')

try:
    print('reading mission_computer_main.log\n\n')
    read = f.read()
    print(read)
except FileNotFoundError:
    print('The file does not exist.')

f.close()