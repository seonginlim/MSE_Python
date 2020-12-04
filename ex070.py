data = [2, 4, 3, 1, 5, 10, 9]           #리스트의 형태로 나타난 원소들을 data라는 변수에 할당
data.sort()                             #sort함수로 정렬, 가장왼쪽이 작은 원소가 오도록 정렬한다
print(data)                             #print함수를 이용해서 data값을 출력

#수업시간에 배운 원본은 손대고 싶지 않을때 사용하는 방법!!!

data = [2, 4, 3, 1, 5, 10, 9]           #리스트의 형태로 나타난 원소들을 data라는 변수에 할당
data2 = sorted(data)                    #sorted라는 함수를 사용해서 data값을 오름차순으로 정렬후, 그 값을 새로운 변수 data2에 할당
print(data2)                            #print함수를 이용해서 data2값을 출력