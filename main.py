import random
import string

def generate_password(length):
  """Generates a random password of the specified length."""

  # Define characters to use in the password
  letters_and_digits = string.ascii_letters + string.digits

  # Generate the password
  password = ''.join(random.choice(letters_and_digits) for _ in range(length))

  return password

# Get the desired password length from the user
password_length = int(input("How long do you want your password to be? "))

# Generate and print the password
password = generate_password(password_length)
print("Your password is:", password)
