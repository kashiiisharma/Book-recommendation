from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from io import BytesIO
import urllib.parse
from tkinter import Menu


class Request:
    def __init__(self,method,args):
        self.args=args
        self.method=method


inc=0
def fetch_information(title,poster,published_date,rating):

    global inc
    inc=inc+1
    text[f'a{inc}'].config(text=title)
    if check_var.get():
        text2[f'a{inc}{inc}'].config(text= published_date) ##possibilotyerror
    else:
        
         text2[f'a{inc}{inc}'].config(text="")

    if check_var.get():
        text3[f'a{inc}{inc}{inc}'].config(text=rating)
    else:
         text3[f'a{inc}{inc}{inc}'].config(text="")     


    response=requests.get(poster)
    img_data=response.content
    img=(Image.open(BytesIO(img_data)))
    resized_image=img.resize((140,200))
    photo2= ImageTk.PhotoImage(resized_image)
    image[f'b{inc}'].config(image=photo2)
    image[f'b{inc}'].image=photo2



def search():
    global inc
    inc=0
    request= Request('GET',{'search': Search.get()})

    if request.method=='GET':
         search=urllib.parse.quote(request.args.get('search',''))
         url=f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
         response=requests.get(url)
             #print(response.json())

         if response.status_code==200:
            data=response.json()
            for item in data.get('items',[]):
              volume_info=item.get('volumeInfo',{})
              title=volume_info.get('title','N/A')
              publisher= volume_info.get('publisher','N/A')
              published_date=volume_info.get('publishedDate', 'N/A')
              author= volume_info.get('authors',['N/A'])
              rating= volume_info.get('averageRating',['N/A'])
              image_links= volume_info.get('imageLinks',{})
              image=image_links.get('thumbnail') if 'thumbnail' in image_links else 'yet publishing'
              print(title)
              print(publisher)
              print(published_date)
              print(author)
              print(rating)
              print(image)

              fetch_information(title,image,published_date,rating)

              if check_var.get() or check_var2.get():
                  
                  frame11.place(x=160,y=600)
                  frame22.place(x=360,y=600)
                  frame33.place(x=560,y=600)
                  frame44.place(x=760,y=600)
                  frame55.place(x=960,y=600)
              else:
                  frame11.place_forget()
                  frame22.place_forget()
                  frame33.place_forget()
                  frame44.place_forget()
                  frame55.place_forget()

         else:
             print("Failed to fetch data")
             messagebox.showinfo("Info","Failed to fetch data from google books API")



def show_menu(event):
    #DISPLAY MENU AT MOUSE POSITION
    menu.post(event.x_root,event.y_root)


root=Tk()
root.title("Book Recommendation system by K.S")
root.geometry("1250x750")
root.config(bg="#C19A6B")
root.resizable(False,False)


#icon
icon_image=PhotoImage(file="Images/icon.png")
root.iconphoto(False,icon_image)

#backgroundlooks
heading_image=PhotoImage(file="Images/background.png")
Label(root,image=heading_image,bg="#C19A6B").place(x=-2,y=-2)

#logoplacement
logo_image=PhotoImage(file="Images/logo.png")
Label(root,image=logo_image,bg="#0099ff").place(x=300,y=80)

#heading
heading=Label(root,text="BOOK RECOMMENDATION",font=("Lato",30,"bold"),fg="white",bg="#0099ff")
heading.place(x=410,y=90)

#searchingbackgroundimage
search_box=PhotoImage(file="Images/Rectangle 2.png")
Label(root,image=search_box,bg="#0099ff").place(x=300,y=155)

#entryboxandsearch station
Search=StringVar()
search_entry=Entry(root,textvariable=Search,width=20,font=("Lato",25),bg="white",fg="black",bd=0)
search_entry.place(x=415,y=172)

#searchbutton
recommend_button_image=PhotoImage(file="Images/Search.png")
recommend_button=Button(root,image=recommend_button_image,bg="#0099ff",bd=0,activebackground="#252532",cursor="hand2",command=search)
recommend_button.place(x=860,y=169)

#settingbuttonplacement
Setting_image=PhotoImage(file="Images/setting.png");
setting=Button(root,image=Setting_image,bd=0,cursor="hand2",activebackground="#0099ff",bg="#0099ff")
setting.place(x=1050,y=175)
setting.bind('<Button-1>',show_menu)

