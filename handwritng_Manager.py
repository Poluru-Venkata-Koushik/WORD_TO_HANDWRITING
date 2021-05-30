import tkinter as tk
from PIL import Image

main_e=tk.Tk()
main_e.geometry('400x200')
main_e.resizable(False,False)
main_e.title("Handwritten text tool")
def input_thing():
    i = 0
    while (1):
        global img1,img2

        a = input("enter alphabet:")
        if a == 'a':
            img2 = Image.open(r'lower_case/a.png')
            img2 = img2.resize((25, 45))
            img1.paste(img2, (25 * i, 0), mask=img2)
        elif a == 'b':
            img2 = Image.open(r'lower_case/b.png')
            img2 = img2.resize((25, 45))
            img1.paste(img2, (25 * i - 2, 0), mask=img2)
        elif a == ' ':
            img2 = Image.open(r'lower_case/blank.png')
            img2 = img2.resize((25, 45))
            img1.paste(img2, (25 * i - 2, 0), mask=img2)

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
