import threading, time

print('Start of program.')

def makeSpace():
    print('\tWhat\'s for breakfast..!?')
    time.sleep(1)
    print()

def takeANap():
    while True:
        time.sleep(5)
        print('Wake Up!')
        makeSpace()

threadObj = threading.Thread(target=takeANap)
threadObj.start()

while True:
    print("I'm sleeping!")
    time.sleep(0.1)
print('End of program.')
