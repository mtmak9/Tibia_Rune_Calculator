import numpy as np
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog
import time

root=Tk()
root.title("Tibia Rune Maker Calculator v1.0")
root.geometry("550x620")
root.configure(bg="#7caff6")
root.iconbitmap('data/icon.ico')

#photo = PhotoImage(file ='background2.jpg')
#w = Label(root, image=photo).pack()

#---GREEN STAMINA REGENERATION---#
#Full_stamina = x
#Depo_reg = z
#Logout_reg = y 
#---STALE DANE/INFORMACJE---#
#---MS/ED MANA REGENERATION---#
Basic_reg = 1
Double_reg = 2
Bonus50_reg = 1.5
#---MS/ED HP REGENERATION---#
BasicHp_reg = 0.083
DoubleHP_reg = 0.166
#---SOFT BOOTS---#
SoftMP_reg = 2
SoftHP_reg = 0.5
SoftTime_reg = 14400
Soft_price = 10000
#---TIARA OF POWER---#
TiaraMP_reg = 1.3333
TiaraHP_reg = 0.3333
TiaraTime_reg = 3600
Tiara_price = 2000
#---LIFE RING---#
LRMP_reg =  1.3333
LRHP_reg = 0.3333
LRTime_reg = 1200
LR_price = 290
#---RING OF HEALING---#
ROH_reg = 4
ROHHP_reg = 1
ROHTime_reg = 450
ROH_price = 2000
#---COLLAR OF GREEN PLASMA AMULET---#
PlasmaMP_reg = 1.3333
GreenPlasmaHP_reg = 0.3333
GreenPlasmaTime_reg = 1800
GreenPlasma_price = 6000
#---RUNES MANA---#
SD_mana = 985
GFB_mana = 530
AVA_mana = 530
SS_mana = 430
TS_mana = 430
FBomb_mana = 600
EBomb_mana = 880
PBomb_mana = 520
EWall_mana = 1000
FWall_mana = 780
PWall_mana = 640
UH_mana = 400
IH_mana = 120
WGrow_mana = 600
MWall_mana = 750
Paral_mana = 1400
#---RUNES PRICE---#
SD_price = 135
GFB_price = 57
AVA_price = 57
TS_price = 47
SS_price = 37
FBomb_price = 147
EBomb_price = 203
PBomb_price = 85
EWall_price = 85
FWall_price = 61
PWall_price = 52
UH_price = 175
IH_price = 95
WGrow_price = 160
MWall_price = 116
Paral_price = 700
#---BLANK RUNE PRICE ---#
BLANK_price = 10
#---BROWN MUSHROM PRICE---#
food_price = 10
food_time = 264
food = food_price/food_time
#---RUNES COUNT---#
SD_szt = 3
GFB_szt = 4
AVA_szt = 4
SS_szt = 4
TS_szt = 4
FBomb_szt = 2
EBomb_szt = 2
PBomb_szt = 2
EWall_szt = 4
FWall_szt = 4
PWall_szt = 4
UH_szt = 1
IH_szt = 1
WGrow_szt = 2
MWall_szt = 3
Paral_szt = 1
#---PRICE ENTRY FOR CALCULATION---#
Tiara_Value = IntVar()
TiaraPrice = Entry(root,textvariable=Tiara_Value)
TiaraPrice.grid(column=1,row=0)
TiaraPrice.insert(0, "")
#---LIFE RING ENTRY---#
LR_Value = IntVar()
LR_price = Entry(root,textvariable=LR_Value)
LR_price.grid(column=1,row=1)
LR_price.insert(0, "")
#---RING OF HEALING ENTRY---#
RoH_Value = IntVar()
RoHPrice = Entry(root,textvariable=RoH_Value)
RoHPrice.grid(column=1,row=2)
RoHPrice.insert(0, "")
#---GREEN PLASMA ENTRY---#
Plasma_Value = IntVar()
PlasmaPrice = Entry(root,textvariable=Plasma_Value)
PlasmaPrice.grid(column=1,row=3)
PlasmaPrice.insert(0, "")
#---TIME ENTRY---#
VarDur = IntVar()
Duration = Entry(root,textvariable=VarDur)
Duration.grid(column=1,row=4)
Duration.insert(0, "")

