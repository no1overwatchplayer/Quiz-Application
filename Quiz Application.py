class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        answer = int(input("Enter the number of your answer: ")) - 1
        if question.options[answer] == question.answer:
            score += 1
            print("Correct!")
        else:
            print("Wrong! The correct answer is:", question.answer)
    print(f"\nYou got {score} out of {len(questions)} correct.")

def main():
    questions = [
        Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Lisbon"], "Paris"),
        Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Mars"),
        Question("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific")
    ]
    run_quiz(questions)

if __name__ == "__main__":
    main()
