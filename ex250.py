import numpy                            #numpy라는 모듈 사용.
for i in numpy.arange(0, 5, 0.1):       #그냥 range는 정수단위로만 증가할수있다. 따라서 numpy.arange를 사용, 0에서 5바로 직전까지 0.1씩증가.
    print(i)                            #for문을 한번 돌때마다 print함수를 통해 i값 출력.