import sqlite3
from collections import Counter
import pandas as pd

def c1():
    conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
    c=conect.cursor()
    suvs=c.execute("""SELECT car_plate_nr FROM car_detail WHERE car_type ="SUV" """).fetchall()
    list_suv=tuple(i[0] for i in suvs)
    lengthofsuvlist=len(list_suv)
    print("  Id    Name")
    i=0
    while i < lengthofsuvlist:
        branchcode=c.execute("""SELECT branch_code FROM linker_table WHERE car_plate_nr =? """,(list_suv[i],)).fetchall()
        listbranchcode=tuple(i[0] for i in branchcode)
        superviosrname=c.execute("""SELECT supervisor_name  FROM branch_info WHERE branch_code =? """,(listbranchcode[0],)).fetchall()
        superviosrid=c.execute("""SELECT supervisor_id  FROM branch_info WHERE branch_code =? """,(listbranchcode[0],)).fetchall()
        print(superviosrid[0]+superviosrname[0])
        i=i+1
    conect.commit()
    conect.close()

def c2():
    conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
    c=conect.cursor()
    bill=c.execute("""SELECT bill_nr FROM bill_detail WHERE final_bill >500 """).fetchall()
    list_bill=tuple(i[0] for i in bill)
    
    lengthbillnr=len(list_bill)
    print("  Id    Name")
    i=0
    while i < lengthbillnr:
        branchcode=c.execute("""SELECT branch_code FROM linker_table WHERE bill_nr =? """,(list_bill[i],)).fetchall()
        listbranchcode=tuple(i[0] for i in branchcode)
        
        superviosrname=c.execute("""SELECT supervisor_name FROM branch_info WHERE branch_code =? """,(listbranchcode[0],)).fetchall()

        superviosrid=c.execute("""SELECT supervisor_id  FROM branch_info WHERE branch_code =? """,(listbranchcode[0],)).fetchall()

        print(superviosrid[0]+superviosrname[0])
        i=i+1
    conect.commit()
    conect.close()

def c3():
    conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
    c=conect.cursor()
    billnr=c.execute("""SELECT bill_nr FROM bill_detail WHERE bill_date >='01/05/2021' AND bill_date <= '31/05/2021' """).fetchall()
    list_billnr=tuple(i[0] for i in billnr)
    lengthbillnr=len(list_billnr)
    print("  Id    Name")
    i=0
    while i < lengthbillnr:
        branchcode=c.execute("""SELECT branch_code FROM linker_table WHERE bill_nr =? """,(list_billnr[i],)).fetchall()
        listbranchcode=tuple(i[0] for i in branchcode)
        
        superviosrname=c.execute("""SELECT supervisor_name FROM branch_info WHERE branch_code =? """,(listbranchcode[0],)).fetchall()

        superviosrid=c.execute("""SELECT supervisor_id  FROM branch_info WHERE branch_code =? """,(listbranchcode[0],)).fetchall()

        print(superviosrid[0]+superviosrname[0])
        i=i+1
    conect.commit()
    conect.close()

def c4():
    conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
    c=conect.cursor()
    billpenalty=c.execute("""SELECT bill_nr FROM bill_detail WHERE penalty > 0 """).fetchall()
    list_billpenalty=tuple(i[0] for i in billpenalty)
    
    lengthbillpenalty=len(list_billpenalty)
    print("  Id    Name")
    i=0
    while i < lengthbillpenalty:
        branchcode=c.execute("""SELECT branch_code FROM linker_table WHERE bill_nr =? """,(list_billpenalty[i],)).fetchall()
        listbranchcode=tuple(i[0] for i in branchcode)
        
        superviosrname=c.execute("""SELECT supervisor_name FROM branch_info WHERE branch_code =? """,(listbranchcode[0],)).fetchall()

        superviosrid=c.execute("""SELECT supervisor_id  FROM branch_info WHERE branch_code =? """,(listbranchcode[0],)).fetchall()

        print(superviosrid[0]+superviosrname[0])
        i=i+1
    conect.commit()
    conect.close()

def c5():
    conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
    c=conect.cursor()
    mostrented=c.execute("""SELECT car_type FROM car_detail """).fetchall()
    list_mostrented=tuple(i[0] for i in mostrented)
    c=Counter(list_mostrented)
    print(c)
    