def activateCheck():
            if Life_active.get() == 1:          #whenever checked
                C3.config(state=DISABLED)
            elif Life_active.get() == 0:        #whenever unchecked
                C3.config(state=NORMAL)
            if RoH_active.get() == 1:
                C2.config(state=DISABLED)
            elif RoH_active.get() == 0:
                C2.config(state=NORMAL)
def RegenerationCheck():
            if Double_active.get() == 1:
                C7.config(state=DISABLED)
            elif Double_active.get() == 0:
                C7.config(state=NORMAL)
            if Single_active.get() == 1:          #whenever checked
                C8.config(state=DISABLED)
            elif Single_active.get() == 0:        #whenever unchecked
                C8.config(state=NORMAL)
#---CHECKBOXES---#
Soft_active = IntVar(value=1)
C1 = Checkbutton(root, text="Soft boots", bg="#7caff6", variable=Soft_active).grid(column=0,row=5, sticky=W)
Life_active = IntVar(value=1)
C2 = Checkbutton(root, text="Life Ring",bg="#7caff6", variable=Life_active, command=activateCheck, onvalue = 1, offvalue = 0)
C2.grid(column=0,row=6, sticky=W)
RoH_active = IntVar(value=0)
C3 = Checkbutton(root, text="RoH",bg="#7caff6", variable=RoH_active, command=activateCheck, onvalue = 1, offvalue = 0, state=DISABLED)
C3.grid(column=3,row=6, sticky=W)
Tiara_active = IntVar()
C4 = Checkbutton(root, text="Tiara",bg="#7caff6", variable=Tiara_active).grid(column=3,row=5, sticky=W)
Plasma_active = IntVar()
C5 = Checkbutton(root, text="Green Plasma",bg="#7caff6", variable=Plasma_active).grid(column=1,row=5, sticky=W)
Bonus_active = IntVar()
C6 = Checkbutton(root, text="50% Bonus Regeneration",bg="#7caff6", variable=Bonus_active).grid(column=1,row=6, sticky=W)
Single_active = IntVar(value=0)
C7 = Checkbutton(root, text="Single Regeneration",bg="#7caff6", variable=Single_active, command=RegenerationCheck, onvalue = 1, offvalue = 0, state=DISABLED)
C7.grid(column=0,row=7, sticky=W)
Double_active = IntVar(value=1)
C8 = Checkbutton(root, text="Double Regeneration",bg="#7caff6", variable=Double_active, command=RegenerationCheck, onvalue = 1, offvalue = 0)
C8.grid(column=1,row=7, sticky=W)

def calculate():
    soft = Soft_active.get()
    life = Life_active.get()
    RoH = RoH_active.get()
    Tiara = Tiara_active.get()
    Plasma = Plasma_active.get()
    SingleMP = Single_active.get()
    DoubleMP = Double_active.get()
    BONUS = Bonus_active.get()   
        #COST PER SECOND
    LR_cena = LR_Value.get()
    RoHcena = RoH_Value.get()
    Tiaracena = Tiara_Value.get()
    Plasmacena = Plasma_Value.get()

    FOOD_S_COST = food
    LR_S_COST = int(LR_cena)/1200
    LIFE_RING_SEC = round(LR_S_COST,2)
    ROH_S_COST = int(RoHcena)/450
    ROH_SEC = round(ROH_S_COST,2)    
    SOFT_SEC = 0.69
    TIARA_S_COST = int(Tiaracena)/3600
    TIARA_SEC = round(TIARA_S_COST,2)
    PLASMA_S_COST = int(Plasmacena)/1800
    PLASMA_SEC = round(PLASMA_S_COST,2)

