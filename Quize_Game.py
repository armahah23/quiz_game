questions = [
    {
        "prompt": "1. What is the capital of Italy?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Delhi"],
        "answer": "C"
    },
    {
        "prompt": "2. What is the capital of Brazil?",
        "options": ["A. Rio de Janeiro", "B. São Paulo", "C. Brasília", "D. Brazil"],
        "answer": "C"
    },
    {
        "prompt": "3. What is the capital of China?",
        "options": ["A. Shanghai", "B. Hong Kong", "C. Beijing", "D. China"],
        "answer": "C"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])  # ✅ fixed
        for option in question["options"]:
            print(option)
        print()
        answer = input("Enter your answer: ")
        if answer == question["answer"]:
            print("Your answer was correct.\n")
            score+=1
        else:
            print("Your answer was incorrect.\n")
    print(f"Your score was {score} out of {len(questions)} answers correct: ")

run_quiz(questions)
