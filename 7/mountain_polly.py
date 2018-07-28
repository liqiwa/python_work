reponses = {}
polling_active = True

while polling_active:
    name = input("\n What is your name?")
    reponse = input("Which mountain would you like to climb somdeday?")
    reponses[name] = reponse
    repeat = input("Would you like to let another person respond ?(yes / no)")
    if repeat == 'no':
  	  polling_active = False

print("\n -- Poll Results ---")
for name,reponse in reponses.items():	
   print(name+" would like to climb "+ reponse + ".")
