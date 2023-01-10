a=dict()
key_list=list()
def readFile():
    with open("vendingitems.txt",'r') as f:
        for line in f:
            (k,v)=line.strip().split('|')
            a[k]=int(v)
    key_list=a.keys()
    print("Items available in vending machine",key_list)
    
def vendingMachine():
    readFile()
    while True:
        item=input("Enter item name\n")
        if(item in a.keys()):
            print("Valid Item Name")
            #break
            cash=int(input("Enter money to deposit\n"))
            if(isinstance(cash,int)==False):
                print("Bad Input {}\n Try Again!".format(str(cash)))
                #continue
            else:
                if(cash>a[item]):
                    print("Thank you for your purchase.Enjoy\n")
                    print("Do not forget to collect your change,{} Rs".format(cash-a[item]))
                    break
                else:
                    print("Not enough Money to but the item\n")
                    continue
        else:
            print("Available Items are {} ,\nTry Again!".format(a.keys()))
            continue
            

vendingMachine()