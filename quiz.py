import random

class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, choices, correct_answer):
        self.questions.append({
            "question": question,
            "choices": choices,
            "correct_answer": correct_answer
        })

    def display_question(self, question_obj):
        question = question_obj["question"]
        choices = question_obj["choices"]
        print(question)
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")

    def get_user_answer(self, num_choices):
        while True:
            try:
                answer = int(input(f"Enter your answer (1-{num_choices}): "))
                if 1 <= answer <= num_choices:
                    return answer
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run_quiz(self):
        random.shuffle(self.questions)
        for question_obj in self.questions:
            self.display_question(question_obj)
            user_answer = self.get_user_answer(len(question_obj["choices"]))
            correct_answer = question_obj["correct_answer"]
            if user_answer == correct_answer:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong. The correct answer is: {question_obj['choices'][correct_answer - 1]}")
            print()
        self.display_final_score()

    def display_final_score(self):
        total_questions = len(self.questions)
        print(f"Quiz completed. Your score: {self.score}/{total_questions}")


if __name__ == "__main__":
    quiz = QuizGame()

    # Add your questions here
    quiz.add_question("What is the capital of France?", ["Paris", "Berlin", "Madrid"], 1)
    quiz.add_question("What is 2 + 2?", ["3", "4", "5"], 2)
    quiz.add_question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"], 1)

    quiz.run_quiz()
