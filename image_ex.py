import cv2
from glob import glob

images = glob("*.jpg")

# Display and save the resized images
for image in images:
    img = cv2.imread(image,0)
    resized = cv2.resize(img,(100,100))
    cv2.imshow("Image",resized)
    cv2.waitKey(500)
    cv2.imwrite("resized_"+image,resized)
    cv2.destroyAllWindows()