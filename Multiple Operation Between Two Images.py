import cv2
import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageFilter
import numpy as np
from matplotlib import pyplot as plt

window = Tk()
window.geometry("1150x650+100+30")
window.configure(background='green')
window.title('Final Lab Report')

out = tkinter.Label(window,text ='Perform Your Operation',fg='green',bg='black',font=('Baskerville Old Face',14))
out.pack()
resout=tkinter.Label(window,text ='OUTPUT',fg='green',bg='black',font=('Baskerville Old Face',14))
resout.place (x=528,y=300)

def insertImage1():
    global imgf
    path = filedialog.askopenfilename(title="Select first Image")
    imgf = cv2.imread(path)
    imgf1 = Image.fromarray(imgf)
    imgf1 = ImageTk.PhotoImage(imgf1)
    imgout = tkinter.Label(window, image=imgf1)
    imgout.image = imgf1
    imgout.place(x=20, y=90)

def insertImage2():
    global imgs
    path2 = filedialog.askopenfilename(title="Select Second Image")
    imgs = cv2.imread(path2)
    imgf2 = Image.fromarray(imgs)
    imgf2 = ImageTk.PhotoImage(imgf2)
    imgout2 = tkinter.Label(window, image=imgf2)
    imgout2.image = imgf2
    imgout2.place(x=825,y=90)

photo = PhotoImage(file="icon-2488093.png")
photoimage = photo.subsample(10,10)
addImgBtn1 = Button (window, text="Browse Image\n1", image=photoimage,compound=LEFT, fg="black", bg="red",command=insertImage1)
addImgBtn1.place(x=100,y=30)

addImgBtn2 = Button(window, text="Browse Image\n2", image=photoimage, compound=RIGHT, fg="black", bg="red", command=insertImage2)
addImgBtn2.place(x=900,y=30)

def addope():
    add = cv2.addWeighted(imgf, 0.5, imgs, 0.3, 0)
    addimg = Image.fromarray(add)
    addimg = ImageTk.PhotoImage(addimg)
    imgout3 = tkinter.Label(window, image=addimg)
    imgout3.image = addimg
    imgout3.place(x=447, y=350)

addiBtn = Button(window, text="ADD", width=10, fg="black", bg="red" ,command=addope)
addiBtn.place(x=360, y=50)

def subope():
    sub = cv2.subtract(imgf, imgs)
    subimg = Image.fromarray(sub)
    subimg = ImageTk.PhotoImage(subimg)
    imgout3 = tkinter.Label(window, image=subimg)
    imgout3.image = subimg
    imgout3.place(x=447, y=350)

subBtn = Button(window, text="SUBTRACT", width=10, fg="black",bg="red", command=subope)
subBtn.place(x=360, y=80)

def Bit_and():
    bitAnd = cv2.bitwise_and(imgf, imgs)
    bitandimg = Image.fromarray(bitAnd)
    bitandimg = ImageTk.PhotoImage(bitandimg)
    imgout3 = tkinter.Label(window, image=bitandimg)
    imgout3.image = bitandimg
    imgout3.place(x=447, y=350)


andBtn = Button(window, text="AND", width=10, fg="black", bg="red", command=Bit_and)
andBtn.place(x=360, y=110)


def Bit_or():
    bitOr = cv2.bitwise_or(imgf, imgs)
    bitorimg = Image.fromarray(bitOr)
    bitorimg = ImageTk.PhotoImage(bitorimg)
    imgout3 = tkinter.Label(window, image=bitorimg)
    imgout3.image = bitorimg
    imgout3.place(x=447, y=350)

orBtn = Button(window, text="OR", width=10, fg="black", bg="red", command=Bit_or)
orBtn.place(x=360, y=140)

def Bit_nor():
    nor = cv2.bitwise_or(imgf, imgs)
    nor2 = cv2.bitwise_not(nor)
    norimg = Image.fromarray(nor2)
    norimg = ImageTk.PhotoImage(norimg)
    imgout3 = tkinter.Label(window, image=norimg)
    imgout3.image = subimg
    imgout3.place(x=447, y=350)


subBtn = Button(window, text="NOR", width=10, fg="black", bg="red", command=subope)
subBtn.place(x=360, y=170)

def Bit_not():
    bitNot = cv2.bitwise_not(imgf, imgs)
    bitnotimg = Image.fromarray(bitNot)
    bitnotimg = ImageTk.PhotoImage(bitnotimg)
    imgout3 = tkinter.Label(window, image=bitnotimg)
    imgout3.image = bitnotimg
    imgout3.place(x=447, y=350)

notBtn = Button(window, text="NOT", width=10, fg="black", bg="red", command=Bit_not)
notBtn.place(x=360, y=200)


def Bit_xor():
    bitxor = cv2.bitwise_xor(imgf, imgs)
    bitxorimg = Image.fromarray(bitxor)
    bitxorimg = ImageTk.PhotoImage(bitxorimg)
    imgout3 = tkinter.Label(window, image=bitxorimg)
    imgout3.image = bitxorimg
    imgout3.place(x=447, y=350)

