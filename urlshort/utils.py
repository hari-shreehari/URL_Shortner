import random
import string
def generate_short_url():
    """
    Generate a random short URL using alphanumeric characters.
    You can customize the length and characters used as needed.
    """
    # Define the characters to choose from for the short URL
    characters = string.ascii_letters + string.digits # Alphanumeric characters
    # Set the desired length of the short URL
    short_url_length = 6 # You can adjust this to your preference
    # Generate a random short URL
    short_url = ''.join(random.choice(characters) for _ in range(short_url_length))
    return short_url
