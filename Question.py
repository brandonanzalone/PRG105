class Question:
    def __init__(self, trivia_question, answer1, answer2, answer3, answer4, correct_answer):
        self.__trivia_question = trivia_question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct_answer = correct_answer
    
    def get_trivia_question(self):
        return self.__trivia_question
    def set_trivia_question(self, trivia_question):
        self.__trivia_question = trivia_question

    def get_answer1(self):
        return self.__answer1
    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def get_answer2(self):
        return self.__answer2
    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def get_answer3(self):
        return self.__answer3
    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def get_answer4(self):
        return self.__answer4
    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def get_correct_answer(self):
        return self.__correct_answer
    def set_correct_answer(self, correct_answer):
        self.__correct_answer = correct_answer


