from Question import Question

def main():
    try:
        player1score = 0
        player2score = 0
        questioncounter = 1
        questions = init_questions()
        for question in questions:
            print(question.get_trivia_question())
            print("Enter 1 ", question.get_answer1())
            print("Enter 2 ", question.get_answer2())
            print("Enter 3 ", question.get_answer3())
            print("Enter 4 ", question.get_answer4())
            
            if questioncounter <= 5:                 
                player1score += answer_question(1, question)
            else:                  
                player2score += answer_question(2, question)
            
            questioncounter += 1
            print('\n')
            print("Player 1's score is:", player1score)
            print("Player 2's score is:", player2score)
        if player1score > player2score:
            print("Player 1 wins.")
        elif player1score < player2score:
            print("Player 2 wins.")
        else:
            print("Tie game.")
    except ValueError as a:
        print(a)
            

def answer_question(player, question):
    if player == 1:
        answer = input('Player 1 what is your answer? ')
    else:
        answer = input('Player 2 what is your answer? ') 
    if not answer or (answer != '1' and answer != '2' and answer != '3' and answer != '4' ):
        raise ValueError("Please answer 1, 2 , 3 or 4.")
    if answer == question.get_correct_answer():
        print("Congratulations you got the correct answer ")
        return 1
    else:
        print("Sorry the correct answer is ", question.get_correct_answer())
        return 0












def init_questions():
    questions = []
    questions.append(Question('What year is it? ', '2011', '2016', '2001', '2017', '4'))
    questions.append(Question('Whose the serving president? ', 'Barrack Obama', 'Jeb Busch', 'Donald Trump', 'Ronald Regan', '3'))
    questions.append(Question('What generation iphone is out? ', 'iphone6', 'iphone7', 'iphone5', 'iphone8', '2'))
    questions.append(Question('What was the name of the gorilla killed last year? ', 'Harambe', 'Betty', 'Jow', 'Joe', '1'))
    questions.append(Question('Who is the largest youtuber on youtube? ', 'Jenna Marbles', 'Adam LZ', 'TJ Hunt', 'Pewdiepie', '4'))
    questions.append(Question('What hockey team plays out of chicago? ', 'Blackhawks', 'Bruins', 'Penguins', 'Kings', '1'))
    questions.append(Question('What time finally won a world series? ', 'Reds', 'White Sox', 'Cubs', 'Yankees', '3'))
    questions.append(Question('Who is the Ceo of Microsoft? ', 'Bill Gates', 'Steve Wozniak', 'Ronald Wayne','Steve Jobs', '1'))
    questions.append(Question('what year was the declaration of Independence signed? ', '1778', '1779', '1776', '1775', '3'))
    questions.append(Question('What is the main character in minecrafts name? ', 'Steve', 'Billy', 'Joe', 'Bob', '1'))

    return questions

main()

