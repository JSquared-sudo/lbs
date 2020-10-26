import sys
import time
import random
from asciimatics.effects import Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
    PalmFirework
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.effects import Print
from asciimatics.particles import Explosion, StarFirework, DropScreen, Rain, \
    ShootScreen
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import keyboard



import random, keyboard, time

l = [chr(65+i) for i in range(26)]  # A-Z

def keyboardpart(l,x,num):
    for i in range(num):
        keyboard.is_pressed(65)  # process OS events
        while len(keyboard._physically_pressed_keys): pass # wait until keys released
        keypress = False
        c = 0
        dn = random.randint(0,25)
        var = l[dn]
        print(dn+1)
        flag1 = False
        start = time.time()
        while time.time()-start < x:
            if len(keyboard._physically_pressed_keys):  # any key down
               if keyboard.is_pressed(var):  # check target key
                   keypress = True
                   break
               else:  # wrong key
                   c+=1
                   if c >= 3: break   # allow 3 tries
                   while len(keyboard._physically_pressed_keys): pass # wait until keys released
               #print(keypress, c)
        #print(keypress,c)
        if not keypress:
            print("Sorry, you missed that key.")
            flag1 = True
            break
             
    if flag1:
        keyboardpart(l,x,num)
        
#keyboardpart(l,100,4)


