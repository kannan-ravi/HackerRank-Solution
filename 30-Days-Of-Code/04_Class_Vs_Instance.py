#I was came with slightly different solution like same output but HackerRank Doesn't take mine, So I change my solution little bit, even all that are same but it contain single extra line Hacker Rank doen't take mine...

#So don't worry if your solution looks different than HackerRank, In Real World People are Genius not like Computer.


class Person:
	#defing the construction or intialize the class
	
	def __init__(self, InitialAge):
		#if initial age is less than 0 self.age is set to 0 and print the following below content if not self.age and Initialage is same
		
		if InitialAge < 0:
			self.age = 0
			print ("Age is not valid, setting age to 0.")
		else: self.age = InitialAge
		
	def amIOld(self):
		#If age is greater than or equal to 18 said old, if greater then or equal to 12 say teenager, otherwise say young
		
		if self.age >= 18:
			print("You are old.")
		elif self.age >= 13:
			print("You are teenager.")
		else:
			print("You are young.")
		
	def yearPasses(self):
		#increment the age of the person in here
		
		self.age += 1

#This is used to get the multiple input according to user choice.

t = input()
for i in range(0, int(t)):
	age = int(input())
	p = Person(age)
	p.amIOld()
	for j in range(0,3):
		p.yearPasses()
	p.amIOld()
	print (" ")

# By 
#	Kanna Ravindran.R