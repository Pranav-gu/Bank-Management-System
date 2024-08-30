# Data and Applications Project
## Team No. 57

Commands executed in the Video are as follows:

1) SELECT First_Name, Middle_Name, Last_Name FROM CUSTOMER WHERE Aadhaar_Card_No IN (SELECT Customer_Aadhaar FROM ACCOUNT_DETAIL WHERE Account_No IN (SELECT Account_No FROM LOAN WHERE Date_of_Sanction BETWEEN "2021-11-16" AND "2022-11-16"));
(This query first searches for all accounts whose date of sanction lies within 1 year of the current date. Then it selects the corresponding Aadhaar Card number and corresponding to that Name of the Customer is retrieved).

2) select First_Name, Middle_Name, Last_Name from CUSTOMER where Aadhaar_Card_No IN (select Nominee_ID from NOMINEE where Gender="Male");
(This query first searches for all nominees who are Male then the name is retrieved for all the Customers).

3) select First_Name, Middle_Name, Last_Name from CUSTOMER where Aadhaar_Card_No IN (select Aadhaar_Card from MADE_BY where Account_No IN (select Account_No from ACCOUNT_DETAIL WHERE Deposits-Withdrawal>=2000.0));
(This query first selects account numbers whose balance>=2000 and then selects the aadhar card numbers correspondingly, at the last the names of the customers are retrieved.)

4) select Account_No from LOAN where Amount<=50000;
(selects all accounts where amount<=5000).

5) select b.Branch_Code as BANK, avg(Deposits-Withdrawal) AS AVERAGE_BALANCE from (ACCOUNT_DETAIL AS a JOIN BANK_BRANCH AS b on a.Account_No=b.Account_No) group by b.Branch_Code;
(This query first joins the 2 tables ACCOUNT_DETAIL, BANK_BRANCH groups them according to Branch Code and then outputs branch code and average Balance corresponding to each Branch Code).

6) select b.Branch_ID AS BANK_BRANCH, max(Amount) AS MAXIMUM_LOAN_SANCTIONED from (LOAN AS l JOIN BANK_BRANCH AS b ON l.Loan_ID=b.Loan_ID) group by b.Branch_ID;
(Similar logic but this time Branch ID and Maximum Amount of Loan Sanctioned is retrieved).

7) SELECT C.First_Name FROM CUSTOMER AS C WHERE Aadhaar_Card_No IN (SELECT Aadhaar_Card FROM MAINTAINS_B WHERE Account_No IN (SELECT Account_No FROM MAINTAINS WHERE Branch_ID IN (SELECT Branch_ID FROM BANK_BRANCH))) AND C.First_Name LIKE "%IN%";
(First joins the necessary tables in between then searches for those customers who have "IN" in their Names).

8) SELECT First_Name, Middle_Name, Last_name FROM CUSTOMER WHERE Aadhaar_Card_No IN (SELECT e1.Aadhaar_Card FROM CUSTOMER_PHONE AS e1, CUSTOMER_PHONE AS e2 WHERE e1.Phone_No="NULL" AND e1.Aadhaar_Card<>e2.Aadhaar_Card);
(Self Join the Table, search for those values where phone number is null, output the Aadhaar Card Numbers to the Outer Query and then retrieve the Names of all the Customers correspondingly).

9) SELECT COUNT(*) AS Total_Number_of_Loans FROM CUSTOMER WHERE Aadhaar_Card_No IN (SELECT Customer_Aadhaar FROM ACCOUNT_DETAIL WHERE Account_No IN (SELECT Account_No FROM LOAN WHERE Date_of_Sanction BETWEEN "2021-11-16" AND "2022-11-16") AND Account_No IN (SELECT Account_No FROM MAINTAINS WHERE Branch_ID="PNB1001"));
(Search for those Aadhar Card Numbers whose corresponding Account Numbers have loans asscociated in the past one Year and search for those Accounts at the same time whose Branch ID="PNB1001" and take the count of the common values as output).

10) INSERT INTO CUSTOMER VALUES ("{aadhaar}", "{First_Name}", "{Middle_Name}", "{Last_Name}", "{pan_card}");
    INSERT INTO CUSTOMER_PHONE VALUES ("{aadhaar}", "{phone_no}");
    INSERT INTO CUSTOMER_ADDRESS VALUES ("{aadhaar}", "{address_line1}", "{address_line2}", "{address_line3}");
    INSERT INTO ACCOUNT_DETAIL VALUES ("{account_no}", "{deposits}", "{withdrawal}", "{aadhaar}");
    INSERT INTO MADE_BY VALUES ("{account_no}", "{aadhaar}");
    INSERT INTO NOMINEE VALUES ("{aadhaar}", "{nominee_First_Name}", "{nominee_Middle_Name}", "{nominee_Last_Name}", "{relation}", "{gender}", "{age}");
    INSERT INTO LOAN VALUES ("{loan_id}", "{loan_amount}", "{account_no}", "{date_of_sanction}");
    INSERT INTO HOME_LOAN VALUES ("{loan_id}", "{property_details}");
    INSERT INTO EDUCATION_LOAN VALUES ("{loan_id}", "{course_name}", "{institute_name}");
    INSERT INTO OTHER_LOAN VALUES ("{loan_id}", "{item_details}");
    INSERT INTO BANK_BRANCH VALUES ("{branch_id}", "{loan_id}", "{account_no}", "{branch_code}", "{branch_address_line1}", "{branch_address_line2}", "{branch_address_line3}", "{branch_phone}");
    INSERT INTO MAINTAINS VALUES ("{branch_id}", "{account_no}");
    INSERT INTO MAINTAINS_A VALUES ("{account_no}", "{loan_id}");
    INSERT INTO MAINTAINS_B VALUES ("{account_no}", "{aadhaar}");
(Inserts the Customer Details in the Database).

11) UPDATE CUSTOMER_PHONE SET Phone_No={c} WHERE Aadhaar_Card={a} AND Phone_No={b};
(updates the phone number of the particular Customer)

12) DELETE FROM CUSTOMER WHERE Aadhaar_Card_No="{a}";
(deletes the Customer Details whose Aadhaar Card Number is the value input by the User).

13) UPDATE NOMINEE SET First_Name="{first_name}", Middle_Name="{middle_name}", Last_Name="{last_name}", Relation="{relation}", Gender="{gender}", Age="{age}" WHERE Nominee_ID="{aadhaar}";
(updates the detail of the Nominee)

14) UPDATE BANK SET Address_Line1="{address_line1}", Address_Line2="{address_line2}", Address_Line3="{address_line3}" WHERE Code="{code}";
(updates the detail of the Bank)

The relevant outputs of all the above executed commands are shown in the video itself.



Link of the Video Of the Project : [Link](https://iiitaphyd-my.sharepoint.com/:v:/g/personal/pranav_g_students_iiit_ac_in/EdIa9LDTEPpErG0mG-eazBEBLse3mrQ4woT77O-vxSIucw?e=XnpaBt)