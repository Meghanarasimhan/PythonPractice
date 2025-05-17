from loguru import logger



labourName=["mahesh","ramesh", "Mithilesh", "Sumesh"]

for name in labourName:
    logger.info(f"Labour {name}")

for i in range(len(labourName)):
    logger.info(f"Labour {i+1} name is {labourName[i]}")

# Printing * like triangle
for i in range(5,0,-1):
    logger.info(i * " *")



#Printing even numbers
for i in range(101):
    if(i!=0):
        if(i%2==0):
            logger.info(i)

# Counting the in a paragraph
count=0
paragraph="Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the data warehouse and business intelligence industry’s thought leader on the dimensional approach. He has educated tens of thousands of IT professionals. The Toolkit books written by Ralph and his colleagues have been the industry’s best sellers since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph coinvented the Star workstation, the fi rst commercial product with windows, icons, and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in electrical engineering from Stanford University"
paragraph=paragraph.lower()
paragraph=paragraph.split(" ")
for i in paragraph:
    if i== "the":
        count+=1
    else:
        continue
logger.info(count)

#Insert number in a sorted list- without using build in functions
index=0
lst=[5,18,77,108,930]
for number in lst:
    if number>100:
        index=index
        break
    else:
        index+=1
# lst.insert(index,100)
# logger.info(lst)
lst.append(0)
for i in range(len(lst)-1,index,-1):
    lst[i]=lst[i-1]

lst[index]=100
logger.info(lst)

#Simple phone like calculator
def phone_calculator():
    logger.info("Welcome to phone calculator")

    result=None
    currentOperator=None
    while True:
        userInput=input("Enter your choice Number/operator (= to evaluate, C to clear): ").strip()

        if userInput=="C":
            result=None
            currentOperator=None
            logger.info(f"calculator is cleared")
            continue

        if userInput=="=":
            if result is None:
                logger.info("Please enter first number")
                continue
            logger.info(f"result is {result}")
            result=None
            currentOperator=None
            continue

        if userInput in ["+", "-", "*", "/"]:
            if result is None:
                logger.info("Please enter first number")
                continue
            else:
                currentOperator=userInput
                continue
        elif userInput.replace(".", "",1).isdigit():
            number=float(userInput)

            if result is None:
                result=number
                continue
            elif currentOperator:
                if currentOperator=="+":
                    result+=number
                elif currentOperator=="-":
                    result-=number
                elif currentOperator=="*":
                    result*=number
                elif currentOperator=="/":
                    if number==0:
                        logger.info("Can not divide by zero")
                        result=None
                        currentOperator=None
                        continue

                    result/=number
                currentOperator=None
            else:
                logger.info("Please enter operator")
        else:
            logger.info("Invalid input")

phone_calculator()







