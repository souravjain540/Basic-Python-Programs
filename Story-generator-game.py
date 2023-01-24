import time
import random
from string import ascii_lowercase

print('This is a game where you guess the randomly chosen word and if you win, you get a randomly generated short story !')
print('Enjoy !!')
print('\n')

time.sleep(4)

name=input('Player Name :- ')
print('\n')
print('Welcome ' + name + '. Let''s play Hangman')
print('')

time.sleep(1)

friends=['Chandler','Joey','Monica','Rachel','Ross','Phoebe','Gunther','Janice','Ugly Naked Guy','Mr Heckles','Judy','Jack']
ramaayan=['Shri Ram','Sita maa','Lakshman','Bharat','Raavan','Hanuman','Maarich','Dashrath','Kaikeyi','King Janak','KumbhKarn','Baali']
Got=['Theon','Danaerys','Jon Snow','Joeffry','Cersie','Tyrion','Drogon','Baratheon','Starks','Greyjoy','Viserys']

print('Choose Category :- ')
choose=int(input('1. F.R.I.E.N.D.S   2. Game Of Thrones   3. Ramaayan   '))
if choose==1:
    word=random.choice(friends)
elif choose==2:
    word=random.choice(Got)
elif choose==3:
    word=random.choice(ramaayan)

print('HINT : Starts with' + word[0])
print('\n')
print("Start guessing...")
time.sleep(0.5)
guess=''
turn=10

