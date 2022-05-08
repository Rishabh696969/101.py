import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
            
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
            
def main():
    access_token = "https://drive.google.com/drive/my-drive"
    transferData = TransferData(access_token)
    
    file_from = input("C:\Users\aggri\OneDrive\Desktop\class 100")
    file_to = input("https://drive.google.com/drive/my-drive") 
    
    transferData.upload_file(file_from,file_to)
    print("file has been moved")
    
main()               