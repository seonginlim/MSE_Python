#문제
def message1():                 #def를 통해 함수 message1을 정의함
    print("A")                  #print함수를 통해 A를 출력하라는 함수

def message2():                 #def를 통해 함수 message2를 정의함
    print("B")                  #print함수를 통해 B를 출력하라는 함수

def message3():                 #def를 토앻 함수 message3을 정의함
    for i in range(3):          #range함수를 통해 0,1,2 총 세번을 for문을 반복하도록 설정
        message2()              #먼저 message2 즉, B를 먼저 출력
        print("C")              #그다음 print함수를 통해 C를 출력
    message1()                  #마지막에 A를 출력하라는 함수

message3()                      #for문을 세번돌며 BCBCBC가 출력되고 마지막에 A가 출력되어 결과는 BCBCBCA가 출력