#menubuttonplacementforsearchbutton
check_var = BooleanVar()
menu=Menu(root,tearoff=0)
menu.add_checkbutton(label="Publish Date",variable=check_var,command=lambda: print(f"check option is{' checked' if check_var.get() else 'unchecked'}"))
check_var2 = BooleanVar()
menu.add_checkbutton(label="Rating",variable=check_var2,command=lambda: print(f"rating check option is{' checked' if check_var.get() else 'unchecked'}"))


#logoutbuttonplacements
logout_image=PhotoImage(file="Images/logout.png")
Button(root,image=logout_image,bg="#0099ff",cursor="hand1",command= lambda :root.destroy()).place(x=1150,y=20)

#-----------------------------------------------------------------------------------------------------------
#firstframeplacement
frame1=Frame(root,width=150,height=240,bg="white")
frame2=Frame(root,width=150,height=240,bg="white")
frame3=Frame(root,width=150,height=240,bg="white")
frame4=Frame(root,width=150,height=240,bg="white")
frame5=Frame(root,width=150,height=240,bg="white")
frame1.place(x=160,y=350)
frame2.place(x=360,y=350)
frame3.place(x=560,y=350)
frame4.place(x=760,y=350)
frame5.place(x=960,y=350)

#booktitles
text={'a1':Label(frame1,text="Book Title",font=("arial",10),fg="green"),'a2':Label(frame2,text="Book Title",font=("arial",10),fg="green"),'a3':Label(frame3,text="Book Title",font=("arial",10),fg="green"),'a4':Label(frame4,text="Book Title",font=("arial",10),fg="green"),'a5':Label(frame5,text="Book Title",font=("arial",10),fg="green")}
text['a1'].place(x=10,y=4)
text['a2'].place(x=10,y=4)
text['a3'].place(x=10,y=4)
text['a4'].place(x=10,y=4)
text['a5'].place(x=10,y=4)

#images and poster for books
image={'b1': Label(frame1),'b2': Label(frame2),'b3': Label(frame3),'b4': Label(frame4),'b5': Label(frame5)}
image['b1'].place(x=3,y=30)
image['b2'].place(x=3,y=30)
image['b3'].place(x=3,y=30)
image['b4'].place(x=3,y=30)
image['b5'].place(x=3,y=30)






#----------------------------------------------------------------------------------------------------------
#secondframeplacement

frame11=Frame(root,width=150,height=50,bg="#e6e6e6")
frame22=Frame(root,width=150,height=50,bg="#e6e6e6")
frame33=Frame(root,width=150,height=50,bg="#e6e6e6")
frame44=Frame(root,width=150,height=50,bg="#e6e6e6")
frame55=Frame(root,width=150,height=50,bg="#e6e6e6")
frame11.place(x=160,y=600)
frame22.place(x=360,y=600)
frame33.place(x=560,y=600)
frame44.place(x=760,y=600)
frame55.place(x=960,y=600)

#published date
text2={'a11':Label(frame11,text="Date",font=("arial",10),fg="red",bg="#e6e6e6"),'a22':Label(frame22,text="Date",font=("arial",10),fg="red",bg="#e6e6e6"),'a33':Label(frame33,text="Date",font=("arial",10),fg="red",bg="#e6e6e6"),'a44':Label(frame44,text="Date",font=("arial",10),fg="red",bg="#e6e6e6"),'a55':Label(frame55,text="Date",font=("arial",10),fg="red",bg="#e6e6e6")}
text2['a11'].place(x=10,y=4)
text2['a22'].place(x=10,y=4)
text2['a33'].place(x=10,y=4)
text2['a44'].place(x=10,y=4)
text2['a55'].place(x=10,y=4)




#rating
text3={'a111':Label(frame11,text="rating",font=("arial",10),bg="#e6e6e6"),'a222':Label(frame22,text="rating",font=("arial",10),bg="#e6e6e6"),'a333':Label(frame33,text="rating",font=("arial",10),bg="#e6e6e6"),'a444':Label(frame44,text="rating",font=("arial",10),bg="#e6e6e6"),'a555':Label(frame55,text="rating",font=("arial",10),bg="#e6e6e6")}
text3['a111'].place(x=20,y=30)
text3['a222'].place(x=20,y=30)
text3['a333'].place(x=20,y=30)
text3['a444'].place(x=20,y=30)
text3['a555'].place(x=20,y=30)



root.mainloop()


