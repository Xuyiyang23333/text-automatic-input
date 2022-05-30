import keyboard, time

def typeIn(t):
    with open(t) as topic:
        t = topic.read()
    for w in t:
        keyboard.write(w)
        time.sleep(0.01)

if __name__ == '__main__':
    keyboard.wait('right ctrl')
    time.sleep(1)
    typeIn('./文章/中英综合练习/CPU.txt')
