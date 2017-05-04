'''
Created by: Muhammad Ali Zia
Date: May 4th, 2017
Subject: DFA for binary strings


----- SAMPLE DATA FOR CUSTOM DFA. ACCEPTS ONLY STRINGS WITH SUBSTRINGS 01

Enter Dfa data
Enter number of states: 3
Enter number of alphabets: 2
Enter number of final states: 1
Enter first state: q1
Enter final state: q2
Enter Aplhabets: 
0
1
Enter Transition Table
(q0,0)--> q1
(q0,1)--> q0
(q1,0)--> q1
(q1,1)--> q2
(q2,0)--> q2
(q2,1)--> q2



'''

class DFA():
    def __init__(self):
        self.numberOfStates='3'
        self.numberOfaplhabets='2'
        self.numberOfFinalStates='1'
        self.firstState='0'
        self.finalState='2'
        self.alphabets=['0','1']
        self.dfa=[[0 for x in range(int(self.numberOfaplhabets))] for y in range(int(self.numberOfStates))]
        self.dfa=[ ['1','0'], ['1','2'], ['2','2']]


    def setDfa(self):
        self.numberOfStates=str(input("Enter number of states: "))
        self.numberOfaplhabets=str(input("Enter number of alphabets: "))
        self.numberOfFinalStates=str(input("Enter number of final states: "))
        self.firstState=str(input("Enter first state: q"))
        self.finalState=input("Enter final state: q")

        print("Enter Aplhabets: ")
        self.alphabets=[0 for x in range(int(self.numberOfaplhabets))]
        for i in range(0, int(self.numberOfaplhabets)):
            self.alphabets[i]=input()
    
        self.dfa=[[0 for x in range(int(self.numberOfaplhabets))] for y in range(int(self.numberOfStates))]

        print("Enter Transition Table")
        for i in range(0,int(self.numberOfStates)):
            for j in range(0, int(self.numberOfaplhabets)):
                self.dfa[i][j]=input("(q"+str(i)+","+str(j)+")--> q")


    def setDfaParam(self,ns,na,nf,fs,ff,a,d):
        self.numberOfStates=ns
        self.numberOfaplhabets=na
        self.numberOfFinalStates=nf
        self.firstState=fs
        self.finalState=ff
        self.alphabets=a
        self.dfa=d



    def showTupleSet(self):
        print("===========================================")
        print("                 TUPLE SET                 ")
        print("===========================================")
        print("Aplhabets:")
        for i in range(0, int(self.numberOfaplhabets)):
            print(self.alphabets[i]),
        print("\n")

        print("States:")
        for i in range(0, int(self.numberOfStates)):
            print("q"+str(i)+" "),
        print("\n")

        print("Transitions:")
        for i in range(0,int(self.numberOfStates)):
            for j in range(0, int(self.numberOfaplhabets)):
                print("(q"+str(i)+","+str(j)+")--> q"+str(self.dfa[i][j]))

        print("\nFirst State: q0")
        print("\nFinal State: q"+str(self.finalState))
        print("\nQxE->Q\n\n")

    def passString(self):
        while True:
            x=input("Enter string: ")
            currentState=0
            for i in range(0,len(x)):
                currentState=int(self.dfa[currentState][int(x[i])])
                            
            if currentState==int(self.finalState):
                print("String "+x+" is Accepted")
            else:
                print("String "+x+" is Rejected")
            t=input("Enter x to exit or press enter to check again")
            if t=='x' or t=='X':
                break
        

if __name__ == "__main__":
    dfaObj=DFA()
    while True:
        print("================= Deterministic Finite Automaton ====================")
        print("Press 1 to create a custom dfa")
        print("Press 2 check dfa that accepts strings which contains 001")
        print("Press 3 check dfa that accepts strings which ends with 100")
        print("Press 4 check dfa that accepts strings which starts with 101")
        t=input("Press 0 to exit\n\n")
        if t=='0':
            break

        elif t=='1':
            print("Enter Dfa data")
            dfaObj.setDfa()
            dfaObj.showTupleSet()
            dfaObj.passString()
        
        elif t=='2':
            print("Dfa that accepts strings which contains 001")
            dfaObj.setDfaParam('4','2','1','0','3',['0','1'],[ ['1','0'], ['2','0'], ['2','3'], ['3','3']])
            dfaObj.showTupleSet()
            dfaObj.passString()

        elif t=='3':
            print("Dfa that accepts strings which ends with 100")
            dfaObj.setDfaParam('4','2','1','0','3',['0','1'],[ ['1','0'], ['2','1'], ['3','1'], ['0','1']])
            dfaObj.showTupleSet()
            dfaObj.passString()

        elif t=='4':
            print("Da that accepts strings which starts with 010")
            dfaObj.setDfaParam('5','2','1','0','3',['0','1'],[ ['4','1'], ['2','4'], ['4','3'], ['3','3'], ['4','4']])
            dfaObj.showTupleSet()
            dfaObj.passString()

    
    
    
