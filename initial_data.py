from werkzeug.security import check_password_hash

entered_password = "1234"  # Replace this with the password entered during login
stored_hashed_password = "scrypt:32768:8:1$gwyL0byYhgrwYW74$0bc96ceb181b637d74ad74abfd8cc5423e3c8121777d91428dc112d0eb701c368da7e64236c8c9dc66fb1b44f71bbdae531a4d92e530846718c597dd7a44e17f"  # Replace this with the hashed password stored in the database

# Debugging
print(f"Entered Password: {entered_password}")
print(f"Stored Hashed Password: {stored_hashed_password}")

# Check if they match
if check_password_hash(stored_hashed_password, entered_password):
    print("Password Matched!")
else:
    print("Password Mismatch!")
