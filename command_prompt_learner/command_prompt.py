import json
from random import choice

save_file = 'hiragana2letter.json'
with open (save_file, encoding='utf8') as f :
    translator2letters = json.load(f)

set_sap_letter = list(translator2letters)

number_of_word = 10
number_of_quizz= 3

for i_quizz in range(number_of_quizz) :
    score = 0
    print(f'session {i_quizz}')
    for _ in range(number_of_word):
        curr_question = choice(set_sap_letter)
        print (curr_question, ' ? ', end='')
        curr_answer = input()
        if translator2letters[curr_question] == curr_answer:
            print('good answer')
            score += 1
        else :
            print('bad answer: ', translator2letters[curr_question])

        print(f'results: {score} / {number_of_word}')
        
    stop = True
    for i in range(5):
        continue_str = input ('Continue ? (y/n)')
        if continue_str == 'y' :
            stop = False
            break
        elif continue_str == 'n':
            break

    if stop:
        break