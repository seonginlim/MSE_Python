def my_print (a, b):             #my_print함수를 정의한다. a,b값은 입력 받을 것이다.
    print("왼쪽:", a)             #함수가 실행되면 print함수를 통하여 왼쪽:a값 이 출력될것이다.
    print("오른쪽:", b)            #그 다음 오른쪽:b값이 출력될것이다.

my_print(b=100, a=200)           #위치가 바뀌어도 변수에 입력될 값을 지정해줬으므로.
                                 #왼쪽:200.
                                 #오른쪽:100 이 출력될것이다.