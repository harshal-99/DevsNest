from questions import QUESTIONS
import random


class KBC:
    def __init__(self, questions: list):
        self.questions = questions
        self.life_lise_used = False
        self.amount_won = 0
        self.minimum_won = 0

    @staticmethod
    def welcome_message() -> None:
        """
        Print welcome message.
        """
        print(f'\t\tWelcome to kaun banenga kabadpati.')
        print(f'\t\t\tEnter quit to quit.')
        print(f'\t\t\tEnter lifeline to use life line')

    @staticmethod
    def is_correct_answer(question: dict, answer: int) -> bool:
        """
        :params question: dictionary
        :params answer: int
        :return:
            True if answer is correct.
            False if answer is incorrect
        """
        return int(question['answer']) == answer

    @staticmethod
    def lifeline(question: dict) -> list[str]:
        """
        :params question: dictionary
        :return:
            A list of 2 valid options.
        """
        options = ['option1', 'option2', 'option3', 'option4']
        final_options = []

        answer = str(question['answer'])

        option = 'option' + answer
        options.remove(option)

        final_options.append(question[option])
        final_options.append(options[random.randint(0, 3)])

        return final_options

    @staticmethod
    def get_input():
        """
        :return:
            int between 1 - 4
            quit
            lifeline
            -1 if int is not in range 1 - 5
        """
        answer = input('Your choice ( 1-4 ) : ')
        if answer.lower() == 'quit':
            return 'quit'
        elif answer.lower() == 'lifeline':
            return 'lifeline'
        elif int(answer) in range(1, 5):
            return int(answer)
        else:
            return -1

    @staticmethod
    def print_options(question) -> None:
        """
        :params question: dictionary
            print the options.
        """
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {question["option1"]}')
        print(f'\t\t\tOption 2: {question["option2"]}')
        print(f'\t\t\tOption 3: {question["option3"]}')
        print(f'\t\t\tOption 4: {question["option4"]}')

    @staticmethod
    def print_question(question, index) -> None:
        """
        prints question and options.
        """
        print(f'\tQuestion {index}: {question["name"]}')

    def validate_input(self, answer):
        """
        if answer is -1 ask for input again.
        """
        while answer == -1:
            answer = self.get_input()
        return answer

    def loop(self):
        """
        main loop to iterate over questions.
        """
        for i in range(len(self.questions)):
            if i >= 5:
                self.minimum_won += 10_000
            elif i >= 10:
                self.minimum_won += 3_20_000

            self.print_question(self.questions[i], i)
            self.print_options(self.questions[i])
            answer = self.get_input()

            self.validate_input(answer)

            if answer == 'quit':
                self.amount_won += self.minimum_won
                print("Congratulation you have won ", self.amount_won, " Rs")
                exit(0)
            # elif answer == 'lifeline':
            #     if i == 15:
            #         print("Can't use lifeline for last question.")
            #         self.print_question(self.questions[i])
            #         answer = self.validate_input(self.get_input())
            #     options = self.lifeline(self.questions[i])
            #     print(f'\t\t\tOption 1: {self.questions[i][options[0]]}')
            #     print(f'\t\t\tOption 2: {self.questions[i][options[1]]}')
            #     self.life_lise_used = True
            #     answer = self.get_input()

            if self.is_correct_answer(self.questions[i], answer):
                self.amount_won += int(self.questions[i]['money'])
                print("Correct answer")
            else:
                print("You have won ", self.minimum_won, " Rs")
                exit(0)

        print("Congratulation you have won ", self.minimum_won + self.amount_won, " Rs")

    def run(self):
        self.welcome_message()
        self.loop()


game = KBC(QUESTIONS)
game.run()
