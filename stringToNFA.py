import sys

def main():
    transition = [[[0,1],[0]], [[4],[2]], [[4],[3]], [[4],[4]]]
    input1 = input("enter the string: ")
    input1 = list(input1) #copy the input1 in list because python strings are immutable and thus can't be changed directly
    for index in range(len(input1)): #parse the string of a,b in 0,1 for simplicity
        if input1[index]=='a':
            input1[index]='0' 
        else:
            input1[index]='1'

    final = "3" #set of final states = {3}
    start = 0

    trans(transition, input1, final, start)
    print("rejected")


def trans(transition, input1, final, state):
    for each in transition[state][int(input1[0])]: #check for each possibility       
        if each < 4:                              #move further only if you are at non-hypothetical state
            state = each
            if len(input1)==1:
                if (str(state) in final): #last symbol is read and current state lies in the set of final states
                    print("accepted")
                    sys.exit()
                else:
                    continue
            trans(transition, input1[1:], final, state) #input1 string for next transition is input1[i+1:]

main()