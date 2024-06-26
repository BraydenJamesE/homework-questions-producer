import random


def endProgram():
    print("You entered the wrong value. Ending the program.")
    quit() 
# end of "endProgram" function   
    
    
def expandRange(beginRange, endRange):
    rangeItems = []
    
    for i in range(int(beginRange),int(endRange) + 1):
        rangeItems.append(i)
        
    return rangeItems
# end of "expandRange" function        
        
        
def sortProblemsIntoList(problems):
    newProblems = []

    for arrayItem in problems:
        # variables
        beginNumberIndex = 0
        beginNumberIndexFound = False
        endIndex = 0
        endIndexFound = False
        rangeFound = False
        rangeIndex = 0
        unitFound = False
        
        for iterator, stringItem in enumerate(arrayItem):
            # ASSESSING THE CHARACTERS IN THE STRING
            if stringItem == ':' and not beginNumberIndexFound:
                unitFound = True
                unit = arrayItem[beginNumberIndex : iterator]
                
            elif not beginNumberIndexFound and stringItem.isnumeric() and (unitFound or ':' not in arrayItem): # Tracking beginNumberIndex
                beginNumberIndex = iterator
                beginNumberIndexFound = True
            
            elif stringItem == '-':
                rangeFound = True
                rangeIndex = iterator
                
            elif stringItem == ',' and not endIndexFound: # Tracking endIndex when comma found.
                endIndex = iterator - 1
                endIndexFound = True
                
            elif iterator == len(arrayItem) - 1 and not endIndexFound: # Tracking endIndex when length reached and no comma found.
                endIndex = iterator 
                endIndexFound = True
            
            
            # APPENDING ITEMS
            if not rangeFound and beginNumberIndexFound and endIndexFound: # appending value with no range
                # Appending the item to the newProblems list
                newProblems.append(arrayItem[beginNumberIndex : endIndex + 1]) 
                
                # resetting variables
                endIndexFound = False 
                beginNumberIndexFound = False
                
            elif rangeFound and beginNumberIndexFound and endIndexFound: # appending values with range
                # assigning the list from expandRange function to a new variable
                rangeItems = []
                rangeItems = expandRange(int(arrayItem[beginNumberIndex : rangeIndex].strip()), int(arrayItem[rangeIndex + 1 : endIndex + 1].strip()))
                
                for i in rangeItems: # looping through the range items to they can be added one-by-one
                    newProblems.append(str(i))
                    
                # resetting variables
                endIndexFound = False 
                beginNumberIndexFound = False
                rangeFound = False
                
    return newProblems
# end of "sortProblemsIntoList" function


def produceProblems(problems, uniqueProblemsDesired):
    newProblems = []
    
    if len(problems) < uniqueProblemsDesired: # if there are not enough problems to accommodate the desired length, changing the length to the max number of problems
        uniqueProblemsDesired = len(problems)
    
    i = 0 # counter for while loop
    while i < uniqueProblemsDesired:
        randomIndex = random.randint(0, len(problems) - 1)
        if problems[randomIndex] not in newProblems: # asking for only unique values  
            newProblems.append(problems[randomIndex]) # appending values at random index
            i = i + 1 # only iterating if unique value was added     
    
        # end of while loop    
         
    return newProblems
# end of "produceProblem" function


def convertFromStringToDouble(problems):
    return problems
# end of "convertFromStringToDouble" function


def printList(problemsToPrint):
    return 0
# end of "printList" function


def getInputFromUser(allProblems, problemsMarkedForReview):
    # Taking input from the user
    problemSelection = input("What database do you wish to study from? (enter 0 for review and non-review or 1 for review only): ")
    numberOfProblems = input("Please enter the number of problems you would like: ")
    
    # using the "sortProblemsIntoList" function to isolate each problem from the string
    allProblems = sortProblemsIntoList(allProblems)
    problemsMarkedForReview = sortProblemsIntoList(problemsMarkedForReview)
    
    allProblemsGreaterThanZero = len(allProblems) > 0
    problemsMarkedForReviewGreaterThanZero = len(problemsMarkedForReview) > 0
    
    
    # Producing Problems 
    if allProblemsGreaterThanZero:
            allProblemsProduced = produceProblems(allProblems, int(numberOfProblems))
        
    if problemsMarkedForReviewGreaterThanZero:
        problemsMarkedForReviewProduced = produceProblems(problemsMarkedForReview, int(numberOfProblems))
    
    
    # Printing List to User
    if problemSelection == '0': # user wants all problems
        if problemsMarkedForReviewGreaterThanZero:
            for i in problemsMarkedForReviewProduced:
                print(i , end = " ") 
        if allProblemsGreaterThanZero:
            for i in allProblemsProduced:
                print(i , end = " ")           
    
    elif problemSelection == '1': # user wants only problems marked for review
        if problemsMarkedForReviewGreaterThanZero:
            for i in problemsMarkedForReviewProduced:
                print(i , end = " ") 
        else:
            print("Sorry; there are no review problems.")
            quit()        
   
    else: 
        endProgram()
        
    
    
    
#"4.10: 470-472, 474-477, 479, 481, 484, 490-497, 499-503", "1.1: 2-11, 42-43", "1.1: 12-15, 20-21, 24-26"
# String Array of Homework Problems    
allproblems = ["4.10: 470-472, 474-477, 479, 481, 484, 490-497, 499-503", "1.1: 2-11, 42-43", "1.1: 12-15, 20-21, 24-26", "Quiz3: 1-10"]
problemsMarkedForReview = ["Quiz3: 1-10"]
newProblems = sortProblemsIntoList(allproblems)

getInputFromUser(allproblems, problemsMarkedForReview)
