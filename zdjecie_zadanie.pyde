add_library('pdf')

def setup():
    global i
    global nazwa
    global ext
    nazwa = "id_photo"
    ext = ".jpg"
    i = loadImage(nazwa+ext)
    beginRecord(PDF, "mojPDFinny.pdf")
    print(type(i))
    imageMode(CENTER)
def draw():
    global i
    global nazwa
    global ext
    image(i, width/2,height/2, width, height)
    endRecord()
    #save(nazwa+".edited"+ext)
