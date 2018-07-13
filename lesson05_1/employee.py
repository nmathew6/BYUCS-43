import sqlite3


connection = sqlite3.connect('employee.db')

try:
    connection.execute('DROP TABLE employees')
except:
    pass

def select_some(string):
    cursor = connection.cursor()
    product_cursor = cursor.execute(string)
    product_list = product_cursor.fetchall()
    return product_list


connection.execute('CREATE TABLE employees (empid, empfname, emplname, empemail, empsalary, empaddress)')
connection.execute('INSERT INTO employees(empid, empfname, emplname, empemail, empsalary, empaddress) VALUES (?,?,?,?,?,?)', [1, 'Nathan', 'Mathew', 'nmathew@company.com', 500, '800 Timbuktoo lane'])
connection.execute('INSERT INTO employees(empid, empfname, emplname, empemail, empsalary, empaddress) VALUES (?,?,?,?,?,?)', [2, 'Aiden', 'Mathew', 'amathew@company.com', 0, '123 Fat lane'])
connection.execute('INSERT INTO employees(empid, empfname, emplname, empemail, empsalary, empaddress) VALUES (?,?,?,?,?,?)', [3,'Bob','Kilo','bkilo@company.com',123,'16 Generic lane'])
connection.execute('INSERT INTO employees(empid, empfname, emplname, empemail, empsalary, empaddress) VALUES (?,?,?,?,?,?)', [4,'Billy','Joe','bjoe@company.com',334,'89 North lane'])
connection.execute('INSERT INTO employees(empid, empfname, emplname, empemail, empsalary, empaddress) VALUES (?,?,?,?,?,?)', [5,'Pete','Etep','petep@company.com',400,'11 South lane'])
connection.commit()

print (select_some('SELECT empid, empfname, emplname FROM employees where empid = 1'))

connection.execute('update employees set empsalary=? where empid = ?', [1000, 1])
connection.commit()

connection.execute('DELETE FROM employees WHERE empid = ?', [4])

