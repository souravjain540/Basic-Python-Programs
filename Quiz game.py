def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    
print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
ans = input("Are you ready to play (yes/no): ")
a ="Note: wrtie answers! do not write option."
score = 0
total_questions = 4

correct_ans =["python", "steve jobs", "artificial intelligence", "bitcoin"]

if ans.lower() == "yes":
    print(a)
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java" )
    ans=input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- Who is the Founder of Apple Inc? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is more better among these? ")
    give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is the best Investment? ")
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    ans = input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
Code language: PHP (php)
Now as we are done with the questions it’s time to show the scores to the user. I will multiply the score with 10 and then I will pass the if-else conditionals to print the status of the result of this Quiz game:

i = score*10
if i &lt; 30:
    print("Ouch, your score is ",i,"/ 40 better luck next time.")
elif i ==30:
    print("Nice! you scored ",i,"/ 40 you are quiet smart.")
else:
    print("Congratulations! it's a perfect ",i,"/ 40 you are Intelligent.")
    
# Coded with 💙 by Mr. Unity Buddy
