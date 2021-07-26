from prettytable import from_db_cursor
import mysql.connector as aq
ad=aq.connect(host='localhost',user='root',passwd='hussain786',database='aqib')
aq=ad.cursor()

def whr():
    print('\nWaist-to-hip ratio, also known as waist-hip ratio, is the circumference of the waist divided by the circumference of the hips.')
    print('The waist-to-hip ratio (WHR) is a quick measure of fat distribution that may help indicate a person overall health. People who carry more weight around their middle than their hips may be at a higher risk of developing certain health conditions.')
    print('\nMeasuring your waist:-')
    print('use your tape measure to measure midway between your lowest rib and the top of your hips - it should be the part just above your belly button.')
    print('Measuring your hips:-')
    print('measure at the widest point around the buttocks. Again, hold the tape snugly but do not pull it in, and make sure its level all the way around.')
    wa=float(input('\nEnter your Waist measurement(inches):'))
    ha=float(input('Enter your Hip measurement(inches):'))
    res=round((wa/ha),3)
    if res<0.85:
       print('YOUR Waist-to-Hip Ratio(WHR) is:',res) 
       print('\nExcellent health!!!')
    elif res>0.85 and res<0.89:
        print('YOUR Waist-to-Hip Ratio(WHR) is:',res)
        print('\nYour Health is GOOD')
    elif res>0.90 and res<0.95:
        print('YOUR Waist-to-Hip Ratio(WHR) is:',res)
        print('\nYour Health is at AVERAGE')
    elif res>0.95 and res<1:
        print('YOUR Waist-to-Hip Ratio(WHR) is:',res)
        print('\nYour Health is at RISK!!')
    else:
        print('YOUR Waist-to-Hip Ratio(WHR) is:',res)
        print('\nYour Health is at HIGH RISK!!')
        
def fwhr():
    print('\nWaist-to-hip ratio, also known as waist-hip ratio, is the circumference of the waist divided by the circumference of the hips. What does a persons waist-to-hip ratio say about their health?')
    print('The waist-to-hip ratio (WHR) is a quick measure of fat distribution that may help indicate a person overall health. People who carry more weight around their middle than their hips may be at a higher risk of developing certain health conditions.')
    print('\nMeasuring your waist:-')
    print('use your tape measure to measure midway between your lowest rib and the top of your hips - it should be the part just above your belly button.')
    print('Measuring your hips:-')
    print('measure at the widest point around the buttocks. Again, hold the tape snugly but do not pull it in, and make sure its level all the way around.')
    wa=float(input('\nEnter your Waist measurement(inches):'))
    ha=float(input('Enter your Hip measurement(inches):'))
    res=round((wa/ha),3)
    if res<0.75:
       print('YOUR Waist-to-Hip Ratio(WHR) is:',res) 
       print('\nExcellent health!!!')
    elif res>0.75 and res<0.80:
        print('YOUR Waist-to-Hip Ratio(WHR) is:',res)
        print('\nYour Health is GOOD')
    elif res>0.80 and res<0.85:
        print('YOUR Waist-to-Hip Ratio(WHR) is:',res)
        print('\nYour Health is at AVERAGE')
    elif res>0.85 and res<0.90:
        print('YOUR Waist-to-Hip Ratio(WHR) is:',res)
        print('\nYour Health is at RISK!!')
    else:
        print('YOUR Waist-to-Hip Ratio(WHR) is:',res)
        print('\nYour Health is at HIGH RISK!!')
        
def bmr():
    print('\nBasal Metabolic Rate (BMR) is the amount of energy your body needs to function.')
    print('We can estimate BMR based on height in inches, weight in pounds, age in years, and gender.')
    print('Given your BMR we can then estimate the number of calories needed per day to maintain your weight.')
    a=float(input('\nEnter height in feet:')) 
    b=float(input('Enter weight in kilogramme:')) 
    c=float(input('Enter age in years:'))
    BMR = 66.47 + (6.23 *2.205* b) + (12.7 *12* a) - (6.8 * c)
    CAL=((BMR*0.55)+BMR)
    print('\nYour BMR is :',round(BMR,3))
    print('\nCalories needed to maintain weight:',round(CAL,3))
