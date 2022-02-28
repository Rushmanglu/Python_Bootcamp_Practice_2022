bill = input("What was the total bill?: $ ")
percentage = input("What percentage of tip would you like to give? 10, 12, or 15?: ")
people = input("How many people to split the bill?: ")
bill_including_tip = int(bill) + int(percentage) * int(bill) / 100
per_person = bill_including_tip / int(people)
formatted_per_person = "{:.2f}".format(per_person)
print("Each person should pay" + " " + "$" + formatted_per_person)
