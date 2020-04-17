# Sort an email list
# Scott Fox
# 4/16/2020


# List of the Email Adresses
email = ['soucymi@hotmail.com', 'soud53af@rogers.com', 'souderbunch@earthlink.net', 'souellette4@yahoo.com', 'michael426@earthlink.net', 'michael_baker@juno.com', 'michael_and_robin@yahoo.com', 
'souellette4@yahoo.com','rjeffreybaker@hotmail.com', 'soph_clement@hotmail.com','sophack1@yahoo.com', 'sophat43@yahoo.com', 'soucymi@hotmail.com', 'soud53af@rogers.com', 'souderbunch@earthlink.net',
'souellette4@yahoo.com', 'soufiane_piaggio@yahoo.com', 'soufirjclaude@aol.com', 'soufsidexiii@yahoo.com', 'souhail21@excite.com', 'stevekhan@aol.com', 'pltt_green@yahoo.com', 'plattem@yahoo.com', 
'platti999@yahoo.ca', 'player_platano_93@hotmail.com''plangebb13@excite.com', 'plangill@rogers.com', 'pcv8335@peoplepc.com']

# sort the emails
email.sort()

# list = Add's a space in sorted list
email.sort(key=lambda x: x.count(' '), reverse=True)

# print emails
print('Sorted Email Adresses:', email)

# Shuffles the email list
import random
new_list = email[:]
random.shuffle(new_list)
print("Shuffled Email Adresses:", new_list)