import os
class BankAccount():

    def __init__(self):
      self.account_number = 0;
      self.pin_number = ""
      self.balance = 0
      self.interest_rate = 0.0
      self.transaction_list = []
      

    def deposit_funds(self, amount):
      try:
        amt = float(amount)
        return True
      except:
        return False
        

    def withdraw_funds(self, amount):
      try:
        amt = float(amount)
        if(self.balance >= amt):
          return True
        else:
          return False
      except:
        return False      
       
        
    def get_transaction_string(self):
      transaction_str = ""
      for t in self.transaction_list:
        if(t >= 0):
          transaction_str = transaction_str + "Deposit\n"
          transaction_str = transaction_str + str(abs(t)) + "\n"
        else:
          transaction_str = transaction_str + "Withdrawal\n"
          transaction_str = transaction_str + str(abs(t)) + "\n"
      return transaction_str          
        


    def save_to_file(self):
      filename = str(self.account_number) + ".txt";
      os.remove(filename);
      f = open(filename,'w')
      f.write(str(self.account_number) + "\n")
      f.write(str(self.pin_number)+ "\n")
      f.write(str(self.balance)+ "\n")
      f.write(str(self.interest_rate)+ "\n")
      transaction_str = self.get_transaction_string()
      f.write(transaction_str)
        