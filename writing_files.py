import os 

# Get the file path from the user
print("Type in the file path for the doucment to be located:")
file_path = input()

# Get the file name
print("\nType in the name of the file:")
file_name = input()

#Prompt user for name, address, and phone #
print("\nEnter in your name:")
name = input()

print("\nEnter in your address:")
address = input()

print("\nEnter in your phone number:")
number = input()

#Check if file path exists
if os.path.isdir(file_path) is not True:
	#Create File path
	os.makedirs(file_path)

#Create the entire path plus the name
complete_path = file_path + '\\' + file_name + '.txt'

with open(complete_path, 'w') as file_object:
	#write the name, address, and phone number to the text document
	file_object.write(name + ', ' + address + ', ' + number)

#Open the file that was created and read the text 
with open(complete_path, 'r') as file_object:
	#Read object
	content = file_object.read()

#print content
print("\n\n\n"content)