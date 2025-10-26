# countdown_timer.py
# Author: Your Name
# Date: October 2025
# Description: A simple countdown timer for Hacktoberfest 🎃
# Counts down from a user-defined number of seconds.

import time

def countdown(seconds):
    """
    Counts down from the given number of seconds and prints remaining time.
    """
    for i in range(seconds, 0, -1):
        print(f"⏰ Time left: {i} seconds", end="\r")
        time.sleep(1)
    print("\n🎉 Time's up!")

def main():
    print("⏳ Countdown Timer")
    try:
        seconds = int(input("Enter the number of seconds to count down: "))
        if seconds <= 0:
            print("⚠️ Please enter a positive number.")
        else:
            countdown(seconds)
    except ValueError:
        print("❌ Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
