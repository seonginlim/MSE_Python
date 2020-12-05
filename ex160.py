list = ['intra.h', 'intra.c', 'define.h', 'run.py']    #list라는 변수에 문자열로 구성된 원소들을 리스트형태로 할당
for i in list:                                         #list 원소의 개수만큼 for문이 반복된다
    name, ext = i.split('.')                           #i라는 문자열을 .을 기점으로 분리를 하는 split함수를 이용, .앞은 name, .뒤는 ext변수에 할당
    if ext == 'h' or ext == 'c':                       #이때, 확장자 ext가 h이거나 c이면
        print(i)                                       #print함수를 이용해서 i를 출력