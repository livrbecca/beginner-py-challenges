# good for writing cleaner code

age = 22
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"
# ALTERNATIVE THROUGH TERNARY OPERATOR 

message = "allowed" if age >= 18 else "not allowed"

print(message)