xorBtn = Button(window, text="XOR", width=10, fg="black", bg="red", command=Bit_xor)
xorBtn.place(x=360, y=230)

def readImage():
    path = filedialog.askopenfilename()
    image1 = cv2.imread(path)
    imgout3 = tkinter.Label(window, text="Successfully Read\nBrowse Image 1", width=15, fg="dark blue",bg="yellow",font=('Times New Roman',24))
    imgout3.place(x=449, y=400)

readBtn = Button(window, text="IMAGE READ", width=10, fg="black", bg="red", command=readImage)
readBtn.place(x=360,y=260)

def showImage():
    showimg = Image.fromarray(imgf)
    showimg = ImageTk.PhotoImage(showimg)
    imgout3 = tkinter.Label(window, image=showimg)
    imgout3.image = showimg
    imgout3.place(x=447, y=350)

showBtn = Button(window, text="IMAGE SHOW", width=10, fg="black", bg="red", command=showImage)
showBtn.place(x=530,y=50)

def writeImage():
    cv2.imwrite("write.jpg", imgf)
    imgout3 = tkinter.Label(window, text="Successfully Write\nBrowse Image 1", width=15, fg="dark blue",bg="yellow",font=('Times New Roman',24))
    imgout3.place(x=449, y=400)

writeBtn = Button(window, text="IMAGE WRITE", width=10, fg="black", bg="red", command=writeImage)
writeBtn.place(x=530,y=80)

def con2gray():
    gray = cv2.cvtColor(imgf, cv2.COLOR_BGR2GRAY)
    grayimg = Image.fromarray(gray)
    grayimg = ImageTk.PhotoImage(grayimg)
    imgout3 = tkinter.Label(window, image=grayimg)
    imgout3.image = grayimg
    imgout3.place(x=447, y=350)

con2grayBtn = Button(window, text="CONV-GRAY", width=10, fg="black", bg="red", command=con2gray)
con2grayBtn.place(x=530,y=110)

def con2bw():
    bandwimage = cv2.cvtColor(imgf, cv2.COLOR_BGR2GRAY)
    (thresh, bandwimage) = cv2.threshold(bandwimage, 127, 255, cv2.THRESH_BINARY)
    bwimg = Image.fromarray(bandwimage)
    bwimg = ImageTk.PhotoImage(bwimg)
    imgout3 = tkinter.Label(window, image=bwimg)
    imgout3.image = bwimg
    imgout3.place(x=447, y=350)

con2bwBtn = Button(window, text="CONV-B&W", width=10, fg="black", bg="red", command=con2bw)
con2bwBtn.place(x=530,y=140)

def con2neg():
    contneg = cv2.bitwise_not(imgf)
    negimg = Image.fromarray(contneg)
    negimg = ImageTk.PhotoImage(negimg)
    imgout3 = tkinter.Label(window, image=negimg)
    imgout3.image = negimg
    imgout3.place(x=447, y=350)

negBtn = Button(window, text="CONV-NEG", width=10, fg="black", bg="red", command=con2neg)
negBtn.place(x=530, y=170)

def mirror():
    mir = cv2.flip(imgf, 1)
    mirimg = Image.fromarray(mir)
    mirimg = ImageTk.PhotoImage(mirimg)
    imgout3 = tkinter.Label(window, image=mirimg)
    imgout3.image = mirimg
    imgout3.place(x=447, y=350)

mirBtn = Button(window, text="MIRROR", width=10, fg="black", bg="red", command=mirror)
mirBtn.place(x=530, y=200)

def sharp():
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    sharp = cv2.filter2D(imgf, -1, kernel)
    mirimg = Image.fromarray(sharp)
    mirimg = ImageTk.PhotoImage(mirimg)
    imgout3 = tkinter.Label(window, image=mirimg)
    imgout3.image = mirimg
    imgout3.place(x=447, y=350)

sharpBtn = Button(window, text="SHARP", width=10, fg="black", bg="red", command=sharp)
sharpBtn.place(x=530, y=230)

