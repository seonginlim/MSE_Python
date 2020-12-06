#아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']


open = float(btc['opening_price'])    #btc라는 dict에서 opening_price라는 key로 접근을 하면 시가를 얻을 수 있고, 그 값의 소수점까지 고려하여 float로 받아 open이라는 변수에 저장.
high = float(btc['max_price'])        #마찬가지로 high값도 저장.
low  = float(btc['min_price'])        #마찬가지로 low값도 저장.
diff = high - low                     #high에서 low를 뺀값이 변동폭, 그 값을 diff라는 변수에 저장.

if (open+diff) > high:                #만약(시가 + 변동폭) 값이 high보다 크면.
    print("상승장")                     #print함수를 이용하여 상승장이라고 출력.
else:
    print("하락장")                     #그렇지 않으면 하락장이라고 출력.