def fbmr():
    print('\nBasal Metabolic Rate (BMR) is the amount of energy your body needs to function.')
    print('We can estimate BMR based on height in inches, weight in pounds, age in years, and gender.')
    print('Given your BMR we can then estimate the number of calories needed per day to maintain your weight.')
    a=float(input('\nEnter height in feet:')) 
    b=float(input('Enter weight in kilogramme:')) 
    c=float(input('Enter age in years:'))
    BMR = 655.1 + (4.35 *2.205* b) + (4.7 * 12 *a) - (4.7* c)
    CAL=((BMR*0.55)+BMR)
    print('Your BMR is :',round(BMR,3))
    print('Calories needed to maintain weight:',round(CAL,3))
    
def bmi():
    ty='and is commonly used as an indicator of whether you might be in a risk category for health problems caused by your weight.'
    print('\nThe body mass index calculator measurement is the calculation of your body weight in relation to your height'+ ty)
    print('Using a BMI calculator such as the one on this programme, you enter your weight and height measurements')
    weightInKilo = float(input('Enter your weight in kilo:'))
    heightInFeet = float(input('Enter your height in feet:'))
    heightInMeter = heightInFeet * 12 * 0.025
    bodyMassIndex = round((weightInKilo / (heightInMeter ** 2)),3)
    if bodyMassIndex < 15:
        print('Your BMI = ' + str(bodyMassIndex)  + '\nYou are very severely underweight.')
    elif bodyMassIndex >= 15 and bodyMassIndex <= 16 :
        print('Your BMI = ' + str(bodyMassIndex)     + '\nYou are severely underweight.')
    elif bodyMassIndex > 16 and bodyMassIndex <= 18.5:
        print('Your BMI = ' + str(bodyMassIndex) + '\nYou are underweight.')
    elif bodyMassIndex > 18.5 and bodyMassIndex <= 25:
        print('Your BMI = ' + str(bodyMassIndex) + ' \nYou are Normal(healthy weight).')
    elif bodyMassIndex > 25 and bodyMassIndex <= 30:
        print('Your BMI = ' + str(bodyMassIndex) + '\nYou are overweight.')
    elif bodyMassIndex > 30 and bodyMassIndex <= 35:
        print('Your BMI = ' + str(bodyMassIndex) + '\nYou are moderately obese.')
    elif bodyMassIndex > 35 and bodyMassIndex <= 40:
        print('Your BMI = ' + str(bodyMassIndex) + '\nYou are severely obese.')
    elif bodyMassIndex > 40:
        print('Your BMI = ' + str(bodyMassIndex) + '\nYou are very severely obese.')
def db():
    import calendar 
    n=input('Enter your Name:' ) 
    g=input('Enter your Gender(m/f):' )   
    a=int(input('Enter your Age:' ))
    p=int(input('Enter your Phone_no. :' )) 
    po=input('Enter your Problem :' )
    qe='select name,specialisation,fees from doctor_details '
    aq.execute(qe)
    mytable = from_db_cursor(aq)
    print(mytable)
    dc=input('Enter Doctor name(same as above given|^|) :')    
    print ("The calender of year 2020 is : ")  
    print (calendar.calendar(2020,2,1,6,6))
    print ('You can choose your date which is given above|^|')
    d=input('Enter your Appointment Date(YYYY-MM-DD):')
    s=input('Enter your Shift(morning\evening) :' )
    u=n[:3]+str(a)+str(p)[:4:-1]
    print('\nYour Appointment ID is:',u)
    ins="INSERT INTO post VALUES ('{}','{}','{}',{},{},'{}','{}','{}','{}')".format(u,n,g,a,p,po,dc,d,s)
    aq.execute(ins)
    ad.commit()
    qer='select * from post where App_id="{}"'.format(u)
    aq.execute(qer)
    mytable = from_db_cursor(aq)
    print(mytable)
    print('Your Appointment has been fixed.please remember your Appointment ID for further use!!\n')
def yrapp():
    try:
        i=input('Enter your Appointment ID:')
        qe='select * from post where App_id="{}"'.format(i)
        aq.execute(qe)
        mytable = from_db_cursor(aq)
        print(mytable)
    except:
        print('error')
