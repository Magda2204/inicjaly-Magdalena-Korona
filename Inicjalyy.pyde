def setup():
    size(400, 400)
    textSize(128)
    textAlign(CENTER)
def draw():
    text("M", width/2-75, (height/3)*2)
    #print(mouseX, mouseY)
    #print(hex(get(mouseX, mouseY)))
    print(LEFT)
    if keyPressed:
        print(keyCode)
        text("K", width/2+75, (height/3)*2)
    
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255, 100)
    s.noStroke()
    s.vertex(50, (height/4)*3)
    s.vertex(width/2-20, (height/4)*3+30)
    s.vertex(width/2, (height/4)*3)
    s.vertex(width/2+20, (height/4)*3-30)
    s.vertex(width-50, (height/4)*3)
    s.endShape(CLOSE)
    shape(s, 25, 25)