#MAIN SCRIPT - SINGLE/DOUBLE REG + SOFT + LIFE RING/ROH + TIARA + PLASMA + 50% - MAIN SCRIPT 
    time = Duration.get()
    mins = float(time) * 60
    time2 = int(time)*60

    if SingleMP == 1:
        SINGLE = float(mins * Basic_reg)
        if BONUS == 1:
            SINGLE = float(SINGLE*Bonus50_reg)
        SINGLE_COST = float(time2*food)
    elif SingleMP == 0:
        SINGLE = 0
        SINGLE_COST = 0
    if DoubleMP == 1:
        DOUBLE = float(mins * Double_reg)
        if BONUS == 1:
            DOUBLE = float(DOUBLE*Bonus50_reg)
        DOUBLE_COST = float(time2*food)
    elif DoubleMP == 0:    
        DOUBLE = 0
        DOUBLE_COST = 0
    if soft == 1:
        SOFTMP = float(mins * SoftMP_reg)
        SOFTMP_COST = float(time2*SOFT_SEC)
    elif soft == 0:
        SOFTMP = 0
        SOFTMP_COST = 0
    if life == 1:
        LIFER = float(mins * LRMP_reg)
        LIFER_COST = float(time2*LR_S_COST)
    elif life == 0:
        LIFER = 0
        LIFER_COST = 0    
    if RoH == 1:
        ROHMP = float(mins * ROH_reg)
        ROHMP_COST = float(time2*ROH_S_COST)
    elif RoH == 0:
        ROHMP = 0
        ROHMP_COST = 0
    if Tiara == 1:
        TIARA = float(mins * TiaraMP_reg)
        TIARA_COST = float(time2*TIARA_S_COST)
    elif Tiara == 0:
        TIARA = 0
        TIARA_COST = 0
    if Plasma == 1:
        PLASMA = float(mins * PlasmaMP_reg)
        PLASMA_COST = float(time2*PLASMA_S_COST)
    elif Plasma == 0:
        PLASMA = 0
        PLASMA_COST = 0
    mana = float(SINGLE + DOUBLE + SOFTMP + ROHMP + TIARA + PLASMA + LIFER)
    mana2 = round(mana)
    manaLabel = Label(root,text=(mana2,"mp"),bg="#7caff6",fg="#000f64")
    manaLabel.grid(column=1,row=30)
#---RUNES LABELS---#
#1.SUDDEN DEATH(SD) RUNE    
    SD = int((mana/SD_mana)*SD_szt)
    SDLabel = Label(root,text=(SD,"x"),bg="#7caff6")
    SDLabel.grid(column=2,row=10)
    SD_VALUE = int(SD * SD_price)
    SDLabel = Label(root,text=(SD_VALUE),bg="#7caff6",fg="#f06400")
    SDLabel.grid(column=1,row=10)
#SD EXPENSE
    SD_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/SD_mana)*BLANK_price))
    SD_RD_COST = round(SD_COST,0)
    SDLabel_COST = Label(root,text=SD_RD_COST,bg="#7caff6",fg="#f00640")
    SDLabel_COST.grid(column=4,row=10)
#SD PROFIT    
    SD_PROFIT = int(SD_VALUE-SD_COST)
    SD_RD_PROFIT = round(SD_PROFIT,0)
    SDLabel_PROFIT = Label(root,text=SD_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    SDLabel_PROFIT.grid(column=5,row=10)
#SD BLANK RUNES
    SD_BLANK = int(mana/SD_mana)
    SD_BLANK = round(SD_BLANK,0)
    SDLabel_BLANK = Label(root,text=SD_BLANK,bg="#7caff6")
    SDLabel_BLANK.grid(column=3,row=10)
#2.GFB(FIRE) RUNE
    GFB = int((mana/GFB_mana)*GFB_szt)
    GFBLabel = Label(root,text=(GFB,"x"),bg="#7caff6")
    GFBLabel.grid(column=2,row=11)
    GFB_VALUE = int(GFB * GFB_price)
    GFBLabel = Label(root,text=(GFB_VALUE),bg="#7caff6",fg="#f06400")
    GFBLabel.grid(column=1,row=11)
#GFB EXPENSE
    GFB_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/GFB_mana)*BLANK_price))
    GFB_RD_COST = round(GFB_COST,0)
    GFBLabel_COST = Label(root,text=GFB_RD_COST,bg="#7caff6",fg="#f00640")
    GFBLabel_COST.grid(column=4,row=11)
#GFB PROFIT    
    GFB_PROFIT = int(GFB_VALUE-GFB_COST)
    GFB_RD_PROFIT = round(GFB_PROFIT,0)
    GFBLabel_PROFIT = Label(root,text=GFB_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    GFBLabel_PROFIT.grid(column=5,row=11)
#GFB BLANK RUNES
    GFB_BLANK = int(mana/GFB_mana)
    GFB_BLANK = round(GFB_BLANK,0)
    GFBLabel_BLANK = Label(root,text=GFB_BLANK,bg="#7caff6")
    GFBLabel_BLANK.grid(column=3,row=11)
#3.AVA(ICE) RUNE
    AVA = int((mana/AVA_mana)*AVA_szt)
    AVALabel = Label(root,text=(AVA,"x"),bg="#7caff6")
    AVALabel.grid(column=2,row=12)
    AVA_VALUE = int(AVA * AVA_price)
    AVALabel = Label(root,text=(AVA_VALUE),bg="#7caff6",fg="#f06400")
    AVALabel.grid(column=1,row=12)
#AVA EXPENSE
    AVA_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/AVA_mana)*BLANK_price))
    AVA_RD_COST = round(AVA_COST,0)
    AVALabel_COST = Label(root,text=AVA_RD_COST,bg="#7caff6",fg="#f00640")
    AVALabel_COST.grid(column=4,row=12)
