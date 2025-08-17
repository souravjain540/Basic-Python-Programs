import time     # Used to measure how long the user takes
import random   # Used to pick a random sentence

# A list of sentences that the player will be asked to type
SENTENCES = [
    "The quick brown fox jumps over the lazy dog",
    "Python makes programming fun and easy to learn",
    "Artificial intelligence is shaping the future",
    "Typing fast requires focus and practice",
    "Simple games help beginners understand coding"
]

def typing_speed_test():
    print("\nWelcome to the Typing Speed Test!")
    print("You will be given a sentence to type.")
    print("Your speed and accuracy will be measured.\n")
    
    # Step 1: Pick a random sentence from the list
    sentence = random.choice(SENTENCES)
    print("Type this sentence exactly as shown:\n")
    print(f"👉 {sentence}\n")

    # Step 2: Wait for the user to be ready
    input("Press Enter when you are ready to start...")

    # Step 3: Give a short countdown so the player is prepared
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)  # Wait 1 second before counting down again

    print("\nGo!\n")
    print(f"Type this sentence:\n👉 {sentence}\n")

    # Step 4: Start the timer just before taking user input
    start_time = time.time()
    user_input = input("Start typing here:\n")
    end_time = time.time()

    # Step 5: Calculate how long it took
    elapsed_time = end_time - start_time

    # Step 6: Calculate Words Per Minute (WPM)
    # Formula: (number of words typed / time in seconds) * 60
    words = len(user_input.split())
    wpm = (words / elapsed_time) * 60 if elapsed_time > 0 else 0

    # Step 7: Calculate accuracy
    # Compare each character typed with the original sentence
    correct_chars = sum(
        1 for i, c in enumerate(user_input) 
        if i < len(sentence) and c == sentence[i]
    )
    accuracy = (correct_chars / len(sentence)) * 100

    # Step 8: Show the results
    print("\n--- Results ---")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the game
if __name__ == "__main__":
    typing_speed_test()
