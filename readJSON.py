import json

fileName = 'sample.json' 

#print(type(json_object))  #type is of 


class Solution:

	def __init__(self):
		self.fileName = 'sample.json'


	def readFromJSONFileWithClose(self, fileName):

		f = open(fileName, 'r')

		data = json.loads(f.read())

		for i in data['contacts']:
			print(i)

		f.close()

	def getNameOfContacts(self, fileName):

		with open('sample.json', 'r') as openfile:
			content = json.load(openfile)

		name = []
		#print(content)
		for contact in content['contacts']:
			for key,value in contact.items():
				# print(key,value)
				if key == 'name':
					name.append(value)

		print(name)

s = Solution()

s.readFromJSONFileWithClose(fileName)

print('--------------------------')

s.getNameOfContacts(fileName)