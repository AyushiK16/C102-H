import dropbox

class BackupFiles:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def uploadFile(self, source, dest):
        dbx = dropbox.Dropbox(self.access_token)

        with open(source, 'rb') as f:
            dbx.files_upload(f.read(), dest)
    

def main():
    access_token = 'sl.AyGQhTMb-gi1VtfUlwAQsI5FxIVI8j1QjoyHSEmMaizez44KUZFaseY6Y9gX25w8jXotv5hgxBuEChz-e7bcX71YqFHchsmii3BH3vvKG_3Afc1nCEo0ewIUCLu1CxTzfIJBKFpbWt0'

    backup = BackupFiles(access_token)

    source = input('Enter the file that needs to be uploaded: ')
    dest = input('Enter the path to the destination:  ')

    backup.uploadFile(source,dest)
    print('The file has been uploaded.')

main()

