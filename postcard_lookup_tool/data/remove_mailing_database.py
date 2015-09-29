import pyodbc
from contextlib import closing

def connect_db(database):
    conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=SQLSERVER; DATABASE='+database+'; Trusted_Connection=yes')
    db = conn.cursor()
    
    return db

def search_name(first_name=None, last_name=None, zip_code=None):
    
    if zip_code:
        zip_code = zip_code.strip()[:5]
    
    databases = ['InkPixi', 'InkPixiArchives2011', 'AlumniOriginals', 'AlumniOriginalsArchives2003', 'AlumniOriginalsArchives2004', 'ESMRetail' ]
    
    sql_select = "SELECT customerID, db_name() as 'database',  firstName, middleName, lastName, company, address, address2, city, state, zip FROM dbo.customers WHERE "
    
    if first_name and last_name:
        sql_where = "firstName = ? AND lastName = ?"
        sql_params = (first_name, last_name)
    elif last_name and zip_code:
        sql_where = "lastName = ? AND LEFT(zip, 5) = ?"
        sql_params = (last_name, zip_code)
    elif first_name and last_name and zip_code:
        sql_where = "firstName = ? AND lastName = ? AND LEFT(zip, 5) = ?"
        sql_params = (first_name, last_name, zip_code)
    else:
        return None
    
    sql = sql_select + sql_where
    
    search_results = []
    for db in databases:
        cur = connect_db(db)
        with closing(cur) as curDB:
            curDB.execute(sql, sql_params)
            ds = curDB.fetchall()
            if ds:
                for row in range(len(ds)):
                    search_results.append(ds[row])
                
    return search_results

def remove_from_mailing_list(cust_id, in_db):
    cur = connect_db(in_db)
    with closing(cur) as db:
        db.execute("""UPDATE dbo.customers SET doNotMail = 1 WHERE customerID = ?""", (cust_id))
        db.commit()
        
def get_user_name():
    cur = connect_db('InkPixi')
    with closing(cur) as db:
        db.execute("SELECT SUSER_NAME() userName")
        ds = db.fetchone()
        user = ds[0]
        # get the user name only after domain name "ESM\\"
        user = user.split("\\")[1].title()
        #Grab last initial and capitalize it.
        lastI = user[-1:].upper()
        #Combine all but last letter of user name and last initial so it looks like login name "FirstL"
        user_nm = user[:-1] + lastI
        
    return user_nm    

def insert_note(cust_id, in_db, note):
    user = get_user_name()
    cur = connect_db(in_db)
    with closing(cur) as db:
        db.execute("""INSERT INTO 
                            dbo.notes 
                            (
                                [type], 
                                numericKey, 
                                itemNumber, 
                                entryDate, 
                                entryTime, 
                                notes, 
                                completed, 
                                enteredBy, 
                                parentType, 
                                parentKey
                            )
                        VALUES
                            (
                                'C',
                                ?,
                                0,
                                GETDATE(),
                                GETDATE(),
                                ?,
                                0,
                                ?,
                                'C',
                                ?
                            )""", (cust_id, note, user, cust_id))
        db.commit()
        
def get_cust_notes(cust_id, in_db):
    cur = connect_db(in_db)
    lstNotes = []
    with closing(cur) as db:
        db.execute("""SELECT 
                            CONVERT(VARCHAR(12), EntryDate, 101) + ' - '
                            + 'Cust Note - '
                            + CAST(Notes AS VARCHAR(300)) + ' \n'note
                        FROM 
                            dbo.notes 
                        WHERE 
                            numericKey = ?
                        AND
                            [Type] = 'C'
                        ORDER BY 
                            [Type], EntryDate""", (cust_id))
        ds = db.fetchall()
    
    for row in ds:
        lstNotes.append(row[0])

    return lstNotes    

def get_cust_ords(cust_id, in_db):
    cur = connect_db(in_db)
    lst_ords = []
    
    with closing(cur) as db:
        db.execute("""SELECT orderNumber FROM dbo.orders WHERE customerID = ?""", (cust_id))
        ds = db.fetchall()
        
    for row in ds:
        lst_ords.append(row[0])
    
    return lst_ords

def get_ord_notes(orders, in_db):
    cur = connect_db(in_db)
    lstNotes = []
    
    for ord in orders:
        with closing(cur) as db:
            db.execute("""SELECT 
                            CONVERT(VARCHAR(12), EntryDate, 101) + ' - '
                            + 'Ord Note - '
                            + CAST(Notes AS VARCHAR(300)) + ' \n'note
                        FROM 
                            dbo.notes 
                        WHERE 
                            numericKey = ?
                        AND
                            [Type] = 'O'
                        AND
                            notes LIKE '%address%'    
                        ORDER BY 
                            EntryDate""", (ord))
            ds = db.fetchall()
            
            for row in ds:
                lstNotes.append(row[0])
            
    return lstNotes
    
