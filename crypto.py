from cryptography.fernet import Fernet
import hashlib
import mysql.connector
import os

if not os.path.exists("master.key"):
    with open("master.key", "wb") as f:
        f.write(Fernet.generate_key())
else:
    print("Done")
        
with open("master.key", "rb") as f:
    KEY =  f.read()
    
cipher = Fernet(KEY)

        
conn  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "secure_contacts"   
)

cursor = conn.cursor()

class Auth():
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, username, password):
        hash_pass = self.hash_password(password)
        cursor.execute("insert into users (username, password) values (%s,%s)", (username, hash_pass))
        conn.commit()
        print("Registration Successful")
    
    def login(self, username, password):
        hash_pass = self.hash_password(password)
        
        try:
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                           (username, hash_pass))
            return cursor.fetchone()
        
        except:
            print("No user found")
            return
        
class manager():
    def __init__(self, owner):
        self.owner =  owner
        
    def encrypt_contact(self, phone):
        return cipher.encrypt(phone.encode())
    
    def decrypt_phone(self, phone):
        return cipher.decrypt(phone).decode()
    
    def addContact(self, name, phone):
        encrypted_contact = self.encrypt_contact(phone)
        cursor.execute("INSERT INTO contacts(owner, name, phone) VALUES (%s,%s,%s)", (self.owner, name, encrypted_contact))
        conn.commit() 
        
        print("-------------------------")
        
    def showcontact(self):
        cursor.execute("SELECT * FROM contacts WHERE owner=%s", (self.owner, ))
        records = cursor.fetchall()
        
        if not records:
            print("No records found")
            return    
        
        for record in records:
            decrypted_contact = self.decrypt_phone(record[3])
            print(f"{record[2]} | {decrypted_contact}") 
            
        print("-------------------------")
        
    def updateContact(self, id):
        try:
            cursor.execute("SELECT * FROM contacts WHERE id=%s", (id,))
            choice = input("Enter the choice: ") 
            if choice == 1:
                name = input("Enter the new name: ")
                cursor.execute("UPDATE contacts SET name = %s WHERE id = %s", (name, id))
            else:
                phone = input("Enter the new name: ")
                encrypted_contact = self.encrypt_contact(phone)
                cursor.execute("UPDATE contacts SET phone = %s WHERE id = %s", (encrypted_contact, id))
                conn.commit()
                
            print("-------------------------")
            
        except:
            print("No contact with this found") 
            print("-------------------------")
            return
        
    def deleteContact(self, name):
        try:
            cursor.execute("DELETE FROM contacts WHERE owner=%s, name=%s", (self.owner, name))
            conn.commit()
            print("-------------------------")
            
        except:
            print("No contact with this found")
            print("-------------------------")
            print("No name") 
                    
        
print("Choose from below option")
print("1 for register")
print("2 for  login")
print("-----------------------------------")

choice = input("Enter your choice: ")

auth = Auth() 

if choice == "1":
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    auth.register(username, password) 
    
elif choice == "2":
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    if auth.login(username, password):
        print("Choose from below option")
        print("1 to add contacts")
        print("2 to show contacts")
        print("3 to update")
        print("4 to delete")
        print("5 to Exist")
        print("-----------------------------") 
        
        while (True):
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("Enter your name: ")
                phone = input("Enter your phone: ")
                manager.addContact(name, phone)
                
            elif choice == "2":
                manager.showcontact()
                
            elif choice == "3":
                id = int(input("Enter your id: "))
                manager.updateContact()
                
            elif choice == "4":
                name = input("Enter the name: ")
                manager.deleteContact(name)
                
            elif choice == "5":
                print("Code Exited")
                break
            
            else:
                print("Invalid choice \nTry Again")
                print("-----------------------------")
    
    else:
        print("Invalid Login")
        
else:
    print("Invalid Choice") 
        






