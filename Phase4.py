import pymysql
import subprocess as s
import pymysql.cursors

def insert_func(query):
    try:
        cur.execute(query)
        conn.commit()
        print("Insertion Successful") 

    except Exception as e:
        conn.rollback()
        print(e)
        print("Sorry, failed to execute the Query, Please Try Again..")

    return


def delete_func(query):
    try:
        cur.execute(query)
        conn.commit()
        print("Deletion Successful")

    except Exception as e:
        conn.rollback()
        print(e)
        print("Sorry, failed to execute the Query, Please Try Again..")

    return


def update_func(query):
    try:
        cur.execute(query)
        conn.commit()
        print("Updation Successful")

    except Exception as e:
        conn.rollback()
        print(e)
        print("Sorry, failed to execute the Query, Please Try Again..")

    return


def select_func(query):
    try:
        cur.execute(query)
        output = cur.fetchall()
        print(output)

    except Exception as e:
        var = s.call("clear", shell = True)
        print(e)
        print("Sorry, failed to execute the Query, Please Try Again..")

    return


def query_1():
    query = '''SELECT First_Name, Middle_Name, Last_Name FROM CUSTOMER WHERE Aadhaar_Card_No IN (SELECT Customer_Aadhaar FROM ACCOUNT_DETAIL WHERE Account_No IN (SELECT Account_No FROM LOAN WHERE Date_of_Sanction BETWEEN "2021-11-16" AND "2022-11-16"));'''
    select_func(query)
    return


def query_2():
    query = '''select First_Name, Middle_Name, Last_Name from CUSTOMER where Aadhaar_Card_No IN (select Nominee_ID from NOMINEE where Gender="Male");'''
    select_func(query)
    return



def query_3():
    query = "select First_Name, Middle_Name, Last_Name from CUSTOMER where Aadhaar_Card_No IN (select Aadhaar_Card from MADE_BY where Account_No IN (select Account_No from ACCOUNT_DETAIL WHERE Deposits-Withdrawal>=2000.0));"
    select_func(query)
    return


def query_4():
    query = "select Account_No from LOAN where Amount<=50000;"
    select_func(query)
    return


def query_5():
    query = "select b.Branch_Code as BANK, avg(Deposits-Withdrawal) AS AVERAGE_BALANCE from (ACCOUNT_DETAIL AS a JOIN BANK_BRANCH AS b on a.Account_No=b.Account_No) group by b.Branch_Code;"
    select_func(query)
    return


def query_6():
    query = "select b.Branch_ID AS BANK_BRANCH, max(Amount) AS MAXIMUM_LOAN_SANCTIONED from (LOAN AS l JOIN BANK_BRANCH AS b ON l.Loan_ID=b.Loan_ID) group by b.Branch_ID;"
    select_func(query)
    return


def query_7():
    query = '''SELECT C.First_Name FROM CUSTOMER AS C WHERE Aadhaar_Card_No IN (SELECT Aadhaar_Card FROM MAINTAINS_B WHERE Account_No IN (SELECT Account_No FROM MAINTAINS WHERE Branch_ID IN (SELECT Branch_ID FROM BANK_BRANCH))) AND C.First_Name LIKE "%IN%";'''
    select_func(query)
    return


def query_8():
    query = '''SELECT First_Name, Middle_Name, Last_name FROM CUSTOMER WHERE Aadhaar_Card_No IN (SELECT e1.Aadhaar_Card FROM CUSTOMER_PHONE AS e1, CUSTOMER_PHONE AS e2 WHERE e1.Phone_No="NULL" AND e1.Aadhaar_Card<>e2.Aadhaar_Card);'''
    select_func(query)
    return


def query_9():
    query = '''SELECT COUNT(*) AS Total_Number_of_Loans FROM CUSTOMER WHERE Aadhaar_Card_No IN (SELECT Customer_Aadhaar FROM ACCOUNT_DETAIL WHERE Account_No IN (SELECT Account_No FROM LOAN WHERE Date_of_Sanction BETWEEN "2021-11-16" AND "2022-11-16") AND Account_No IN (SELECT Account_No FROM MAINTAINS WHERE Branch_ID="PNB1001"));'''
    select_func(query)
    return