#AVA PROFIT    
    AVA_PROFIT = int(AVA_VALUE-AVA_COST)
    AVA_RD_PROFIT = round(AVA_PROFIT,0)
    AVALabel_PROFIT = Label(root,text=AVA_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    AVALabel_PROFIT.grid(column=5,row=12)
#AVA BLANK RUNES
    AVA_BLANK = int(mana/AVA_mana)
    AVA_BLANK = round(AVA_BLANK,0)
    AVALabel_BLANK = Label(root,text=AVA_BLANK,bg="#7caff6")
    AVALabel_BLANK.grid(column=3,row=12)
#4.STONESHOWER(POISON) RUNE
    SS = int((mana/SS_mana)*SS_szt)
    SSLabel = Label(root,text=(SS,"x"),bg="#7caff6")
    SSLabel.grid(column=2,row=13)
    SS_VALUE = int(SS * SS_price)
    SSLabel = Label(root,text=(SS_VALUE),bg="#7caff6",fg="#f06400")
    SSLabel.grid(column=1,row=13)
#SS EXPENSE
    SS_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/SS_mana)*BLANK_price))
    SS_RD_COST = round(SS_COST,0)
    SSLabel_COST = Label(root,text=SS_RD_COST,bg="#7caff6",fg="#f00640")
    SSLabel_COST.grid(column=4,row=13)
#SS PROFIT    
    SS_PROFIT = int(SS_VALUE-SS_COST)
    SS_RD_PROFIT = round(SS_PROFIT,0)
    SSLabel_PROFIT = Label(root,text=SS_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    SSLabel_PROFIT.grid(column=5,row=13)
#SS BLANK RUNES
    SS_BLANK = int(mana/SS_mana)
    SS_BLANK = round(SS_BLANK,0)
    SSLabel_BLANK = Label(root,text=SS_BLANK,bg="#7caff6")
    SSLabel_BLANK.grid(column=3,row=13)
#5.THUNDERSTORM(ENERGY) RUNE
    TS = int((mana/TS_mana)*TS_szt)
    TSLabel = Label(root,text=(TS,"x"),bg="#7caff6")
    TSLabel.grid(column=2,row=14)
    TS_VALUE = int(TS * TS_price)
    TSLabel = Label(root,text=(TS_VALUE),bg="#7caff6",fg="#f06400")
    TSLabel.grid(column=1,row=14)
#TS EXPENSE
    TS_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/TS_mana)*BLANK_price))
    TS_RD_COST = round(TS_COST,0)
    TSLabel_COST = Label(root,text=TS_RD_COST,bg="#7caff6",fg="#f00640")
    TSLabel_COST.grid(column=4,row=14)
#TS PROFIT    
    TS_PROFIT = int(TS_VALUE-TS_COST)
    TS_RD_PROFIT = round(TS_PROFIT,0)
    TSLabel_PROFIT = Label(root,text=TS_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    TSLabel_PROFIT.grid(column=5,row=14)
#TS BLANK RUNES
    TS_BLANK = int(mana/TS_mana)
    TS_BLANK = round(TS_BLANK,0)
    TSLabel_BLANK = Label(root,text=TS_BLANK,bg="#7caff6")
    TSLabel_BLANK.grid(column=3,row=14)
#6.FIREBOMB RUNE
    FBomb = int((mana/FBomb_mana)*FBomb_szt)
    FBombLabel = Label(root,text=(FBomb,"x"),bg="#7caff6")
    FBombLabel.grid(column=2,row=15)
    FBomb_VALUE = int(FBomb * FBomb_price)
    FBombLabel = Label(root,text=(FBomb_VALUE),bg="#7caff6",fg="#f06400")
    FBombLabel.grid(column=1,row=15)
#FBomb EXPENSE
    FBomb_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/FBomb_mana)*BLANK_price))
    FBomb_RD_COST = round(FBomb_COST,0)
    FBombLabel_COST = Label(root,text=FBomb_RD_COST,bg="#7caff6",fg="#f00640")
    FBombLabel_COST.grid(column=4,row=15)
