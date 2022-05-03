import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
    
def main():
    access_token = 'sl.BG0j8PfHcd6YsGpIxh6WPDxPZcv9QPVfK03EjhD2m5ed4IfU-FLlURY8U-zOojaGqrP4oR_LCHMokstFhnngxGpLbUh3Xp1fmADZbPR2Il0IYw8yuTTVjBFXr9EhWnGoSub5gfk'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer :-")
    file_to = input("enter the full path to upload the dropbox")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()