def query_10():
    # bank_branch = input("Enter the Bank Branch in which the new Customer has his/her Bank Account: ")
    aadhaar = input("Enter the Aadhaar Card Number of the new Customer (Mandatory) : ")
    First_Name = input("Enter the first name of the new Customer : ")
    Middle_Name = input("Enter the middle name of the new Customer : ")
    Last_Name = input("Enter the last name of the new Customer : ")
    pan_card = input("Enter the Pan Card Number of the new Customer : ")
    query = f'''INSERT INTO CUSTOMER VALUES ("{aadhaar}", "{First_Name}", "{Middle_Name}", "{Last_Name}", "{pan_card}");'''
    insert_func(query)

    number = input("Enter the number of phone numbers provided by the customer : ")
    number = int(number)
    for i in range(0, number, 1):
        phone_no = input("Enter the Phone Number of the new Customer : ")
        query = f'''INSERT INTO CUSTOMER_PHONE VALUES ("{aadhaar}", "{phone_no}");'''
        insert_func(query)
    
    number = input("Enter the number of addresses provided by the Customer : ")
    number = int(number)
    for i in range(0, number, 1):
        address_line1 = input("Enter the Address Line 1 of the new Customer : ")
        address_line2 = input("Enter the Address Line 2 of the New Customer : ")
        address_line3= input("Enter the Address Line 3 of the new Customer : ")
        query = f'''INSERT INTO CUSTOMER_ADDRESS VALUES ("{aadhaar}", "{address_line1}", "{address_line2}", "{address_line3}");'''
        insert_func(query)

    account_no = input("Enter the Account Number of the new Customer : ")
    deposits = input("Enter the Deposits of the New Customer : ")
    withdrawal = input("Enter the Amount Withdrawal by the New Customer : ")
    query = f'''INSERT INTO ACCOUNT_DETAIL VALUES ("{account_no}", "{deposits}", "{withdrawal}", "{aadhaar}");'''
    insert_func(query)
    query = f'''INSERT INTO MADE_BY VALUES ("{account_no}", "{aadhaar}");'''
    insert_func(query)

    a = input("Is there any Nominee Nominated by the new Customer (Press 1 if Yes / any other Key if No): ")
    if (int(a) == 1):
        nominee_First_Name = input("Enter the first name of the Nominee : ")
        nominee_Middle_Name = input("Enter the middle name of the Nominee : ")
        nominee_Last_Name = input("Enter the last name of the Nominee : ")
        relation = input("Enter the Relation of the Nominee with the new Customer : ")
        gender = input("Enter the Gender of the Nominee : ")
        age = input("Enter the age of the Nominee (In Years): ")
        query = f'''INSERT INTO NOMINEE VALUES ("{aadhaar}", "{nominee_First_Name}", "{nominee_Middle_Name}", "{nominee_Last_Name}", "{relation}", "{gender}", "{age}");'''
        insert_func(query)
    
    a = input("Has the new Customer availed any Loan (Press 1 if Yes / any other Key if No): ")
    if (int(a) == 1):
        loan_reason = input("Enter what kind of Loan it is (1 for Home Loan / 2 for Education Loan / 3 for Other Loan) : ")
        loan_id = input("Enter the Loan ID of the new Customer : ")
        loan_amount = input("Enter the Loan Value availed by the new Customer : ")
        date_of_sanction = input("Enter the Date of Sanction of the Loan : ")
        query = f'''INSERT INTO LOAN VALUES ("{loan_id}", "{loan_amount}", "{account_no}", "{date_of_sanction}");'''
        insert_func(query)
        if (int(loan_reason) == 1):
            property_details = input("Enter the Property Details of the New Customer : ")
            query = f'''INSERT INTO HOME_LOAN VALUES ("{loan_id}", "{property_details}");'''
            insert_func(query)

        elif (int(loan_reason) == 2):
            course_name = input("Enter the Course name in which the new Customer is enrolled : ")
            institute_name = input("Enter the Institute Name of the new Customer : ")
            query = f'''INSERT INTO EDUCATION_LOAN VALUES ("{loan_id}", "{course_name}", "{institute_name}");'''
            insert_func(query)

        elif (int(loan_reason) == 3):
            item_details = input("Enter the Item Details of the new Customer : ")
            query = f'''INSERT INTO OTHER_LOAN VALUES ("{loan_id}", "{item_details}");'''
            insert_func(query)
        


    branch_id= input("Enter the Branch ID where the new Customer is getting his/her Bank Account : ")
    branch_code= input("Enter the Branch Code of the Bank in which the new Customer is getting his/her Bank Account : ")
    branch_address_line1 = input("Enter the Address Line 1 of the Bank Branch : ")
    branch_address_line2 = input("Enter the Address Line 2 of the Bank Branch : ")
    branch_address_line3 = input("Enter the Address Line 3 of the Bank Branch : ")
    branch_phone = input("Enter the Phone No. of the Bank Branch : ")
    query = f'''INSERT INTO BANK_BRANCH VALUES ("{branch_id}", "{loan_id}", "{account_no}", "{branch_code}", "{branch_address_line1}", "{branch_address_line2}", "{branch_address_line3}", "{branch_phone}");'''
    insert_func(query)

    query = f'''INSERT INTO MAINTAINS VALUES ("{branch_id}", "{account_no}");'''
    insert_func(query)

    query = f'''INSERT INTO MAINTAINS_A VALUES ("{account_no}", "{loan_id}");'''
    insert_func(query)

    query = f'''INSERT INTO MAINTAINS_B VALUES ("{account_no}", "{aadhaar}");'''
    insert_func(query)
    return


