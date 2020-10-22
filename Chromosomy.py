from random import seed
from random import uniform 

class Individual:
    def __init__(self, No):
        self.InternalList = []
        self.No = No
    
    def append(self, Element):
        self.InternalList.append(Element)
    
    def getElement(self, ElementNo):
        return self.InternalList[ElementNo]

    def getList(self):
        return self.InternalList

    def getLength(self):
        return len(self.InternalList)
    
    def __del__(self):
        pass

def AdjustFunction(List):
    AdjustValue = 0
    for element in List:
        AdjustValue += int(element)

    return AdjustValue ** 2

def SelectionFunction(AdjustValue, SumOfAGeneration):
    x = AdjustValue * 100 / SumOfAGeneration
    if x < 5 or x > 75:
        return 0 # Individual dies
    if ( x >= 5 and x < 25 ) or ( x > 50 and x <= 75 ):
        return 1 # Individual lives but not reproduce
    if ( x >= 25 or x <= 50 ):
        return 2 # Individual reproduces

def createGeneration(lines, k, g, ActualGeneration, NumberOfLines):
    GenerationLength = 0
    SumOfAGeneration = 0

    for line in lines:
        if line[0] == "-":
            ActualGeneration += 1
            if ActualGeneration == g:
                break
        GenerationLength += 1

    i = NumberOfLines
    while i < (NumberOfLines + GenerationLength):
        TempIndividual = []
        for word in lines[i].split():
            TempIndividual.append(word)
        SumOfAGeneration += AdjustFunction(TempIndividual)
        i += 1

    ReproductionNumber = 0
    while ReproductionNumber < k:

        while True:
            IndividualToReproduce_A = Individual(int(uniform(NumberOfLines, GenerationLength + NumberOfLines)))
            for word in lines[IndividualToReproduce_A.No].split():
                IndividualToReproduce_A.append(word)
            if SelectionFunction(AdjustFunction(IndividualToReproduce_A.getList()), SumOfAGeneration) == 2:
                break
            else:
                del IndividualToReproduce_A

        while True:
            IndividualToReproduce_B = Individual(int(uniform(NumberOfLines, GenerationLength + NumberOfLines)))
            for word in lines[IndividualToReproduce_B.No].split():
                IndividualToReproduce_B.append(word)
            if SelectionFunction(AdjustFunction(IndividualToReproduce_B.getList()), SumOfAGeneration) == 2 and IndividualToReproduce_B.No != IndividualToReproduce_A.No:
                break
            else:
                del IndividualToReproduce_B

        
        NewIndividual = []
        ChromosomeCrack_A = int(uniform(0, IndividualToReproduce_A.getLength()))
        ChromosomeCrack_B = int(uniform(0, IndividualToReproduce_B.getLength()))
        
        i = 0
        while i <= ChromosomeCrack_A:
            NewIndividual.append(IndividualToReproduce_A.getElement(i))
            i += 1
        i = ChromosomeCrack_B
        while i < IndividualToReproduce_B.getLength():
            NewIndividual.append(IndividualToReproduce_B.getElement(i))
            i += 1

        f = open("Chromosomy.txt", "a", encoding = "utf-8")
        f.write("\n")
        for word in NewIndividual:
            f.write(word)
            f.write(" ")
        f.close
        ReproductionNumber += 1

    i = NumberOfLines
    while i < (NumberOfLines + GenerationLength):
        TempIndividual = []
        for word in lines[i].split():
            TempIndividual.append(word)

        if SelectionFunction(AdjustFunction(TempIndividual), SumOfAGeneration) >= 1:
            f = open("Chromosomy.txt", "a", encoding = "utf-8")
            f.write("\n")
            for word in TempIndividual:
                f.write(word)
                f.write(" ")
            f.close

        i += 1

    f = open("Chromosomy.txt", "a", encoding = "utf-8")
    f.write("\n-----------------------------------")
    f.close()

    return GenerationLength



try:
    f = open("Chromosomy.txt", "r", encoding = "utf-8")
except IOError:
    print("Irrcorect path or file does not exist!")
else:
    print("File was successfully opened\n")
    k = 2 # Number of reproductions in each generation
    g = 1 # Number of generations to create
    lines = f.readlines()
    f.close()
    ActualGeneration = 0
    NumberOfLines = 0
    NumberOfLines = NumberOfLines + createGeneration(lines, k, g, ActualGeneration, NumberOfLines) + 1

