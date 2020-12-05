per = ["10.31", "", "8.00"]     #per이란 변수에 리스트 형태로 원소들을 할당


for i in per:                   #per 리스트 안의 원소개수만큼 for문을 반복
    try:                        #실행코드 : i를 실수로 변환을 한다
        print(float(i))         #print함수를 통해 그 값을 출력
    except:                     #위에서 try되지 않고 예외가 발생하면 실행할 코드
        print(0)                #print함수를 통해 0을 출력
    else:                       #예외가 발생하지 않았을때 실행할 코드
        print("clean data")     #print함수를 통해 clean data를 출력
    finally:                    #예외 발생 여부와 관계없이 항상 실행할 코드
        print("변환 완료")        #print함수를 통해 변환 완료 출력

                                #따라서 10.31은 변환이 되므로 clean data와 변환완료가 같이출력
                                #공백은 변환이 안되므로 0이뜨고 clean data는 뜨지않고 변환완료가 뜬다
                                #8.00은 변환이 되고 clean data와 변환완료가 같이 출력된다