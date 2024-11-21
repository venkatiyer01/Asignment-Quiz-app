import json
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": 0  # Index of the correct option
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 1
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Leo Tolstoy"],
        "answer": 2
    }
]
import json

# Load quiz data from file
def load_quiz_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Quiz data file not found. Please make sure 'quiz_data.json' exists.")
        return []  # Return an empty list to indicate no data
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the quiz data file.")
        return []  # Return an empty list to indicate no data

# Function to run the quiz
def run_quiz(quiz):
    if not quiz:  # Check if the quiz list is empty
        print("No quiz data available to run the quiz.")
        return
    score = 0
    for index, q in enumerate(quiz):
        print(f"Question {index + 1}: {q['question']}")
        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")
        try:
            user_answer = int(input("Enter the number of your answer: ")) - 1
            if user_answer == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {q['options'][q['answer']]}\n")
        except ValueError:
            print("Invalid input. Skipping question.\n")
    print(f"Quiz Over! Your score is {score}/{len(quiz)}.")

# Main program
if __name__ == "__main__":
    print("Welcome to the Quiz App!")
    quiz_data = load_quiz_data('quiz_data.json')
    if quiz_data:
        run_quiz(quiz_data)
    else:
        print("Exiting the app. Please fix the quiz data file and try again.")
