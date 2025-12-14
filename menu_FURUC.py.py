import os
os.system("cls")

print("Welcome to the Main Menu")
name = input("What's your name? ")
os.system("cls")
greet = input(f"Hi {name}, Do you want to start the program? (Yes/No) ").lower()

if greet == "yes":
    os.system("cls")
    while True:
        print("\n""+++++++++++++++++++++++++++++++++++++++++++++\n\t\t""- MAIN MENU -")
        print("\n\t1. PRINTING""\n\t2. VARIABLES""\n\t3. OPERATORS""\n\t4. CONDITIONAL STATEMENT""\n\t5. LOOPS""\n\t6. LIST""\n\t7. FUNCTIONS""\n\t0. EXIT")
        print("+++++++++++++++++++++++++++++++++++++++++++++")

        option = input("Select from the option above. ")
        
        if option == "1":
            os.system("cls")
            while True:
                print("\t\t- PRINTING -")
                print("\n• Printing in Python is the process of displaying information to the user.")
                print("  We use the print() function to show messages, results, or values on the screen.")
                print("\n""********************************************\n\t\t""- SUB MENU -")
                print('\n\t1. BASIC PRINTING')
                print('\t2. PRINT WITH CONCATENATION.')
                print('\t3. PRINT WITH F-STRING.')
                print('\t0. BACK TO MAIN MENU.')   
                print("********************************************")

                option1 = input('Enter the option you want to proceed with --> ')
                
                if option1 == "1":
                    os.system("cls")
                    print("\n• Basic printing means using the print() function to display text or messages on the screen.")
                    print("\n********************************************")

                    print("\n\tINPUT:")
                    print('\t\tprint("Welcome to Python.")')
                    print('\t\tprint("Hello World.")')
                    print('\t\tprint("Hello my friend.")')
                    print('\t\tprint("Thank You.")')
                    print('\t\tprint("Welcome.")')

                    print("\n\tOUTPUT:")
                    print("\t\tWelcome to Python.")
                    print("\t\tHello World.")
                    print("\t\tHello my friend.")
                    print("\t\tThank You.")
                    print("\t\tWelcome.")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option1 == "2":
                    os.system("cls")
                    print("\n• Concatenation means joining strings together using the + operator before printing.")
                    print("\n********************************************")

                    print("\n\tINPUT:")
                    print('\t\tfirst_name = Jhandail\n\t\tprint("I am" + first_name)\n')
                    print('\t\tmiddle_name = Perdigones\n\t\tprint("My Middle Name is" + middle_name)\n')
                    print('\t\tsurname = Furuc\n\t\tprint("My Surname is" + surname)\n')
                    print('\t\thobby = Instruments\n\t\tprint("My Hobby is" + hobby)\n')
                    print('\t\twhat = Performer\n\t\tprint("I am" + what)\n')

                    print("\n\tOUTPUT:")
                    print("\t\tI am Jhandail")
                    print("\t\tMy Middle Name is Perdigones")
                    print("\t\tMy Surname is Furuc")
                    print("\t\tMy Hobby is Instruments")
                    print("\t\tI am Performer")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                    
                elif option1 == "3":
                    os.system("cls")
                    print("\n• In Python, an f-string (formatted string literal) is a string that lets you embed Python expressions directly inside the string by using {}.")
                    print("  It is one of the most convenient and efficient ways to format strings.")
                    print("  An f-string is a string literal prefixed with f or F that evaluates expressions inside curly braces at runtime.")
                    print("\n********************************************")

                    print("\n\tINPUT:")
                    print('\t\tguitar = Jhandail\n\t\tprint(f"Lead Guitarist is {guitar}")\n')
                    print('\t\tbass = Charcey\n\t\tprint("Bassist is {bass}")\n')
                    print('\t\tkeyboard = Iya\n\t\tprint("Keyboard is {keyboard}")\n')
                    print('\t\tdrummer = Lex\n\t\tprint("Drummer is {drummer}")\n')
                    print('\t\tvocal = Monica\n\t\tprint("Vocalist is {vocal}")\n')
                    
                    print("\n\tOUTPUT:")
                    print("\t\tLead Guitarist is Jhandail")
                    print("\t\tBassist is Charcey")
                    print("\t\tKeyboard is Iya")
                    print("\t\tDrummer is Lex")
                    print("\t\tVocalist is Monica")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                    
                elif option1 == "0":
                    os.system("cls")
                    break
                    
                else:
                    os.system("cls")
                    print("Invalid Input")
                
                
        if option == "2":
            os.system("cls")
            while True:
                os.system("cls")
                print("\t\t- VARIABLE -")
                print("\n• A variable is a name that stores a value in the computer’s memory so you can use or change it later.")
                print("\n""********************************************\n\t\t""- SUB MENU -")
                print('\n\t1. PLUS AND CONCATENATION.')
                print('\t2. INPUT OF CODES.')
                print('\t0. BACK TO MAIN MENU.')   
                print("********************************************")
                
                option2 = input('Enter the option you want to proceed with --> ')
                
                if option2 == "1":
                    os.system("cls")
                    print("\n• In Python, the + operator serves two different purposes depending on the type of the operands.")
                    print("  When applied to numbers, it performs addition, combining the numerical values.")
                    print("\n**********************************************")

                    print("\t. EXAMPLE OF PLUS & CONCATENATION.")
                    num1 = int(input("\n\tEnter any number: "))
                    num2 = int(input("\tEnter any number: "))
                    sum = num1 + num2
                    print(f"\n\tAnswer = {sum}")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                    
                    
                elif option2 == "2":
                    os.system("cls")
                    print("\nHere's the INPUT:")
                    print("\n********************************************")
                    
                    print("\n\tINPUT:")
                    print('\t\tnum1 = int(input("Enter any number --> "))')
                    print('\t\tnum2 = int(input("Enter any number --> "))')
                    print('\t\tsum = num1 + num2')
                    print('\t\tprint(f"Answer: {sum}")')
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option2 == "0":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("INVALID INPUT.")
                    
        if option == "3":
            os.system("cls")
            while True:
                print("\t\t- OPERATOR -")
                print("\n• An operator in Python is a special symbol or keyword used to perform an operation on values or variables..")
                print("• Operators tell Python what action to perform such as adding numbers, comparing values, or combining logical conditions.")
                print("\n""********************************************\n\t\t""- SUB MENU -")
                print('\n\t1. DEFINITION')
                print('\t2. EXAMPLE')
                print('\t0. BACK TO MAIN MENU.')   
                print("********************************************")
                
                option3 = input('Enter the option you want to proceed with --> ')

                if option3 == "1":
                    os.system("cls")
                    print("\nDEFINITION:")
                    print("\n• An operator in Python is a symbol or a keyword that tells the interpreter to perform a specific operation on one or more values (called operands).")
                    print("  Operators define how data is processed, manipulated, or compared inside a program.")
                    print("They allow Python to perform mathematical calculations, make decisions, evaluate relationships, combine logical expressions, and modify variable values.")

                    print("\n\t• Every operator performs a well-defined task such as:")
                    
                    print("\t\t- ARITHMETIC PROCESSING")
                    print("\t\t- COMPARISON BETWEEN VALUES")
                    print("\t\t- LOGICAL DECISION MAKING")
                    print("\t\t- ASSIGNMENT OF DATA TO VARIABLES")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option3 == "2":
                    os.system("cls")
                    print("\n- EXAMPLES -")
                    
                    print("\n\t- ARITHMETIC OPERATORS -")
                    print('\t\tADDITION: 5 + 2 = 7')
                    print('\t\tSUBTRACTION: 5 - 2 = 3')
                    print('\t\tMULTIPLICATION: 5 * 2 = 10')
                    print('\t\tTRUE DIVISION (FLOAT): 5 / 2 = 2.5')
                    print('\t\tFLOOR DIVISION (FLOAT): 5 // 2 = 2')
                    print('\t\tMODULUS (REMAINDER): 5 % 2 = 1 ')
                    print('\t\tEXPONENT (POWER): 5 ** 2 = 25')
                    
                    print("\n\t- COMPARISON OPERATOR -")
                    print('\t\tEQUAL T0: 5 == 5 (TRUE)')
                    print('\t\tNOT EQUAL TO: 5 != 3 (TRUE)')
                    print('\t\tGREATER THAN: 5 > 3')
                    print('\t\tLESS THAN: 5 < 3')
                    print('\t\tGREATER OR EQUAL 5 >= 3')
                    print('\t\tLESS OR EQUAL: 5 <= 3 ')
                    
                    print("\n\t- LOGICAL OPERATOR -")
                    print('\t\tTRUE IF BOTH CONDITIONS ARE TRUE: x > 0 and x < 10)')
                    print('\t\tTRUE iF AT LEAST ONE CONDITIONS IS TRUE: x < 0 or x > 10')
                    print("\t\tREVERSE BOOLEAN VALUE: NOT TRUE = FALSE")
                    
                    
                    print("\n\t- ASSIGNMENT OPERATOR -")
                    print('\t\tASSIGN VALUE: x = 10')
                    print('\t\tADD THEN ASSIGN: x += 5 -> x = x + 5')
                    print('\t\tSUBTRACT THEN ASSIGN: x -= 3')
                    print('\t\tMULTIPLY THEN ASSIGN: x *= 2')
                    print('\t\tDIVIDE THEN ASSIGN: x /= 2')
                    print('\t\tFLOOR DIVIDE THEN ASSIGN: x //= 2')
                    print('\t\tMODULUS THEN ASSIGN: x %= 4')
                    print("\t\t EXPONENT THEN ASSIGN: x **= 3")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option3 == "0":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("INVALID INPUT.")
                    
        if option == "4":
            os.system("cls")
            while True:
                print("\t\t- CONDITIONAL STATEMENT  -")
                print("\n• A conditional statement in Python lets your program make decisions.")
                print("\n""********************************************\n\t\t""- SUB MENU -")
                print('\n\t1. DEFINITION')
                print('\t2. EXAMPLE')
                print('\t3. INPUTS OF CODES')
                print('\t0. BACK TO MAIN MENU')   
                print("********************************************")
                
                option4 = input('Enter the option you want to proceed with --> ')
                
                if option4 == "1":
                    os.system("cls")
                    print("\nDEFINITION:")
                    print("\n• A conditional statement in Python is a programming construct that allows a program to perform different actions based on whether a certain condition or set of conditions is true or false.")            
                    print("• In other words, conditional statements let your program make decisions and execute specific blocks of code depending on certain criteria. These statements are fundamental for controlling the flow of execution in a program.")
                    
                    print("\n\t• if - Executes a block if the condition is True.")
                    print("\t• elif (else if) – Checks another condition if previous if or elif statements were False.")
                    print("\t• else – Executes a block when none of the if or elif conditions are True.")
                    print("\n\n\tDECISION MAKING:")
                    print("\t\tConditional statements allow Python to choose between two or more paths of execution.")
                    print("\n\tBOOLEAN EVALUATION:")
                    print("\t\tThe conditions are expressions that evaluate to True or False.")
                    print("\n\tFLEXIBLE EXECUTION:")
                    print("\t\tYou can have multiple conditions using elif and provide a default case using else.")
                    print("\n\tCONTROL FLOW:")
                    print("\t\tThey control the flow of the program, enabling the execution of certain statements only when specific conditions are met.")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")    
                    continue
                
                elif option4 == "2":
                    os.system("cls")
                    print("\nEXAMPLE:")
                    item_price = eval(input("\n\tItem Price: "))
                    quantity = eval(input("\tQuantity: "))
                    total_cost = (item_price * quantity) 
                    
                    if total_cost >= 500:
                        discount = total_cost * 0.5
                        final_cost = total_cost - discount
                        
                        print("\n\t\tItem Price: ", item_price)
                        print("\t\tQuantity", quantity)
                        print("\t\tTotal Cost: ", total_cost)
                        print("\t\tFinal Cost: ", total_cost - discount)
                        print("\n\tDiscounted 50%.")
                        
                        input("\nPress Enter to exit..")
                        os.system("cls")
                        continue
                        
                    elif total_cost <= 499:
                        print("\t\tHere's the Breakdown:")
                        print("\t\tItem Price: ", item_price)
                        print("\t\tQuantity:", quantity)
                        print("\t\tTotal Cost: ", total_cost)
                        print("\t\tFinal Cost: ", total_cost)
                        print("\n\tNo Discount.")
                        
                        input("\nPress Enter to exit..")
                        os.system("cls")
                        continue
                        
                
                elif option4 == "3":
                    os.system("cls")
                    print("\nINPUT:")
                    print('\n\titem_price = eval(input("Item Price: "))')
                    print('\tquantity = eval(input("Quantity: "))')
                    print("\ttotal_cost = (item_price * quantity) ")
                    
                    print("\n\tif total_cost >= 100:")
                    print("\t\tdiscount = total_cost * 0.1")
                    print("\t\tfinal_cost = total_cost - discount")
                    print('\n\t\tprint("Item Price: ", item_price)')
                    print('\t\tprint("Quantity", quantity)')
                    print('\t\tprint("Total Cost: ", total_cost)')
                    print('\t\tprint("Final Cost: ", total_cost - discount)')
                        
                    print('\n\telif total_cost <= 99:')
                    print('\t\tprint("Here is the Breakdown:")')
                    print('\t\tprint("Item Price: ", item_price)')
                    print('\t\tprint("Quantity:", quantity)')
                    print('\t\tprint("Total Cost: ", total_cost)')
                    print('\t\tprint("Final Cost: ", total_cost - discount)')
                    
                    print("\n\telse:")
                    print('\t\tprint("Invalid Input.")')
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option4 == "0":
                    os.system("cls")
                    break
                
                else:
                    os.system("cls")
                    print("INVALID INPUT.")
                    
        if option == "5":
            os.system("cls")
            while True:
                print("\t\t- LOOPS -")
                print("\n• Loops are control structures that let you repeat a block of code multiple times..")
                print("\n""********************************************\n\t\t""- SUB MENU -")
                print('\n\t1.LOOPING IN PYTHON')
                print('\t2. SAMPLE LOOPS')
                print('\t0. BACK TO MAIN MENU')   
                print("********************************************")
                
                option5 = input('Enter the option you want to proceed with --> ')
                
                if option5 == "1":
                    os.system("cls")
                    print("\n\t• Looping in Python is the runtime execution of a cyclic control-flow construct, where the Python interpreter:")
                    print("\n\t\t- Evaluates an iteration control mechanism (an iterable or a Boolean expression)")
                    print("\t\t- Repeatedly enters a block of code until a termination condition is reached")
                    print("\t\t- Manages loop state, including iteration variables, scope, and exit conditions,")
                    print("\t\t- May accept explicit loop-control instructions (break, continue, pass),")
                    print("\t\t- Internally relies on bytecode instructions (like FOR_ITER, JUMP_ABSOLUTE, etc.) to manage repetition.")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option5 == "2":
                    os.system("cls")
                    print("\n\t- SAMPLE LOOPS -")
                    print("\n\tINPUT:")
                    print("\tfor i in range (5):") 
                    print('\t\tprint("Welcome to Python)')
                    
                    print("\n\tOUTPUT:")
                    print("\t\tWelcome to python")
                    print("\t\tWelcome to python")
                    print("\t\tWelcome to python")
                    print("\t\tWelcome to python")
                    print("\t\tWelcome to python")
                        
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                    
                    
                elif option5 == "0":
                    os.system("cls")
                    break
                
                else:
                    os.system("cls")
                    print("INVALID INPUT.")
                    
        if option == "6":
            os.system("cls")
            while True:
                print("\t\t- LISTS -")
                print("\n• list is an ordered, changeable (mutable) collection of items.")
                print("• Lists can store multiple values of any data type numbers, strings, booleans, other lists, or even mixed types.")
                print("\n""********************************************\n\t\t""- SUB MENU -")
                print('\n\t1. LISTS')
                print('\t2. DEFINITIONS')
                print('\t0. BACK TO MAIN MENU')   
                print("********************************************")
                
                option6 = input('Enter the option you want to proceed with --> ')
                
                if option6 == "1":
                    os.system("cls")
                    print('\n\t- LIST -')
                    print("\n\tINPUT:")
                    print("\t\tfruit = ['Dalanghita', 'Ubas', 'Mansanas']")
                    print("\t\tprint(fruit)")
                        
                    print("\n\tOUTPUT:") 
                    print("\t\t['Dalanghita', 'Ubas', 'Mansanas'])")
                    
                    print("\n\t- LIST WITH APPEND -")
                    print("\n\tINPUT:")
                    print("\t\tfruit = ['Dalanghita', 'Ubas', 'Mansanas']")
                    print("\t\tprint(fruit)")
                        
                    print("\t\tfruit.apppend('Orange')")
                        
                    print("\n\tOUTPUT:")
                    print("\t\t['Dalanghita', 'Ubas', 'Mansanas', 'Orange']")
                    
                    print('\n\t- LIST WITH POP -')  
                    print("\n\tINPUT:")
                    print("\t\tfruit = ['Dalanghita', 'Ubas', 'Mansanas']")
                    print("\t\tprint(fruit)")
                        
                    print("\t\tfruit.pop()")
                        
                    print("\n\tOUTPUT:") 
                    print("\t\t['Dalanghita', 'Ubas']")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option6 == "2":
                    os.system("cls")
                    print("\nDEFINITION:")
                    print("\n\t• A finite, ordered, mutable collection of object references, stored in a contiguous block of memory, supporting constant-time element access and amortized constant-time append operations, and represented internally in CPython as a dynamic array.")
                    print("\t\t- It remembers the order of elements.")
                    print("\t\t- It can grow or shrink at runtime.")
                    print("\t\t- It stores references to objects, not the objects themselves.")
                    print("\t\t- It provides O(1) element access time because it uses an array.")
                    print("\t\t- It maintains an internal capacity and resizes when necessary.")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option6 == "0":
                    os.system("cls")
                    break
                
                else:
                    os.system("cls")
                    print("INVALID INPUT.")
                    
        if option == "7":
            os.system("cls")
            while True:
                print("\t\t- FUNCTIONS  -")
                print("\n• A function in Python is a reusable block of code that performs a specific task.")
                print("  It can take inputs (parameters), process them, and optionally return outputs.")
                print("\n""********************************************\n\t\t""- SUB MENU -")
                print('\n\t1. PRINT FUNCTION')
                print('\t2.RETURN FUNCTION')
                print('\t0. BACK TO MAIN MENU')   
                print("********************************************")
                
                option7 = input('Enter the option you want to proceed with --> ')
                
                if option7 == "1":
                    os.system("cls")
                    print("\nPRINT FUNCTION:")
                    print("\n\tINPUT:")
                    print('\t\tprint("Hello Python")')
                    
                    print("\n\tOUTPUT:")
                    print("\t\tHello Python")
                    
                    print("\n\t- 'print' is the function of printing or displaying output.")
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option7 == "2":
                    os.system("cls")
                    print("\nRETURN FUNCTION:")
                    print("\n\tINPUT:")
                    print("\t\tdef add(a, b):")
                    print("\t\t\treturn a + b")
                    print("\n\t\tresult = add(5, 3)")
                    print('\t\tprint(result)')
                    
                    print("\n\tOUTPUT:")
                    print("\t\t8")
                    
                    print("\n\t- 'return()' is the return function.")     
                    
                    input("\nPress Enter to exit..")
                    os.system("cls")
                    continue
                
                elif option7 == "0":
                    os.system("cls")
                    break
                
                else:
                    os.system("cls")
                    print("INVALID INPUT.")
                
        if option == "0":
            os.system("cls")
            break

elif greet == "no":
    print("THANK YOU.")
else:
    print("INVALID INPUT.")