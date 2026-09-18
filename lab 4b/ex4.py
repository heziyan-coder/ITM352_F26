# phrase through the portions of an eamil address and print out the username and domain name
# name: Ziyan He
# date: 9/18/2026

# mothed 1: using splits()
email_address = input("enter an email address:")
parts = email_address.split("@")
username = parts[0]
domain_name = parts[1]

print("parts of the email address:", parts )
print("username:",username)
print("domain name:", domain_name)

#mothed2 2: using index and slicing
at_sign_index = email_address.index("@")
username2 =email_address[:at_sign_index]
domain_name2 = email_address[at_sign_index +1:]

print("username (method 2):", username)
print("domain name (method 2):", domain_name2)

