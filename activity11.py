temperature = eval(input("Temperature: "))


if temperature <= 0 :
    print("Freezing Temperature")
    
if temperature >= 1 and temperature <=15 :
    print("Extremely Cold Temperature")
    
elif temperature >= 16 and temperature <= 30 :
    print("Cold Temperature")
    
elif temperature >= 31 and temperature <= 38 :
    print("Lukewarm Temperature")
    
elif temperature >= 39 and temperature <= 42 :
    print("Warm Temperature")
    
elif temperature >= 43 and temperature <= 50 :
    print("Hot Temperature")
    
elif temperature >= 51 and temperature <= 60 :
    print("Extremely Hot Temperature")
    
elif temperature >= 61:
    print("Burning Temperature")
    
else:
    print("Invalid Temperature")