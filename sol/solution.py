
import pygame,sys

pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
CYAN=(0,255,255)
GREY=(169,169,169)
widht,height=900,700
screen=pygame.display.set_mode((widht,height))
pygame.display.set_caption("solution")
clock = pygame.time.Clock()
font=pygame.font.SysFont('comic sans',20)
FPS=60

#-------------------elements dictionnairy : element--->list[COLOR,opacity,colorName,pH,cons]------------------------------

#needs more elements
elements={"CuCl4 2-":[(224, 224, 128, 255),'opaque','light yellow','any'], #piss color
"Ag3+":[(128, 64, 0, 255),"opaque",'Marron foncé','any'],#brown color
"Ti3+":[(128, 0, 128, 255),'opaque','violet','any'],#violet color
"VO2+":[(32, 160, 192, 255),'opaque','cyan','any'],#sky color
"Cr2O2−7":[(224, 128, 0, 255),'opaque','orange','any'],#orange color
"Co2+":[(255, 0, 255, 255),'opaque','pink','any'],#pink color
}

myPath="python\\pygame\\" #remove this from the asset importing section 
#----------------------import +scale assets---------------
paletteImage=pygame.image.load(myPath+"sol\\assets\\pallet2.png")
tubeImage=pygame.image.load(myPath+"sol\\assets\\tubeE.png")
plusImage=pygame.image.load(myPath+"sol\\assets\\plus.png")
plusImage=pygame.transform.scale(plusImage,(30,30))
minusImage=pygame.image.load(myPath+"sol\\assets\\minus.png")
minusImage=pygame.transform.scale(minusImage,(30,30))
panelImage=pygame.image.load(myPath+"sol\\assets\\gPanel.png")
panelImage=pygame.transform.scale(panelImage,(100,85))
brownPanelImage=pygame.image.load(myPath+"sol\\assets\\panel.png")
brownPanelImage=pygame.transform.scale(brownPanelImage,(100,85))
numPadImage=pygame.image.load(myPath+"sol\\assets\\numPad.png")
numPadImage=pygame.transform.scale(numPadImage,(100,130))

#--------------------text drawing fonction------------------
def drawText(text,font,color,surface,x,y):
    textObj=font.render(str(text),1,color)
    textRect=textObj.get_rect()
    textRect.topleft=(x,y)
    surface.blit(textObj,textRect)

#----------------------Finder--------------------------
def getElement(elements,color,opacity,ph,cons):
    global adv
    #element--->list[COLOR,opacity,colorName,pH,cons]
    for element,value in elements.items():
        
        if not adv:
            if color==value[0] and opacity==value[1]:
                drawText("for the color ",font,BLACK,screen,50,500)
                drawText(value[2],font,BLACK,screen,130,500)
                drawText('and opacity ',font,BLACK,screen,170,500)
                drawText(value[1],font,BLACK,screen,250,500)
                drawText("your solute is : ",font,BLACK,screen,300,500)
                drawText(element,font,BLACK,screen,410,500)


            if color !=value[0] and opacity !=value[1]:#not finished 
                drawText("Please choose another color couldn't find the solution",font,BLACK,screen,50,600)
        
        
        else:
            if color==value[0] and opacity==value[1] and ph==value[3] and cons==value[4]:
                drawText("for the color ",font,BLACK,screen,50,500)
                drawText(value[2],font,BLACK,screen,130,500)
                drawText('and opacity ',font,BLACK,screen,170,500)
                drawText(value[1],font,BLACK,screen,250,500)
                drawText('and ph ',font,BLACK,screen,170,500)
                drawText(value[3],font,BLACK,screen,170,500)
                drawText('and consontration ',font,BLACK,screen,170,500)
                drawText(value[4],font,BLACK,screen,170,500)
                drawText("your solute is : ",font,BLACK,screen,300,500)
                drawText(element,font,BLACK,screen,410,500)
            elif color != value[0] :
                drawText("Please choose another color",font,BLACK,screen,50,500)



#------------------------alpha---------------------------
def draw_rect_alpha(screen, color,alpha,size,coords):
    s = pygame.Surface(size)  # the size of your rect
    s.set_alpha(alpha)                # alpha level
    s.fill(color)           # this fills the entire surface
    screen.blit(s, coords)    # (0,0) are the top-left coordinates

