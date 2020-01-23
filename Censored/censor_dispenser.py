# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

censoring_word = "learning algorithms"

proprietary_terms = ["she", "personality matrix", "sense of self", 
"self-preservation", "learning algorithms", "her", "herself"]

def censor_words(email,proprietary_terms):
    for text in proprietary_terms:
        if text in email:
            email = email.replace(text,"*"*len(text))
    return email

print(censor_words(email_two,proprietary_terms))