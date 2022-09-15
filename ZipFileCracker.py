import zipfile

file_path = 'Zip File//test.zip'
pass_path = 'Passwords\passwords_zip.txt'

def extact_zip_file(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('Wrong Guess')
        return

def read_file():
    zip_file = zipfile.ZipFile(file_path)
    passwords = open(pass_path)
    for line in passwords.readlines():
        password = line.strip('\n')
        assume = extact_zip_file(zip_file, password)
        if assume:
            print(f'Password: {password}')
            break

if __name__ == "__main__":
    read_file()