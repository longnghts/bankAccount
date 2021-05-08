class BankAccount:
	bankName = "First National Dojo"
	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		if balance == None:
			self.balance = 0
		else:
			self.balance = balance
	def deposit(self, amount):
		self.balance += amount
		return self
	def withdraw(self, amount):
		self.balance -= amount
		return self
	def displayAccountInfo(self):
		print("balance: ", self.balance)
	def yeildInterest(self):
		self.balance *= self.int_rate
		return self




Mitch = BankAccount(1.01, 5000)
Mike = BankAccount(1.07, None)


Mitch.deposit(2000).deposit(2000).deposit(3000).withdraw(2000).yeildInterest().displayAccountInfo()
Mike.deposit(2000).deposit(3000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yeildInterest().displayAccountInfo()