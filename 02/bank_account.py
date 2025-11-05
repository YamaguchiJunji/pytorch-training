class BankAccount:
    def __init__(self,name):
        self.name=name
        self.balance=0
        self.interest_rate=0.01
    def deposit(self,num):
        self.balance+=num
        
    def withdraw(self,num):
        if self.balance<num:
            print("預金が足りません")
        else:
            self.balance-=num
            print(f"預金を引き出しました。現在の預金：{self.balance}")

    def get_balance(self): 
        print(f"現在の預金：{self.balance}")
    
    def set_interest_rate(self,num):
        self.interest_rate=num
        print(f"金利を設定しました。金利：{self.interest_rate}")

    def apply_interest(self):
        self.balance=self.balance*self.interest_rate
        print(f"現在の預金：{self.balance}")