def grade( name, homework, assessment, exam):
    return

def checkscore(theQuestion, theLimit):
    while True:
        score = int(input(theQuestion))
        if score > theLimit:
            print("too high, re-enter")
        else:
            break
    return score
    

name = input("Name: ")

homework = checkscore( "Homework Score upto 25: ", 25 ) 
assessment = checkscore ("Assessment Score upto 50: ", 50)
exam = checkscore("Exam Score upto 100: ", 100)

tscore=(((int(homework) + int(assessment) + int(exam))/175)*100)

print(f"{name}, your Homework score is {homework}, Assessment score is {assessment}, and Exam score is {exam} with a total score off {tscore}%. ")