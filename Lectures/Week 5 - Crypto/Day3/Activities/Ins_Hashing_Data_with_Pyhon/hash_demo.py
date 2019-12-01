# Import the hashlib module
import hashlib

# Dummy data for demonstration
# The `b` prefix creates binary data
demo_data = b"this is a bytes string!"

# Create a hash generator
md5 = hashlib.md5()

# Update the generator
md5.update(demo_data)

# Generate the hexdigest
hash = md5.hexdigest()

# Print result
print(hash)