def alapp():
    aq.execute('select * from post')
    mytable = from_db_cursor(aq)
    print(mytable)
    
def chge():
    isd=input('Enter your Appointment ID:')
    qer='select * from post where App_id="{}"'.format(isd)
    aq.execute(qer)
    mytable = from_db_cursor(aq)
    print(mytable)
    up=input('Enter which field you would change(*case sensitive language):' )
    op=input('Enter new '+str(up)+':')
    qer='UPDATE post SET {}="{}" WHERE App_id="{}" '.format(up,op,isd)
    aq.execute(qer)
    ad.commit()
    print('Your Appointment has been updated!!' )
    pk=input('Do you want to see the changes?(y/n):')
    if pk=='y':
        qr='select * from post where App_id="{}"'.format(isd)
        aq.execute(qr)
        mytable = from_db_cursor(aq)
        print(mytable)
def ch_pat():
    sd=input("Enter your name:")
    qer='select * from post where doctor_name="{}" '.format(sd)
    aq.execute(qer)
    mytable = from_db_cursor(aq)
    print(mytable)
    
def doc_chge():
    isd=input("Enter your Doctor's name:")
    qer='select * from doctor_details where name="{}"'.format(isd)
    aq.execute(qer)
    mytable = from_db_cursor(aq)
    print(mytable)
    up=input('Enter which field you would change(*case sensitive language):' )
    op=input('Enter new '+str(up)+':')
    qer='UPDATE doctor_details SET {}="{}" WHERE name="{}" '.format(up,op,isd)
    aq.execute(qer)
    ad.commit()
    print('Your Details has been updated!!' )
    pk=input('Do you want to see the changes?(y/n):')
    if pk=='y':
        qr='select * from doctor_details where name="{}"'.format(isd)
        aq.execute(qr)
        mytable = from_db_cursor(aq)
        print(mytable)
def del_doc():
    isd=input("Enter your Doctor's name:")
    aq.execute("select * from doctor_details where name='"+isd+"'")
    mytable = from_db_cursor(aq)
    print(mytable)
    p=input("you really wanna delete this data? (y/n):")
    if p=="y":
      aq.execute("delete from doctor_details where name='"+isd+"'")
      ad.commit()
      print("SUCCESSFULLY DELETED!!")
    else:
      print("NOT DELETED")

def doc_add():
    name=input("ENTER DR. NAME:")
    spe=input("ENTER SPECIALISATION:")
    age=input("ENTER AGE:")
    add=input("ENTER ADDRESS:")
    cont=input("ENTER CONTACT NO.:")
    fees=input("ENTER FEES:")
    ms=input("ENTER MONTHLY_SALARY:")
    aq.execute("insert into doctor_details values('"+name+"','"+spe+"','"+age+"','"+add+"','"+cont+"','"+fees+"','"+ms+"')")
    ad.commit()
    print("SUCCESSFULLY ADDED !!!")
    
