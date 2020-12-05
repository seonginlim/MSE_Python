class 부모:                        #부모 class
    def __init__(self):           #생성자
        print("부모생성")           #print함수를 통하여 부모생성 출력
        
class 자식(부모):                   #부모class를 상속받는 자식class생성
    def __init__(self):           #생성자
        print("자식생성")           #자식class가 생성될때, 자식생성을 먼저 출력한다
        super().__init__()        #super라는걸 이용하여 부모class에 접근, 그 다음 부모class에 있는 생성자를 명시적으로 호출
        
나 = 자식()                         #자식class의 객체를 생성
                                  #자식class의 객체가 생성되면 생성자가 호출되고, 자식생성을 먼저 출력
                                  #그다음 부모class를 명시적으로 호출했기 때문에, 부모생성을 출력