# QuizGenius
# Author: MALALATIANA Hervean Rolando
# Email: herveanrolando@gmail.com
# Version: 1.0
# Date: 02/15/2024
# Description: An interactive text-based quiz game featuring multiple categories including capitals, animals, and general knowledge.
# License: MIT License. See LICENSE.md for more information.

import random

class QuizGame:
    def __init__(self, filename):
        # Initialisation du jeu avec chargement des questions depuis un fichier texte
        self.questions = []
        self.load_questions(filename)
        self.score = 0

    def load_questions(self, filename):
        # Chargement des questions, options et réponses depuis un fichier texte
        with open(filename, 'r') as file:
            for line in file:
                question, options, answer = line.strip().split('|')
                options = options.split(',')
                random.shuffle(options)  # Mélanger les options
                self.questions.append((question, options, answer))

    def play_game(self, num_questions):
        # Méthode pour jouer au jeu avec un nombre spécifié de questions
        random.shuffle(self.questions)    # Mélange des questions pour chaque partie
        self.score = 0    # Réinitialisation du score
        for i, (question, options, answer) in enumerate(self.questions[:num_questions]):
            print(f'Question {i+1}: {question}')
            for j, option in enumerate(options):
                print(f'{j+1}. {option}')
            user_answer = input('Votre réponse (entrez le numéro de l\'option) : ')
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                if options[int(user_answer) - 1] == answer:
                    print('Bonne réponse !')
                    self.score += 1
                else:
                    print('Mauvaise réponse.')
            else:
                print('Réponse invalide.')
        print(f'Votre score final est de {self.score}/{num_questions}.')

    def replay(self):
        # Méthode pour demander au joueur s'il veut rejouer
        while True:
            replay = input('Voulez-vous rejouer ? (oui/non) : ').lower()
            if replay == 'oui':
                return True
            elif replay == 'non':
                return False
            else:
                print('Réponse invalide. Veuillez répondre par "oui" ou "non".')

def main():
    print("Bienvenue au Quiz Genius!")
    while True:
        print("Choisissez le quiz que vous souhaitez jouer :")
        print("1. Quiz sur les capitales")
        print("2. Quiz sur les animaux")
        print("3. Quiz de culture générale")
        quiz_choice = input("Entrez le numéro du quiz : ")

        if quiz_choice == '1':
            filename = 'quiz_capitales.txt'
        elif quiz_choice == '2':
            filename = 'quiz_animaux.txt'
        elif quiz_choice == '3':
            filename = 'quiz_culture_generale.txt'
        else:
            print("Choix invalide. Veuillez choisir un numéro de quiz valide.")
            continue

        quiz = QuizGame(filename)
        difficulty = None

        while difficulty not in ['1', '2', '3']:
            print('Choisissez le niveau de difficulté :')
            print('1. Facile (5 questions)')
            print('2. Moyen (10 questions)')
            print('3. Difficile (15 questions)')
            difficulty = input('Entrez votre choix : ')

            if difficulty not in ['1', '2', '3']:
                print('Choix invalide. Veuillez choisir un niveau de difficulté valide.')

        num_questions = int(difficulty) * 5
        quiz.play_game(num_questions)

        if not quiz.replay():
            print("Merci d'avoir joué au Super Quiz !")
            break


if __name__ == '__main__':
    main()
