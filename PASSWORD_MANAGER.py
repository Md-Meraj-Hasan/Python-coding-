import json
def loadPassword():
    try:
        with open('passwords.json') as file:
            passwords=json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        passwords={} 
    return passwords or {}
def savePasswords(passwords):
    with open('passwords.json' ,'w') as file:
        json.dump(passwords,file)
def addPassword(account, password, passwords):        
        passwords[account] = password 
        savePasswords(passwords)
def showPassword(account, passwords):
    return passwords.get(account, 'account not found')
if __name__=="__main__":
    passwords=loadPassword() 
    while True:
        print("\nPassword Manager Menu")
        print('1. Add password')
        print('2. Retrieve password')
        print('3. Exit')
        user=input('please select menu: ')
        if user=='1':
            account =input('enter your account: ')
            password =input('enter your password: ')
            addPassword(account, password, passwords)
            print("successful added your password")
        elif user=='2':
            account =input('enter old account: ')  
            your_password=showPassword(account, passwords)
            print('your password: ',your_password)
        elif user=='3':
            print('you are exited password manager')
            break
        else:
            print('you enter invalid option: \npls re_enter option')     
               
    