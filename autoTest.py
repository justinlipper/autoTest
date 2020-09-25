'''
autoTest Version 1.0
Written by Justin Lee Lipper

Functionality:
	This program takes into account your operating system (limited to Windows and Linux as of 24092020) and runs your python assignment with test cases.

Requirements:
	- This program assumes that your assignment is labeled using the following convention "assignmentX-X.py". For example, "assignement3-1.py", "assignment1-1.py"...etc.
	- This program assumes that the test_X-X-X.in files are all in the same directory as your assignment file.

Input:
	1). Default - User provides a string of the full path of the directory of where their assignment and test files are kept.
	2). -c - run autoTest.py in the current directory.
	3). -s - specify a directory as a command line argument.
	4). -o - Will run autoTest in the current directory and print the output of the test files.
	5). -h - Help

Please see README.txt for more informatio on this program
'''

import os, sys, platform, re, argparse

############################################# Handles user errors ##############################################
def error_messages(message, directory, additional_info):
	if message == 1:
		print("ERROR 1: Assignment file not found:\n\nYour given directory: ", directory, "\n\n"\
			"It looks like autoTest was not able to find your python assignment file.\n"\
			"Please note that autoTest expects your python file to be named according to the template \"assignmentX-X.py\"\n"\
			"For Example: \"assignment1-1.py\", \"assignment2-3.py\"...etc.\n"\
			"Please rename your file accordingly and rerun the program to try again")
		exit()

	elif message == 2:
		print("ERROR 2: There were no test cases found:\n\nYour given directory: ", directory, "\n"\
			"Your python file: ", additional_info, "\n\n"\
			"It looks like autoTest was not able to find the test files for this assignment.\n"\
			"Please note that autoTest expects your test files to be in the same directory as", additional_info, "\n"\
			"Please rename your file accordingly and rerun the program to try again")
		exit()

	elif message == 3:
		print("ERROR 3: Could not find directory:\n\nYour given directory: ", directory, "\n\n"\
			"It looks like autoTest was not able to find the directory that you've specified.\n"\
			"Please try again.")
		exit()

############################### Tests the directory to make sure that it exists ################################
def directory_test(initial_directory):
	try:
		os.listdir(initial_directory)
	except:
		error_messages(3, initial_directory, None)

####################### Finds the python assignment and runs tests on it from a Linux OS #######################
def for_linux(scripts_directory, user_wants_test_output):
	directory_test(scripts_directory)
	#Functionality 1: We need to make sure that the user enters a string that has the spaces excaped (using the \ character)
	#Format the directory:
	new_directory = []

	#Go through the string
	for char in range(0,len(scripts_directory)):
		#If the current character is a space and the previous character is not the excape character
		if scripts_directory[char] == " " and scripts_directory[char - 1] != "\\":
			#Turn the string into a list (so we can use functions on it like insert())
			scripts_directory = list(scripts_directory)
			#Insert the excape character
			new_directory.append("\\")
		#Now we are ready to add the current character to our new string
		new_directory.append(scripts_directory[char])

	#We need to make sure that there is a / at the end of the directory string
	if new_directory[-1] != "/":
		new_directory.append("/")

	#Turn the list into a string
	temp_string = ""
	for i in range(len(new_directory)):
		temp_string = temp_string + new_directory[i]
	new_directory = temp_string

	#Functionality 2: We will start to find the files that we will be using
	#Get the files that are listed in the directory
	file_names_in_directory = os.popen("ls " + new_directory).readlines()
	
	#Go through the files and find one that is the pyhton file and others that are the test files
	#All other files will be neglected
	python_file_name = ""
	test_files_list = []

	#For each file that we found
	for file in file_names_in_directory:
		#remove the extra whitespaces
		file = file.strip()
		#Check to see if the current file is the python file
		python_file = re.findall("assignment\d-\d\.py", file)
		#If it is the python file then we would like to save it
		if python_file != []:
			python_file_name = python_file[0]
			assignment_numbers = re.findall("assignment(\d)-(\d)\.py", file)

	#Test to see if the python file was found
	if python_file_name == "":
		error_messages(1, new_directory, None)

	for file in file_names_in_directory:			
		#If it is one of the test files then we would like to keep it
		is_test = re.findall("test_" + str(assignment_numbers[0][0]) + "-" + str(assignment_numbers[0][1]) + "-\d\.in", file)
		if is_test != []:
			test_files_list.append(file)

	#Test to see if there were any test cases
	if test_files_list == []:
		error_messages(2, new_directory, python_file_name)

	#For each test file we would like to run the python script that we found.
	for test_file in test_files_list:
		print("Your output for", test_file.strip() + ":")
		cmd = "python3 " + new_directory + python_file_name + " " + new_directory + test_file
		os.system(cmd)
		#Print the output of each test file
		if user_wants_test_output == 1:
			print("\nOutput of " + test_file)
			os.system("cat " + test_file)
			print("_______________________________________________")
		elif user_wants_test_output == 0:
			print("_______________________________________________\n")

