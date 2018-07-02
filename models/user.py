class user:
	"""
	function adds users
	"""
	def add_user(self,user_type,username,password,user_data):
		item = {
		'user_type':user_type,
		'username': username,
		'password':password,
		'id':len(user_data)
		}
		user_data.append(item)
		return({'result':'Account created'})

	"""
	function gets all user
	"""
	def get_all(self,user_data):
		return(user_data)

	"""
	function to get one user(if user exist)
	"""
	def get_one(self,username,user_data):
		items = user_data
		for item in items:
			if item['username'] == username:
				return(item)
			else:
				return({'result':'username does not exist'})

	def get_userType(self,username,user_data):
		items = user_data
		for item in items:
			if item['username'] == username:
				return({'result':item['user_type']})
			else:
				return({'result':'username does not exist'})

	def login_check(self,password,username,user_data):
		items = user_data
		for item in items:
			if item['username'] == username and item['password'] == password:
				return ({'result':True})
			else:
				return({'result':False})

