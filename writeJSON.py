import json

# with open("sample.json", "w") as outfile:
# 	json.dump(contactDict, outfile)


class Solution:

	def __init__(self):
		self.fileName = 'sample.json'

	def writeToJSON(self, fileName, dictionary):

		with open(fileName, "w") as outfile:
			json.dump(dictionary, outfile)

contactDict = {
	"contacts": [
		{"name" : "Brandon",
		"phoneNumber" : "6789998212",
		"id" : 0
		},
		{
		"name" : "Pineapple",
		"phoneNumber" : "6789998212",
		"id" : 1
		}
	]
}

dictionary={

	"name" : "Rex",
	"phoneNumber" : "6789998212",
	"id" : 3
}

fileName = 'sample.json'
s = Solution()

s.writeToJSON(fileName, contactDict)
