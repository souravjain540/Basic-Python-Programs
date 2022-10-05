def twoSum(self, nums, target):
		buffer_dictionary = {}
		for i in rangenums.__len():
			if nums[i] in buffer_dictionary:
				return [buffer_dictionary[nums[i]], i] #if a number shows up in the dictionary already that means the 
														#necesarry pair has been iterated on previously
			else: # else is entirely optional
				buffer_dictionary[target - nums[i]] = i 
				# we insert the required number to pair with should it exist later in the list of numbers