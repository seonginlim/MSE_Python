fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}   #fruit라는 변수에 dict형태의 값을 할당
user = input("좋아하는 과일은?")                           #사용자로부터 좋아하는 과일은? 이란 질문의 값을 받고 그 값을 user라는 변수에 할당
if user in fruit.values():                             #할당받은 값이 fruit안에 있는 value값중 하나면
    print("정답입니다.")                                  #print함수를 이용하여 정답을 출력하고
else:
    print("오답입니다.")                                  #그렇지 않으면 오답을 출력하라