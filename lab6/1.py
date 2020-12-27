correct_email = "ceng113@example.com"
user_email = input("your email: ")

user_email_lower = user_email.lower()

two_parts = user_email.split("@")
#print(two_parts)
first_part = two_parts[0].replace(".","")

email = first_part + "@" + two_parts[1]

print(email == correct_email)

