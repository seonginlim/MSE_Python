ohlc = [["open", "high", "low", "close"],     #2차원의 리스트를 ohlc변수에 저장.
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
        
total_profit = 0                              #total_profit이란 변수에 초기값 0설정.
for day_price in ohlc[1:]:                    #ohlc리스트에서 slicing을 통해 0번째를 제외한 1번째부터 for문을 반복.
    profit = day_price[0] - day_price[3]      #이익 = 시가 - 종가 이므로, profit이란 변수에 {(원소리스트 0번째 자리의 값) - (원소리스트 3번째 자리의 값)}을 저장. 
    total_profit += profit                    #for문을 돌며 profit값을 total_profit에 더해주며 total_profit에 저장. 
    
print(total_profit)                           #print함수를 이용해서 total_profit값을 출력.