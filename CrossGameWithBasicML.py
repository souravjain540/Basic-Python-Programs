 
import time
import random



import json
class ML:
    file_path="./data.json"
    def UPDATE_DATA(self,data):
        decoded_data=self.GET_DATA()
        decoded_data['record'].append(data)
        self.WRITE_DATA(decoded_data=decoded_data)


    def UPDATE_FIRST_STEP(self,step):
        decoded_data=self.GET_DATA()
        decoded_data['FirstStep'][step]=decoded_data['FirstStep'][step]+1
        self.WRITE_DATA(decoded_data=decoded_data)

    def GET_DATA(self):
        decoded_data=None
        with open(self.file_path,'r') as dataSet:
            decoded_data=json.loads(dataSet.read()) 
        return(decoded_data) 

    def WRITE_DATA(self,decoded_data):
        with open(self.file_path,'w') as dataSet:
            dataSet.write(json.dumps(decoded_data))

    def FIRSTSTEP(self):
        return self.GET_DATA()["FirstStep"].index(max(self.GET_DATA()["FirstStep"]))

    def NextStep(self,Previous_Step=[]):
        if len(Previous_Step)==0:
            return (self.FIRSTSTEP())
        else:
            data=self.GET_DATA()['record']
            nextStep=False
            for i in data:
                # print(list(zip(i,Previous_Step)))
                nextStep=i
                for j,k in zip(i,Previous_Step):
                    if j['pos']!=k['pos']:
                        nextStep=False
                        continue
                if nextStep!=False:
                    nextStep=i
                    break
            
            if (nextStep!=False and nextStep[len(Previous_Step)]['id']==0 ):
                try:
                    print("Defent")
                    return(nextStep[len(Previous_Step)+1]["pos"])
                except:
                    nextStep=False
            
            if nextStep==False:
                print('Random Move')
                return("Random")
            
            # print('---1')
            print("Attack")
            # print(nextStep[len(Previous_Step)]['id'])
            return(nextStep[len(Previous_Step)]["pos"])
            
# n=[{"pos":0,'id':1},{"pos":7,'id':0},{"pos":1,'id':1},{"pos":5,'id':0},{"pos":2,'id':1}]
    
ml=ML()
# print(ML.NextStep([{"pos":0,'id':1},{"pos":7,'id':0}]))


GameArea=[[0,0,0],[0,0,0],[0,0,0]]

state=0
round=random.randint(0,1)
record=[]
def CheckIfWin(Guess):
    
    F_I=Guess//3
    S_I=(Guess-F_I*3)
    XY=GameArea[F_I][S_I]
    if (GameArea[F_I][0]==XY and GameArea[F_I][1]==XY and GameArea[F_I][2]==XY):
        return XY
    elif (GameArea[0][S_I]==XY and GameArea[1][S_I]==XY and GameArea[2][S_I]==XY):
        return XY
    
    elif (GameArea[0][0]==XY and GameArea[1][1]==XY and GameArea[2][2]==XY) or (GameArea[0][2]==XY and GameArea[1][1]==XY and GameArea[2][0]==XY):
        return XY
        
    else:
        return False

def CheckIfTie():
    for i in GameArea:
        for j in i:
            if j==0: 
                return False
    return True

def Countinue():
    global GameArea,round,record,state
    Play=input("PLay Again?(yes/no)").lower()
    if Play=='yes':
        GameArea=[[0,0,0],[0,0,0],[0,0,0]]
        round=random.randint(0,1)
        record=[]
    else:
        state=1
def drawGame():
    print('\n')
    for i in GameArea:
        arr=""
        for j in i:
            if j==0:
                arr+=" ? "
            elif j==1:
                arr+=" O "
            else:
                arr+=" X "
        print(arr)

def RandomAI():
    while True :
        Guess=random.randint(0,8)
        F_A=(Guess//3)
        S_A=(Guess-(F_A*3))
        if GameArea[F_A][S_A]==0:
            record.append({"pos":Guess})
            GameArea[F_A][S_A]=2
            return(Guess)
            break


while state==0:
    if round==0:print(" \n\n\nPOSITION \n 0  1  2 \n 3  4  5 \n 6  7  8 \n ##########START############")
    drawGame()
    Guess=None
    if round%2==0:
        print("\n######### Your Trun #########\n")
        while True:
            Guess=int(input(""))
            if Guess>8 or Guess<0:
                print("Must in 0-8")
                continue
            F_A=(Guess//3)
            S_A=(Guess-(F_A*3))
            if GameArea[F_A][S_A]==0:
                GameArea[F_A][S_A]=1
                record.append({"pos":Guess})
                break
            else:
                print("block Already used")
    else :
        print("\n######### AI Trun #########\n")
        time.sleep(random.randint(0,1))
        print('I am thinking....\n')
        time.sleep(random.randint(1,2))
        Guess=ml.NextStep(record)
        if Guess!="Random":
            F_A=(Guess//3)
            S_A=(Guess-(F_A*3))
            if GameArea[F_A][S_A]==0:
                record.append({"pos":Guess})
                GameArea[F_A][S_A]=2
            else:
                Guess= RandomAI()
        else:
            Guess=RandomAI()


    Win=CheckIfWin(Guess=Guess)
    round+=1
    if Win!=False:
        drawGame()

        new_record=[]
        if len(record)%2==0:
            index=0
            for i in record:
                if index%2==0:
                    new_record.append({"pos":i["pos"],"id":0})
                else:
                    new_record.append({"pos":i["pos"],"id":1})
                index+=1
            
        else:
            index=0
            for i in record:
                if index%2==0:
                    new_record.append({"pos":i["pos"],"id":1})
                else:
                    new_record.append({"pos":i["pos"],"id":0})
                index+=1
            ml.ML.UPDATE_FIRST_STEP(record[0]["pos"])
        ml.ML.UPDATE_DATA(new_record)




        if Win==1:print("\n######## YOU WIN! #########")
        else:print("\n######## AI WIN! #########")
        Countinue()
        

    elif CheckIfTie():
        drawGame()
        print("\n######## TIE! #########")
        Countinue()


    



    