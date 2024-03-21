# Rasmane Sawadogo
# CNE 370 - Final Project
# Collaborated with Rosa H

# This is a python that script will talk to Maxscale instance, perform the following queries, and print the output to the console.

import mysql.connector

conn = mysql.connector.connect(user="maxuser", password="maxpwd", host="127.0.0.1", port="4000")

cursor = conn.cursor()

# Query 1: The largest zipcode in zipcodes_one
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one")
largest_zipcode = cursor.fetchall()
for zipcode in largest_zipcode:
    print("The largest zipcode in zipcodes_one:", largest_zipcode)
    break

# Query 2: All zipcodes where state=KY (Kentucky)
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one  WHERE state='KY'")
ky_zipcodes = cursor.fetchall()
print("All zipcodes where state=KY (Kentucky):")
for row in ky_zipcodes:
    print(row)
    break

# Query 3: All zipcodes between 40000 and 41000
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000")
zipcodes_between = cursor.fetchall()
print("All zipcodes between 40000 and 41000:")
for row in zipcodes_between:
    print(row)
    break
# Query 4: The TotalWages column where state=PA (Pennsylvania)
cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state='PA'")
total_wages_pa = cursor.fetchall()
print("The TotalWages column where state=PA (Pennsylvania):")
for row in total_wages_pa:
    print(row[0])
    break


# Query 2: The largest zipcode in zipcodes_two
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two")
largest_zipcode = cursor.fetchall()
for zipcode in largest_zipcode:
    print("The largest zipcode in zipcodes_two:", largest_zipcode)
    break

# Query 2: All zipcodes where state=KY (Kentucky)
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two  WHERE state='KY'")
ky_zipcodes = cursor.fetchall()
print("All zipcodes where state=KY (Kentucky):")
for row in ky_zipcodes:
    print(row)
    break

# Query 3: All zipcodes between 40000 and 41000
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000")
zipcodes_between = cursor.fetchall()
print("All zipcodes between 40000 and 41000:")
for row in zipcodes_between:
    print(row)
    break
# Query 4: The TotalWages column where state=PA (Pennsylvania)
cursor.execute("SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE state='PA'")
total_wages_pa = cursor.fetchall()
print("The TotalWages column where state=PA (Pennsylvania):")
for row in total_wages_pa:
    print(row[0])
    break


cursor.close()
conn.close()

