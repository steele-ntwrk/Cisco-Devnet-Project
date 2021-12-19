InName = input("What is your name?")

if InName == 'emily':
    print("Hi " + InName + ", what's your favorite food?")
    food = input()
    
    if food == 'pho':
        print('Wow, you must not be a android sent by musk')
        
        loveQ = input('Since you are the real emily, would you like to know a secret?')
        
        if loveQ == 'yes':
            love = 0
            while love < 5: 
                print("""
      ..     ..      
    ' L  '.`    '    
>>--`.  U    )).'-->>
      `.  V  .'      
        `. .`        
          U          """)
                love = love + 1
                
        else:
            print('Okay your loss!')
                
            
    
    elif food != 'pho':
        print("I knew you were not the real emlay, goodbye!")
    
    
elif InName == 'matt':
    print ("Hi Master " + InName + ", would you like a treat?")
    treat = input()
    
    if treat == 'yes':
        print("Okay here is a cookie")
        
    else:
        print("Okay, maybe tomorrow!!")
    

elif InName != 'matt' or 'emily':
    print("Sorry, don't know you!!")