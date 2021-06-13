import tkinter as tk
from PIL import Image

main_e=tk.Tk()
main_e.geometry('400x200')
main_e.resizable(False,False)
main_e.title("Handwritten text tool")
def input_thing():
    sent=input("Enter something:")
    i = 1
    j = 30
    size_of_letters=(15,50)
    for p in range(len(sent)):
        a=sent[p]
        global img1,img2
        if (18 * i) >= 680:
            j += 60
            i=1

        if a == 'a':
            img2 = Image.open(r'to_add/a-removebg-preview.png')
        elif a == 'b':
            img2 = Image.open(r'to_add/b-removebg-preview.png')
        elif a == 'c':
            img2 = Image.open(r'to_add/c-removebg-preview.png')
        elif a == 'd':
            img2 = Image.open(r'to_add/d-removebg-preview.png')
        elif a == 'e':
            img2 = Image.open(r'to_add/e-removebg-preview.png')
        elif a == 'f':
            img2 = Image.open(r'to_add/f-removebg-preview.png')
        elif a == 'g':
            img2 = Image.open(r'to_add/g-removebg-preview.png')
        elif a == 'h':
            img2 = Image.open(r'to_add/h-removebg-preview.png')
        elif a == 'i':
            img2 = Image.open(r'to_add/i-removebg-preview.png')
        elif a == 'j':
            img2 = Image.open(r'to_add/j-removebg-preview.png')
        elif a == 'k':
            img2 = Image.open(r'to_add/k-removebg-preview.png')
        elif a == 'l':
            img2 = Image.open(r'to_add/l-removebg-preview.png')
        elif a == 'm':
            img2 = Image.open(r'to_add/m-removebg-preview.png')
        elif a == 'n':
            img2 = Image.open(r'to_add/n-removebg-preview.png')
        elif a == 'o':
            img2 = Image.open(r'to_add/o-removebg-preview.png')
        elif a == 'p':
            img2 = Image.open(r'to_add/p-removebg-preview.png')
        elif a == 'q':
            img2 = Image.open(r'to_add/q-removebg-preview.png')
        elif a == 'r':
            img2 = Image.open(r'to_add/r-removebg-preview.png')
        elif a == 's':
            img2 = Image.open(r'to_add/s-removebg-preview.png')
        elif a == 't':
            img2 = Image.open(r'to_add/t-removebg-preview.png')
        elif a == 'u':
            img2 = Image.open(r'to_add/u-removebg-preview.png')
        elif a == 'v':
            img2 = Image.open(r'to_add/v-removebg-preview.png')
        elif a == 'w':
            img2 = Image.open(r'to_add/w-removebg-preview.png')
        elif a == 'x':
            img2 = Image.open(r'to_add/x-removebg-preview.png')
        elif a == 'y':
            img2 = Image.open(r'to_add/y-removebg-preview.png')
        elif a == 'z':
            img2 = Image.open(r'to_add/z-removebg-preview.png')
        elif a == 'A':
            img2 = Image.open(r'to_add/aa-removebg-preview.png')
        elif a == 'B':
            img2 = Image.open(r'to_add/bb-removebg-preview.png')
        elif a == 'C':
            img2 = Image.open(r'to_add/cc-removebg-preview.png')
        elif a == 'D':
            img2 = Image.open(r'to_add/dd-removebg-preview.png')
        elif a == 'E':
            img2 = Image.open(r'to_add/ee-removebg-preview.png')
        elif a == 'F':
            img2 = Image.open(r'to_add/ff-removebg-preview.png')
        elif a == 'G':
            img2 = Image.open(r'to_add/gg-removebg-preview.png')
        elif a == 'H':
            img2 = Image.open(r'to_add/hh-removebg-preview.png')
        elif a == 'I':
            img2 = Image.open(r'to_add/ii-removebg-preview.png')
        elif a == 'J':
            img2 = Image.open(r'to_add/jj-removebg-preview.png')
        elif a == ' ':
            img2 = Image.open(r'to_add/blank.png')
        elif a == '.':
            img2 = Image.open(r'to_add/dot-removebg-preview.png')
        elif a == ',':
            img2 = Image.open(r'to_add/comma-removebg-preview.png')
        elif a == '0':
            img2 = Image.open(r'to_add/0-removebg-preview.png')
        elif a == '1':
            img2 = Image.open(r'to_add/1-removebg-preview.png')
        elif a == '2':
            img2 = Image.open(r'to_add/2-removebg-preview.png')
        elif a == '3':
            img2 = Image.open(r'to_add/3-removebg-preview.png')
        elif a == '4':
            img2 = Image.open(r'to_add/4-removebg-preview.png')
        elif a == '5':
            img2 = Image.open(r'to_add/5-removebg-preview.png')
        elif a == '6':
            img2 = Image.open(r'to_add/6-removebg-preview.png')
        elif a == '7':
            img2 = Image.open(r'to_add/7-removebg-preview.png')
        elif a == '8':
            img2 = Image.open(r'to_add/8-removebg-preview.png')
        elif a == '9':
            img2 = Image.open(r'to_add/9-removebg-preview.png')
        else:
            break
        if(a==','):
            img2 = img2.resize((10, 25))
            img1.paste(img2, (18 * i - 3, j+45), mask=img2)
        else:
            img2 = img2.resize(size_of_letters)
            img1.paste(img2, (18 * i - 3, j), mask=img2)

        i +=1


def white_sheet_doc():
    global img1, img2
    img1 = Image.open('white.jpg')
    img1=img1.resize((700,1000))
    input_thing()
    img1.show()

def ruled_sheet_doc():
    global img1, img2
    img1 = Image.open('lines.jpg')
    img1=img1.resize((700, 1000))
    input_thing()
    img1.show()


white_sheet=tk.Button(main_e,command=white_sheet_doc,text="UNruled")
white_sheet.place(x=20,y=50)

ruled_sheet=tk.Button(main_e,command=ruled_sheet_doc,text="Ruled")
ruled_sheet.place(x=100,y=50)
main_e.mainloop()
