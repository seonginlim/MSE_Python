date = ['09/05', '09/06', '09/07', '09/08', '09/09']   #data라는 변수에 각 원소들을 리스트 형태로 저장.
close_price = [10500, 10300, 10100, 10800, 11000]      #close_price라는 변수에 각 원소들을 리스트 형태로 저장.
close_table = dict(zip(date, close_price))             #각 자리번호끼리 묶어주는 zip함수를 이용해서 두개의 리스트를 묶어주고, 그 값을 dict의 형태로 변환하여 close_table라는 변수에 저장.
print(close_table)                                     #print함수를 이용해서 close_table값을 출력.