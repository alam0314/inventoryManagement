import os
import tempfile
from tkinter import*
import mysql.connector
import time
from datetime import datetime
from PIL import Image,ImageTk
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk

############### Login id and password--->user- alam, pass- 12345 #########################

root=Tk()

####### These are the Variables which is used for taking input from the user ############ 
ProductId=StringVar()
ProductName=StringVar()
Quantity=IntVar()
Price=DoubleVar()
MfgCompany=StringVar()
ProductDesc=StringVar()

ProductIdU=StringVar()
ProductNameU=StringVar()
QuantityU=IntVar()
PriceU=DoubleVar()
MfgCompanyU=StringVar()
ProductDescU=StringVar()

ProductIdS=StringVar()
ProductNameS=StringVar()
QuantityS=IntVar()
PriceS=DoubleVar()
MfgCompanyS=StringVar()
CustomerName=StringVar()
CustomerMobile=StringVar()

SEARCH= StringVar()

######## Login window  ########

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x7200+0+0")
        self.F=Image.open(r'images\loginImage.jpg')
        self.bg=ImageTk.PhotoImage(self.F)
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        frame_login=Frame(self.root,bg="pink")
        frame_login.place(x=40,y=80,height=340,width=500)

        title=Label(frame_login,text="Login Here",font=("Impact",35,"bold"),bg="pink",fg="blue",).place(x=90,y=30)
        desc=Label(frame_login,text="User Login Page",font=("Goudy old style",15,"bold"),bg="pink",fg="blue",).place(x=90,y=100)

        label_user=Label(frame_login,text="Username",font=("Goudy old style",15,"bold"),bg="pink").place(x=90,y=140)
        self.txt_user=Entry(frame_login,font=("times new roman",15),bg="gray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        label_password=Label(frame_login,text="Password",font=("Goudy old style",15,"bold"),bg="pink").place(x=90,y=210)
        self.txt_pass=Entry(frame_login,font=("times new roman",15),bg="gray",show="*")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        login_button=Button(self.root,text="Login",bg="blue",fg="white",command=self.login_function,font=("times new roman",20)).place(x=200,y=400,width=150,height=35)

        #forget=Button(frame_login,text="Forget username?",bg="pink",fg="blue",font=("times new roman",12)).place(x=220,y=280)
        #forget=Button(frame_login,text="Forget Password?",bg="pink",fg="blue",font=("times new roman",12)).place(x=90,y=280)
        #forget=Button(frame_login,text="Add new user",bg="pink",fg="blue",font=("times new roman",12)).place(x=350,y=280)
        
    def login_function(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            tkMessageBox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_user.get()!="alam"or self.txt_pass.get()!="12345":
            tkMessageBox.showerror("Error","Invalid username/password",parent=self.root)
        else:
             tkMessageBox.showinfo("Welcome",f"Welcome {self.txt_user.get()}",parent=self.root)
             IMS(root)

######### user panel ########
          
class IMS:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1350x7200" )
        self.root.title("Inventory Management System")
        self.Cart=Image.open(r'images\cart.png')
        self.icon_title=ImageTk.PhotoImage(self.Cart)
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        btn_logout=Button(self.root,text="Logout",command=Logout,font=("times new roman",15,"bold"),bg="red",fg='white',bd='5',cursor="hand2").place(x=1100,y=10,height=35,width="150")
        self.lbl_clock=Label(self.root,text="Inventory Management System\t\t Date:DD-MM-YY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="green",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        self.MenuLogo=Image.open(r'images\menu.png')
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.Resampling.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        Leftmenu=Frame(self.root,bd=5,relief=RIDGE,bg="yellow")
        Leftmenu.place(x=0,y=100,width=200,height=570)
        lbl_menuLogo=Label(Leftmenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        lbl_menu=Label(Leftmenu,text="Menu",font=("times new roman",20),bg="purple",fg='white').pack(side=TOP,fill=X)
        lbl_addProduct=Button(Leftmenu,text="Add product",command=add_product,compound=LEFT,font=("times new roman",20),bg="black",fg="white",bd='3',cursor="hand2").pack(side=TOP,fill=X)
        lbl_saleProduct=Button(Leftmenu,text="Sale Product",command=Sale_Product,compound=LEFT,font=("times new roman",20),bg="black",fg="white",bd='2',cursor="hand2").pack(side=TOP,fill=X)
        lbl_Update=Button(Leftmenu,text="Update product",command=update_product,compound=LEFT,font=("times new roman",20),bg="black",fg="white",bd='2',cursor="hand2").pack(side=TOP,fill=X)
        lbl_Search=Button(Leftmenu,text="Search Product",command=SearchProduct,compound=LEFT,font=("times new roman",20),bg="black",fg="white",bd='2',cursor="hand2").pack(side=TOP,fill=X)
        lbl_delete=Button(Leftmenu,text="Delete Product",command=ProductDelete,compound=LEFT,font=("times new roman",20),bg="black",fg="white",bd='2',cursor="hand2").pack(side=TOP,fill=X)
        lbl_exit=Button(Leftmenu,text="Exit",command=exit,compound=LEFT,font=("times new roman",20),bg="black",fg="white",bd='3',cursor="hand2").pack(side=TOP,fill=X)
        
    
        global product_table
        Dataframe=Frame(bd=5,relief=RIDGE,bg="black")
        Dataframe.place(x=200,y=100,width=1090,height=570)
        MidViewForm =LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
        MidViewForm.place(x=0,y=0,width=1060,height=560)
        scrollbarx = ttk.Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = ttk.Scrollbar(MidViewForm, orient=VERTICAL)
        product_table = ttk.Treeview(MidViewForm, columns=("ProductID", "ProductName", "ProductQty", "ProductPrice","MfgCompany","ProductInformation"), xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        scrollbarx.pack(side=BOTTOM,fill=X)
        scrollbary.pack(side=RIGHT,fill=Y)
        scrollbarx=ttk.Scrollbar(command=product_table.xview)
        scrollbary=ttk.Scrollbar(command=product_table.yview)
        product_table.heading('ProductID', text="Product Id")
        product_table.heading('ProductName', text="Product Name")
        product_table.heading('ProductQty', text="Quantity")
        product_table.heading('ProductPrice', text="Price")
        product_table.heading('ProductInformation', text="Product Information")
        product_table.heading('MfgCompany', text="Mfg Company")
        product_table["show"]="headings"
        product_table.column("ProductID", width=100)
        product_table.column("ProductName", width=100)
        product_table.column("ProductQty", width=100)
        product_table.column("ProductPrice", width=100)
        product_table.column("ProductInformation", width=100)
        product_table.pack(fill= BOTH,expand=1)
        fetch_data()
        
        lbl_footer=Label(self.root,text="IMS- Inventory Management System | Developed by Alam Aanash",font=("times new roman",12),bg="#4d636d",fg="white").place(x=0,y=670,relwidth=1,height=25)
        self.date_time()
        
    def date_time(self):
        time_= time.strftime("%I:%M:%S %p")
        date_= time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:{str(date_)}\t\t Time:{str(time_)}")
        self.lbl_clock.after(200,self.date_time)  

        
####### From here we have used various types of function for different-different work ###########


#### Adding product and database related work #######

def add_product():

    Dataframe=Frame(bd=5,relief=RIDGE,bg="black")
    Dataframe.place(x=200,y=100,width=1080,height=570)

    dataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Add Product")
    dataframeLeft.place(x=100,y=70,width=510,height=220)

    lblProduct_id=Label(dataframeLeft,text="Product Id:",font=("arial",12,"bold"),padx=2,pady=6)
    lblProduct_id.grid(row=0,column=0)
    txtProduct_id=Entry(dataframeLeft,font=("arial",12),textvariable=ProductId,width=35)
    txtProduct_id.grid(row=0,column=1)
     
    lblProduct_Name=Label(dataframeLeft,text="Product Name:",font=("arial",12,"bold"),padx=2,pady=6)
    lblProduct_Name.grid(row=1,column=0)
    txtProduct_Name=Entry(dataframeLeft,font=("arial",12),textvariable=ProductName,width=35)
    txtProduct_Name.grid(row=1,column=1)

    lblProduct_Quantity=Label(dataframeLeft,text="Quantity:",font=("arial",12,"bold"),padx=2,pady=6)
    lblProduct_Quantity.grid(row=2,column=0)
    txtProduct_Quantity=Entry(dataframeLeft,font=("arial",12),textvariable=Quantity,width=35)
    txtProduct_Quantity.grid(row=2,column=1)

    lblProduct_Price=Label(dataframeLeft,text="Product Price:",font=("arial",12,"bold"),padx=2,pady=6)
    lblProduct_Price.grid(row=3,column=0)
    txtProduct_Price=Entry(dataframeLeft,font=("arial",12),textvariable=Price,width=35)
    txtProduct_Price.grid(row=3,column=1)

    lblProduct_MfgCompany=Label(dataframeLeft,text="Mfg Company:",font=("arial",12,"bold"),padx=2,pady=6)
    lblProduct_MfgCompany.grid(row=4,column=0)
    txtProduct_MfgCompany=Entry(dataframeLeft,font=("arial",12),textvariable=MfgCompany,width=35)
    txtProduct_MfgCompany.grid(row=4,column=1)

    dataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Product Information")
    dataframeRight.place(x=611,y=70,width=300,height=220)
    #txtProductInformation=Text(dataframeRight,font=("arial",12,"bold"),width=28,height=9,padx=2,pady=6)
    txtProductInformation=Entry(dataframeRight,font=("arial",12),textvariable=ProductDesc,width=28)
    #txtProductInformation.grid(row=0,column=0)
    txtProductInformation.place(x=10,y=10,height=160,width=230)

    buttonFrame=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10)
    buttonFrame.place(x=300,y=300,width=365,height=50)

    btnSave=Button(buttonFrame,text="Save",bg="blue",fg="white",font=("arial",12,"bold"),command=AddDatabase,width=10,padx=2,pady=6)
    btnSave.grid(row=0,column=1)
    
    btnSave=Button(buttonFrame,text="Clear",bg="blue",fg="white",font=("arial",12,"bold"),command=ClearAddProduct,width=10,padx=2,pady=6)
    btnSave.grid(row=0,column=2)

    btnSave=Button(buttonFrame,text="Close",bg="blue",fg="white",font=("arial",12,"bold"),command=close,width=10,padx=2,pady=6)
    btnSave.grid(row=0,column=3)

def AddDatabase(): 
    try:
        if ProductId.get()=="" or ProductName.get()==""or Price.get()==""or Quantity.get()=="":
            tkMessageBox.showerror("Error","All fields are required") 
        else:
        
             conn=mysql.connector.connect(host="localhost",username="root",password="pass",database="inventory1")
             my_cursor=conn.cursor()
             my_cursor.execute("insert into product values(%s,%s,%s,%s,%s,%s)",(ProductId.get(),ProductName.get(),Quantity.get(),Price.get(),MfgCompany.get(),ProductDesc.get()))
             conn.commit()
             tkMessageBox.showinfo("Add Product",'Product Added Succesfully!')
             ProductId.set("")
             ProductName.set("")
             Quantity.set("")
             Price.set("")
             MfgCompany.set("")
             ProductDesc.set("")
             conn.close()  
    except:
            tkMessageBox.showerror("Error","Enter only digit in price and quantity")
def ClearAddProduct():
         ProductId.set("")
         ProductName.set("")
         Price.set("")
         Quantity.set("")
         MfgCompany.set("")
         ProductDesc.set("")

######### Saling product and database related work ###########        

def Sale():
    global Billing_table
    if ProductIdS.get()=="":
        tkMessageBox.showerror("Error","Click on the product name then click on sale button") 
    else:

         Dataframe=Frame(bd=5,relief=RIDGE,bg="black")
         Dataframe.place(x=200,y=100,width=1072,height=570)
         btn_print = Button(Dataframe,bd=5,command=printBill, text="Print",font=("arial",12,"bold"),bg="yellow",fg="black")
         btn_print.place(x=760,y=390,width=80)

         dataframeLeft=LabelFrame(Dataframe,bd=15,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Sale Product")
         dataframeLeft.place(x=45,y=70,width=510,height=290)
         lblProduct_Name=Label(dataframeLeft,text="Product name:",font=("arial",12,"bold"),padx=2,pady=6)
         lblProduct_Name.grid(row=0,column=0)
         txtProduct_Name=Entry(dataframeLeft,font=("arial",12),textvariable=ProductNameS,width=35)
         txtProduct_Name.grid(row=0,column=1)
          
     
         lblProduct_id=Label(dataframeLeft,text="Product Id:",font=("arial",12,"bold"),padx=2,pady=6)
         lblProduct_id.grid(row=1,column=0)
         txtProduct_id=Entry(dataframeLeft,font=("arial",12),textvariable=ProductIdS,width=35)
         txtProduct_id.grid(row=1,column=1)
         
         lblQuantity=Label(dataframeLeft,text="Quantity:",font=("arial",12,"bold"),padx=2,pady=6)
         lblQuantity.grid(row=2,column=0)
         txtQuantity=Entry(dataframeLeft,font=("arial",12),textvariable=QuantityS,width=35)
         txtQuantity.grid(row=2,column=1)
     
         lblProduct_Price=Label(dataframeLeft,text="Product Price:",font=("arial",12,"bold"),padx=2,pady=6)
         lblProduct_Price.grid(row=3,column=0)
         txtProduct_Price=Entry(dataframeLeft,font=("arial",12),textvariable=PriceS,width=35)
         txtProduct_Price.grid(row=3,column=1)
     
         lblMfgComp=Label(dataframeLeft,text="Mfg Company:",font=("arial",12,"bold"),padx=2,pady=6)
         lblMfgComp.grid(row=4,column=0)
         txtMfgComp=Entry(dataframeLeft,font=("arial",12),textvariable=MfgCompanyS,width=35)
         txtMfgComp.grid(row=4,column=1)
     
         lblCusName=Label(dataframeLeft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
         lblCusName.grid(row=5,column=0)
         txtCusName=Entry(dataframeLeft,font=("arial",12),textvariable=CustomerName,width=35)
         txtCusName.grid(row=5,column=1)
     
         lblCusMobile=Label(dataframeLeft,text="Customer Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
         lblCusMobile.grid(row=6,column=0)
         txtCusMobile=Entry(dataframeLeft,font=("arial",12),textvariable=CustomerMobile,width=35)
         txtCusMobile.grid(row=6,column=1)
     
         buttonFrame=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10)
         buttonFrame.place(x=120,y=380,width=365,height=50)
     
         btnSave=Button(buttonFrame,text="Sale",command=saleDatabase,bg="blue",fg="white",font=("arial",12,"bold"),width=16,padx=0,pady=6)
         btnSave.grid(row=0,column=0)
         
         btnclose=Button(buttonFrame,text="Back",command=Sale_Product,bg="blue",fg="white",font=("arial",12,"bold"),width=16,padx=0,pady=6)
         btnclose.grid(row=0,column=1)
     
         DataframeRight =LabelFrame(Dataframe,bd=15,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Billing Area")
         DataframeRight.place(x=570,y=60,width=450,height=305)
         scrollbarx = ttk.Scrollbar(DataframeRight, orient=HORIZONTAL)
         scrollbary = ttk.Scrollbar(DataframeRight, orient=VERTICAL)
         Billing_table = Text(DataframeRight,font=("times new roman",13),width=44,height=13,padx=2,pady=6)
         Billing_table.grid(row=0,column=0)
         #scrollbarx.pack(side=BOTTOM,fill=X)
         #scrollbary.pack(side=RIGHT,fill=Y)
         #scrollbarx=ttk.Scrollbar(command=product_table.xview)
         #scrollbary=ttk.Scrollbar(command=product_table.yview)

def printBill():
    file1=tempfile.mktemp(".txt")
    open(file1,'w').write(Billing_table.get('1.0',END))
    os.startfile(file1,'print')
     
def BillingArea():
    totalAmount=PriceS.get()*QuantityS.get()
    now=datetime.now()
    DateTime=now.strftime('%Y-%m-%d %H:%M:%S')
    Billing_table.insert(END,"Product Name\t\t : "+ProductNameS.get()+"\n")
    Billing_table.insert(END,"Product Id\t\t : "+ProductIdS.get()+"\n")
    Billing_table.insert(END,"Price   \t\t : "+str(PriceS.get())+"\n")
    Billing_table.insert(END,"Quantity\t\t : "+str(QuantityS.get())+"\n")
    Billing_table.insert(END,"Mfg Company\t\t : "+MfgCompanyS.get()+"\n")
    Billing_table.insert(END,"Customer Name\t\t : "+CustomerName.get()+"\n")
    Billing_table.insert(END,"Customer Mobile\t\t : "+CustomerMobile.get()+"\n")
    Billing_table.insert(END,"Date & Time\t\t : "+DateTime+"\n")
    Billing_table.insert(END,"Total Amount\t\t : "+str(totalAmount)+"\n")
    ProductIdS.set("")
    ProductNameS.set("")
    PriceS.set("")
    QuantityS.set("")
    MfgCompanyS.set("")
    CustomerName.set("")
    CustomerMobile.set("")

def Sale_Product():
    global product_table
    Dataframe=Frame(bd=5,relief=RIDGE,bg="black")
    Dataframe.place(x=200,y=100,width=1072,height=570)
    dataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    dataframeLeft.place(x=0,y=0,width=300,height=560)
    
    lbl_txtsearch = Label(dataframeLeft, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(dataframeLeft, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(dataframeLeft, text="Search",bg="yellow",command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_Sale = Button(dataframeLeft, text="Sale",bg="gray",command=Sale)
    btn_Sale.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_ViewSale = Button(dataframeLeft, text="View Sold Product",command=ViewSoldProduct,bg="blue",fg="white")
    btn_ViewSale.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_Close = Button(dataframeLeft, text="close",bg="green",command=close)
    btn_Close.pack(side=TOP, padx=10, pady=10, fill=X)

    MidViewForm =LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    MidViewForm.place(x=300,y=0,width=760,height=560)
    scrollbarx = ttk.Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = ttk.Scrollbar(MidViewForm, orient=VERTICAL)
    product_table = ttk.Treeview(MidViewForm, columns=("ProductID", "ProductName", "ProductQty", "ProductPrice","MfgCompany"), xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    scrollbarx.pack(side=BOTTOM,fill=X)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx=ttk.Scrollbar(command=product_table.xview)
    scrollbary=ttk.Scrollbar(command=product_table.yview)
    product_table.heading('ProductID', text="Product Id")
    product_table.heading('ProductName', text="Product Name")
    product_table.heading('ProductQty', text="Quantity")
    product_table.heading('ProductPrice', text="Price")
    product_table.heading('MfgCompany', text="Mfg Company")
    product_table["show"]="headings"
    product_table.column("ProductID", width=100)
    product_table.column("ProductName", width=100)
    product_table.column("ProductQty", width=100)
    product_table.column("ProductPrice", width=100)
    product_table.pack(fill= BOTH,expand=1)
    fetch_data()
    product_table.bind("<ButtonRelease-1>",fillInSale)
    

def fillInSale(event=""):
    try:
         cursor_row=product_table.focus()
         content=product_table.item(cursor_row)
         row=content["values"]
         ProductIdS.set(row[0])
         ProductNameS.set(row[1])
         QuantityS.set(row[2])
         PriceS.set(row[3])
         MfgCompanyS.set(row[4])
    except:
        tkMessageBox.showerror("Error","Click on the product name!")

def saleDatabase():
    now=datetime.now()
    DateTime=now.strftime('%Y-%m-%d %H:%M:%S')
    conn=mysql.connector.connect(host="localhost",username="root",password="pass",database="inventory1")
    my_cursor=conn.cursor()
    my_cursor.execute("insert into sale values(%s,%s,%s,%s,%s,%s,%s,%s)",(ProductNameS.get(),ProductIdS.get(),QuantityS.get(),PriceS.get(),MfgCompanyS.get(),CustomerName.get(),CustomerMobile.get(),DateTime))
    my_cursor.execute("update product set Quantity=Quantity-%s where ProductId=%s",(QuantityS.get(),ProductIdS.get()))
    conn.commit()
    tkMessageBox.showinfo("Add Product",'Product has been sold.')
    BillingArea()
    conn.close()  

def ViewSoldProduct():
    global product_table
    Dataframe=Frame(bd=5,relief=RIDGE,bg="black")
    Dataframe.place(x=200,y=100,width=1072,height=570)
    lbl_txtsearch = Label(Dataframe, text="View Sold Product", font=('arial',15,"bold"),bg="purple",fg="white")
    Button(Dataframe,text="Go Back",bd=5,font=('times and new roman',10,"bold"),bg="gray",fg="blue",command=Sale_Product,cursor="hand2").place(x=450,y=42,width=120,height=28)
    lbl_txtsearch.pack(side=TOP,padx=10,pady=10)
    MidViewForm =LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    MidViewForm.place(x=0,y=70,width=1060,height=490)
    scrollbarx = ttk.Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = ttk.Scrollbar(MidViewForm, orient=VERTICAL)
    product_table = ttk.Treeview(MidViewForm, columns=("ProductName", "ProductId", "ProductQty", "ProductPrice","MfgCompany","CustomerName","CustomerMobile","DateTime"), xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    scrollbarx.pack(side=BOTTOM,fill=X)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx=ttk.Scrollbar(command=product_table.xview)
    scrollbary=ttk.Scrollbar(command=product_table.yview)
    product_table.heading('ProductName', text="Product Name")
    product_table.heading('ProductId', text="Product Id")
    product_table.heading('ProductQty', text="Quantity")
    product_table.heading('ProductPrice', text="Price")
    product_table.heading('MfgCompany', text="Mfg Company")
    product_table.heading('CustomerName', text="Customer Name")
    product_table.heading('CustomerMobile', text="Customer Mobile")
    product_table.heading('DateTime', text="Date & Time")
    product_table["show"]="headings"
    product_table.column("ProductName", width=100)
    product_table.column("ProductId", width=100)
    product_table.column("ProductQty", width=100)
    product_table.column("ProductPrice", width=100)
    product_table.column("MfgCompany", width=100)
    product_table.column("CustomerName", width=100)
    product_table.column("CustomerMobile", width=100)
    product_table.column("DateTime", width=100)
    product_table.pack(fill= BOTH,expand=1)
    FetchSoldData()

def FetchSoldData():
    conn=mysql.connector.connect(host="localhost",username="root",password="pass",database="inventory1")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from sale")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        #product_table.delete(product_table.get_children())
        for i in rows:
            product_table.insert("",END,values=i)
        conn.commit()
    conn.close()

######## Updating product and database related work ##########

def update_product():
    global product_table
    Dataframe=Frame(bd=5,relief=RIDGE,bg="black")
    Dataframe.place(x=200,y=100,width=1072,height=570)
    dataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    dataframeLeft.place(x=0,y=0,width=300,height=515)
    
    lbl_txtsearch = Label(dataframeLeft, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(dataframeLeft, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(dataframeLeft, text="Search",bg="yellow",command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_delete = Button(dataframeLeft, text="Update",bg="blue",command=update)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(dataframeLeft, text="close",bg="green",command=close)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    MidViewForm =LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    MidViewForm.place(x=300,y=0,width=710,height=515)
    scrollbarx = ttk.Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = ttk.Scrollbar(MidViewForm, orient=VERTICAL)
    product_table = ttk.Treeview(MidViewForm, columns=("ProductID", "ProductName", "ProductQty", "ProductPrice","MfgCompany"), xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    scrollbarx.pack(side=BOTTOM,fill=X)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx=ttk.Scrollbar(command=product_table.xview)
    scrollbary=ttk.Scrollbar(command=product_table.yview)
    product_table.heading('ProductID', text="Product Id")
    product_table.heading('ProductName', text="Product Name")
    product_table.heading('ProductQty', text="Quantity")
    product_table.heading('ProductPrice', text="Price")
    product_table.heading('MfgCompany', text="Mfg Company")
    product_table["show"]="headings"
    product_table.column("ProductID", width=100)
    product_table.column("ProductName", width=100)
    product_table.column("ProductQty", width=100)
    product_table.column("ProductPrice", width=100)
    product_table.pack(fill= BOTH,expand=1)
    fetch_data()
    product_table.bind("<ButtonRelease-1>",fill_data)
    
    
def fetch_data():
    conn=mysql.connector.connect(host="localhost",username="root",password="pass",database="inventory1")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from product")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        #product_table.delete(product_table.get_children())
        for i in rows:
            product_table.insert("",END,values=i)
        conn.commit()
    conn.close()

##########################Fill the product in the frame###############

def fill_data(event=""):
    try:
         cursor_row=product_table.focus()
         content=product_table.item(cursor_row)
         row=content["values"]
         ProductIdU.set(row[0])
         ProductNameU.set(row[1])
         QuantityU.set(row[2])
         PriceU.set(row[3])
         MfgCompanyU.set(row[4])
         ProductDescU.set(row[5])
    except:
        tkMessageBox.showerror("Error","Click on the product name!")

##################### Database connection for search product #############################3

def Search():
    try:
        if SEARCH.get()=="":
            tkMessageBox.showerror("Error","Product name should be required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="pass",database="inventory1")
            cursor=conn.cursor()
            #add_product.delete(*add_product.get_children())
            cursor.execute("SELECT * FROM product WHERE ProductName =%s", (SEARCH.get(),))
            row = cursor.fetchone()
            if row!=None:
                product_table.delete(*product_table.get_children())
                product_table.insert('', END, values=(row))
                SEARCH.set("")
            else:
                tkMessageBox.showerror("Error","No record found!")
                SEARCH.set("")
    except Exception as ex:
        tkMessageBox.showerror("Error",f"Error due to:{str(ex)}")

############## Product update frame #####################

def update():
    if ProductIdU.get()=="":
        tkMessageBox.showerror("Error","Click on the product name then click on Update button") 
    else:
        Dataframe=Frame(bd=5,relief=RIDGE,bg="black")
        Dataframe.place(x=200,y=100,width=1072,height=570)
    
        dataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Update Product")
        dataframeLeft.place(x=100,y=100,width=510,height=220)
    
        lblProduct_id=Label(dataframeLeft,text="Product Id:",font=("arial",12,"bold"),padx=2,pady=6)
        lblProduct_id.grid(row=0,column=0)
        txtProduct_id=Entry(dataframeLeft,font=("arial",12),textvariable=ProductIdU,width=35)
        txtProduct_id.grid(row=0,column=1)
         
        lblProduct_name=Label(dataframeLeft,text="Product Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblProduct_name.grid(row=1,column=0)
        txtProduct_name=Entry(dataframeLeft,font=("arial",12),textvariable=ProductNameU,width=35)
        txtProduct_name.grid(row=1,column=1)
    
        lblProduct_quantity=Label(dataframeLeft,text="Quantity:",font=("arial",12,"bold"),padx=2,pady=6)
        lblProduct_quantity.grid(row=2,column=0)
        txtProduct_quantity=Entry(dataframeLeft,font=("arial",12),textvariable=QuantityU,width=35)
        txtProduct_quantity.grid(row=2,column=1)

        lblProduct_price=Label(dataframeLeft,text="Product Price:",font=("arial",12,"bold"),padx=2,pady=6)
        lblProduct_price.grid(row=3,column=0)
        txtProduct_price=Entry(dataframeLeft,font=("arial",12),textvariable=PriceU,width=35)
        txtProduct_price.grid(row=3,column=1)
    
        lblProduct_mfg=Label(dataframeLeft,text="Mfg Company:",font=("arial",12,"bold"),padx=2,pady=6)
        lblProduct_mfg.grid(row=4,column=0)
        txtProduct_mfg=Entry(dataframeLeft,font=("arial",12),textvariable=MfgCompanyU,width=35)
        txtProduct_mfg.grid(row=4,column=1)
    
        dataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12),text="Product Information")
        dataframeRight.place(x=611,y=100,width=300,height=220)
        #txtProductInformation=Text(dataframeRight,font=("arial",12,"bold"),widt=28,height=9,padx=2,pady=6)
        txtProductInformation=Entry(dataframeRight,font=("arial",12),textvariable=ProductDescU,width=30)
        #txtProductInformation.grid(row=0,column=0)
        txtProductInformation.place(x=10,y=10,height=160,width=230)

        buttonFrame=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10)
        buttonFrame.place(x=300,y=340,width=365,height=50)
    
        btnUpdate=Button(buttonFrame,text="Update",bg="gray",fg="white",font=("arial",12,"bold"),command=UpdateDatabase,width=16,padx=0,pady=6)
        btnUpdate.grid(row=0,column=0)
        
        btnBack=Button(buttonFrame,text="Back",bg="blue",fg="white",font=("arial",12,"bold"),command=update_product,width=16,padx=0,pady=6)
        btnBack.grid(row=0,column=1)
        
##################### Database connection for updating product ################## 

def UpdateDatabase(): 
    if ProductIdU.get()=="" or ProductNameU.get()==""or PriceU.get()==""or QuantityU.get()=="":
        tkMessageBox.showerror("Error","All fields are required") 
    else:
         conn=mysql.connector.connect(host="localhost",username="root",password="pass",database="inventory1")
         my_cursor=conn.cursor()
         my_cursor.execute("update product set ProductId=%s, ProductName=%s,Quantity=%s,Price=%s,MfgCompany=%s,ProductDesc=%s where ProductId=%s",(ProductIdU.get(),ProductNameU.get(),QuantityU.get(),PriceU.get(),MfgCompanyU.get(),ProductDescU.get(),ProductIdU.get()))
         conn.commit()
         tkMessageBox.showinfo("Update Product",'Product has been updated!')
         ProductIdU.set("")
         ProductNameU.set("")
         PriceU.set("")
         QuantityU.set("")
         MfgCompanyU.set("")
         ProductDescU.set("")
         conn.close()  

####################### Searching product frame ########################

def SearchProduct():
    global product_table
    Dataframe=Frame(bd=5,relief=RIDGE,bg="gray")
    Dataframe.place(x=200,y=100,width=1072,height=570)

    txtSearch=Label(Dataframe,bd=0,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    lbl_txtsearch = Label(Dataframe, text="Search Product", font=('arial',15,"bold"),bg="purple",fg="white")
    lbl_txtsearch.pack(side=TOP,padx=10,pady=10)
    Entry(Dataframe, textvariable=SEARCH, font=('arial', 10),cursor="hand2").place(x=300,y=55,width=120,height=28)
    Button(Dataframe,text="Search",font=('times and new roman',10,"bold"),bg="Yellow",fg="blue",command=Search,cursor="hand2").place(x=425,y=55,width=120,height=28)
    Button(Dataframe,text="Close",font=('times and new roman',10,"bold"),bg="black",fg="white",command=close,cursor="hand2").place(x=550,y=55,width=120,height=28)
    dataframeDown=LabelFrame(Dataframe,bd=6,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    dataframeDown.place(x=0,y=100,width=1060,height=460)
    
    scrollbarx = ttk.Scrollbar(dataframeDown, orient=HORIZONTAL)
    scrollbary = ttk.Scrollbar(dataframeDown, orient=VERTICAL)
    product_table = ttk.Treeview(dataframeDown, columns=("ProductID", "ProductName", "ProductQty", "ProductPrice","MfgCompany","ProductDesc"), xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    scrollbarx.pack(side=BOTTOM,fill=X)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx=ttk.Scrollbar(command=product_table.xview)
    scrollbary=ttk.Scrollbar(command=product_table.yview)
    product_table.heading('ProductID', text="Product Id")
    product_table.heading('ProductName', text="Product Name")
    product_table.heading('ProductQty', text="Quantity")
    product_table.heading('ProductPrice', text="Price")
    product_table.heading('MfgCompany', text="Mfg Company")
    product_table.heading('ProductDesc', text="Product Information")
    product_table["show"]="headings"
    product_table.column("ProductID", width=100)
    product_table.column("ProductName", width=100)
    product_table.column("ProductQty", width=100)
    product_table.column("ProductPrice", width=100)
    product_table.pack(fill= BOTH,expand=1)
    fetch_data()
    product_table.bind("<ButtonRelease-1>",fill_data)

########################### Delete product frame #################################3

def ProductDelete():
    global product_table
    Dataframe=Frame(bd=5,relief=RIDGE,bg="black")
    Dataframe.place(x=200,y=100,width=1072,height=570)

    dataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    dataframeLeft.place(x=0,y=0,width=300,height=560)
    
    lbl_txtsearch = Label(dataframeLeft, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(dataframeLeft, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(dataframeLeft, text="Search",bg="yellow", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_delete = Button(dataframeLeft, text="Delete",bg="red", command=DeleteProductIn)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(dataframeLeft, text="close",bg="green", command=close)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    MidViewForm =LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"))
    MidViewForm.place(x=300,y=0,width=760,height=560)
    scrollbarx = ttk.Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = ttk.Scrollbar(MidViewForm, orient=VERTICAL)
    product_table = ttk.Treeview(MidViewForm, columns=("ProductID", "ProductName", "ProductQty", "ProductPrice","MfgCompany"), xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
    scrollbarx.pack(side=BOTTOM,fill=X)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx=ttk.Scrollbar(command=product_table.xview)
    scrollbary=ttk.Scrollbar(command=product_table.yview)
    product_table.heading('ProductID', text="Product Id")
    product_table.heading('ProductName', text="Product Name")
    product_table.heading('ProductQty', text="Quantity")
    product_table.heading('ProductPrice', text="Price")
    product_table.heading('MfgCompany', text="Mfg Company")
    product_table["show"]="headings"
    product_table.column("ProductID", width=100)
    product_table.column("ProductName", width=100)
    product_table.column("ProductQty", width=100)
    product_table.column("ProductPrice", width=100)
    product_table.pack(fill= BOTH,expand=1)
    fetch_data()
    product_table.bind("<ButtonRelease-1>",fill_data)

############## Database connection for deleting an element #################3

def DeleteProductIn():
             conn=mysql.connector.connect(host="localhost",username="root",password="pass",database="inventory1")
             my_cursor=conn.cursor()
             my_cursor.execute("delete from product where ProductId=%s",(ProductIdU.get(),))
             conn.commit()
             conn.close()
             ProductDelete()
             tkMessageBox.showinfo("Delete Product",'Product has been deleted!')

######################### Exit,Logout,Close and Mainloop #######################################

def exit():
    result = tkMessageBox.askquestion('Simple Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()

def Logout():
    result = tkMessageBox.askquestion('Inventory Management', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        login(root) 

def close():
    IMS(root)
    root.mainloop()

login(root)
root.mainloop()
  