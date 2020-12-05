def print_max(a, b, c):             #print_max함수를 정의한다. 나중에 a,b,c,값은 입력받을 것이다
    if a > b and a > c:             #만약 a가 b보다 크고 a가 c보다 크면
        print(a)                    #print함수를 이용하여 a값을 출력하라
    elif b > c and b > a:           #그렇지 않고 만약 b가 c보다 크고 b가 a보다 크면
        print(b)                    #print함수를 이용하여 b값을 출력하라
    else:                           #그렇지 않으면
        print(c)                    #print함수를 이용하여 c값을 출력하라
        
print_max(10, 20, 30)               #만약 이걸 실행하면 c값인 30이 가장 크므로 30이 출력될것이다