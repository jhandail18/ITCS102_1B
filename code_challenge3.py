# ask user to input his/her name, after doing so, ask user as well his/her fare fee and if she/he is currentle a student.
# If user is a student apply 20% discount on fare. Promptly display the discounted price and calculated discount. If user is not student, promptly display a message indicating that his/her not eligible for a discount.


username = input("What is your name? ")
fare = eval(input("Fare fee: "))
isStudent = input("Are you currently a student (yes / no) ")

if isStudent == 'yes':
	discount = fare * 0.2
	#fare -= discount
	new_fare = fare - discount
	print("Hi ", username)
	print("Your discount ", discount)
	print("Your new fare ", new_fare)

else:
	print("Sorry, ", username, "You're not eligible for student discount")
	print("Your fare is ", fare)