def dem(screen):
    screen.set_title("Loading Bar Simulator")

    scenes = []

    # First scene: title page
    effects = [
        Print(screen,
              Rainbow(screen, FigletText("Loading Bar Simulator!", font="big")),
              y=screen.height // 4 - 5),
        Print(screen,
              FigletText("==>  A time-wasting  <=="),
              screen.height // 2 - 3),
        Print(screen,
              FigletText("===>  game  <==="),
              screen.height * 3 // 4 - 3),
        Print(screen,
              SpeechBubble("Press SPACE to continue..."),
              screen.height - 3,
              transparent=False,
              start_frame=70)
    ]
    scenes.append(Scene(effects, -1))

    # Next scene: just dissolve the title.
    effects = [
        ShootScreen(screen, screen.width // 2, screen.height // 2, 100),
    ]
    scenes.append(Scene(effects, 40, clear=False))
    screen.play(scenes, stop_on_resize=True, repeat=False)


Screen.wrapper(dem)


l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]




print("Loading bars.\n")
time.sleep(1)
print("We've all seen them.\n")
time.sleep(3)
print("Whether you're downloading a file off the internet, whether you're downloading a shady file off the the dark side of the internet, whether you're downloading a video game that takes up 75% of your hard drive, we've all seen them.\n")
time.sleep(10)
print("And when you have too much time and too little to do, you decide to make a game based around it- Oh wait? Just me? Ok...")
time.sleep(7)
print("Anyway, welcome to the first world of the three-world DLC!")

l1 = input("Whenever you're ready to start a level, simply type 'ready'. When you're ready to initiate the program, type ready." + "\n")
if l1 == "ready":
    print("Level 1-1 - Easy Peasy")
    x = 0
    b = 5
    for _ in range(5):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.1)
        sys.stdout.write('\b' * len(a))
    l2 = input("\n" + "Nice job! You're crushing it! Ready for level 2?" + "\n")
    if l2 != "ready":
        exit()
    print("Level 1-2 - Nice and Simple")
    x = 0
    b = 15
    for _ in range(15):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.1)
        sys.stdout.write('\b' * len(a))
    l3 = input("\n" + "Incredible! Watch out though, level 3 is slightly harder." + "\n")
    if l3 != "ready":
        exit()
    print("Level 1-3 - Getting Harder")
    x = 0
    b = 25
    for _ in range(25):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.1)
        sys.stdout.write('\b' * len(a))
    l4 = input("\n" + "3 Level Combo! Prepare yourself - This is about to get harder." + "\n")
    if l4 != "ready":
        exit()
    print("Level 1-4 - Slow and steady wins the race.")
    x = 0
    b = 20
    for _ in range(20):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.5)
        sys.stdout.write('\b' * len(a))
    l5 = input("\n" + "Approaching medium difficulty..." + "\n")
    if l5 != "ready":
        exit()
    print("Level 1-5 - Marathoning.")
    x = 0
    b = 100
    for _ in range(100):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.1)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Achievement Unlocked - Patience I")
    l6 = input("\n" + "Wow! That took a while. Hope you're ready for a challenge next game." + "\n")
    if l6 != "ready":
        exit()
    print("Level 1-6 - Falling asleep.")
    x = 0
    b = 40
    for _ in range(40):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.5)
        sys.stdout.write('\b' * len(a))
    l7 = input("\n" + "Still here? This next one will drive you insane. Good Luck." + "\n")
    if l7 != "ready":
        exit()
    print("Level 1-7 - Insane in the Membrane.")
    x = 0
    b = 100
    for _ in range(100):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(1)
        sys.stdout.write('\b' * len(a))
    l8 = input("\n" + "Zzzzz..." + "\n")
    if l8 != "ready":
        exit()
    print("Level 1-8 - Hands and Feet, Fallin' Asleep.")
    x = 0
    b = 100
    for _ in range(100):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(5)
        sys.stdout.write('\b' * len(a))
    l9 = input("\n" + "You're STILL here? One more level! :D" + "\n")
    if l9 != "ready":
        exit()
    print("Level 1-9 - 9-5 Job")
    x = 0
    b = 100
    for _ in range(100):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(15)
        sys.stdout.write('\b' * len(a))
    l10 = input("\n" + "No words left. Good luck." + "\n")
    if l4 != "ready":
        exit()
    print("Level 1-10 - Productivity [Boss Fight]")
    x = 0
    b = 100
    for _ in range(100):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(60)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Wait..you actually did it? Well, kudos to you, I guess. Have some fireworks!")
    time.sleep(5)
    from asciimatics.effects import Stars, Print
    from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
        PalmFirework
    from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
    from asciimatics.scene import Scene
    from asciimatics.screen import Screen
    from asciimatics.exceptions import ResizeScreenError
    from random import randint, choice
    import sys


    def demow1(screen):
        scenes = []
        effects = [
            Stars(screen, screen.width),
            Print(screen,
                  SpeechBubble("Press spacebar to exit out."),
                  y=screen.height - 3,
                  start_frame=300)
        ]
        for _ in range(20):
            fireworks = [
                (PalmFirework, 25, 30),
                (PalmFirework, 25, 30),
                (StarFirework, 25, 35),
                (StarFirework, 25, 35),
                (StarFirework, 25, 35),
                (RingFirework, 20, 30),
                (SerpentFirework, 30, 35),
            ]
            firework, start, stop = choice(fireworks)
            effects.insert(
                1,
                firework(screen,
                         randint(0, screen.width),
                         randint(screen.height // 8, screen.height * 3 // 4),
                         randint(start, stop),
                         start_frame=randint(0, 250)))

        effects.append(Print(screen,
                             Rainbow(screen, FigletText("CONGRATULATIONS!")),
                             screen.height // 2 - 6,
                             speed=1,
                             start_frame=100))
        effects.append(Print(screen,
                             Rainbow(screen, FigletText("YOU BEAT WORLD 1!")),
                             screen.height // 2 + 1,
                             speed=1,
                             start_frame=100))
        scenes.append(Scene(effects, -1))

        screen.play(scenes, stop_on_resize=True, repeat = False)

    Screen.wrapper(demow1)
    l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print("\n" + "World 2...")
    print("\n" + "This part of the game is harder, and requires more experience with the keyboard. How to play you ask? Every part of the level gives a number ")
    print("between 1 and 26, and you have to type the letter. If you type one wrong, you must restart the entire 'set' of letters. Seems easy? There's a time limit. Good luck!")
    print("Level 2-1 - Keyboardin'")
    flag = False
    num = 8
    x = 10
    keyboardpart(l,x,num)
    print("Nice job. That wasn't so hard, now was it?")
    time.sleep(3)
    print("Level 2-2 - Clickity Clackity")
    flag = False
    num = 12
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-3 - Are you cheating?")
    flag = False
    num = 15
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-4 - Sense of Urgency")
    flag = False
    num = 20
    x = 3
    keyboardpart(l,x,num)
    print("Level 2-5 - 26 letters, 26 chances")
    flag = False
    num = 26
    x = 4
    keyboardpart(l,x,num)
    print("Level 2-6 - Carpal Tunnel")
    flag = False
    num = 12
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-7 - Speed of Sound")
    flag = False
    num = 10
    x = 1
    keyboardpart(l,x,num)
    print("Level 2-8 - Mach 10")
    flag = False
    num = 5
    x = 0.5
    keyboardpart(l,x,num)
    print("Level 2-9 - Speed of Light")
    flag = False
    num = 3
    x = 0.25
    print("Level 2-10 - Quantum Spacetime")
    flag = False
    num = 2
    x = 0.1
    keyboardpart(l,x,num)
    print("Amazing! Take a kudos and...fireworks? Ok!")
    time.sleep(5)
    from asciimatics.effects import Stars, Print
    from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
        PalmFirework
    from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
    from asciimatics.scene import Scene
    from asciimatics.screen import Screen
    from asciimatics.exceptions import ResizeScreenError
    from random import randint, choice
    import sys


    def demo1(screen):
        scenes = []
        effects = [
            Stars(screen, screen.width),
            Print(screen,
                  SpeechBubble("Press spacebar to exit out."),
                  y=screen.height - 3,
                  start_frame=300)
        ]
        for _ in range(20):
            fireworks = [
                (PalmFirework, 25, 30),
                (PalmFirework, 25, 30),
                (StarFirework, 25, 35),
                (StarFirework, 25, 35),
                (StarFirework, 25, 35),
                (RingFirework, 20, 30),
                (SerpentFirework, 30, 35),
            ]
            firework, start, stop = choice(fireworks)
            effects.insert(
                1,
                firework(screen,
                         randint(0, screen.width),
                         randint(screen.height // 8, screen.height * 3 // 4),
                         randint(start, stop),
                         start_frame=randint(0, 250)))

        effects.append(Print(screen,
                             Rainbow(screen, FigletText("CONGRATULATIONS!")),
                             screen.height // 2 - 6,
                             speed=1,
                             start_frame=100))
        effects.append(Print(screen,
                             Rainbow(screen, FigletText("YOU BEAT WORLD 1!...maybe?")),
                             screen.height // 2 + 1,
                             speed=1,
                             start_frame=100))
        scenes.append(Scene(effects, -1))

        screen.play(scenes, stop_on_resize=True, repeat = False)


    Screen.wrapper(demo1)
    l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print("\n" + "World 2...")
    print("\n" + "This part of the game is harder, and requires more experience with the keyboard. How to play you ask? Every part of the level gives a number ")
    print("between 1 and 26, and you have to type the letter. If you type one wrong, you must restart the entire 'set' of letters. Seems easy? There's a time limit. Good luck!")
    time.sleep(10)
    print("Level 2-1 - Keyboardin'")
    flag = False
    num = 8
    x = 10
    keyboardpart(l,x,num)
    print("Nice job. That wasn't so hard, now was it?")
    time.sleep(3)
    print("Level 2-2 - Clickity Clackity")
    flag = False
    num = 12
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-3 - Are you cheating?")
    flag = False
    num = 15
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-4 - Sense of Urgency")
    flag = False
    num = 20
    x = 3
    keyboardpart(l,x,num)
    print("Level 2-5 - 26 letters, 26 chances")
    flag = False
    num = 26
    x = 4
    keyboardpart(l,x,num)
    print("Level 2-6 - Carpal Tunnel")
    flag = False
    num = 12
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-7 - Speed of Sound")
    flag = False
    num = 10
    x = 1
    keyboardpart(l,x,num)
    print("Level 2-8 - Mach 10")
    flag = False
    num = 5
    x = 0.5
    keyboardpart(l,x,num)
    print("Level 2-9 - Speed of Light")
    flag = False
    num = 3
    x = 0.25
    keyboardpart(l,x,num)
    print("Level 2-10 - Quantum Spacetime")
    flag = False
    num = 2
    x = 0.1
    keyboardpart(l,x,num)
elif l1 == "root":
    print("Level 1-1 - Easy Peasy")
    x = 0
    b = 5
    for _ in range(5):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-2 - Nice and Simple")
    x = 0
    b = 5
    for _ in range(5):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-3 - Getting Harder")
    x = 0
    b = 5
    for _ in range(5):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-4 - Slow and steady wins the race.")
    x = 0
    b = 2
    for _ in range(2):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-5 - Marathoning.")
    x = 0
    b = 10
    for _ in range(10):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-6 - Falling asleep.")
    x = 0
    b = 4
    for _ in range(4):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-7 - Insane in the Membrane.")
    x = 0
    b = 10
    for _ in range(10):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-8 - Hands and Feet, Fallin' Asleep.")
    x = 0
    b = 10
    for _ in range(10):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-9 - 9-5 Job")
    x = 0
    b = 10
    for _ in range(10):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n" + "Level 1-10 - Productivity [Boss Fight]")
    x = 0
    b = 10
    for _ in range(10):
        if b == -1:
            break
        a = "[" + "█" * x + " " * ( b-1) + "]"
        sys.stdout.write(a)
        sys.stdout.flush()
        b-=1
        x+=1
        time.sleep(0.0000001)
        sys.stdout.write('\b' * len(a))
    print("\n poggers you won")
    time.sleep(5)
    from asciimatics.effects import Stars, Print
    from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
        PalmFirework
    from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
    from asciimatics.scene import Scene
    from asciimatics.screen import Screen
    from asciimatics.exceptions import ResizeScreenError
    from random import randint, choice
    import sys


    def demo1(screen):
        scenes = []
        effects = [
            Stars(screen, screen.width),
            Print(screen,
                  SpeechBubble("Press spacebar to exit out."),
                  y=screen.height - 3,
                  start_frame=300)
        ]
        for _ in range(20):
            fireworks = [
                (PalmFirework, 25, 30),
                (PalmFirework, 25, 30),
                (StarFirework, 25, 35),
                (StarFirework, 25, 35),
                (StarFirework, 25, 35),
                (RingFirework, 20, 30),
                (SerpentFirework, 30, 35),
            ]
            firework, start, stop = choice(fireworks)
            effects.insert(
                1,
                firework(screen,
                         randint(0, screen.width),
                         randint(screen.height // 8, screen.height * 3 // 4),
                         randint(start, stop),
                         start_frame=randint(0, 250)))

        effects.append(Print(screen,
                             Rainbow(screen, FigletText("CONGRATULATIONS!")),
                             screen.height // 2 - 6,
                             speed=1,
                             start_frame=100))
        effects.append(Print(screen,
                             Rainbow(screen, FigletText("YOU BEAT WORLD 1!...maybe?")),
                             screen.height // 2 + 1,
                             speed=1,
                             start_frame=100))
        scenes.append(Scene(effects, -1))

        screen.play(scenes, stop_on_resize=True, repeat = False)


    Screen.wrapper(demo1)
    l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print("\n" + "World 2...")
    print("\n" + "This part of the game is harder, and requires more experience with the keyboard. How to play you ask? Every part of the level gives a number ")
    print("between 1 and 26, and you have to type the letter. If you type one wrong, you must restart the entire 'set' of letters. Seems easy? There's a time limit. Good luck!")
    time.sleep(10)
    print("Level 2-1 - Keyboardin'")
    flag = False
    num = 8
    x = 10
    keyboardpart(l,x,num)
    print("Nice job. That wasn't so hard, now was it?")
    time.sleep(3)
    print("Level 2-2 - Clickity Clackity")
    flag = False
    num = 12
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-3 - Are you cheating?")
    flag = False
    num = 15
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-4 - Sense of Urgency")
    flag = False
    num = 20
    x = 3
    keyboardpart(l,x,num)
    print("Level 2-5 - 26 letters, 26 chances")
    flag = False
    num = 26
    x = 4
    keyboardpart(l,x,num)
    print("Level 2-6 - Carpal Tunnel")
    flag = False
    num = 12
    x = 5
    keyboardpart(l,x,num)
    print("Level 2-7 - Speed of Sound")
    flag = False
    num = 10
    x = 1
    keyboardpart(l,x,num)
    print("Level 2-8 - Mach 10")
    flag = False
    num = 5
    x = 0.5
    keyboardpart(l,x,num)
    print("Level 2-9 - Speed of Light")
    flag = False
    num = 3
    x = 0.25
    keyboardpart(l,x,num)
    print("Level 2-10 - Quantum Spacetime")
    flag = False
    num = 2
    x = 0.1
    keyboardpart(l,x,num)
    print("Amazing! Take a kudos and...fireworks? Ok!")
    print("\n" + "Hey! You cheated! Not fair! The max you're getting is some fireworks.")
    time.sleep(5)
    from asciimatics.effects import Stars, Print
    from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
        PalmFirework
    from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
    from asciimatics.scene import Scene
    from asciimatics.screen import Screen
    from asciimatics.exceptions import ResizeScreenError
    from random import randint, choice
    import sys


    def demo2(screen):
        scenes = []
        effects = [
            Stars(screen, screen.width),
            Print(screen,
                  SpeechBubble("Press spacebar to exit out."),
                  y=screen.height - 3,
                  start_frame=300)
        ]
        for _ in range(20):
            fireworks = [
                (PalmFirework, 25, 30),
                (PalmFirework, 25, 30),
                (StarFirework, 25, 35),
                (StarFirework, 25, 35),
                (StarFirework, 25, 35),
                (RingFirework, 20, 30),
                (SerpentFirework, 30, 35),
            ]
            firework, start, stop = choice(fireworks)
            effects.insert(
                1,
                firework(screen,
                         randint(0, screen.width),
                         randint(screen.height // 8, screen.height * 3 // 4),
                         randint(start, stop),
                         start_frame=randint(0, 250)))

        effects.append(Print(screen,
                             Rainbow(screen, FigletText("CONGRATULATIONS!")),
                             screen.height // 2 - 6,
                             speed=1,
                             start_frame=100))
        effects.append(Print(screen,
                             Rainbow(screen, FigletText("YOU BEAT WORLD 2!...maybe?")),
                             screen.height // 2 + 1,
                             speed=1,
                             start_frame=100))
        scenes.append(Scene(effects, -1))

        screen.play(scenes, stop_on_resize=True, repeat = False)

    Screen.wrapper(demo2)
