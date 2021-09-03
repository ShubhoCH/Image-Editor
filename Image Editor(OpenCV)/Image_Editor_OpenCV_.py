import tkinter as tk
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
from tkinter import filedialog
import cv2
import numpy as np


# Command Methords:

def displayImage(displayImage):
    ImagetoDisplay = displayImage.resize((900, 600), Image.ANTIALIAS)
    ImagetoDisplay = ImageTk.PhotoImage(ImagetoDisplay)
    showWindow.config(image=ImagetoDisplay)
    showWindow.photo_ref = ImagetoDisplay
    showWindow.pack()


def importButton_callback():
    global originalImage
    filename = filedialog.askopenfilename()
    originalImage = Image.open(filename)
    displayImage(originalImage)
    brightnessSlider.set(1)
    contrastSlider.set(1)


def saveButton_callback():
    savefile = filedialog.asksaveasfile(defaultextension=".jpg")
    outputImage.save(savefile)


def closeButton_callback():
    window.destroy()


def brightness_callBack(brightness_pos):
    brightness_pos = float(brightness_pos)
    global outputImage
    enhancer = ImageEnhance.Brightness(originalImage)
    outputImage = enhancer.enhance(brightness_pos)
    displayImage(outputImage)


def contrast_callback(contrast_pos):
    contrast_pos = float(contrast_pos)
    global outputImage
    enhancer = ImageEnhance.Contrast(originalImage)
    outputImage = enhancer.enhance(contrast_pos)
    displayImage(outputImage)


def yellowButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 2] = 20
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    displayImage(outputImage)


def blueButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 2] = 100
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    displayImage(outputImage)


def pinkButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 1] = 100
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    displayImage(outputImage)


def orangeButton_callback():
    opencvImage = cv2.cvtColor(np.array(originalImage), cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 2] = 200
    global outputImage
    outputImage = Image.fromarray(cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB))
    displayImage(outputImage)


def noneButton_callback():
    pass


window = tk.Tk()

# Set To FullScreen Mode:
screen_width = window.winfo_screenwidth()  # Get Screen Width
screen_height = window.winfo_screenheight()  # Get Screen Height
window.geometry(f'{screen_width}x{screen_height}')  # Apply to Geometry

Frame1 = tk.Frame(window, height=20, width=200)
Frame1.pack(anchor=tk.N)

Frame2 = tk.Frame(window, height=20, width=screen_width)
Frame2.pack(anchor=tk.NW)

Frame3 = tk.Frame(window, height=20, width=screen_width)
Frame3.pack(anchor=tk.N)

# Import Button:
importButton = tk.Button(Frame1, text="Import", padx=10, pady=5, command=importButton_callback)
# Divides the whole column into row and window:
importButton.grid(row=0, column=0)

# Save Button:
saveButton = tk.Button(Frame1, text="Save", padx=10, pady=5, command=saveButton_callback)
# Divides the whole column into row and window:
saveButton.grid(row=0, column=1)

# Close Button:
closeButton = tk.Button(Frame1, text="Close", padx=10, pady=5, command=closeButton_callback)
# Divides the whole column into row and window:
closeButton.grid(row=0, column=2)

# BrightNess Slider:
brightnessSlider = tk.Scale(Frame2, label="Brightness", from_=0, to=2, orient=tk.HORIZONTAL,
                            length=screen_width, resolution=0.1, command=brightness_callBack)
brightnessSlider.pack(anchor=tk.N)

# Contrast Slider:
contrastSlider = tk.Scale(Frame2, label="Contrast", from_=0, to=2, orient=tk.HORIZONTAL,
                          length=screen_width, resolution=0.1, command=contrast_callback)
contrastSlider.pack(anchor=tk.N)

# Radio Buttons:

yellowButton = tk.Radiobutton(Frame3, text="Yellow", width=30, value=1, command=yellowButton_callback)
yellowButton.grid(row=0, column=0)

blueButton = tk.Radiobutton(Frame3, text="Blue", width=30, value=2, command=blueButton_callback)
blueButton.grid(row=0, column=1)

pinkButton = tk.Radiobutton(Frame3, text="Pink", width=30, value=3, command=pinkButton_callback)
pinkButton.grid(row=0, column=2)

orangeButton = tk.Radiobutton(Frame3, text="Orange", width=30, value=4, command=orangeButton_callback)
orangeButton.grid(row=0, column=3)

noneButton = tk.Radiobutton(Frame3, text="None", width=30, value=5, command=noneButton_callback)
noneButton.grid(row=0, column=4)
noneButton.select()

showWindow = tk.Label(window)

# Apply for it to Keep Running in a loop:
tk.mainloop()