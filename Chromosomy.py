from random import randint
from random import uniform 

class Individual:
    def __init__(self, No):
        self.InternalList = []
        self.No = No
    
    def getNo(self):
        return self.No

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

def SelectionFunction(AdjustValue, AverageOfAGeneration):
    x = AdjustValue * 100 / AverageOfAGeneration
    if x < 50:
        return 0 # Individual dies
    if ( x >= 50 and x < 95 ):
        return 1 # Individual lives but not reproduce
    if ( x >= 95 ):
        return 2 # Individual reproduces

def createGeneration(lines, k, NumberOfLines):
    GenerationLength = 0
    SumOfAGeneration = 0
    AverageOfAGeneration = 0
    
    Gen = 0
    for line in reversed(lines):
        if line[0] == "-":
            Gen += 1
            if Gen == 2:
                break
            else:
                GenerationLength = 0
        GenerationLength += 1
    GenerationLength -= 1

    i = NumberOfLines - GenerationLength
    
    while i < (NumberOfLines - 1):
        TempIndividual = []
        for word in lines[i].split():
            TempIndividual.append(word)
        SumOfAGeneration += AdjustFunction(TempIndividual)
        i += 1
    AverageOfAGeneration = SumOfAGeneration / GenerationLength
    ReproductionNumber = 0

    while ReproductionNumber < k:

        while True:
            IndividualToReproduce_A = Individual(randint(NumberOfLines - GenerationLength, NumberOfLines - 2))

            for word in lines[IndividualToReproduce_A.getNo()].split():
                IndividualToReproduce_A.append(word)
            if SelectionFunction(AdjustFunction(IndividualToReproduce_A.getList()), AverageOfAGeneration) == 2:
                break
            else:
                del IndividualToReproduce_A
        
        while True:
            IndividualToReproduce_B = Individual(randint(NumberOfLines - GenerationLength, NumberOfLines - 2))
            
            for word in lines[IndividualToReproduce_B.getNo()].split():
                IndividualToReproduce_B.append(word)
            if SelectionFunction(AdjustFunction(IndividualToReproduce_B.getList()), AverageOfAGeneration) == 2 and IndividualToReproduce_B.No != IndividualToReproduce_A.No:
                break
            else:
                del IndividualToReproduce_B

        
        NewIndividual = []
        ChromosomeCrack_A = randint(0, IndividualToReproduce_A.getLength() - 1)
        ChromosomeCrack_B = randint(0, IndividualToReproduce_B.getLength() - 1)
        
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

    NewGenerationLength = k
    i = NumberOfLines - GenerationLength - 1
    while i < (NumberOfLines - 1):
        TempIndividual = []
        for word in lines[i].split():
            TempIndividual.append(word)

        if SelectionFunction(AdjustFunction(TempIndividual), AverageOfAGeneration) >= 1:
            f = open("Chromosomy.txt", "a", encoding = "utf-8")
            f.write("\n")
            for word in TempIndividual:
                f.write(word)
                f.write(" ")
            f.close
            NewGenerationLength += 1

        i += 1

    f = open("Chromosomy.txt", "a", encoding = "utf-8")
    f.write("\n-----------------------------------")
    f.close()
    return NewGenerationLength

k = 2 # Number of reproductions in each generation
# Each time programm is run a new generation is created

try:
    f = open("Chromosomy.txt", "r", encoding = "utf-8")
except IOError:
    print("Irrcorect path or file does not exist!")
else:
    print("File was successfully opened")

    lines = f.readlines()
    f.close()
    createGeneration(lines, k, len(lines))