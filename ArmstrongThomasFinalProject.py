# Main selection area (with image)
# Videos
# Video categories (such as YouTube shorts and different series I have)
# 1 video per category for storage
# Image
# Images thrown in a list
# Each button has a back button and a close button
# Manual
# Integrated user manual (without pictures) for easy use
# Actual user manual includes only more professional lines

# Import statements
from tkinter import *
from PIL import ImageTk, Image
from tkvideo import tkvideo
main = Tk()
main.title("SFM Hub")

# Home page image
home_image = ImageTk.PhotoImage(Image.open("Final Project Images/Nightmare (with custom watermark).jpg"))
image_label = Label(image=home_image)
image_label.grid(row=3, column=0)


# Video window 1
def open1():
    vid_window = Toplevel()
    vid_window.title("Video Viewer")
    # Video
    video_label = Label(vid_window)
    video_label.grid(row=1, column=0, columnspan=3)
    vid = tkvideo("Final Project Images/short 2.mp4", video_label, loop=1, size=(1280, 720))
    vid.play()
    # Buttons and labels
    close_button = Button(vid_window, text="Close Window", command=vid_window.destroy, width=15)
    close_button.grid(row=2, column=1)
    quit_button = Button(vid_window, text="Close Program", command=vid_window.quit, width=15)
    quit_button.grid(row=2, column=2)
    info_label1 = Label(vid_window, text="Videos do not have sound with the tkvideo package, check the files for sound."
                                         "Videos in the files will appear darker due to compression.")
    info_label1.grid(row=0, column=0, columnspan=3)


# Video window 2
def open2():
    vid_window = Toplevel()
    vid_window.title("Video Viewer")
    # Video
    video_label = Label(vid_window)
    video_label.grid(row=1, column=0, columnspan=3)
    vid = tkvideo("Final Project Images/showcase.mp4", video_label, loop=1, size=(1280, 720))
    vid.play()
    # Buttons and labels
    close_button = Button(vid_window, text="Close Window", command=vid_window.destroy, width=15)
    close_button.grid(row=2, column=1)
    quit_button = Button(vid_window, text="Close Program", command=vid_window.quit, width=15)
    quit_button.grid(row=2, column=2)
    info_label1 = Label(vid_window, text="Videos do not have sound with the tkvideo package, check the files for sound."
                                         "Videos in the files will appear darker due to compression.")
    info_label1.grid(row=0, column=0, columnspan=3)


# Video window 3
def open3():
    vid_window = Toplevel()
    vid_window.title("Video Viewer")
    # Video
    video_label = Label(vid_window)
    video_label.grid(row=1, column=0, columnspan=3)
    vid = tkvideo("Final Project Images/Donut Gif MP4.mp4", video_label, loop=1, size=(1280, 720))
    vid.play()
    # Buttons and labels
    close_button = Button(vid_window, text="Close Window", command=vid_window.destroy, width=15)
    close_button.grid(row=2, column=1)
    quit_button = Button(vid_window, text="Close Program", command=vid_window.quit, width=15)
    quit_button.grid(row=2, column=2)
    info_label1 = Label(vid_window, text="Video does not have any sound.")
    info_label1.grid(row=0, column=0, columnspan=3)


# Image viewer window
def open4():
    img_window = Toplevel()
    img_window.title("Image Viewer")
    # Images
    img1 = ImageTk.PhotoImage(Image.open("Final Project Images/trainer003064 (720_720).jpg"))
    img2 = ImageTk.PhotoImage(Image.open("Final Project Images/Outro000000 (720_950).jpg"))
    img3 = ImageTk.PhotoImage(Image.open("Final Project Images/nightmares000000 (1280_720).jpg"))
    img4 = ImageTk.PhotoImage(Image.open("Final Project Images/OC fog000000 (1280_720).jpg"))
    img5 = ImageTk.PhotoImage(Image.open("Final Project Images/Split Story Intro Rain003359 (1280_720).jpg"))
    img6 = ImageTk.PhotoImage(Image.open("Final Project Images/Split Story Intro001071 (1280_720).jpg"))
    img7 = ImageTk.PhotoImage(Image.open("Final Project Images/Split Story Intro003059 (1280_720).jpg "))

    # Making a list of images
    image_list = [img1, img2, img3, img4, img5, img6, img7]
    img_window.img_reference = image_list
    image_number = 0

    # widgets
    img_label = Label(img_window, image=img1)
    img_label.grid(row=1, column=0, columnspan=3)
    notice_label = Label(img_window, text="Images displayed in 720p or something near (for images that aren't 16:9) "
                                          "for the sake of storage space.")
    notice_label.grid(row=0, column=0, columnspan=3)
    forward_button = Button(img_window, text=">>", command=lambda: update_img(image_number + 1), width=15)
    forward_button.grid(row=3, column=2)
    back_button = Button(img_window, text="<<", command=lambda: update_img(image_number - 1), width=15)
    back_button.grid(row=3, column=0)
    exit_button = Button(img_window, text="Close Program", command=main.quit, width=15)
    exit_button.grid(row=2, column=2)
    close_button = Button(img_window, text="Close Window", command=img_window.destroy, width=15)
    close_button.grid(row=2, column=1)

    def update_img(new_number):
        nonlocal image_number
        image_number = new_number % len(image_list)
        img_label.config(image=image_list[image_number])


