import time
name = input('Enter your name: ')
Recenttime = int(time.strftime('%H'))
recenttime = time.strftime('%H:%M:%S')
c= name.capitalize()
if(4<=Recenttime<12):
    print('GOOD MORNING',c,'its time to wake up and do some exercise because the time is',recenttime)
elif(12<=Recenttime<17):
    print('GOOD AFTERNOON',c,'its',recenttime)
elif(17<=Recenttime<21):
    print('GOOD EVENING',c,'its',recenttime)
else:
    print('GOOD NIGHT',c,'its',recenttime)
# print('Hii',name,'its',recenttime)
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59
