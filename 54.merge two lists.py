
test_keys = ["roshith", "kishore", "Vishnu"]
test_values = [1, 4, 5]


print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))

res = {}
for key in test_keys:
	for value in test_values:
		res[key] = value
		
		break

print ("Resultant dictionary is : " + str(res))
