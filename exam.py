class Question:
    def __init__(self, question, option1, option2, option3, option4, answer):
        self.question = question
        self.options = [option1, option2, option3, option4]
        self.answer = answer


class OnlineExam:
    def __init__(self):
        self.questions = []
        self.results = {}

    def add_question(self, question, o1, o2, o3, o4, answer):
        q = Question(question, o1, o2, o3, o4, answer)
        self.questions.append(q)

    def start_exam(self, student_name):
        score = 0
        print("\nStarting Exam for", student_name)

        for q in self.questions:
            print("\n", q.question)
            for i, option in enumerate(q.options):
                print(i+1, ".", option)

            user_answer = int(input("Enter option number: "))

            if user_answer == q.answer:
                score += 1

        self.results[student_name] = score
        print("\nExam Completed!")

    def show_results(self):
        print("\nResult Report")
        for student, score in self.results.items():
            print(student, "scored", score, "out of", len(self.questions))



exam = OnlineExam()

exam.add_question(
    "What is the capital of India?",
    "Mumbai", "Delhi", "Kolkata", "Chennai", 2
)

exam.add_question(
    "Which language is used for AI/ML?",
    "Python", "HTML", "CSS", "C", 1
)

exam.start_exam("Student1")

exam.show_results()