def resize():
    scale_percent = 60  # percent of original size
    width = int(imgf.shape[1] * scale_percent / 100)
    height = int(imgf.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(imgf, dim, interpolation=cv2.INTER_AREA)

    resimg = Image.fromarray(resized)
    resimg = ImageTk.PhotoImage(resimg)
    imgout3 = tkinter.Label(window, image=resimg)
    imgout3.image = resimg
    imgout3.place(x=447, y=350)

resBtn = Button(window, text="RESIZE", width=10, fg="black", bg="red", command=resize)
resBtn.place(x=530, y=260)

def rotate():
    width, height = imgf.shape[0:2]
    imgRotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
    rotateimg = cv2.warpAffine(imgf, imgRotationMatrix, (width, height))
    rotimg = Image.fromarray(rotateimg)
    rotimg = ImageTk.PhotoImage(rotimg)
    imgout3 = tkinter.Label(window, image=rotimg)
    imgout3.image = rotimg
    imgout3.place(x=347, y=350)

rotBtn = Button(window, text="ROTATE", width=10, fg="black", bg="red", command=rotate)
rotBtn.place(x=700, y=50)

def blur():
    blur = cv2.blur(imgf, (10, 10))
    blurimg = Image.fromarray(blur)
    blurimg = ImageTk.PhotoImage(blurimg)
    imgout3 = tkinter.Label(window, image=blurimg)
    imgout3.image = blurimg
    imgout3.place(x=447, y=350)

blurBtn = Button(window, text="BLUR", width=10, fg="black", bg="red", command=blur)
blurBtn.place(x=700, y=80)

def noise():
    gauss = np.random.normal(0, 1, imgf.size)
    gauss = gauss.reshape(imgf.shape[0], imgf.shape[1], imgf.shape[2]).astype('uint8')
    noise = imgf + imgf * gauss
    noiseimg = Image.fromarray(noise)
    noiseimg = ImageTk.PhotoImage(noiseimg)
    imgout3 = tkinter.Label(window, image=noiseimg)
    imgout3.image = noiseimg
    imgout3.place(x=447, y=350)

noiseBtn = Button(window, text="NOISE", width=10, fg="black", bg="red", command=noise)
noiseBtn.place(x=700, y=110)

def denoise():
    denoise = cv2.fastNlMeansDenoisingColored(imgf, None, 10, 10, 7, 21)
    denimg = Image.fromarray(denoise)
    denimg = ImageTk.PhotoImage(denimg)
    imgout3 = tkinter.Label(window, image=denimg)
    imgout3.image = denimg
    imgout3.place(x=447, y=350)

denBtn = Button(window, text="De-NOISE", width=10, fg="black", bg="red", command=denoise)
denBtn.place(x=700, y=140)

def powerlaw():
    gamma = np.array(255 * (imgf / 255) ** 2.5, dtype='uint8')
    gammaimg = Image.fromarray(gamma)
    gammaimg = ImageTk.PhotoImage(gammaimg)
    imgout3 = tkinter.Label(window, image=gammaimg)
    imgout3.image = gammaimg
    imgout3.place(x=447, y=350)

denBtn = Button(window, text="POWER_LAW", width=10, fg="black", bg="red", command=powerlaw)
denBtn.place(x=700, y=170)

def logarithm():
    c = 255 / (np.log(1 + np.max(imgf)))
    log = c *np.log(1 + imgf)
    log = np.array(log, dtype=np.uint8)
    logimg = Image.fromarray(log)
    logimg = ImageTk.PhotoImage(logimg)
    imgout3 = tkinter.Label(window, image=logimg)
    imgout3.image = logimg
    imgout3.place(x=447, y=350)

denBtn = Button(window, text="LOGARITHM", width=10, fg="black", bg="red", command=logarithm)
denBtn.place(x=700, y=200)

def filter():
    filt = cv2.medianBlur(imgf, 3)
    filtimg = Image.fromarray(filt)
    filtimg = ImageTk.PhotoImage(filtimg)
    imgout3 = tkinter.Label(window, image=filtimg)
    imgout3.image = filtimg
    imgout3.place(x=447, y=350)

filtBtn = Button(window, text="FILTER", width=10, fg="black", bg="red", command=filter)
filtBtn.place(x=700, y=230)

def histogram():
    histr = cv2.calcHist([imgf], [0], None, [256], [0, 256])
    histimg = Image.fromarray(histr)
    plt.plot(histr)
    plt.show()

histoBtn = Button(window, text="HISTOGRAM", width=10, fg="black", bg="red", command=histogram)
histoBtn.place(x=700, y=260)

def subby():
    imgout3 = tkinter.Label(window,text="SHAMOL KUMAR DAS\nBatch: 39(1st shift)\nDept: CSE\nRoll: 19\nDhaka International University", width=23, fg="black",bg="green",font=('Times New Roman',24))
    imgout3.place(x=380, y=350)

subbyBtn = Button(window, text="Submitted By", width=15, fg="black", bg="red", command=subby)
subbyBtn.place(x=100, y=600)

def subto():
    imgout3 = tkinter.Label(window,text="Mr. SAMRAT KUMAR DEY\nAsst. Prof.\nDept. of CSE\nDhaka International University", width=23, fg="black",bg="green",font=('Times New Roman',24))
    imgout3.place(x=380, y=350)

subtoBtn = Button(window, text="Submitted to", width=15, fg="black", bg="red", command=subto)
subtoBtn.place(x=920, y=600)

def close_window():
    window.destroy()
photo1 = PhotoImage(file="Exit-PNG-Image.png")
photoimage1 = photo1.subsample(10,10)
exitBtn = Button(image=photoimage1,compound=LEFT,bg="red",fg="white",command=close_window)
exitBtn.place(x=550,y=600)

window.mainloop()