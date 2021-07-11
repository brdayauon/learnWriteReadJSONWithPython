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

			json_object = json.load(openfile)

		name = []
		#print(json_object)
		for contact in json_object['contacts']:
			for key,value in contact.items():
				# print(key,value)
				if key == 'name':
					name.append(value)

		print(name)

s = Solution()

print('--------------------------')
#one way to open json file


s.readFromJSONFileWithClose(fileName)

print('--------------------------')

s.getNameOfContacts(fileName)