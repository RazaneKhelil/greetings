import datetime  
time = datetime.datetime.now().hour
if (time > 5)&(time < 12):
    print("Good Morning")
elif(time<17)&(time>12):
    print("Good aftenoon")
else:     
    print("Good evening")