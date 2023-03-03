import os
from qrcode import QRCode
#from django.conf import settings
from views import directory_path

class pdfClass:
    #def __init__(self, data):
    #    self.data= data

    def generateImage(self, data):
        qr = QRCode()
        qr.add_data(self.data)
        qr.make_image()
        return qr 

    def getLastImageSaved(self):
        dir_path_work = os.path.join(BASE_DIR, 'pdfs')
        if dir_path_work is None:
            os.mkdir(os.path.join(BASE_DIR, 'pdfs'))
        else:
            print(FileExistsError)
        


if __name__ == '__main__':
    p = pdfClass()
    p.getLastImageSaved()