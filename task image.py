import cv2
import numpy as np
import matplotlib.pyplot as plt


# load image using cv2
path= "colors.jpg"
image = cv2.imread(path)

#show image
plt.figure(figsize=(10,10))
# convert the image from BGR to RGB format.
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()

#display histogram
color = ('blue', 'green', 'red')
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=col + " channel")

    plt.xlim([0, 256])
plt.legend()
plt.title("Histogram Channels")
plt.show()

# contract
alpha = 2
# for the brightness
beta = 100
edited_image = cv2.addWeighted(image, alpha, np.zeros_like(image), 0, beta)

# Display the edited image

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(edited_image,cv2.COLOR_BGR2RGB))
plt.show()

#display edited histogram
color = ('blue', 'green', 'red')
for i, col in enumerate(color):
    hist = cv2.calcHist([edited_image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=col + " channel")

    plt.xlim([0, 256])
plt.legend()
plt.title("Edited Histogram Channels")
plt.show()