class User:
	# pass
	def __init__(self, user_id, username): # a special fucntion to initialize the object
		print("new user being created...")
		self.id = user_id
		self.username = username
		self.followers = 0
		self.following = 0
	
	def follow(self, user):
		user.followers += 1
		self.following += 1
	



user_1 = User("001", "angela")
print(user_1.id)
print(user_1.username)

user_1.id = "111"
user_1.username = "blablabla"

print(user_1.id)
print(user_1.username)

user_2 = User("002", "jack")

print(user_2.username)
print(user_2.followers)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)