###################### Finds the python assignment and runs tests on it from a Windows OS ######################
def for_windows(scripts_directory, user_wants_test_output):
	directory_test(scripts_directory)
	list_of_files = os.listdir(scripts_directory + "\\")

	python_file_name = ""
	test_files_list = []

	#For each file that we found
	for file in list_of_files:
		#remove the extra whitespaces
		file = file.strip()

		#Check to see if the current file is the python file
		python_file = re.findall("assignment\d-\d\.py", str(file))
		#If it is the python file then we would like to save it
		if python_file != []:
			python_file_name = python_file[0]
			assignment_numbers = re.findall("assignment(\d)-(\d)\.py", file)

	#Test to see if the python file was found
	if python_file_name == "":
		error_messages(1, new_directory, None)

	for file in list_of_files:			
		#If it is one of the test files then we would like to keep it
		is_test = re.findall("test_" + str(assignment_numbers[0][0]) + "-" + str(assignment_numbers[0][1]) + "-\d\.in", file)
		if is_test != []:
			test_files_list.append(file)

	#Test to see if there were any test cases
	if test_files_list == []:
		error_messages(2, new_directory, python_file_name)

	#Put a \ at the end of the directory string if you haven't already
	if scripts_directory[-1] != "\\":
		scripts_directory = scripts_directory + "\\"

	for test_case in test_files_list:
		print("Your output for", test_case, ":")
		os.system("python \"" + scripts_directory + python_file_name + "\" \"" + scripts_directory + test_case + "\"")
		print()

		if user_wants_test_output == 1:
			print("\nOutput of " + test_case)
			os.system("type " + test_case)
			print("_______________________________________________")
		elif user_wants_test_output == 0:
			print("_______________________________________________\n")

##################################### Determines User's Operating System #######################################
def os_test(scripts_directory, user_wants_test_output):
	#Trying to make sure that this program works for Linux and Windows
	find_os = platform.system()

	if find_os == "Windows":
		return for_windows(scripts_directory, user_wants_test_output)
	elif find_os == "Linux":
		return for_linux(scripts_directory, user_wants_test_output)
	else:
		print("Could not find the OS that you are using.\nAttempting to run program regardless...")
		try:
			for_linux(scripts_directory, user_wants_test_output)
		except:
			print("Failed: Could not run program. Issue with OS compatability.")

##################################################### MAIN #####################################################
def main():

	pareser = argparse.ArgumentParser()
	#Defining the options that the user can use
	pareser.add_argument("-c", "--currentDir", action='store_true', help="Will execute autoTest in your current working directory")
	pareser.add_argument("-s", "--specifyDir", nargs=1, help="Will take a directory string")
	pareser.add_argument("-o", "--printTestOutput", action='store_true', help="Will print the test output and run autoTest.py in the current directory")
	argsP = pareser.parse_args()

	#If the user passes -c
	if argsP.currentDir:
		os_test(os.getcwd(), 0)
	#If the user passes -s
	elif argsP.specifyDir:
		os_test(argsP.specifyDir[0], 0)
	#if the user passes -o
	elif argsP.printTestOutput:
		os_test(os.getcwd(), 1)
	#Default
	else:
		scripts_directory = input("Please input the directory where your script is located:")
		os_test(scripts_directory)

if __name__ == '__main__':
    main()