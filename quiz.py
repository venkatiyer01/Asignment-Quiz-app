# Sample quiz data stored in memory
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

# Function to run the quiz
def run_quiz(quiz):
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

# Run the app
if __name__ == "__main__":
    print("Welcome to the Quiz App!")
    run_quiz(quiz_data)
