"""tables positions:"""

from databases import generateDatabase

#generateDatabase()

def generateTables(conn):

    DbObj = conn.cursor()

    DbObj.execute("Create Table Positions (id integer PRIMARY KEY, name TEXT, description TEXT, paymentNumbers integer, deleted BOOLEAN, createdDate DATETIME, lastModifiedDate DATETIME)")
    DbObj.execute("Create Table Salaries (id integer PRIMARY KEY, name TEXT, baseSalary float, isBonusSalary BOOLEAN, BonusAmount FLOAT, taxesPercentage FLOAT, insurancePercentage FLOAT, deleted BOOLEAN, createdDate DATETIME, lastModifiedDate DATETIME)")
    DbObj.execute("Create Table Employees (id integer PRIMARY KEY, firstName TEXT, lastName TEXT, phoneNumber TEXT, address TEXT, email TEXT, socialSecurityNumber TEXT, salaryid TEXT, positionId TEXT, deleted BOOLEAN, createdDate DATETIME, lastModifiedDate DATETIME)")

    conn.commit()

dataconection = generateDatabase()

generateTables(dataconection)