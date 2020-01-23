# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

censoring_word = "learning algorithms"

proprietary_terms = ["she", "personality matrix", "sense of self", 
"self-preservation", "learning algorithm", "her", "herself"]

def censor_words(email,censoring_word):
    if censoring_word in email:
        email = email.replace(censoring_word,"*"*len(censoring_word))
    return email

print(censor_words(email_one,censoring_word))