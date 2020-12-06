string = 'abcd'                     #abcd문자열을 string이란 변수에 저장.
string.replace('b', 'B')            #replace를 이용하여 b를 B로 대체.
print(string)                       #print함수를 이용해서 string을 출력.
                                    #위의 결과는 abcd이다. 이유는 문자열 그 자체는 replace할 수 없기 때문이다.
                                    #만약, string = string.replace('b', 'B')라고 입력 했다면 결과값은 aBcd일 것이다.
                                    #하지만 문제에서 새로운 변수를 선언하지 않았기에 결과값은 기존의 string값이 출력될것이다.