import cv2

def display_img(filepath, filename):
    cv2.namedWindow(filename, cv2.WINDOW_NORMAL)
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    cv2.imshow(filename, img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord("s"):
        cv2.imwrite(filename, img)
        cv2.destroyAllWindows()


display_img("F:\Wallpaper\watch-dogs-2-3000x2008-2016-pc-ps4-xbox-875.jpg", "watchdogs2.jpg")