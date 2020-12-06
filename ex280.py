import random                                                   #숫자를 랜덤으로 뽑기 위하여 random모듈 사용.

class Account:                                                  #Account라는 class생성.

    account_count = 0                                           #account_count라는 변수가 초기값 0으로 설정. class variable이다. 계좌가 만들어질때마다 이 값이 증가. 
    
    def __init__(self, name, balance):                          #생성자를 생성, 입력받는 값은 이름과 잔고.
        self.deposit_count = 0                                  #객체가 생성될때 입금횟수가 0번이므로 0으로 초기화.
        self.deposit_log = []                                   #deposit_log에 비어있는 리스트를 생성. 입금이 될때마다 그 값을 기록하기 위해서.
        self.withdraw_log = []                                  #withdraw_log에 비어있는 리스트를 생성. 출금이 될때마다 그 값을 기록하기 위해서.
        
        self.name = name                                        #입력받은 이름을 self가 가리키는 공간에 name이라는 이름을 만들고 name을 저장한다.
        self.balance = balance                                  #입력받은 잔고를 self가 가리키는 공간에 balance라는 이름을 만들고 balance를 저장한다.
        self.bank = "SC은행"                                     #은행이름은 SC은행으로 저장.
        
        num1 = random.randint(0, 999)                           #random모드를 이용해서 세자리 수를 num1이라는 변수에 저장.
        num2 = random.randint(0, 99)                            #random모드를 이용해서 두자리 수를 num2라는 변수에 저장.
        num3 = random.randint(0, 999999)                        #random모드를 이용해서 여섯자리 수를 num3라는 변수에 저장.
        
        num1 = str(num1).zfill(3)                               #num1을 문자열로 만들어주고 zfill을 통해 빈자릿수는 0으로 채워준뒤, 그 값을 다시 num1에 저장.
        num2 = str(num2).zfill(2)                               #num2를 문자열로 만들어주고 zfill을 통해 빈자릿수는 0으로 채워준뒤, 그 값을 다시 num2에 저장.
        num3 = str(num3).zfill(6)                               #num3를 문자열로 만들어주고 zfill을 통해 빈자릿수는 0으로 채워준뒤, 그 값을 다시 num3에 저장.
        self.account_number = num1 + '-' + num2 + '-' + num3    #이렇게 만들어진 문자열을 self가 가리키는 객체공간에 account_number라는 변수를 만들고 저장.
        
        Account.account_count += 1                              #계좌가 하나 증가할때마다 Account에 접근하여 값이 증가. class안에 있는 값이기에 Account로 접근.
        
    @classmethod                                                #특별한 경우에, data가 각 객체에 저장되는게 아니라 class자체에 저장될때 앞에 써준다.
    def get_account_num(cls):                                   #따라서 self를 받을 필요가 없고 cls라고 적어준다.
        print(cls.account_count)                                #cls에 접근하여 account_count를 print함수를 통해 출력.
        
    def deposit(self, amount):                                  #입금액을 amount변수로 받는다.
        if amount >= 1:                                         #입금액이 1원 이상이라면.
            self.deposit_log.append(amount)                     #입금이 한번 일어날때마다 deposit_log에 append함수를 이용해서 amount값을 리스트에 추가한다.      
            self.balance += amount                              #입금은 self가 가리킨는 공간에 balance라는 잔고가 있는데 거기에 amount입금액을 더하면 그게 입금.
            self.deposit_count += 1                             #self가 가리키는 공간에 deposit_count값이 있는데 이 값을 하나 증가시킨다.
            if self.deposit_count % 5 == 0:                     #즉, 5의 배수라면.
                self.balance = (self.balance * 1.01)            #값에 1.01을 곱하여 이자를 지급한다.
                
    def withdraw(self, amount):                                 #출금액을 amount변수로 받는다.
        if self.balance > amount:                               #마이너스 통장을 고려하기 위해 잔고와 출금액을 if문으로 비교.
            self.withdraw_log.append(amount)                    #출금이 한번 일어날때마다 withdraw_log에 append함수를 이용해서 amount값을 리스트에 추가한다.
            self.balance -= amount                              #출금은 잔고 balance에서 출금액 amount를 빼주면 된다.
                
    def display_info(self):                                     #self가 가리키는 객체를 보여준다.
        print("은행이름:", self.bank)                             #은행이름은 self.bank에 저장.
        print("예금주:", self.name)                              #이름은 self.name에 저장.
        print("계좌번호:", self.account_number)                   #계좌번호는 self.account_number에 저장. 
        print("잔고:", self.balance )                            #잔고는 self.balance에 저장.
    
    def withdraw_history(self):                                 #withdraw_history를 정의.
        for amount in self.withdraw_log:                        #self가 가리키는 객체공간안에 withdraw_log가 있는데 순서대로 for문이 반복된다. 
            print(amount)                                       #for문이 반복될때마다 그 값을 print함수를 이용해서 출력한다.
            
    def deposit_history(self):                                  #deposit_history를 정의.
        for amount in self.deposit_log:                         #self가 가리키는 객체공간안에 deposit_log가 있는데 순서대로 for문이 반복된다.
            print(amount)                                       #for문이 반복될때마다 그 값을 print함수를 이용해서 출력한다.
            
k = Account("Kim", 1000)                                        #Account에 이름은 Kim, 입금액은 1000원을 넣은것을 k라는 객체로 받음.
k.deposit(100)                                                  #예금을 100원.    
k.deposit(200)                                                  #예금을 200원.
k.deposit(300)                                                  #예금을 300원.
k.deposit_history()                                             #k라는 객체의 deposit_history를 호출.
                                                                #100 200 300이 출력될것이다.

k.withdraw(100)                                                 #출금을 100원.
k.withdraw(200)                                                 #출금을 200원.   
k.withdraw_history()                                            #k라는 객체의 withdraw_history를 호출.
                                                                #100 200이 출력될것이다. 