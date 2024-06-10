class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = list()
    #Keep track of the balance of a current category
    self.balance = list()  

  #Check whether the amount > the balance of the budget category
  def check_funds(self, amount):
    if float(amount) >= sum(self.balance):
      return False
    else:
      return True

  def deposit(self, amount, description=""):
    self.ledger.append({"amount":amount,"description": description})
    self.balance.append(float(amount))

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": - amount, "description": description})
      self.balance.append(-float(amount))
      return True
    else:
      return False

  def  get_balance(self):
    current_balance = sum(self.balance)
    return current_balance

  def transfer(self, amount, destination):
    if self.check_funds(amount) == True:
      self.withdraw(amount, "Transfer to {}".format(destination.category))
      destination.deposit(amount, "Transfer from {}".format(self.category))
      return True
    else:
      return False

  #Print out the output(ledger)
  def __str__(self):  
    #header
    str = self.category.center(30,"*") + "\n"
    #list of items in ledger
    for item in self.ledger:
      line_description = "{:<23}".format(item["description"])   #23 chars left-aligned description 
      line_amount = "{:>7.2f}".format(item["amount"]) #7 chars 2 deci right-aligned amount 
      #Combine aligned lines together (max 23 chars for description & max 7 chars for amount)
      str += "{}{}\n".format(line_description[:23], line_amount[:7])
    #Total
    total = "Total: " + "{:.2f}".format(self.get_balance())
    return str + total
    

    
def create_spend_chart(categories):
