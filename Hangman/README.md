# 🪓 Hangman Game (CLI Version)

A simple **command-line Hangman game** written in Python.  
Guess the hidden word one letter at a time — but be careful!  
Each wrong guess costs you a life, and the ASCII art hangman will get closer to completion 😬.

---

## 🎮 How the Game Works

- The program randomly picks a word from a list (defined in `words.py`).
- You’ll see blank spaces representing each letter in the word.
- Type one letter at a time to guess.
- For every incorrect guess, you **lose a life** and the ASCII art (from `arts.py`) updates to show your progress — or your downfall!
- If you guess all the letters correctly, you win.
- If you run out of lives, it’s **Game Over** — the full hangman appears and the correct word is revealed.

---

## 🧩 Project Structure

hangman/
│
├── game.py # Main game logic and user interaction
├── words.py # Contains the list of possible words
├── arts.py # Stores the ASCII art for the hangman and logo
└── README.md # Project documentation (this file)

---

## 🚀 How to Run the Game

1. **Clone or download** this repository.

   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
   python3 game.py