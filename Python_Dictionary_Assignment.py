# 1. Convert two lists into a dictionary
''''
Given - keys = ['Ten', 'Twenty', 'Thirty']  values = [10, 20, 30]
Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''

# Solution1: The zip() function and a dict() construtor
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = dict(zip(keys, values))
print(res_dict)

# Solution2: Using a loop and update() method of a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

# 2. Merge two python dictionaries into one
''''
Given - dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''

# Solution1
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)

# Solution2

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

# 3. Print the value of key 'history' from the below dict
''''
Given - 

sampleDict = {
   "class":{
     "student":{
       "name": "mike",
         "marks": {
           "physics": 70,
           "history": 80
         }
     }
   }
}
Expected output - 80

understand how to locate the nested key

1. sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
2. sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
3. sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}
'''

# Solution
sampleDict = {
   "class":{
     "student":{
       "name": "mike",
         "marks": {
           "physics": 70,
           "history": 80
         }
     }
   }
}

print(sampleDict['class']['student']['marks']['history'])


# 4. initialize dictionary with default values
''''
The fromkeys() method returns a dictionary with the specified keys and the specified value

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "Salary": 8000}
Expected output: {'Kelly':{"designation": 'Developer', "Salary": 8000}, 'Emma': {"designation": 'Developer', "Salary": 8000}}
'''

# Solution
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "Salary": 8000}
res = dict.fromkeys(employees, defaults)
print(res)

# indivisual data
print(res["Kelly"])

# 5. Create a dictionary by extracting the keys from a given dictionary
''''
sample_dict = {"name": "Kelly", "age": "25", "salary": "8000", "city": "New York"}

keys_to_extract = ["name", "salary"]

Expected output: {'name': 'Kelly', 'salary': 8000}
'''

# Solution1 Dictionary comprehension
sample_dict = {"name": "Kelly", "age": "25", "salary": "8000", "city": "New York"}
keys_to_extract = ["name", "salary"]
extracted_dict = {k: sample_dict[k] for k in keys_to_extract}
print(extracted_dict)

# Solution2 Using the update() method and loop
sample_dict = {"name": "Kelly", "age": "25", "salary": "8000", "city": "New York"}
# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its value from sample_dict
   res.update({k: sample_dict[k]})
print(res)

# 6. Delete a list of keys from a dictionary
''''
sample_dict = {"name": "Kelly", "age": "25", "salary": "8000", "city": "New York"}
# keys to remove - ["name", "salary"]
Expected output: {"age": "25","city": "New York"}
'''

# Solution1  Using the pop() method and loop
sample_dict = {"name": "Kelly", "age": "25", "salary": "8000", "city": "New York"}
# keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)

# Solution2 Dictionary Comprehension
sample_dict = {"name": "Kelly", "age": "25", "salary": "8000", "city": "New York"}
# keys to remove
keys = ["name", "salary"]

sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)

# 7. Check if a value exists in a dictionary
''''
sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output: 200 present in a dict
'''

# Solution
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')

# 8. Rename key of a dictionary
''''
Given - sample_dict = {"name": "Kelly", "age": "25", "salary": "8000", "city": "New York"}
Expected output: {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''

# Solution
sample_dict = {"name": "Kelly", "age": "25", "salary": "8000", "city": "New York"}
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

# 9. Get the keys of a minimum value from the following dictionary
''''
sample_dict = {'Physics': 82, 'Math':65, 'history': 75}
Expected output: Math
'''

# Solution
sample_dict = {'Physics': 82, 'Math':65, 'history': 75}
print(min(sample_dict, key = sample_dict.get))

# 10. Change value of a key in a nested dictionary
''''
sample_dict = {
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 500}
}
Expected output: 
{
  'emp1': {'name': 'Jhon', 'salary': 7500},
  'emp2': {'name': 'Emma', 'salary': 8000},
  'emp3': {'name': 'Brad', 'salary': 8500}
}
'''
# Solution
sample_dict = {
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)

# ============= COMPLETED =================