#FBomb PROFIT    
    FBomb_PROFIT = int(FBomb_VALUE-FBomb_COST)
    FBomb_RD_PROFIT = round(FBomb_PROFIT,0)
    FBombLabel_PROFIT = Label(root,text=FBomb_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    FBombLabel_PROFIT.grid(column=5,row=15)
#FBomb BLANK RUNES
    FBomb_BLANK = int(mana/FBomb_mana)
    FBomb_BLANK = round(FBomb_BLANK,0)
    FBombLabel_BLANK = Label(root,text=FBomb_BLANK,bg="#7caff6")
    FBombLabel_BLANK.grid(column=3,row=15)
#7.ENERGYBOMB RUNE
    EBomb = int((mana/EBomb_mana)*EBomb_szt)
    EBombLabel = Label(root,text=(EBomb,"x"),bg="#7caff6")
    EBombLabel.grid(column=2,row=16)
    EBomb_VALUE = int(EBomb * EBomb_price)
    EBombLabel = Label(root,text=(EBomb_VALUE),bg="#7caff6",fg="#f06400")
    EBombLabel.grid(column=1,row=16)
#EBomb EXPENSE
    EBomb_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/EBomb_mana)*BLANK_price))
    EBomb_RD_COST = round(EBomb_COST,0)
    EBombLabel_COST = Label(root,text=EBomb_RD_COST,bg="#7caff6",fg="#f00640")
    EBombLabel_COST.grid(column=4,row=16)
#EBomb PROFIT    
    EBomb_PROFIT = int(EBomb_VALUE-EBomb_COST)
    EBomb_RD_PROFIT = round(EBomb_PROFIT,0)
    EBombLabel_PROFIT = Label(root,text=EBomb_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    EBombLabel_PROFIT.grid(column=5,row=16)
#EBomb BLANK RUNES
    EBomb_BLANK = int(mana/EBomb_mana)
    EBomb_BLANK = round(EBomb_BLANK,0)
    EBombLabel_BLANK = Label(root,text=EBomb_BLANK,bg="#7caff6")
    EBombLabel_BLANK.grid(column=3,row=16)
#8.POISONBOMB RUNE
    PBomb = int((mana/PBomb_mana)*PBomb_szt)
    PBombLabel = Label(root,text=(PBomb,"x"),bg="#7caff6")
    PBombLabel.grid(column=2,row=17)
    PBomb_VALUE = int(PBomb * PBomb_price)
    PBombLabel = Label(root,text=(PBomb_VALUE),bg="#7caff6",fg="#f06400")
    PBombLabel.grid(column=1,row=17)
#PBomb EXPENSE
    PBomb_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/PBomb_mana)*BLANK_price))
    PBomb_RD_COST = round(PBomb_COST,0)
    PBombLabel_COST = Label(root,text=PBomb_RD_COST,bg="#7caff6",fg="#f00640")
    PBombLabel_COST.grid(column=4,row=17)
#PBomb PROFIT    
    PBomb_PROFIT = int(PBomb_VALUE-PBomb_COST)
    PBomb_RD_PROFIT = round(PBomb_PROFIT,0)
    PBombLabel_PROFIT = Label(root,text=PBomb_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    PBombLabel_PROFIT.grid(column=5,row=17)
#PBomb BLANK RUNES
    PBomb_BLANK = int(mana/PBomb_mana)
    PBomb_BLANK = round(PBomb_BLANK,0)
    PBombLabel_BLANK = Label(root,text=PBomb_BLANK,bg="#7caff6")
    PBombLabel_BLANK.grid(column=3,row=17)
#9.ENERGYWALL RUNE
    EWall = int((mana/EWall_mana)*EWall_szt)
    EWallLabel = Label(root,text=(EWall,"x"),bg="#7caff6")
    EWallLabel.grid(column=2,row=18)
    EWall_VALUE = int(EWall * EWall_price)
    EWallLabel = Label(root,text=(EWall_VALUE),bg="#7caff6",fg="#f06400")
    EWallLabel.grid(column=1,row=18)
#EWall EXPENSE
    EWall_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/EWall_mana)*BLANK_price))
    EWall_RD_COST = round(EWall_COST,0)
    EWallLabel_COST = Label(root,text=EWall_RD_COST,bg="#7caff6",fg="#f00640")
    EWallLabel_COST.grid(column=4,row=18)
