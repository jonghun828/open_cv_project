import cv2

def main():
    print("hello opencv")
    print(cv2.__version__)
    imgfile = '/home/kjonghun0828/open_cv_project/data/lenna.bmp'
    img = cv2.imread(imgfile)
    cv2.imshow("lenna img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()