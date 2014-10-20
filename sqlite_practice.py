
import sqlite3

createDb = sqlite3.connect(':memory:') #only for temporary memory; use an actual *.db file to store memory

queryCurs = createDb.cursor()

def createTable():
    queryCurs.execute('''CREATE TABLE customers
    (id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT, state TEXT, balance REAL)''')

def addCust(name,street,city,state,balance):
    queryCurs.execute('''INSERT INTO customers (name,street,city,state,balance)
    VALUES(?,?,?,?,?)''', (name,street,city,state,balance))

def main():
    createTable()
    
    addCust('Jacob Albritton', '7950 N Stadium Dr', 'Houston', 'TX', 150.75)
    addCust('Sam Paulsen', '6500 Main Street', 'Houston', 'TX', 225.12)
    addCust('Bagrat Grigorian', '1234 Bissonnet St', 'Houston', 'TX', -50.50)
    
    createDb.commit()
    
    queryCurs.execute('SELECT * FROM customers ORDER BY balance')
    
    listTitle = ['ID Num ','Name ','Street ','City ','State ','Balance ']
    k=0
    
    
    for i in queryCurs:
        print "\n"
        for j in i:
            print listTitle[k],
            print j
            if k < 5: k+=1
            else: k=0
    
    queryCurs.close()

if __name__ == '__main__': main()