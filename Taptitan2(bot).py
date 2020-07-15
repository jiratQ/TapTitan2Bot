from PIL import ImageGrab, ImageOps
import pyautogui
import keyboard
import time
from numpy import *

class Skill():
    _1=(710,960)
    _2=(810,960)
    _3=(910,960)
    _4=(1010,960)
    _5=(1110,960)
    _6=(1210,960)

buy0=(810,1060)
buy1=(1150,750)
buy2=(1150,850)
buy3=(1150,960)
buy4=(1150,1020)
buy5=(1250,600)

ClanMate=(900,560)

Fairy=[(750,271)]
for i in range(1,10):
    Fairy.append((750+50*i,271))

Dagger=[]
for i in range(0,5):
    Dagger.append((870+45*i,465))

Buff=[]
k=0
Buff.append((785,200))
for i in range(0,14):
    if(i>=7):
        k=15
    Buff.append((735+k,235+25*i))
    Buff.append((1210-k,200+25*i))
Buff.append((1210,200+25*15))
Buff.append((1150,200+25*15))

def SkillPress():
    pyautogui.click(Skill._2)
    time.sleep(0.2)
    pyautogui.click(Skill._3)
    time.sleep(0.2)
    pyautogui.click(Skill._4)
    time.sleep(0.2)
    pyautogui.click(Skill._5)
    time.sleep(0.2)
    pyautogui.click(Skill._6)
    time.sleep(0.2)


def FairyPress():
    for f in Fairy:
        pyautogui.click(f)
    time.sleep(5)

def DaggerPress():
    for d in Dagger:
        pyautogui.click(d)

def BuffPress():
    for b in Buff:
        pyautogui.click(b)

def ClanPress():
    pyautogui.click(ClanMate)

def BuyHero():
    pyautogui.click(buy0)
    time.sleep(0.3)
    pyautogui.moveTo(buy1)
    time.sleep(0.1)
    pyautogui.scroll(100)
    time.sleep(0.75)
    pyautogui.click(buy1)
    time.sleep(0.1)
    pyautogui.click(buy2)
    time.sleep(0.1)
    pyautogui.click(buy3)
    time.sleep(0.1)
    pyautogui.click(buy4)
    time.sleep(2)
    pyautogui.click(buy5)
    time.sleep(0.3)

def imageGrabAd():
    box = (700,260,1200,600)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())      
    #print(a.sum())
    return (a.sum()) 

def FightBoss():
    box = (1120,25,1250,65)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors()) 
    #print(a.sum())
    return (a.sum()) 

def main():
    second = time.time()
    while True:
        if(time.time()-second>=900):
            second = time.time()
            pyautogui.click(700,1060)
            #Respawn
            time.sleep(0.3)
            pyautogui.click(1170,890)
            time.sleep(0.3)
            pyautogui.click(975,900)
            time.sleep(0.3)
            pyautogui.click(1070,730)
            time.sleep(15)
            #CheckSkill
            pyautogui.click(700,1060)
            time.sleep(0.3)
            pyautogui.click(1140,600)
            time.sleep(0.3)
            #UpgradeLevel
            pyautogui.click(1150,175)
            time.sleep(0.3)
            pyautogui.click(1150,175)
            time.sleep(0.3)
            pyautogui.click(1150,175)
            time.sleep(0.3)
            pyautogui.click(1150,175)
            time.sleep(0.3)
            #UpgradeSkill
            pyautogui.click(1150,425)
            time.sleep(0.3)
            pyautogui.click(1150,525)
            time.sleep(0.3)
            pyautogui.click(1150,625)
            time.sleep(0.3)
            pyautogui.click(1150,725)
            time.sleep(0.3)
            pyautogui.click(1150,825)
            time.sleep(0.3)
            pyautogui.click(1150,925)
            time.sleep(0.3)
            #Exit
            pyautogui.click(1150,15)
            time.sleep(0.5)
            pyautogui.click(1225,600)
            time.sleep(3)

        while keyboard.is_pressed('1'):
            time.sleep(2)
        if FightBoss()==35442:
            pyautogui.click(1185,45)
        SkillPress()
        FairyPress()
        if imageGrabAd()==202116 or imageGrabAd()==202602 or imageGrabAd()==202628 or imageGrabAd()==201625:
            pyautogui.click(800,800)
        BuyHero()
        ClanPress()
        if imageGrabAd()==202116 or imageGrabAd()==202602 or imageGrabAd()==202628 or imageGrabAd()==201625:
            pyautogui.click(800,800)
        for i in range(6):
            pyautogui.click(buy5)
            BuffPress()
        ClanPress()
        DaggerPress()
        if imageGrabAd()==202116 or imageGrabAd()==202602 or imageGrabAd()==202628 or imageGrabAd()==201625:
            pyautogui.click(800,800)

main()