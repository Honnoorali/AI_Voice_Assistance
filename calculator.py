def speak(audio):
    engine.say(audio)
    engine.runAndWait()


calculator("add")


def calculator():
    global query
    try:
        if 'add' in query or 'edi' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to add')
            b = float(input("Enter another number to add:"))
            c = a+b
            print(f"{a} + {b} = {c}")
            speak(f'The addition of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'sub' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to subtract')
            b = float(input("Enter another number to subtract:"))
            c = a-b
            print(f"{a} - {b} = {c}")
            speak(f'The subtraction of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                    
        elif 'mod' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number')
            b = float(input("Enter another number:"))
            c = a%b
            print(f"{a} % {b} = {c}")
            speak(f'The modular division of {a} and {b} is equal to {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                    
        elif 'div' in query:
            speak('Enter a number as dividend')
            a = float(input("Enter a number:"))
            speak('Enter another number as divisor')
            b = float(input("Enter another number as divisor:"))
            c = a/b
            print(f"{a} / {b} = {c}")
            speak(f'{a} divided by {b} is equal to {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'multi' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to multiply')
            b = float(input("Enter another number to multiply:"))
            c = a*b
            print(f"{a} x {b} = {c}")
            speak(f'The multiplication of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'square root' in query:
            speak('Enter a number to find its sqare root')
            a = float(input("Enter a number:"))
            c = a**(1/2)
            print(f"Square root of {a} = {c}")
            speak(f'Square root of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'square' in query:
            speak('Enter a number to find its sqare')
            a = float(input("Enter a number:"))
            c = a**2
            print(f"{a} x {a} = {c}")
            speak(f'Square of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cube root' in query:
            speak('Enter a number to find its cube root')
            a = float(input("Enter a number:"))
            c = a**(1/3)
            print(f"Cube root of {a} = {c}")
            speak(f'Cube root of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cube' in query:
            speak('Enter a number to find its sqare')
            a = float(input("Enter a number:"))
            c = a**3
            print(f"{a} x {a} x {a} = {c}")
            speak(f'Cube of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'fact' in query:
            try:
                n = int(input('Enter the number whose factorial you want to find:'))
                fact = 1
                for i in range(1,n+1):
                    fact = fact*i
                print(f"{n}! = {fact}")
                speak(f'{n} factorial is equal to {fact}. Your answer is {fact}.')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                #print(e)
                speak('I unable to calculate its factorial.')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                    
        elif 'power' in query or 'raise' in query:
            speak('Enter a number whose power you want to raised')
            a = float(input("Enter a number whose power to be raised :"))
            speak(f'Enter a raised power to {a}')
            b = float(input(f"Enter a raised power to {a}:"))
            c = a**b
            print(f"{a} ^ {b} = {c}")
            speak(f'{a} raise to the power {b} = {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        
                
        elif 'percent' in query:
            speak('Enter a number whose percentage you want to calculate')
            a = float(input("Enter a number whose percentage you want to calculate :"))
            speak(f'How many percent of {a} you want to calculate?')
            b = float(input(f"Enter how many percentage of {a} you want to calculate:"))
            c = (a*b)/100
            print(f"{b} % of {a} is {c}")
            speak(f'{b} percent of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
            
        elif 'interest' in query:
            speak('Enter the principal value or amount')
            p = float(input("Enter the principal value (P):"))
            speak('Enter the rate of interest per year')
            r = float(input("Enter the rate of interest per year (%):"))
            speak('Enter the time in months')
            t = int(input("Enter the time (in months):"))            
            interest = (p*r*t)/1200
            sint = round(interest)
            fv = round(p + interest) 
            print(f"Interest = {interest}")
            print(f"The total amount accured, principal plus interest, from simple interest on a principal of {p} at a rate of {r}% per year for {t} months is {p + interest}.")
            speak(f'interest is {sint}. The total amount accured, principal plus interest, from simple interest on a principal of {p} at a rate of {r}% per year for {t} months is {fv}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        
    
        elif 'si' in query:
            speak('Enter the angle in degree to find its sine value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.sin(b)
            speak('Here is your answer.')
            print(f"sin({a}) = {c}")
            speak(f'sin({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cos' in query:
            speak('Enter the angle in degree to find its cosine value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.cos(b)
            speak('Here is your answer.')
            print(f"cos({a}) = {c}")
            speak(f'cos({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'cot' in query or 'court' in query:
            try:
                speak('Enter the angle in degree to find its cotangent value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c = 1/math.tan(b)
                speak('Here is your answer.')
                print(f"cot({a}) = {c}")
                speak(f'cot({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print("infinity")
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                
            
                
        elif 'tan' in query or '10' in query:
            speak('Enter the angle in degree to find its tangent value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.tan(b)
            speak('Here is your answer.')
            print(f"tan({a}) = {c}")
            speak(f'tan({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'y' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        
                
        elif 'cosec' in query:
            try:
                speak('Enter the angle in degree to find its cosecant value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c =1/ math.sin(b)
                speak('Here is your answer.')
                print(f"cosec({a}) = {c}")
                speak(f'cosec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                    
        elif 'caus' in query:
            try:
                speak('Enter the angle in degree to find its cosecant value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c =1/ math.sin(b)
                speak('Here is your answer.')
                print(f"cosec({a}) = {c}")
                speak(f'cosec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                
        elif 'sec' in query:
            try:
                speak('Enter the angle in degree to find its secant value')
                a = int(input("Enter the angle:"))
                b = a * 3.14/180
                c = 1/math.cos(b)
                speak('Here is your answer.')
                print(f"sec({a}) = {c}")
                speak(f'sec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'y' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            
                
    except Exception as e:
        speak('I unable to do this calculation.')
        speak('Do you want to do another calculation?')
        query = takeCommand().lower()
        if 'y' in query:
            speak('ok which calculation you want to do?')
            query = takeCommand().lower()
            calculator()
        else:
            speak('ok')
        
 