

# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

# Update configuration values
port = 443
is_https_enabled = False

# Print the updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")

text = "Python is awesome"
words = text.split()
print("Words:", words)

print('what is your name')
name = input('Hello, my name is ')
print('Hello, ' + name + '!')

# #concatenation example
greeting = 'Hello '
name = 'Alice'
print(greeting + name + '!')
response = input('How are you today? ')
print('its good to know you\'re ' + response)
age = input('How old are you? ')
print('You are ' + age + ' years old.   Nice to meet you, ' + name + '!')

#inbuilt functions example

# length example
Fullname = "Oluwafunmilayo Deborah Adewale-Michael"
length = len(Fullname)
print(f"Your name has {length} characters")

# case conversion example from upper to lower and lower to upper
Fullname = "Oluwafunmilayo Deborah Adewale-Michael"
uppercase = Fullname.upper()
lowercase = Fullname.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Fullname:", Fullname)

#split function example
Fullname = "Oluwafunmilayo Deborah Adewale-Michael"
see = Fullname.split()
print("Names:", see)

# replace example
Fullname = "Oluwafunmilayo Deborah Adewale-Michael"
maiden_name = Fullname.replace("Adewale-Michael", "Odu")
maiden_name = maiden_name.replace("Oluwafunmilayo", "Funmi")
print("Before I got married I was called:", maiden_name)

# stripping example - removing leading and trailing spaces
messy_name = "   Oluwafunmilayo Deborah Adewale-Michael    "
clean_name = messy_name.strip()
print("Cleaned Name:", clean_name)

# substring example
Fullname = "Oluwafunmilayo Deborah Adewale-Michael"
first_name = Fullname[0:12]
print("First Name:", first_name)

# type conversion example
# year_born = input('What year were you born? ')
# age = 2024 - int(year_born)
# print('So you are ' + str(age) + ' years old!')