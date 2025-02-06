from cv2 import VideoCapture,imshow,imwrite,destroyWindow,waitKey,imread
# from cv2 
from datetime import datetime as dt


class Camera:

    def __init__(self,format:str="png"):
        self.camport = 0
        self.format = format
    

    def snap(self):
        cam = VideoCapture(self.camport)
        result,image = cam.read()
        
        datetime = dt.now()

        if result:
            x = f"./pictures/{datetime.day}{datetime.hour}{datetime.minute}{datetime.second}{datetime.microsecond}.{self.format}"

            imwrite(x,image)
            return x

            


if __name__ == "__main__":
    x = Camera()

    x.snap()