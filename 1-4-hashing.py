import hashlib

# Creating a SHA-256 hashing object
hash_obj = hashlib.sha256()

# Input to be hashed
input_data = "my-passwor;lsiehg;lksh;gkljs;gkljshgo"

# Encoding the input string
encoded_data = input_data.encode()

# Updating the hash object with the encoded data
hash_obj.update(encoded_data)

# Obtaining the hashed value
hashed_data = hash_obj.hexdigest()

# Printing the hashed value
print("Hashed value:", hashed_data)