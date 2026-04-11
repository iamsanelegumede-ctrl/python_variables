weather = int(input( "what is the temperature in fahrenheit :" ))
#print("what is the temperature" ,weather) 
#fahrenheit = 500 
celcius = int(weather-32* 5/9) 
if celcius >= 32: 
    print(f"The weather {celcius} Degrees celcius, Its hot") 
elif celcius <= 10: 
    print(f"The weather {celcius} Degrees celcius, Its Cold")
elif celcius in range(11,31):  
    print(f"The weather {celcius} Degrees celcius, Its Average")