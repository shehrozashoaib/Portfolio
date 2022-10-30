class QuestionClass:
    def __init__(self, QuestionP="", AnswerP="", DifficultyP=0):
        self.__Question = QuestionP
        self.__Answer = AnswerP
        self.__Difficulty = DifficultyP

    def GetQuestion(self):
        return self.__Question

    def GetAnswer(self):
        return self.__Answer

    def GetDifficulty(self):
        return self.__Difficulty


class QuizClass(QuestionClass):
    def __init__(self):
        self.__Questions = [[] for i in range(20)]
        self.__NumberOfQuestions = 0
        self.__QuestionOutput = 0

    def AddQuestion(self, QuestionIn, AnswerIn, DifficultyIn):
        if self.__NumberOfQuestions < 20:
            a = QuestionClass(QuestionIn, AnswerIn, DifficultyIn)
            self.__Questions[self.__NumberOfQuestions] = a
            self.__NumberOfQuestions+=1
            return True
        else:
            return False

    def GetQuestion(self):
        Q = self.__Questions[self.__QuestionOutput].GetQuestion()
        print(Q)

    def CheckAnswer(self, AnswerInput):
        Q = self.__Questions[self.__QuestionOutput].GetAnswer()
        if int(AnswerInput) == int(Q[0:len(Q)-3]):
            self.__QuestionOutput += 1
            return True
        else:
            self.__QuestionOutput += 1
            return False
  

def ReadFile():
    firstQuiz = QuizClass()
    counter = 0
    with open("QuizQuestions.txt", "r") as f:
        while True:
            lineRead = f.readline()
            if lineRead == "" or counter == 19:
                break
            else:
                lineRead2 = f.readline()
                lineRead3 = f.readline()
                firstQuiz.AddQuestion(lineRead, lineRead2, int(lineRead3))
                counter+=1
    difficulty = 0
    for i in range(20):
        firstQuiz.GetQuestion()
        if firstQuiz.CheckAnswer(int(input("Please enter response: "))):
            difficulty+=1
    print(str(difficulty))


ReadFile()