def crate_and_insert():
    try:
        conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
        c=conect.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS "branch_info" ("branch_code" INTEGER,"branch_name" CHAR,"supervisor_id"INTEGER,"supervisor_name" CHAR,PRIMARY KEY("branch_code"))""")
        conect.commit()
        c.execute("""INSERT INTO branch_info ( branch_code, branch_name, supervisor_id, supervisor_name )
                    VALUES
                    (100023,'Coventry',871,'Anna Smith'),
                    (456109,'Leamington Spa',149,'John Cruise'),
                    (555901,'Wolverhampton',111,'Catherine Johnson'),
                    (876734,'Walsall',102,'David Brown'),
                    (981256,'Warwick',823,'James Doherty')""")
        conect.commit()
        print("done branch info")  
    except:
        print("failed")

    try:
        conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
        c=conect.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS car_detail (car_plate_nr VARCHAR, car_description VARCHAR, car_type CHAR, PRIMARY KEY (car_plate_nr))")
        conect.commit()
        c.execute("""INSERT INTO car_detail ( car_plate_nr, car_description, car_type)
                VALUES
                ('DS4049','BA1234','SUV'),
                ('DL3434','BA6753','Sports_Car'),
                ('OP9817','BA1561','SUV'),
                ('SJ7182','BA9878','Hatchback'),
                ('BN9745','BA9123','SUV'),
                ('LA5142','BA8177','Sedan'),
                ('CB0098','BA4545','Sports_Car'),
                ('ZX7222','BA1000','Coupe'),
                ('QW0128','BA8882','Sedan'),
                ('PO8123','BA5656','SUV'),
                ('IU7878','BA0012','Hatchback'),
                ('GF5612','BA3421','Sedan'),
                ('NM8787','BA4545','Sports_Car'),
                ('VC1111','BA8177','Sedan'),
                ('FG7100','BA9123','Hatchback'),
                ('RE6000','BA9878','Sedan'),
                ('TR6199','BA1561','SUV'),
                ('DR1166','BA6753','Sports_Car'),
                ('BP9111','BA1234','Coupe')
                """)
        conect.commit()
        print("done car  detail ")
    except:
        print("failed")

    try:
        conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
        c=conect.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS bill_detail (bill_nr INTEGER, bill_date DATE, penalty INTEGER, final_bill INTEGER, PRIMARY KEY (bill_nr))""")
        conect.commit()
        c.execute("""INSERT INTO bill_detail ( bill_nr, bill_date,penalty, final_bill)
                VALUES
                (166651, '18/01/2021',50,1050),
                (123111, '19/02/2021',0,500),
                (561909, '06/03/2021',0,480),
                (565690, '29/01/2021',0,680),
                (128976, '10/10/2021',0,710),
                (511899, '25/11/2021',20,1500),
                (141421, '03/12/2021',0,850),
                (514879, '29/10/2021',0,1250),
                (771100, '16/11/2021',20,300),
                (675912, '06/01/2022',50,350),
                (991762, '08/02/2022',0,950),
                (110054, '19/07/2021',100,1400),
                (378123, '12/08/2021',20,450),
                (808051, '18/09/2021',0,670),
                (100023, '21/07/2021',0,1030),
                (611554, '27/08/2021',50,520),
                (888712, '10/04/2021',0,490),
                (343412, '28/05/2021',20,1230),
                (222678, '04/06/2021',0,1680)
                """)
        conect.commit()
        print("done bill detail")
    except:
        print("failed")
    
    try:
        conect=sqlite3.connect("C:/Users/Talha/Desktop/R/4005/test.db")
        c=conect.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS linker_table (bill_nr INTEGER PRIMARY KEY REFERENCES bill_detail (bill_nr) MATCH "FULL", branch_code INTEGER REFERENCES branch_info (branch_code) MATCH SIMPLE, car_plate_nr VARCHAR REFERENCES car_detail (car_plate_nr) MATCH "FULL")""")
        conect.commit()
        c.execute("""INSERT INTO linker_table  ( bill_nr, branch_code, car_plate_nr)
                VALUES
                (166651,876734, 'DS4049'),
                (123111,876734, 'DL3434'),
                (561909,876734, 'OP9817'),
                (565690,876734, 'SJ7182'),
                (128976,100023, 'BN9745'),
                (511899,100023, 'LA5142'),
                (141421,100023, 'CB0098'),
                (514879,100023, 'ZX7222'),
                (771100,100023, 'QW0128'),
                (675912,456109, 'PO8123'),
                (991762,456109, 'IU7878'),
                (110054,981256, 'GF5612'),
                (378123,981256, 'NM8787'),
                (808051,981256, 'VC1111'),
                (100023,981256, 'FG7100'),
                (611554,981256, 'RE6000'),
                (888712,555901, 'TR6199'),
                (343412,555901, 'DR1166'),
                (222678,555901, 'BP9111')
                """)
        conect.commit()
        print("done main detail")
    except:
        print("failed")
    
    conect.close()

def analyze():
    data=pd.read_csv(r"C:/Users/Talha/Desktop/R/4005/work..csv")
    print(data.shape)
    a=matplotib inline
    print(data.hist(columns="car_type",bin=20))

analyze()