print("\t\t       *********           ")
print("\t\t       *:::::::*           ")
print("\t\t       *:::::::*           ")
print("\t\t********::::::::********** ")
print("\t\t*:::::::::MEDICOX::::::::* ")
print("\t\t*:::::A VIRTUAL CLINIC:::* ")
print("\t\t********::::::::********** ")
print("\t\t       *:::::::*           ")
print("\t\t       *:::::::*           ")
print("\t\t       *********           ")
while True:
    print(' ___________________________ ')
    print('|1.Check your Health Status |')
    print('|2.Change/Fix an Appointment|')
    print('|3.Health Awareness         |')
    print('|4.ADMINISTRATION           |')
    print('|5.EXIT                     |')
    print('|___________________________|')
    ch= int(input('\nENTER YOUR CHOICE:'))
    if ch==1:
        while True:
            print('\n')
            print('|***************************|')
            print('|1.Body Mass Index(BMI)     |')
            print('|2.Basal Metabolic Rate(BMR)|')
            print('|3.Waist-to-Hip Ratio(WHR)  |')
            print('|4.RETURN TO MAIN MENU      |')
            print('|***************************|')
            f= int(input('\nENTER YOUR CHOICE:'))
            if f==1:
               bmi()
            elif f==2:
                print('\n|-----------------------|')
                print('|1.For Male canditate   |')
                print('|2.For Female canditate |')
                print('|-----------------------|')
                d=int(input('\nENTER YOUR CHOICE:'))
                if d==1:
                    bmr()
                elif d==2:
                    fbmr()
                else:
                    print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')
            elif f==3:
                print('\n|-----------------------|')
                print('|1.For Male canditate   |')
                print('|2.For Female canditate |')
                print('|-----------------------|')
                d=int(input('\nENTER YOUR CHOICE:'))
                if d==1:
                    whr()
                elif d==2:
                    fwhr()
                else:
                    print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')  
            elif f==4:
                break
            else:
                 print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')
    elif ch==2:
         while True:
            print('|***************************|')
            print('|1.Fix an Appointment       |')
            print('|2.Check Appointment List   |')
            print('|3.Change your Appointment  |')
            print('|4.RETURN TO MAIN MENU      |')
            print('|***************************|')
            x= int(input('\nENTER YOUR CHOICE:'))
            if x==1:
               db()
            elif x==3:
               chge()
            elif x==2:
               print('\n|---------------------------|')
               print('|1.For Your Appointment     |')
               print('|2.For All Appointment List |')
               print('|---------------------------|')
               p=int(input('\nENTER YOUR CHOICE:'))
               if p==1:
                    yrapp()
               elif p==2:
                    alapp()
               else:
                    print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')
            elif x==4:
                break
            else:
             print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')
    elif ch==3:
        while True:
            print('\n|----------------------|')
            print('|1.Malaria             |')
            print('|2.Dengue              |')
            print('|3.Chickenpox          |')
            print('|4.Typhoid             |')
            print('|5.Hair Loss           |')
            print('|6.RETURN TO MAIN MENU |')
            print('|----------------------|')
            p=int(input('\nENTER YOUR CHOICE:'))
            if p==1:
                f= open(r'C:\Users\HP\Desktop\waste\project data\malaria.txt','r')
                k=f.read()
                print(k)
            elif p==2:
                f= open(r'C:\Users\HP\Desktop\waste\project data\dengue.txt','r')
                k=f.read()
                print(k)
            elif p==3:
                f= open(r'C:\Users\HP\Desktop\waste\project data\chickenpox.txt','r')
                k=f.read()
                print(k)
            elif p==4:
                f= open(r'C:\Users\HP\Desktop\waste\project data\typhoid.txt','r')
                k=f.read()
                print(k)
            elif p==5:
                f= open(r'C:\Users\HP\Desktop\waste\project data\hair loss.txt','r')
                k=f.read()
                print(k)
            elif p==6:
                break
            else:
             print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')
    elif ch==4:
        while True:
            print('\n|----------------------------------|')
            print('|1.Check appointment with patients |')
            print('|2.Show Details Of Doctors         |')
            print('|3.Add new Doctor                  |')
            print("|4.change Doctor's record          |")
            print("|5.Delete Doctor's record          |")
            print('|6.RETURN TO MAIN MENU             |')
            print('|----------------------------------|')
            p=int(input('\nENTER YOUR CHOICE:'))
            if p==1:
                ch_pat()
            elif p==2:
               print('\n|----------------------|')
               print('|1.For Specific Doctor |')
               print('|2.For All Doctors     |')
               print('|----------------------|')
               p=int(input('\nENTER YOUR CHOICE:'))
               if p==1:
                   i=input('Enter your Name:')
                   qe='select * from doctor_details where name="{}"'.format(i)
                   aq.execute(qe)
                   mytable = from_db_cursor(aq)
                   print(mytable)
               elif p==2:
                   aq.execute('select * from doctor_details ')
                   mytable = from_db_cursor(aq)
                   print(mytable)
               else:
                print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')
            elif p==3:
                doc_add()
            elif p==4:
                doc_chge()
            elif p==5:
                del_doc()
            elif p==6:
                break
            else:
             print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')
        
    elif ch==5:
        break
    else:
        print('INVALID ENTRY!!! PLEASE ENTER A VALID ENTRY.')
