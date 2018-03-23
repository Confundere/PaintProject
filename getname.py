from pygame import *
from glob import *

# i will only add comments to parts of code i modified
showfilesflag = 0 # flag

def getName(screen,showFiles):
    ans = ""
    actualans = ""              # ans is the letters you see in the text box, actualans is what this program actually returns
                                # there's 2 ans because if the user types a really long text, then ans would show the shortened version of the text, while actualans will show the actual text the user wrote
    cavestoryfnt = font.Font("Cave_Story.ttf",30) # custom font
    back = screen.copy()
    textArea = Rect(875,100,325,25)
    if showFiles:
        pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
        n = len(pics)
        global choiceArea # because it's in a def, i have to use global to make it "known" by the rest of the code not in the def
        choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
        draw.rect(screen,(255,255,255),choiceArea)
        draw.rect(screen,(0,0,0),choiceArea,1)
        for i in range(n):
            screentxtPic = cavestoryfnt.render(pics[i], True, (0,111,0))   #
            screen.blit(screentxtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
            global showfilesflag
            showfilesflag = 1 # knows that it's in "showfiles" mode and not "text tool" mode
    else:
        showfilesflag = 0

    cursorShow = 0
    myclock = time.Clock()
    typing = True
    while typing:
        cursorShow += 1
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    if len(ans)>0: # if there's a letter that is already typed...
                        ans = ans[:-1] # removes the last letter
                        actualans = actualans[:-1] # imitates ans
                    if len(actualans)>= 23: # if the word is more than 23 letters long (23 because that's how many capital Ws will fit in the textbox before going outside of the textbox
                        ans = actualans[(len(actualans)-len(ans)-1):(len(actualans)-len(ans))]+ans
                        # ans = "urfourfourfourfourfours" 23 letters and it's missing a "fo" at the beginning the missing "f" is explained later below the code
                        # actualans = "fourfourfourfourfourfours" 24 letters and it's not missing a "fo"
                        # so when pressing backspace, it takes the last letter ans deleted (in this case, it's the letter "o" and it adds it back to ans
                        # ans = "ourfourfourfourfourfour" it's missing a "s" because the user just backspaced it
                        # pressing backspace again will result
                        # ans = "fourfourfourfourfourfou"
                elif e.key == K_KP_ENTER or e.key == K_RETURN or e.key == K_ESCAPE:
                    if e.key == K_ESCAPE:
                        ans = ""
                        actualans = ""
                    typing = False
                elif e.key < 256:
                    ans += e.unicode
                    actualans+= e.unicode
                    if len(ans)> 23: # the part where the missing "f" is explained
                        ans = ans[1:len(ans)] # because the textbox could only fit 23 letters i have to hide the excess letters in the beginning
                        # the way i did that is by deleting the first letter the user entered
                        # so "fourfourfourfourfourfou" 23 letters
                        # will become "ourfourfourfourfourfour" still 23 letters
                        # this is the only part of the code where actualans does not imitate ans, because actualans will not appear in the textbox so the 23 letter rule does not apply to it
            if e.type == MOUSEBUTTONDOWN and showfilesflag == 1:
                mb = mouse.get_pressed()
                mx,my = mouse.get_pos()
                if choiceArea.collidepoint(mx,my) and mb[0] == 1: # if the user presses one of the boxes below the textbox
                    i = int((my/textArea.height)-5) # will determine which "box" it is
                    ans  = pics[i] # ans will become the name of the box selected
                    actualans = ans # actualans will also change to match
            if e.type == MOUSEBUTTONUP:     # added e.type otherwise the mouse won't appear after clicking the text tool in my paint program
                mouse.set_visible(True)

        screentxtPic = cavestoryfnt.render(ans, True, (0,0,0))   # ans is shown in the textbox
        draw.rect(screen,(255,255,255),textArea)
        draw.rect(screen,(0,0,0),textArea,2)
        screen.blit(screentxtPic,(textArea.x+3,textArea.y+2))
        if cursorShow // 50 % 2 == 1:
            cx = textArea.x+screentxtPic.get_width()+3
            cy = textArea.y+3
            draw.rect(screen,(255,0,0),(cx,cy,2,textArea.height-6))
        myclock.tick(100)
        display.flip()
    screen.blit(back,(0,0))
    return actualans # ans is shown in the textbox but actualans will be returned to the user

