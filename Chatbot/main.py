
import re

import tkinter as tk

import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):

message_certainty = 0

has_required_words = True

# Counts how many words are present in each predefined message

for word in user_message:

if word in recognised_words:

message_certainty += 1

# Calculates the percent of recognised words in a user message

percentage = float(message_certainty) / float(len(recognised_words))

# Checks that the required words are in the string

for word in required_words:

if word not in user_message:

has_required_words = False

break

# Must either have the required words, or be a single response

if has_required_words or single_response:

return int(percentage * 100)

else:

return 0

def check_all_messages(message):

highest_prob_list = {}

# Simplifies response creation / adds it to the dict

def response(bot_response, list_of_words, single_response=False, required_words=[]):

nonlocal highest_prob_list

highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

# Responses

response('Hello!', ['hello', 'hi', 'hey'], single_response=True)

response('See you!', ['bye', 'goodbye'], single_response=True)

response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])

response('You\'re welcome!', ['thank', 'thanks'], single_response=True)

response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
# Longer responses

response(long.R_avcourse, ['available', 'courses', 'college'], required_words=['courses', 'available'])

response(long.R_infocom, ['more', 'information ', 'computer'], required_words=['computer', 'engineering'])

response(long.R_infocivil, ['more', 'information ', 'civil'], required_words=['civil', 'engineering'])

response(long.R_infomech, ['more', 'information ', 'mechanical'], required_words=['mechanical', 'engineering'])

response(long.R_infoele, ['more', 'information ', 'electrical'], required_words=['electrical', 'engineering'])

response(long.R_infochem, ['more', 'information ', 'chemical'], required_words=['chemical', 'engineering'])

response(long.R_duration, ['duration', 'of', 'each', 'course'], required_words=['duration', ])

response(long.R_spec, ['special', 'about', 'eat'], required_words=['special'])

response(long.R_fees, ['fees'], required_words=['fees'])

response(long.R_hostel, ['facility', 'hostel', 'available'], required_words=['facility', 'hostel', 'available'])

response(long.R_sports, ['part', 'in ', 'sports'], required_words=['sports'])

response(long.R_addmi, ['what', 'admission ', 'process'], required_words=['admission', 'process'])

response(long.R_name, ['name', 'institute '], required_words=['name'])

response(long.R_lab, ['labs', 'library', 'available', 'college'], single_response=True)

best_match = max(highest_prob_list, key=highest_prob_list.get)

return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Create the Tkinter window

window = tk.Tk()

window.title("ChatBot")

window.geometry("1000x1000")

# Create a text box for displaying the conversation

conversation = tk.Text(window, bd=1, bg="white", font=("Arial", 12), height="15", width="100")

conversation.pack(pady=10)

# Create an entry field for user input

entry_field = tk.Entry(window, font=("Arial", 20))

entry_field.pack(pady=10)

# Function to handle user input and display bot's response

def send_message():

user_message = entry_field.get()

conversation.insert(tk.END, "You: " + user_message + "\n")

bot_response = get_response(user_message)

conversation.insert(tk.END, "Bot: " + bot_response + "\n")

entry_field.delete(0, tk.END)

# Bind the send_message function to the Enter key

window.bind('<Return>', lambda event: send_message())

# Send button

send_button = tk.Button(window, text="Send", command=send_message)

send_button.pack()

# Function to get the bot's response

def get_response(user_input):

split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())

response = check_all_messages(split_message)

return response

# Close the Tkinter window on closing the application

window.mainloop()