#EWall PROFIT    
    EWall_PROFIT = int(EWall_VALUE-EWall_COST)
    EWall_RD_PROFIT = round(EWall_PROFIT,0)
    EWallLabel_PROFIT = Label(root,text=EWall_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    EWallLabel_PROFIT.grid(column=5,row=18)
#EWall BLANK RUNES
    EWall_BLANK = int(mana/EWall_mana)
    EWall_BLANK = round(EWall_BLANK,0)
    EWallLabel_BLANK = Label(root,text=EWall_BLANK,bg="#7caff6")
    EWallLabel_BLANK.grid(column=3,row=18)
#10.FIREWALL RUNE
    FWall = int((mana/FWall_mana)*FWall_szt)
    FWallLabel = Label(root,text=(FWall,"x"),bg="#7caff6")
    FWallLabel.grid(column=2,row=19)
    FWall_VALUE = int(FWall * FWall_price)
    FWallLabel = Label(root,text=(FWall_VALUE),bg="#7caff6",fg="#f06400")
    FWallLabel.grid(column=1,row=19)
#FWall EXPENSE
    FWall_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/FWall_mana)*BLANK_price))
    FWall_RD_COST = round(FWall_COST,0)
    FWallLabel_COST = Label(root,text=FWall_RD_COST,bg="#7caff6",fg="#f00640")
    FWallLabel_COST.grid(column=4,row=19)
#FWall PROFIT    
    FWall_PROFIT = int(FWall_VALUE-FWall_COST)
    FWall_RD_PROFIT = round(FWall_PROFIT,0)
    FWallLabel_PROFIT = Label(root,text=FWall_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    FWallLabel_PROFIT.grid(column=5,row=19)
#FWall BLANK RUNES
    FWall_BLANK = int(mana/FWall_mana)
    FWall_BLANK = round(FWall_BLANK,0)
    FWallLabel_BLANK = Label(root,text=FWall_BLANK,bg="#7caff6")
    FWallLabel_BLANK.grid(column=3,row=19)
#11.ULTIMATE HEALING(UH) RUNE
    UH = int((mana/UH_mana)*UH_szt)
    UHLabel = Label(root,text=(UH,"x"),bg="#7caff6")
    UHLabel.grid(column=2,row=20)
    UH_VALUE = int(UH * UH_price)
    UHLabel = Label(root,text=(UH_VALUE),bg="#7caff6",fg="#f06400")
    UHLabel.grid(column=1,row=20)
#UH EXPENSE
    UH_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/UH_mana)*BLANK_price))
    UH_RD_COST = round(UH_COST,0)
    UHLabel_COST = Label(root,text=UH_RD_COST,bg="#7caff6",fg="#f00640")
    UHLabel_COST.grid(column=4,row=20)
#UH PROFIT    
    UH_PROFIT = int(UH_VALUE-UH_COST)
    UH_RD_PROFIT = round(UH_PROFIT,0)
    UHLabel_PROFIT = Label(root,text=UH_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    UHLabel_PROFIT.grid(column=5,row=20)
#UH BLANK RUNES
    UH_BLANK = int(mana/UH_mana)
    UH_BLANK = round(UH_BLANK,0)
    UHLabel_BLANK = Label(root,text=UH_BLANK,bg="#7caff6")
    UHLabel_BLANK.grid(column=3,row=20)
#12.INTENSE HEALING(IH) RUNE
    IH = int((mana/IH_mana)*IH_szt)
    IHLabel = Label(root,text=(IH,"x"),bg="#7caff6")
    IHLabel.grid(column=2,row=21)
    IH_VALUE = int(IH * IH_price)
    IHLabel = Label(root,text=(IH_VALUE),bg="#7caff6",fg="#f06400")
    IHLabel.grid(column=1,row=21)
#IH EXPENSE
    IH_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/IH_mana)*BLANK_price))
    IH_RD_COST = round(IH_COST,0)
    IHLabel_COST = Label(root,text=IH_RD_COST,bg="#7caff6",fg="#f00640")
    IHLabel_COST.grid(column=4,row=21)