while turn>0:
    fail=0
    for c in word:
        if c in guess:
            print(c)
        else:
            print('_')
            fail+=1
    if fail==0:
        print('You Won ' + name + ' !')
        print('\n')
        print('Here is your story - ')
        theme=random.choice(["real world","high fantasy","space sci-fi","alt-history","cyberpunk"])
        if theme == "real world":
            subsetting=random.choice(["the Ayodhya","Kishkindha","Lanka","Panchvati","Janakpuri"])
            setting=random.choice(["a small town in ","a big city in ","a farm in ","a school in ","the ocean","the entire world"])
            if setting != "the ocean" or "the entire world":
                setting=setting+subsetting
            age=random.choice(["newborn ","toddler ","child ","teenager ","young adult ","adult ","middle aged ","elder "])
            race=random.choice(["ayodhyan ","janakis ","lankan ","indian "])
            gengender=random.randint(0,100)
            if gengender <= 10:
                 gender = ("transgender ")
            if gengender >= 9:
                 if gengender >= 47:
                     gender = ("male ")
                 if gengender <= 46:
                     gender = ("female ")
            protagonist=age+race+gender
            antagonist=random.choice(["a female","a male","a king","a government","a tragic event","traffic","religion","a disease","a rival","the law","an old friend","a dog"])
        if theme == "high fantasy":
            setting=random.choice(["The Great Empire","a vast desert","a dark corrupted land","a magic swamp","a unending labryinth","floating islands","a mystical forest","a frozen wasteland","a dangerous jungle land"])
            gender=random.choice(["male ","male ","male ","female ","female ","female ","magical transgender ","agender ","third gender "])
            race=random.choice(["human ","human ","elf ","orc ","dwarf ","gnome ","demon ","angel ","kitsune ","dark elf ","troll ","unicorn "])
            classs=random.choice(["marksmen ","warrior ","wizard ","bard ","thief ","merchant","knight ","spellsword ","peasant ","necromancer ","preist ","bandit ","monarch"])
            protagonist = gender+race+classs
            antagonist=random.choice(["a female","a male","an entire race","a god","an evil mage","an order of knights","evil itself","a giant","an invading army","a tyrant","magic","a greedy merchant","a monster","a dragon"])
        if theme == "space sci-fi":
            setting=random.choice(["the deep void of space","an asteroid belt","an ice planet","a lava planet","a gas giant","an alien home world","future Earth","another galaxy, far far away","the multiverse"])
            protagonist=random.choice(["human","robot","hive mind","alien","alien","blob","human"])
            antagonist=random.choice(["a female","a male","an entire alien race","a starfleet","an alien","an artifical intellgence","a galactic federation","a glitch in space-time","an invading army","a incredibly infectious space fungus","the limits of science","a robot"])
        if theme == "alt-history":
            setting=random.choice(["America","Religion","the Classical Era","the Middle Ages","the Renaissance","the Industrial Era","World War I","World War II","the Modern Era"])
            if setting == "America":
                figures=["Abraham Lincoln","George W. Bush Jr.","Benjamin Franklin","Donald Trump","Ronald Reagan","John Adams","Hilary Clinton","King George III","King George Washington","Andrew Jackson","Thomas Edison","Steve Jobs"]
                figure=random.choice(figures)
                antagonist=random.choice(figures)
            if setting == "Religion":
                figure=random.choice(["Jesus","Muhammad","Buddha","Krishna","Moses","L. Ron Hubbard","Joseph Smith","Zeus","Ra","Thor"])
                antagonist=random.choice(["Christianity","Islam","Hinduism","Buddhism","Greek mythology","Scientology","the Mormons","Paganism","Heresies"])
            if setting == "the Classical Era":
                figures=["Alexander The Great","Julius Caesar","Aristotle","King Tut","Qin Shi Huang","Homer","Augustus","Plato","Cleopatra","Ashoka","Attila the Hun","Leonidas"]
                figure=random.choice(figures)
                antagonist=random.choice(figures)
            if setting == "the Middle Ages":
                figures=["Charlemagne","Ghenghis Khan","Saladin","William the Conqueror","Ragnar Lodbrok","Oda Nobunaga","King Richard III","William Wallace","El Cid","Eleanor of Aquitaine","Erik the Red","Vlad the Impaler"]
                figure=random.choice(figures)
                antagonist=random.choice(figures)
            if setting == "the Renaissance":
                figures=["Marco Polo","Joan of Arc","Christopher Columbus","Blackbeard","Leonardo da Vinci","William Shakespeare","Henry VIII","Michelangelo","Donatello","Galileo","Admiral Yi Sun-sin","Suleiman the Magnificent"]
                figure=random.choice(figures)
                antagonist=random.choice(figures)
            if setting == "the Industrial Era":
                figures=["Henry Ford","Karl Marx","Charles Dickens","John D. Rockefeller","Thomas Edison","Nikola Tesla","Amelia Earheart","Frank C. Mars","Albert Einstein","Napoleon","Ghandi","Mark Twain"]
                figure=random.choice(figures)
                antagonist=random.choice(figures)
            if setting == "World War I":
                figure=random.choice(["Woodrow Wilson","Winston Churchill","Tsar Nicholas II","Lenin","Paul von Hindenburg","Ataturk"])
                antagonist=random.choice(["the Ottoman Empire","Germany","the United States","Britain","Austria-Hungary","France"])
            if setting == "World War II":
                figure=random.choice(["Hitler","Queen Elizabeth","Franklin D. Roosevelt","Joseph Stalin","Harry Truman","General Hideki Tojo"])
                antagonist=random.choice(["the United States","Germany","the Soviet Union","the United Kingdom","Japan","Italy"])
            if setting == "the Modern Era":
                figures=["Obama","Putin","Kim Jong-un","Kanye West","Bill Gates","Guido van Rossum","The Beatles","ISIS","Pope Francis","Mike Tyson","Pewdiepie","Hilary Cliton"]
                figure=random.choice(figures)
                antagonist=random.choice(figures)
            afigure=("figure known as ")     
            protagonist= afigure+figure     
        if theme == "cyberpunk":
            setting=random.choice(["high-tech Tokyo","New New York","a dystopia","a utopia","a computer simulation","the SuperWeb","Mega Silicon Valley","an underwater city","an extensive underground facility"])
            gender=random.choice(["male ","male ","female ","female ","robogender ","unigender ","agender ","mega genderfluid ","third gender "])
            classs=random.choice(["hacker","cyborg","DJ","technopath","engineer","bomber","corporate","street rat","anarchist"])
            protagonist=gender+classs
            antagonist=random.choice(["a large corporation","an evil AI","Python","a gang","a secret society","a new technology","robots","internet trolls","the most powerful cyborg"])
        conflict=random.choice(["fell in love with ","fought against ","attempted to stop ","defended against ","tried to befriend ","explored with ","tried to evade ","competed with ","exceeded beyond ","sought revenge against "])
        end=random.choice(["It did not end well.","It ended very well.","Died tragically.","Lived happily ever after.","It ended sadly.","It was glorious.","In the end, nothing changed.","It ended with a twist.","Gave up."])
        print("In the",theme,"setting of",setting,", there was a", protagonist, "who",conflict,antagonist,".",end)

        break


        
    guesses=input('Guess a character :- ')
    guess=guess+guesses
    if guesses not in word:
        turn-=1
        print('Wrong. You have ' + str(turn) + ' more guesses.')
        if turn==0:
            print('You lose ! The word was ' + word + '. Sorry, you don''t get the story.')
            print('\n')
            print('Write your story on your own.')
#Winstoryhangman
