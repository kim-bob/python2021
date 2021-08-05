class Account :
    def __init__(self, ano, owner, balance): #ano = account number
 
        self.ano = ano
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount) :
        if self.__balance + amount >= 10000000:
            print('더이상 지갑에 돈을 넣을 수 없습니다..')
            return
        self.__balance += amount

    def withdraw(self, amount) :
        if self.__balance - amount < 0:
            print('지갑에 돈이 부족합니다.')
            return
        self.__balance -= amount
   
    def __str__(self) :
        return f'계좌번호 : {self.ano}, 소유주 : {self.owner}, balance :{self.__balance:9,d}'