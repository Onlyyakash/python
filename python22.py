name = input('Enter your name: ')
print("Kaun Banega Crorepati me aapka swagat hai",name,"jii !")
print("Aapka pehla prashna ye raha screen ke saamne")
questions = ["Bharat ki rajdhani kya hai?" , "supreme kon hai?" , "Bharat ka rashtriya phool kya hai?" , "Bharat ka rashtriya pakshi kya hai?" , "Bharat ka rashtriya jaanwar kya hai?" , "Bharat ka rashtriya geet kya hai?"]
answers = ["delhi" , "akash" , "lotus" , "peacock" , "lion" , "jan gan"]
a = 1000
b = 2000
c = 3000
d = 4000
e = 5000
f = 6000
answer1 = input(questions[0])
if answer1.lower() == answers[0]:
    print("Sahi jawab. Aapne jeete hain",a,"INR")
    answer2 = input(questions[1])
    if answer2.lower() == answers[1]:
        print("Sahi jawab. Aapne jeete hain",b,"INR")
        answer3 = input(questions[2])
        if answer3.lower() == answers[2]:
            print("Sahi jawab. Aapne jeete hain",c,"INR")
            answer4 = input(questions[3])
            if answer4.lower() == answers[3]:
                print("Sahi jawab. Aapne jeete hain",d,"INR")
                answer5 = input(questions[4])
                if answer5.lower() == answers[4]:
                    print("Sahi jawab. Aapne jeete hain",e,"INR")
                    answer6 = input(questions[5])
                    if answer6.lower() == answers[5]:
                        print("Sahi jawab. Aapne jeete hain",f,"INR")
                    else:
                        print("Galat jawab, aapka ghar ka kharch hai",e,"INR")
                else:
                    print("Galat jawab, aapka ghar ka kharch hai",d,"INR")
            else:
                print("Galat jawab, aapka ghar ka kharch hai",c,"INR")
        else:
            print("Galat jawab, aapka ghar ka kharch hai",b,"INR")
    else:
        print("Galat jawab, aapka ghar ka kharch hai",a,"INR")