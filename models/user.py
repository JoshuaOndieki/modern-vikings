class user_data:
	register_data = []
	"""
	check if data entry is empty
	"""
	def signup_empty(self,user_type,user_name,password):
		pass

	def signup_whitespace(self,user_type,user_name,password):
		pass

	def user_type(self,user_type):
		pass

	def user_exist(self,user_name):
		pass

	def register_user(self,user_type,user_name,password):
		pass


class signup_user(user_data):
	def __init__(self,user_type,user_name,password):
		self.user_name = user_name
		self.user_type = user_type
		self.password = password





