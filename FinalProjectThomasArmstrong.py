# Main selection area (with image)
# Videos
# Video categories (such as YouTube shorts and different series I have, all with the thumbnail images)
# All relevant videos in the category
# Images
# Categories (organized by what the work is based off of)
# All relevant images for the category
# Each category has a back button and “home” button

# Import statements
from tkinter import *
from PIL import ImageTk, Image
main = Tk()
main.title("SFM Hub")

# Home page image
home_image = ImageTk.PhotoImage(Image.open("Final Project Images/Nightmare (with custom watermark).jpg"))
image_label = Label(image=home_image)
image_label.grid(row=1, column=0)


# Video window
def open1():
    vid_window = Toplevel()
    vid_window.title("Video Viewer")


# Image viewer window
def open2():
    img_window = Toplevel()
    img_window.title("Image Viewer")
    # Images
    img1 = ImageTk.PhotoImage(Image.open("Final Project Images/trainer003064 (720_720).jpg"))
    img2 = ImageTk.PhotoImage(Image.open("Final Project Images/Outro000000 (720_950).jpg"))
    img3 = ImageTk.PhotoImage(Image.open("Final Project Images/nightmares000000 (1280_720).jpg"))
    img4 = ImageTk.PhotoImage(Image.open("Final Project Images/OC fog000000 (1280_720).jpg"))
    img5 = ImageTk.PhotoImage(Image.open("Final Project Images/Split Story Intro Rain003359 (1280_720).jpg"))

    image_list = [img1, img2, img3, img4, img5]
    img_window.img_reference = image_list
    image_number = 0

    # define widgets
    img_label = Label(img_window, image=img1)
    img_label.grid(row=0, column=0, columnspan=3)

    forward_button = Button(img_window, text=">>", command=lambda: update_img(image_number + 1))
    forward_button.grid(row=1, column=2)
    back_button = Button(img_window, text="<<", command=lambda: update_img(image_number - 1))
    back_button.grid(row=1, column=0)
    exit_button = Button(img_window, text="Close Program", command=main.quit)
    exit_button.grid(row=1, column=1)

    def update_img(new_number):
        nonlocal image_number
        image_number = new_number % len(image_list)
        img_label.config(image=image_list[image_number])


# Home page of widgets
# Title at the top
description_label = Label(main, text="This is a collection of some of my work!")
description_label.grid(row=0, column=0)

# Video button and open window command
video_button = Button(main, text="Show videos", command=open1)
video_button.grid(row=2, column=0)

# Image viewer button and open window command
image_button = Button(main, text="Show images", command=open2)
image_button.grid(row=3, column=0)

# Close program button and command
quit_button = Button(main, text="Close Program", command=main.quit)
quit_button.grid(row=6, column=0)
# End of home page widgets

mainloop()
