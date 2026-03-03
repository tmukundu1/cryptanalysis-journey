import string
from collections import Counter
import matplotlib.pyplot as plt

def plot_letter_frequency(text, email_id):
    filtered_text = ''.join(ch.lower() for ch in text if ch.isalpha())
    if not filtered_text:
        print("No alphabetic characters found.")
        return
    letter_counts = Counter(filtered_text)
    letters = list(string.ascii_lowercase)
    counts = [letter_counts.get(letter, 0) for letter in letters]
    total_letters = sum(counts)
    frequencies = [(count / total_letters) for count in counts]
    plt.figure()
    plt.bar(letters, frequencies)
    plt.xlabel("Letter")
    plt.ylabel("Frequency (%)")
    plt.title(f"Email {email_id}")
    plt.show()

if __name__ == "__main__":
    emails = ['',
              '',
              '',
              '',
              '']
    for email in emails:
        plot_letter_frequency(email, email_id=emails.index(email)+1)
