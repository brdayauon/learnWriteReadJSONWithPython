import json

dictionary={
	"name" : "Brandon",
	"phoneNumber" : "4154206261",
	"id" : 0
}

with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile)