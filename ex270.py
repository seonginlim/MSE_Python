class Stock:                                                #class Stock 정의
    def __init__(self, name, code, per, pbr, dividend):     #생성자를 생성하여 각 인자를 포함시킨다
        self.name = name                                    #self라는 객체공간안에 name이라는 변수를 만들고, 함수인자가 가리키는 값을 저장한다
        self.code = code                                    #self라는 객체공간안에 code라는 변수를 만들고, 함수인자가 값을 저장한다.
        self.per = per                                      #self라는 객체공간안에 per라는 변수를 만들고, 함수인자가 값을 저장한다.
        self.pbr = pbr                                      #self라는 객체공간안에 pbr이라는 변수를 만들고, 함수인자가 값을 저장한다.
        self.dividend = dividend                            #self라는 객체공간안에 dividend라는 변수를 만들고, 함수인자가 값을 저장한다.
        
종목 = []                                                    #나중에 채워질 종목이라는 빈 리스트 생성

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)           #Stock class의 삼성이라는 객체생성
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)            #Stock class의 현대차라는 객체생성
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)         #Stock class의 LG전자라는 객체생성
    
종목.append(삼성)                                               #종목이라는 리스트에 append함수를 이용해서 삼성이라는 객체를 원소로 추가
종목.append(현대차)                                              #종목이라는 리스트에 append함수를 이용해서 현대차라는 객체를 원소로 추가
종목.append(LG전자)                                             #종목이라는 리스트에 append함수를 이용해서 LG전자라는 객체를 원소로 추가

for i in 종목:                                                 #종목 리스트의 원소개수만큼 for문 반복
    print(i.code, i.per)                                      #i(즉, for문을 돌때 각 객체)에 접근해서 code값과 per값을 차례대로 출력 