#IH PROFIT    
    IH_PROFIT = int(IH_VALUE-IH_COST)
    IH_RD_PROFIT = round(IH_PROFIT,0)
    IHLabel_PROFIT = Label(root,text=IH_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    IHLabel_PROFIT.grid(column=5,row=21)
#IH BLANK RUNES
    IH_BLANK = int(mana/IH_mana)
    IH_BLANK = round(IH_BLANK,0)
    IHLabel_BLANK = Label(root,text=IH_BLANK,bg="#7caff6")
    IHLabel_BLANK.grid(column=3,row=21)
#13.WILD GROWTH RUNE
    WGrow = int((mana/WGrow_mana)*WGrow_szt)
    WGrowLabel = Label(root,text=(WGrow,"x"),bg="#7caff6")
    WGrowLabel.grid(column=2,row=22)
    WGrow_VALUE = int(WGrow * WGrow_price)
    WGrowLabel = Label(root,text=(WGrow_VALUE),bg="#7caff6",fg="#f06400")
    WGrowLabel.grid(column=1,row=22)
#WGrow EXPENSE
    WGrow_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/WGrow_mana)*BLANK_price))
    WGrow_RD_COST = round(WGrow_COST,0)
    WGrowLabel_COST = Label(root,text=WGrow_RD_COST,bg="#7caff6",fg="#f00640")
    WGrowLabel_COST.grid(column=4,row=22)
#WGrow PROFIT    
    WGrow_PROFIT = int(WGrow_VALUE-WGrow_COST)
    WGrow_RD_PROFIT = round(WGrow_PROFIT,0)
    WGrowLabel_PROFIT = Label(root,text=WGrow_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    WGrowLabel_PROFIT.grid(column=5,row=22)
#WGrow BLANK RUNES
    WGrow_BLANK = int(mana/WGrow_mana)
    WGrow_BLANK = round(WGrow_BLANK,0)
    WGrowLabel_BLANK = Label(root,text=WGrow_BLANK,bg="#7caff6")
    WGrowLabel_BLANK.grid(column=3,row=22)
#14.MAGICWALL RUNE
    MWall = int((mana/MWall_mana)*MWall_szt)
    MWallLabel = Label(root,text=(MWall,"x"),bg="#7caff6")
    MWallLabel.grid(column=2,row=23)
    MWall_VALUE = int(MWall * MWall_price)
    MWallLabel = Label(root,text=(MWall_VALUE),bg="#7caff6",fg="#f06400")
    MWallLabel.grid(column=1,row=23)
#MWall EXPENSE
    MWall_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/MWall_mana)*BLANK_price))
    MWall_RD_COST = round(MWall_COST,0)
    MWallLabel_COST = Label(root,text=MWall_RD_COST,bg="#7caff6",fg="#f00640")
    MWallLabel_COST.grid(column=4,row=23)