# User manual
def open_help():
    manual = Toplevel()
    manual.title("User Manual")
    # Text
    line_1 = Label(manual, text="Hello user,")
    line_1.grid(row=0, column=0)
    line_2 = Label(manual, text="I see you may be in need of some help.  Allow this to teach you"
                                "the basics of this app!")
    line_2.grid(row=2, column=0)
    line_3 = Label(manual, text="When you first start this app, you will be greeted with the home screen.  "
                                "This is where you will find all the buttons you can interact with as "
                                "well as an image and some fun text at the top.")
    line_3.grid(row=4, column=0)
    line_4 = Label(manual, text="However, I assume you already know a lot of this since you are here and that "
                                "required you to click on a button.")
    line_4.grid(row=5, column=0)
    line_5 = Label(manual, text="The text at the top is only for fun and serves no programmed purpose, "
                                "you cannot click on it or copy/paste it.")
    line_5.grid(row=7, column=0)
    line_6 = Label(manual, text="Underneath the text, you will find an image which also has no "
                                "programmed purpose, there is no clicking or copying.")
    line_6.grid(row=8, column=0)
    line_7 = Label(manual, text="Now onto the actual buttons:")
    line_7.grid(row=10, column=0)
    line_8 = Label(manual, text="Underneath the image is where all the buttons lie.  "
                                "These buttons all have their own purpose.  "
                                "The ones labeled with “Videos” will each open a window with a specific video file.")
    line_8.grid(row=12, column=0)
    line_9 = Label(manual, text="Since I can't actually fit the images in here, feel free to play"
                                "around with those video buttons!")
    line_9.grid(row=13, column=0)
    line_10 = Label(manual, text="Each video button will have a video played on a loop as well as text at the top "
                                 "to describe if the video has sound and if so, how to find it.")
    line_10.grid(row=15, column=0)
    line_11 = Label(manual, text="Now onto the show image button:")
    line_11.grid(row=17, column=0)
    line_12 = Label(manual, text="The button labeled “Show Images” will open a window with an image viewer.")
    line_12.grid(row=19, column=0)
    line_13 = Label(manual, text="Within the image viewer, you will find:")
    line_13.grid(row=20, column=0)
    line_14 = Label(manual, text="1) A back button on the left")
    line_14.grid(row=21, column=0)
    line_15 = Label(manual, text="2) A forward button on the right")
    line_15.grid(row=22, column=0)
    line_16 = Label(manual, text="3) A close program button")
    line_16.grid(row=23, column=0)
    line_17 = Label(manual, text="3) A close window button")
    line_17.grid(row=24, column=0)
    line_18 = Label(manual, text="All of these buttons are fairly self explanatory:")
    line_18.grid(row=26, column=0)
    line_19 = Label(manual, text="The back button will take you back one image")
    line_19.grid(row=27, column=0)
    line_20 = Label(manual, text="The forward button will take you forward one image")
    line_20.grid(row=28, column=0)
    line_21 = Label(manual, text="The close program button will exit the entire app")
    line_21.grid(row=29, column=0)
    line_22 = Label(manual, text="The close window button will close only the image viewer window")
    line_22.grid(row=30, column=0)
    line_23 = Label(manual, text="I think that is all for the manual, enjoy the app!")
    line_23.grid(row=34, column=0)
    line_24 = Label(manual, text="And for the final button, there is the help button, "
                                 "but I won’t say anything here since you have already clicked on this one.")
    line_24.grid(row=32, column=0)

    # Line spaces (I don't know, it just looked better, but it ruined my time)
    space_1 = Label(manual, text=" ")
    space_1.grid(row=1, column=0)
    space_2 = Label(manual, text=" ")
    space_2.grid(row=3, column=0)
    space_3 = Label(manual, text=" ")
    space_3.grid(row=6, column=0)
    space_4 = Label(manual, text=" ")
    space_4.grid(row=9, column=0)
    space_5 = Label(manual, text=" ")
    space_5.grid(row=11, column=0)
    space_6 = Label(manual, text=" ")
    space_6.grid(row=14, column=0)
    space_7 = Label(manual, text=" ")
    space_7.grid(row=16, column=0)
    space_8 = Label(manual, text=" ")
    space_8.grid(row=18, column=0)
    space_9 = Label(manual, text=" ")
    space_9.grid(row=25, column=0)
    space_10 = Label(manual, text=" ")
    space_10.grid(row=31, column=0,)
    space_11 = Label(manual, text=" ")
    space_11.grid(row=33, column=0)
    space_12 = Label(manual, text=" ")
    space_12.grid(row=35, column=0)
    # I sadly realized after doing this that I could have imported a document, but this is already done, so I won't

    # Buttons
    exit_button = Button(manual, text="Close Program (seems too complicated)", command=main.quit)
    exit_button.grid(row=37, column=0)
    close_button = Button(manual, text="Close Window", command=manual.destroy, width=15)
    close_button.grid(row=36, column=0)


# Home page of widgets
# Title at the top
description_label = Label(main, text="This is a collection of some of my work!")
description_label.grid(row=0, column=0)
home_text_label = Label(main, text="All images are my own work and the watermark is also mine.")
home_text_label.grid(row=1, column=0)
info_label = Label(main, text="Videos do not have sound with the tkvideo package, check the files for sound.")
info_label.grid(row=2, column=0)

# Video button and open window command
video_button = Button(main, text="Videos: Shorts", command=open1, width=15)
video_button.grid(row=4, column=0)
video_button2 = Button(main, text="Videos: Showcase", command=open2, width=15)
video_button2.grid(row=5, column=0)
video_button3 = Button(main, text="Videos: GIF", command=open3, width=15)
video_button3.grid(row=6, column=0)

# Image viewer button and open window command
image_button = Button(main, text="Show images", command=open4, width=15)
image_button.grid(row=7, column=0)

# Manual
help_button = Button(main, text="HELP", command=open_help, width=15)
help_button.grid(row=8, column=0)

# Close program button and command
quit_button_home = Button(main, text="Close Program", command=main.quit, width=15)
quit_button_home.grid(row=9, column=0)
# End of home page widgets

mainloop()