#----------------------main program----------------------
def main():
    run=True
    color=(255,255,255,255)
    global opacity
    opacity='opaque'
    global ph
    ph=0
    global cons
    cons=""
    global click
    click=False
    global mx,my
    mx,my=0,0
    confirm=False
    global adv
    adv=False
    alpha=255
    
    while run:
        clock.tick(FPS)
        screen.fill(WHITE)
        mx,my=pygame.mouse.get_pos()

        #----------------------color+tube choosing drawing--------------------
        
        paletteBorder=pygame.Rect(50,52,175,190)
        screen.blit(paletteImage,(50,50))
        screen.blit(tubeImage,(800,100))# tube drawing
        screen.blit(brownPanelImage,(770,30))
        clearRect=pygame.Rect(770,40,100,50)
        drawText("clear",font,BLACK,screen,800,60)
        
        #----------------------------Opacity drawing----------------------------
        
        screen.blit(brownPanelImage,(50,290))
        drawText('Opacity',font,BLACK,screen,70,320)
        transRect=pygame.Rect(500,300,100,50)
        screen.blit(panelImage,(500,290))
        drawText("Transparent",font,BLACK,screen,515,315)
        opacRect=pygame.Rect(350,300,100,50)
        screen.blit(panelImage,(350,290))
        drawText("Opaque",font,BLACK,screen,365,315)
        transvideRect=pygame.Rect(200,300,100,50)
        screen.blit(panelImage,(200,290))
        drawText("Translucent",font,BLACK,screen,215,315)
        
        #---------------------------advanced option------------------------------
        screen.blit(brownPanelImage,(50,400))
        advRect=pygame.Rect(50,410,100,50)
        drawText("advanced",font,BLACK,screen,60,430)
        screen.blit(brownPanelImage,(250,400))
        drawText("hide advanced",font,BLACK,screen,255,430)
        hideAdvRect=pygame.Rect(250,410,100,50)
        if advRect.collidepoint(mx,my):
            if click:
                adv=True
        if hideAdvRect.collidepoint(mx,my):
            if click:
                adv=False

        if adv:
            advanced()
       
        #------------------------final step drawing------------------------
        
        screen.blit(brownPanelImage,(620,30))
        confirmRect=pygame.Rect(620,30,100,50)
        drawText("Confirm",font,BLACK,screen,650,55)
        if confirmRect.collidepoint(mx,my):
            if click:
                confirm=True

        draw_rect_alpha(screen, color,alpha,(43,150),(805,240))
        draw_rect_alpha(screen,color,alpha,(35,5),(809,390))
        draw_rect_alpha(screen,color,alpha,(30,3),(813,395))
        
        #-------------------------program system-------------------------
        if paletteBorder.collidepoint(mx,my): #color choice
            if click:
                color=screen.get_at((mx,my))
                print(color)

        if clearRect.collidepoint(mx,my):
            if click:
                color=WHITE
                cons=""
                opacity='opaque'
                ph=0
                alpha=255
                confirm=False
        
        if opacRect.collidepoint(mx,my):
            if click:
                opacity="opaque"
                alpha=255
                
        if transRect.collidepoint(mx,my):
            if click:
                opacity="transparent"
                alpha=0
                
        if transvideRect.collidepoint(mx,my):
            if click:
                opacity="translucent"
                alpha=100
                
        if confirm:
            getElement(elements,color,opacity,ph,cons)
           
        click=False
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True


       
        
        pygame.display.update()
    pygame.quit()
    sys.exit()

def advanced():
    global click
    global ph
    global mx,my
    global cons
    #-----------------------PH drawing--------------------------------
    screen.blit(brownPanelImage,(250,50))
    drawText("pH",font,BLACK,screen,270,75)
    addPh=pygame.Rect(370,70,30,30)
    subPh=pygame.Rect(440,70,30,30)
    screen.blit(plusImage,(370,70))
    screen.blit(minusImage,(440,70))
    drawText(ph,font,BLACK,screen,415,78)
    if addPh.collidepoint(mx,my):
        if click:
            ph+=1
            if ph>=14:
                ph=14
    if subPh.collidepoint(mx,my):
        if click:
            ph-=1
            if ph<0:
                ph=0  
     #-----------------------------concentration drawing----------------------

    screen.blit(brownPanelImage,(250,150))
    screen.blit(panelImage,(400,150))
    screen.blit(panelImage,(550,150))
    molRect=pygame.Rect(550,160,100,50)
    glRect=pygame.Rect(670,160,100,50)
    drawText("mol/L",font,BLACK,screen,570,175)
    screen.blit(panelImage,(670,150))
    drawText("g/L",font,BLACK,screen,710,175)
    drawText("Concentration",font,BLACK,screen,255,175)
    screen.blit(numPadImage,(650,270))#450/480
    drawText(cons,font,BLACK,screen,420,180)

    if glRect.collidepoint(mx,my):
        if click:
            unit="g/L"
    if molRect.collidepoint(mx,my):
        if click:
            unit="mol/L"
            #color change add

    zeroRect=pygame.Rect(690,370,25,25)
    if zeroRect.collidepoint(mx,my):
        if click:
            cons=cons+"0"
    backRect=pygame.Rect(720,370,25,25)
    if backRect.collidepoint(mx,my):
        if click:
            cons=cons[:-1]
    dotRect=pygame.Rect(655,370,25,25)
    if dotRect.collidepoint(mx,my):
        if click:
            cons=cons+"."
    oneRect=pygame.Rect(655,340,25,25)
    if oneRect.collidepoint(mx,my):
        if click:
            cons=cons+"1"
    twoRect=pygame.Rect(689,338,25,25)
    if twoRect.collidepoint(mx,my):
        if click:
            cons=cons+"2"
    threeRect=pygame.Rect(720,340,25,25)
    if threeRect.collidepoint(mx,my):
        if click:
            cons=cons+"3"
    fourRect=pygame.Rect(655,308,25,25)
    if fourRect.collidepoint(mx,my):
        if click:
            cons=cons+"4"
    fiveRect=pygame.Rect(689,308,25,25)
    if fiveRect.collidepoint(mx,my):
        if click:
            cons=cons+"5"
    sixRect=pygame.Rect(720,308,25,25)
    if sixRect.collidepoint(mx,my):
        if click:
            cons=cons+"6"
    sevenRect=pygame.Rect(655,276,25,25)
    if sevenRect.collidepoint(mx,my):
        if click:
            cons=cons+"7"
    eightRect=pygame.Rect(689,276,25,25)
    if eightRect.collidepoint(mx,my):
        if click:
            cons=cons+"8"
    nineRect=pygame.Rect(720,276,25,25)
    if nineRect.collidepoint(mx,my):
        if click:
            cons=cons+"9"
    if len(cons)==8:
        pass

main()