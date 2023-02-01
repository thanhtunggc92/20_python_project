def add(a,b):
    anwser=a + b
    print('the anwser is :'+str(anwser))
def sub(a,b):
    anwser=float(a-b)
    print('the anwser is :'+str(anwser))
def mul(a,b):
    anwser=float(a*b)
    print('the anwser is :'+str(anwser))
def devide(a,b):
    anwser=float(a/b)
    print('the anwser is :'+str(anwser))

while True:
    print("""
    Chose the following option to calculate numbers
    a for add.
    s for subtract.
    m for multiply.
    d for devide.
    """)

    options=input('Enter your options or q for quit')
   

   
    if options=='a':
        first_num=int(input('Enter your first number'))
        second_number=int(input('Enter your second number'))
        add(first_num,second_number)
     
    elif options=='s':
        first_num=int(input('Enter your first number'))
        second_number=int(input('Enter your second number'))
        sub(first_num,second_number)
    elif options=='m':
        first_num=int(input('Enter your first number'))
        second_number=int(input('Enter your second number'))
        mul(first_num,second_number)
    elif options=='d':
        first_num=int(input('Enter your first number'))
        second_number=int(input('Enter your second number'))
        devide(first_num,second_number)
    else:
        quit()

        
    
