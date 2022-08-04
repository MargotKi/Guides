
def withWhoWantTalk(robo, question):
    robo_int = int(robo)
    question_int = int(question)

    #   1>>> Olga:
                    #>> Que: 1
                    # >> Que: 2
                    # >> Que: 3
    #   2>>> Krzychu:
                    # >> Que: 1
                    # >> Que: 2
                    # >> Que: 3
    #   3>>> Kajtek
                    # >> Que: 1
                    # >> Que: 2
                    # >> Que: 3

    if robo_int == 1:
        return "Olga"
    #elif robo_int == 1 and question_int == 2:
        #return "Olga. Wczoraj na śniadanie jadłam placki"
   # elif robo_int == 1 and question_int == 3:
        #return "Olga. Moje imie to obelga"
    if question_int == 1:
        return "Życie ze mną to katorga :)"



    if robo_int == 2 and question_int == 1:
        return "Mateusz. Wajchę przełóż"
    elif robo_int == 2 and question_int == 2:
        return "Mateusz. Nie lubię kałuż"
    elif robo_int == 2 and question_int == 3:
        return "Mateusz. Załóż kapelusz"

    if robo_int == 3 and question_int == 1:
        return "Kajtek. Codziennie chodzę bez majtek"
    elif robo_int == 3 and question_int == 2:
        return "Kajtek. Nie jadłem dzisiaj ciastek"
    elif robo_int == 3 and question_int == 3:
        return "Kajtek. Jeszcze nie mam dziatek"

    return "Kogo tu szukasz?"

def main():

    robo = input("With who you want to talk? 1/2/3: ")
    question = input("What would you like to hear? 1/2/3: ")

    print(f"Siema, elo 320! Jestem {withWhoWantTalk(robo, question)}.")


main()






