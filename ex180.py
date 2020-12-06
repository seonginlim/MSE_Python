low_prices  = [100, 200, 400, 800, 1000]    #low_prices라는 변수에 리스트값을 저장.
high_prices = [150, 300, 430, 880, 1000]    #high_prices라는 변수에 리스트값을 저장.


volatility = []                              #volatility라는 변수에 나중에 값들을 받을 수 있는 빈 list를 담아둔다.
for i in range(5):                           #range함수를 이용해서 0,1,2,3,4까지 만들 수 있다. 그 만큼을 for문을 통해 반복.
    diff = high_prices[i] - low_prices[i]    #변동폭을 diff라는 변수로 설정하고, 그 변수에 고가의 i번째 값과 저가의 i번째 값의 차를 저장한다.
    volatility.append(diff)                  #append멤버함수를 통해 diff값을 차례대로 빈 리스트에 넣는다.
    
print(volatility)                            #print함수를 통해서 volatility를 출력하면 리스트형태로 출력된다.