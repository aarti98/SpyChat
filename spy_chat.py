from spydetails import spy
from steganography.steganography import Steganography

#WELCOME
print("Hello!")
print('Let\'s get started')



#TO ADD A NEW USER
def new_user():
	print("Hey new user! It's time to introduce yourself")
	spy_name = input("Enter your name")
	spy_salutation = input("What should we call you? Mr. or Ms.\n")

		# spy_salutation = input("What should we call you? Mr. or Ms.\n")
	while (True):
			
		if spy_salutation.upper() == "MR" or spy_salutation.upper() == "MS" :
			spy_name = spy_salutation + " " + spy_name
			break
		else:
			print("Enter valid salutation")
			spy_salutation = input("What should we call you? Mr. or Ms.\n")
			
	spy_name = spy_salutation + " " + spy_name
	
	spy_age = int(input("What is your age?"))
	#TO CHECK IF YOU ARE OLD ENOUGH
	#TO CHECK IF YOU ARE OLD ENOUGH TO SPY
	if spy_age > 12 and spy_age < 50:
		global spy_rating
		spy_rating =  float(input("What is your rating?"))

		if type(spy_rating) == float:
			print("Lets proceed further")
		else:
			print("Please enter correct rating")	
	
		#CHECK THE RATING
		if spy_rating > 4.5:
			print ('Great ace!')
		elif spy_rating > 3.5 and spy_rating <= 4.5:
			print ('You are one of the good spy')
		elif spy_rating >= 2.5 and spy_rating <= 3.5:
			print ('You can always do better!')
		else:
			print('We can always use somebody to help in the office')	

		spy_is_online = True
		print(("Authentication complete. Welcome %s! spy_age: %d and rating of: %.1f. Proud to have you onboard") %(spy_name, spy_age, spy_rating))	

	else:
		print('Sorry you are not eligible.')

  
#TO ADD NEW FRIENDS
friends = []


def add_friend():
	
	#MAKING A DICTIONARY TO ADD DETAIL OF FRIENDS
	new_friend = {
	'name': " ",
	'salutation': " ",
	'age': 0,
	'spy_rating': 0.0
	}

	#ENTER THE DETAILS OF YOUR FRIEND
	new_friend['name'] = input("Enter your friend's name: ")
	new_friend['salutation'] = input("Mr. or Ms.: ")
	new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
	new_friend['age'] = int(input("age?: "))
	new_friend['rating'] = float(input("rating: "))


	if len(new_friend['name']) > 0 and new_friend['age'] >12 and new_friend['rating'] >= spy_rating:
		#ADD FRIEND TO THE LIST FRIENDS
		friends.append(new_friend)
		print('Created')
		total_friends = len(friends)
		print(("You have %d friends") %(total_friends))
		
	
	else:
		print("Sorry! Invalid entry")		




#TO ADD OR UPDATE STATUS
Status_message = ['My name is bond, James Bond', 'Shaken, not stirred.']
# Status_message = []
def status(Status_message):
	# global Status_message
	# Status_message = ['My name is bond, James Bond', 'Shaken, not stirred.']
	current_status_message= ""

	
	# if current_status_message != None:
	if current_status_message != "":
	
		print("Your current status is" + current_status_message + "\n")

	else:
		print("You don't have any status yet")

	default = input("Do you want to choose from existing status? Y or N\n")

	if default == "Y" or default == "y" :
		position = 1

		for message in Status_message:
			print(str(position) + "." + message)
			position = position + 1
		select_message = int(input("Choose from above messages\n"))		

		if len(Status_message) >= select_message:
			updated_status_message = Status_message[select_message-1]
			current_status_message = Status_message[select_message-1]

			print("Your current status is" + " " + updated_status_message +  "\n")
			return updated_status_message




	elif (default == "N" or default == "n"):
		new_status_message = input("What status message do you want to set?\n")

		# if len(new_status_message) > 0:
		Status_message.append(new_status_message)
		current_status_message = new_status_message	#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		# current_status_message = new_status_message	
		print ("Your new status is " + new_status_message + "\n")	

	# else:
	# 	print("Invalid input")


#FUNCTION TO SELECT A FRIEND TO CHATkya ho 
def select_friend():
	item_number = 0

	for friend in friends:
		print(('%d. %s')%(item_number+1), friends['name'])
		item_number = item_number + 1

	friend_choice = input('Choose from your friends: ')
	friend_choice_position = int(friend_choice)-1
	return friend_choice_position	


#FUNCTION TO SEND A MESSAGE
def send_message():

	choose_friend = select_friend()


	original_message = input("What is the name of image?")
	output_path = "output.jpg"
	text = input("What do you want to say?")

	#TO ENCODE THE MESSAGE
	Steganography.encode(original_message, output_path, text)

	new_chat = {
	"message": text,
	"time": datetime.now(),
	"sent_by_me": True
	}

	
	
	print("Your secret message is ready")


#TO READ A SECRET MESSAGE
def read_message():
	sender = select_friend()

	output_path = input("What is the name of the file?")
	secret_text = Steganography.decode(output_path)

	new_chat = {
	"message": secret_text,
	"time": datetime.now(),
	"sent_by_me": False
	}



def menu():
	show_menu = True

	while show_menu:
		menu_choice= 'What do you want to do?\n 1. Add a new user\n 2. Use default user\n 3. Add friend\n 4. Update or add status\n 5. Send message\n 6. Read message\n 7. Exit\n'
		menu_choice= int(input(menu_choice))

		if menu_choice == 1:
			print("Welcome new user. Let's begin!")
			#CALL THE FUNCTION TO ADD USER
			new_user()


		elif menu_choice == 2:

			#DEFAULT USER
			print("You chose to be a default user")

			spy_name= spy['salutation'] + spy['name']
			spy_age = spy['age']
			spy_rating = spy['rating']
			spy_online = spy['is_online']
			print(("Authentication complete. Welcome %s! spy_age: %d and rating of: %.1f. Proud to have you onboard") %(spy_name, spy_age, spy_rating))  


	
		elif menu_choice == 3:
			print("Let's add friends to your list!")
			#ADD FUNCTION FOR ADDING FRIEND
			add_friend()

	
		elif menu_choice == 4:
			print("Let's update your status")
			#CALL FUNCTION TO ADD STATUS
			status(Status_message)
	
		elif menu_choice == 5:
			print("Send message to other spies")
			#CALL FUNCTION FOR READING MESSAGES"
			send_message()

	
		elif menu_choice == 6:
			print("Read message from your friends")
			#CALL FUNCTION TO READ MESSAGE
			read_message()
	
		else:
			show_menu = False

if __name__ =='__main__':
	menu()

