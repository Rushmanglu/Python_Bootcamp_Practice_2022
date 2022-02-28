print("Hi future drill artist")

city = input("Which city did you grow up in?: ")
pet = (input("Do you own a pet?(Reply with Yes or leave blank): "))
bool(pet)

if bool(pet) == True:
  pet_name = input("Which pet do you own?: ")
  print("Your band name can be"+" "+ city + " " + pet_name)
else:
  school_name = input("Okay. Which school did you go to?: ")
  print("Your band name can be" + " " + city + " " + school_name)
