def sphere_area(diameter, material = 'glass', thickness = 1):
    PI = 3.141592653589793

    # 반지름(cm), 면적, 화성 중력
    radius = diameter * 100 / 2
    area = 2 * PI * (radius ** 2)   # 돔 형태라하여 3*PI*r^2이 아닌 2*PI*r^2으로 계산함
    mars_gravity = 0.38
    
    # material에 다른 무게 계산
    if material == 'glass':
        weight = area * thickness * 2.4 * mars_gravity
    elif material == 'aluminum':
        weight = area * thickness * 2.7 * mars_gravity
    elif material == 'steel':
        weight = area * thickness * 7.85 * mars_gravity
    else:
        material = 'glass'
        weight = area * thickness * 2.4 * mars_gravity
    
    return material, diameter, thickness, round(area, 3), round(weight/1000, 3)

while True:
    print("\n--- 돔의 면적과 무게 계산 프로그램 ---")

    # 종료 프로그램
    exit = input("press 'Enter' to Start. If you want to quit press 'q' or 'quit' : ")
    if exit.lower() in ['q', 'quit']:
        print("exit program.")
        break
    
    # 재질 입력
    material = input('meterial : ')

    # 지름 입력
    try:
        diameter = float(input('diameter(m) : '))
    except:
        diameter = 10

    # 두께 입력
    try:
        thickness = float(input('thickness(cm) : '))
    except:
        thickness = 1

    # 전역 변수에 저장
    material, diameter, thickness, area, weight = sphere_area(diameter, material, thickness)

    print(f'material => {material}, diameter => {diameter}m, thickness => {thickness}cm, '
        f'area =⇒ {area}, weight => {weight}kg')
    
"""
보너스 문제
- 파라메터에 숫자가 아닌 문자가 들어갔을 때 오류가 발생하지 않도록 처리한다.

line 16 - material에 아무 입력도 하지 않았을 때, else문을 사용하여 material을 기본값 'glass'로 초기화
line 37, 43 -  예외처리
"""