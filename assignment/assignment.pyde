def setup():
    size(600, 700)
    textSize(70)
    global violet, dark_violet, pink # w tensposób jest czytelniej bez komentarzy - kod sam się komentuje :)
    violet = "#EC98F2"
    dark_violet = "#671EB7"
    pink = "#FF29D8"
    
def draw():
    clear()
    
    background(violet)  # jw.
    fill(dark_violet)
    
    text('LM', width/7, height/5)
    
    # zmiana koloru inicjałów po nacisnięciu jednego z przycisków
    if keyPressed:
        if key == 'l' or key == 'm' or key == 'L' or key == 'M':
            fill(pink)
            text('LM', width/7, height/5)
    
    s = createShape()
    s.beginShape()
    s.fill(245, 222, 109) #F5DE6D - kolor żółty
    s.vertex(252, 161)
    s.vertex(294, 117)
    s.vertex(335, 159)
    s.vertex(230, 371)
    s.vertex(374, 371)
    s.endShape(CLOSE)
    shape(s, 0, 0)
    
    s2 = createShape()
    s2.beginShape()
    s2.fill(245, 222, 109)
    s2.vertex(254, 371)
    s2.vertex(254, 456)
    s2.vertex(278, 456)
    s2.vertex(278, 371)
    s2.vertex(326, 371)
    s2.vertex(326, 456)
    s2.vertex(350, 456)
    s2.vertex(350, 371)
    s2.endShape(CLOSE)
    shape(s2, 0, 0)
    
    # zmiana koloru inicjałów po najechaniu na kształt
    if hex(get(mouseX, mouseY)) == 'FFF5DE6D':  # kolor żółty
        fill(245, 222, 109)
        text('LM', width/7, height/5)
        
    #2pkt
