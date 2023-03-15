


import random
import time

# List of quotes
quotes = [
    "The best way to predict the future is to invent it. - Alan Kay",
    "If you want to go fast, go alone. If you want to go far, go together. - African Proverb",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
]

# Main loop
while True:
    # Select a random quote
    quote = random.choice(quotes)
    
    # Print the quote
    print(quote)
    
    # Wait for 2 minutes

    time.sleep(10)





