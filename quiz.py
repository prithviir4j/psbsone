import random

def quiz():
    L1=["Who is known as the 'Queen of Pop'?","a)Madonna b)Whitney Houston c)Britney Spears d)Lady Gaga",'a']
    L2=["What is the name of Coldplay's debut album?","a)X&Y b)Parachutes c)Viva la Vida or Death and All His Friends d)A Rush of Blood to the Head",'b']
    L3=["Which member of The 1975 is the lead vocalist and guitarist?","a)Ross MacDonald b)George Daniel c)Matthew Healy d)Adam Hann",'c']
    L4=["Which song by The Strokes was released as the lead single from their 2003 album Room on Fire?","a)Reptilia b)Hard to Explain c)12:51 d)Under Control",'a']
    L5=["What year was the Red Hot Chili Peppers' debut album released?","a)1986 b)1991 c)1999 d)1983",'a']
    L6=["Which Taylor Swift album features the song 'Blank Space'?",'a)Reputation b)1989 c)Red d)Lover','b']
    L7=["What is the title of Gracie Abrams’ debut EP?","a)This Is What It Feels Like b)Minor c)Good Riddance d)Call It What It Is",'a']
    L8=["Which genre is Chappell Roan primarily known for?","a)Pop b)Indie Rock c)Country d)R&B",'a']
    L9=["What is the name of Chase Atlantic’s second studio album, released in 2020?","a)Phases b)Go on Then, Love c)Beauty in Death d)Chase Atlantic 2",'c']
    L10=["Which of these songs is NOT by The Neighbourhood?","a)'You Get Me So High' b)'Stargazing' c)'Im Sorry' d)'In the Morning'",'d']
    L11=["What is the name of Travis Scott's daughter?","a)Dream b)Stormi c)North d)Chicago",'b']
    L12=["Which song by The Weeknd won a Grammy for Best R&B Performance in 2016?","a)'The Hills' b)'Earned It' c)'Starboy' d)'In the Night'",'b']
    L13=["Which of these songs is from Beach House's 2010 album Teen Dream?","a)Myth b)Zebra c)Norway d)Silver Soul",'c']
    L14=["What is the real name of the Girl in Red","a)Maren b)Emily Vu c)Sophie Hunger d)Marie Ulven",'d']
    L15=["Which Kendrick Lamar album won the Pulitzer Prize for Music in 2018?","a)Section.80 b)To Pimp a Butterfly c)good kid, m.A.A.d city d)DAMN.",'d']
    L16=["Carwash is known for his contributions to which genre of music?",'a)Jazz b)Funk c)Electronic d)Hip-Hop','c']
    L17=["Sabrina Carpenter starred in which Disney Channel show, where she played the character Maya Hart?","a)Liv and Maddie b)The Suite Life of Zack & Cody c)Girl Meets World d)Andi Mack",'c']
    L18=["Which Arctic Monkeys album features the hit single 'Do I Wanna Know?'","a)Whatever People Say I Am, That's What I'm Not b)AM c) Humbug d)Suck It and See",'b']
    L19=["Which song by Lana Del Rey includes the lyrics, 'I am your man' and 'I am your man'?","a)Blue Jeans b)Freak c)The Blackest Day d)West Coast",'d']
    L20=["Which Juice WRLD song features the line, 'I still see your shadows in my room'?","a)All Girls Are the Same b)Robbery c)Legends d)Lucid Dreams",'d']
    L = [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20]
    print ("choose your quiz format")
    choice = int(input("select how many questions quiz do you want: "))
    points = 0
    for i in range (0,choice):
        k = random.randint(0,20)
        print (L[k][0])
        print (L[k][1])
        ans = input("enter your answer:")
        if ans == L[k][2]:
            points +=1
        else:
            continue
    print ("your score is:",points,'/',choice)
quiz()
    
        


    
 


    
    