#MWall PROFIT    
    MWall_PROFIT = int(MWall_VALUE-MWall_COST)
    MWall_RD_PROFIT = round(MWall_PROFIT,0)
    MWallLabel_PROFIT = Label(root,text=MWall_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    MWallLabel_PROFIT.grid(column=5,row=23)
#MWall BLANK RUNES
    MWall_BLANK = int(mana/MWall_mana)
    MWall_BLANK = round(MWall_BLANK,0)
    MWallLabel_BLANK = Label(root,text=MWall_BLANK,bg="#7caff6")
    MWallLabel_BLANK.grid(column=3,row=23)
#15.PARALYZE RUNE
    Paral = int((mana/Paral_mana)*Paral_szt)
    ParalLabel = Label(root,text=(Paral,"x"),bg="#7caff6")
    ParalLabel.grid(column=2,row=24)
    Paral_VALUE = int(Paral * Paral_price)
    ParalLabel = Label(root,text=(Paral_VALUE),bg="#7caff6",fg="#f06400")
    ParalLabel.grid(column=1,row=24)
#Paral EXPENSE
    Paral_COST = int(SINGLE_COST + DOUBLE_COST + SOFTMP_COST + LIFER_COST + TIARA_COST + PLASMA_COST + ((mana/Paral_mana)*BLANK_price))
    Paral_RD_COST = round(Paral_COST,0)
    ParalLabel_COST = Label(root,text=Paral_RD_COST,bg="#7caff6",fg="#f00640")
    ParalLabel_COST.grid(column=4,row=24)
#Paral PROFIT    
    Paral_PROFIT = int(Paral_VALUE-Paral_COST)
    Paral_RD_PROFIT = round(Paral_PROFIT,0)
    ParalLabel_PROFIT = Label(root,text=Paral_RD_PROFIT,bg="#7caff6",fg="#0f6400")
    ParalLabel_PROFIT.grid(column=5,row=24)
#Paral BLANK RUNES
    Paral_BLANK = int(mana/Paral_mana)
    Paral_BLANK = round(Paral_BLANK,0)
    ParalLabel_BLANK = Label(root,text=Paral_BLANK,bg="#7caff6")
    ParalLabel_BLANK.grid(column=3,row=24)

    #---FRAME---#
    costlabel = Label(root,text="Expense:",bg="#7caff6",fg="#f00640")
    costlabel.grid(column=4, row=8)

    worthlabel = Label(root,text="Value:",bg="#7caff6",fg="#f06400")
    worthlabel.grid(column=1, row=8)

    profitlabel = Label(root,text="Profit:",bg="#7caff6",fg="#0f6400")
    profitlabel.grid(column=5, row=8)

    countlabel = Label(root,text="Qty:",bg="#7caff6")
    countlabel.grid(column=2, row=8)

    blankslabel = Label(root,text="Blanks:",bg="#7caff6")
    blankslabel.grid(column=3, row=8)

    foodlabel = Label(root,text="Food Qty:",bg="#7caff6")
    foodlabel.grid(column=2, row=30)

    manalabel = Label(root,text="Generated Mana:",bg="#7caff6",fg="#000f64")
    manalabel.grid(column=0, row=30)

#---RUNES LABELS 0 COLUMN---#
    SDlabel = Label(root,text="SD:",bg="#7caff6")
    SDlabel.grid(column=0, row=10)
    GFBlabel = Label(root,text="GFB:",bg="#7caff6")
    GFBlabel.grid(column=0, row=11)
    AVAlabel = Label(root,text="AVA:",bg="#7caff6")
    AVAlabel.grid(column=0, row=12)
    SSlabel = Label(root,text="SS:",bg="#7caff6")
    SSlabel.grid(column=0, row=13)
    Thunderlabel = Label(root,text="TS:",bg="#7caff6")
    Thunderlabel.grid(column=0, row=14)
    FBlabel = Label(root,text="FBomb:",bg="#7caff6")
    FBlabel.grid(column=0, row=15)
    EBlabel = Label(root,text="EBomb:",bg="#7caff6")
    EBlabel.grid(column=0, row=16)
    PBlabel = Label(root,text="PBomb:",bg="#7caff6")
    PBlabel.grid(column=0, row=17)
    EWlabel = Label(root,text="EWall:",bg="#7caff6")
    EWlabel.grid(column=0, row=18)
    FWlabel = Label(root,text="FWall:",bg="#7caff6")
    FWlabel.grid(column=0, row=19)
    UHlabel = Label(root,text="UH:",bg="#7caff6")
    UHlabel.grid(column=0, row=20)
    IHlabel = Label(root,text="IH:",bg="#7caff6")
    IHlabel.grid(column=0, row=21)
    WGlabel = Label(root,text="WGrow:",bg="#7caff6")
    WGlabel.grid(column=0, row=22)
    MWlabel = Label(root,text="MWall:",bg="#7caff6")
    MWlabel.grid(column=0, row=23)
    PARlabel = Label(root,text="Paral:",bg="#7caff6")
    PARlabel.grid(column=0, row=24)

def clear():
    print('')
    #e.delete(0, END)

#Tiara of Power Entry
TiaraPrice_label = Label(root,text="Tiara:",bg="#7caff6")
TiaraPrice_label.grid(column=0, row=0)
#Life Ring Entry   
LFPrice_label = Label(root,text="Life Ring:",bg="#7caff6")
LFPrice_label.grid(column=0, row=1)
#Ring of Healing Entry
ROHPrice_label = Label(root,text="RoH:",bg="#7caff6")
ROHPrice_label.grid(column=0, row=2)
#Collar of Green Plasma Amulet
GreenPlasma_label = Label(root,text="Green Plasma:",bg="#7caff6")
GreenPlasma_label.grid(column=0, row=3)
#Time
Duration_label = Label(root,text="Time:",bg="#7caff6")
Duration_label.grid(column=0, row=4)
#CALCULATE BUTTON
calc_button = Button(root, text="Calculate", bg="#97DB98" , command=calculate)
calc_button.grid(column=2, row=4)

root.mainloop()