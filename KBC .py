import random

# List of questions and their corresponding answers
questions = [
    {"question": "What is the capital of France?", "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"], "answer": "B"},
    {"question": "What is the tallest mammal?", "options": ["A. Elephant", "B. Giraffe", "C. Rhino", "D. Hippo"], "answer": "B"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"], "answer": "A"},
    {"question": "What is the chemical symbol for water?", "options": ["A. Wa", "B. Wo", "C. H2O", "D. W"], "answer": "C"},
    {"question": "Who painted the Mona Lisa?", "options": ["A. Michelangelo", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Vincent van Gogh"], "answer": "B"}
]

def kbc_game(): 
    total_amount = 0
    print("Welcome to KBC!")
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question['question']}")
        for option in question['options']:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer == question['answer']:
            print("Correct Answer!")
            total_amount += 10000  # Assuming each correct answer adds Rs. 10,000 to the total amount
        else:
            print("Wrong Answer!")
            break  # End the game if the answer is wrong
    print(f"\nYou are taking home Rs. {total_amount}!")

if __name__ == "__main__":
    kbc_game()
