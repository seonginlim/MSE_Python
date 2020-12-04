data = "    삼성전자    "   #data라는 변수에 양쪽 공백이 있는 삼성전자를 대입
data1 = data.strip()      #양쪽 공백을 지워주는 멤버함수 strip을 사용후, 문자열은 수정이 불가하므로 새로운 변수data1에 대입
print(data1)              #print함수를 사용하여 data1을 출력