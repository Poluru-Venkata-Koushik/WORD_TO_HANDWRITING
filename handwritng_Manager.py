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
    for p in range(len(sent)):
        a=sent[p]
        global img1,img2

        if (25 * i) >= 680:
            j += 80
            i=1

        if a == 'a':
            img2 = Image.open(r'lower_case/a-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i-3, j), mask=img2)
        elif a == 'b':
            img2 = Image.open(r'lower_case/b-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'c':
            img2 = Image.open(r'lower_case/c-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'd':
            img2 = Image.open(r'lower_case/d-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'e':
            img2 = Image.open(r'lower_case/e-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'f':
            img2 = Image.open(r'lower_case/f-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'g':
            img2 = Image.open(r'lower_case/g-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'h':
            img2 = Image.open(r'lower_case/h-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'i':
            img2 = Image.open(r'lower_case/i-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'j':
            img2 = Image.open(r'lower_case/j-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'k':
            img2 = Image.open(r'lower_case/k-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'l':
            img2 = Image.open(r'lower_case/l-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i -3, j), mask=img2)

        elif a == 'm':
            img2 = Image.open(r'lower_case/m-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'n':
            img2 = Image.open(r'lower_case/n-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'o':
            img2 = Image.open(r'lower_case/o-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'p':
            img2 = Image.open(r'lower_case/p-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'q':
            img2 = Image.open(r'lower_case/q-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'r':
            img2 = Image.open(r'lower_case/r-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 's':
            img2 = Image.open(r'lower_case/s-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 't':
            img2 = Image.open(r'lower_case/t-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'u':
            img2 = Image.open(r'lower_case/u-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'v':
            img2 = Image.open(r'lower_case/v-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'w':
            img2 = Image.open(r'lower_case/w-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'x':
            img2 = Image.open(r'lower_case/x-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'y':
            img2 = Image.open(r'lower_case/y-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)
        elif a == 'z':
            img2 = Image.open(r'lower_case/z-removebg-preview.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)

        elif a == ' ':
            img2 = Image.open(r'lower_case/blank.png')
            img2 = img2.resize((18, 70))
            img1.paste(img2, (18 * i - 3, j), mask=img2)

        else:
            break
        i += 1


def white_sheet_doc():
    global img1, img2
    img1 = Image.open('white.jpg')
    img1=img1.resize((700,1000))
    input_thing()
    img1.show()

def ruled_sheet_doc():
    global img1, img2
    img1 = Image.open('lines.jpg')
    img1=img1.resize((700,1000))
    input_thing()
    img1.show()


white_sheet=tk.Button(main_e,command=white_sheet_doc,text="UNruled")
white_sheet.place(x=20,y=50)

ruled_sheet=tk.Button(main_e,command=ruled_sheet_doc,text="Ruled")
ruled_sheet.place(x=100,y=50)
main_e.mainloop()