def query_11():
    a = input("Enter the Aadhaar Card Number of the Customer whose Phone Number you want to get updated : ")
    b = input("Enter the Phone Number which you want to be updated to a new value : ")
    c = input("Enter the new Phone Number of the Customer : ")
    query = f"UPDATE CUSTOMER_PHONE SET Phone_No={c} WHERE Aadhaar_Card={a} AND Phone_No={b};"
    update_func(query)
    return


def query_12():
    a = input("Enter the Aadhaar Card Number of the Customer whose Account you want to delete : ")
    query = f'''DELETE FROM CUSTOMER WHERE Aadhaar_Card_No="{a}";'''
    delete_func(query)
    return


def query_13():
    aadhaar = input("Enter the Aadhaar Card Number of the Customer whose Nominee Details you want to get updated : ")
    first_name = input("Enter the new Nominee's First Name : ")
    middle_name = input("Enter the new Nominee's Middle Name : ")
    last_name = input("Enter the new Nominee's Last Name : ")
    relation = input("Enter the new Nominee's relation with the Customer : ")
    gender = input("Enter the new Nominee's Gender : ")
    age = input("Enter the new Nominee's age : ")
    query = f'''UPDATE NOMINEE SET First_Name="{first_name}", Middle_Name="{middle_name}", Last_Name="{last_name}", Relation="{relation}", Gender="{gender}", Age="{age}" WHERE Nominee_ID="{aadhaar}";'''
    update_func(query)
    return


def query_14():
    code = input("Enter the Code of the Bank whose Address you want to get updated : ")
    address_line1 = input("Enter the new Address Line 1 of the Bank : ")
    address_line2 = input("Enter the new Address Line 2 of the Bank : ")
    address_line3 = input("Enter the new Address Line 3 of the Bank : ")
    query = f'''UPDATE BANK SET Address_Line1="{address_line1}", Address_Line2="{address_line2}", Address_Line3="{address_line3}" WHERE Code="{code}";'''
    update_func(query)
    return


while True:
    var = s.call("clear", shell = True)
    username = input("Enter the Username of the MySQL Server : ")
    password = input("Enter the Password of the MySQL Server : ")

    try:
        conn = pymysql.connect(host = "localhost", port = 3306, user = "root", password = "", db = "project", cursorclass=pymysql.cursors.DictCursor)  #replace password in the required string
        var = s.call("clear", shell = True)

        if(conn.open):
            print("Connection Successful")
        else:
            print("Connection Failed.")
        
        var = input("Press any Key to Continue : ")

        with conn.cursor() as cur:
            while True:
                print("Please Read the Options Carefully and Choose the Operation you want to perform : ")
                print("Enter 1 if you want to select all the customers who have availed Loan in the past One Year.")
                print("Enter 2 if you want to select all the Customers who have nominated Male Nominees.")
                print("Enter 3 if you want to select customers whose Balance in their Bank Account >= 2000.")
                print("Enter 4 if you want to select all Bank Accounts whose associated Loan Value <= 50000.")
                print("Enter 5 if you want to find the Average of Balance of all Customers in a particular Bank Branch.")
                print("Enter 6 if you want to find the Maximum Loan Amount Sanctioned by any Bank Branch.")
                print('''Enter 7 if you want to select all the Customers in a Bank Branch whose Name contains "IN".''')
                print("Enter 8 if you want to select all the Customers who have not given any Phone Number for opening of Bank Account.") 
                print("Enter 9 if you want to find out the Total Number of Loans Sanctioned in an Year in a Branch.") 
                print("Enter 10 if you want to insert data of a new Customer in a Bank Branch") 
                print("Enter 11 if you want to update the Phone Number of a Customer.")
                print("Enter 12 if you want to delete Account of a particular Customer.")
                print("Enter 13 if you want to update the Nominee Details of a Customer.")
                print("Enter 14 if you want to update the Address of a Customer.")
                print("Enter 15 if you want to Logout..") 


                a = input()
                a = int(a)
                
                if (a == 1):
                    query_1()
                elif (a == 2):
                    query_2()
                elif (a == 3):
                    query_3()
                elif (a == 4):
                    query_4()
                elif (a == 5):
                    query_5()
                elif (a == 6):
                    query_6()
                elif (a == 7):
                    query_7()
                elif (a == 8):
                    query_8()
                elif (a == 9):
                    query_9()
                elif (a == 10):
                    query_10()
                elif (a == 11):
                    query_11()
                elif (a == 12):
                    query_12()
                elif (a == 13):
                    query_13()
                elif (a == 14):
                    query_14()
                elif (a == 15): 
                    exit()

                var = input("Enter any Key to Continue : ")
                var = s.call("clear", shell = True)

    except Exception as e:
        var = s.call("clear", shell = True)
        print(e)
        print("Sorry, failed to connect to the Database, Please Try Again.")
        var = input("Press any Key to Continue : ")