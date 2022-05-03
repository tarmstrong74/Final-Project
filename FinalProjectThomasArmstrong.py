# Main selection area (with image)
# Videos
# Video categories (such as YouTube shorts and different series I have, all with the thumbnail images)
# All relevant videos in the category
# Images
# Categories (organized by what the work is based off of)
# All relevant images for the category
# Text/teasers
# Categories (such as YouTube shorts and different series I have)
# All relevant teasers for the category
# Feedback
# Feedback or idea
# Box for video title (feedback only)
# Anonymous user text entries
# Each category has a back button and “home” button

# I actually have a massive amount of files that will take up over 1 TB
# of storage after being unzipped, so I will be placing only 1 video file in each
# category. They will be redone in a lower quality format for storage purposes
# (original images and videos done in 4k and 60 fps with PNGs file format)

from tkinter import *
from PIL import ImageTk, Image
main = Tk()
main.title("SFM Hub")

# home page image
home_image = ImageTk.PhotoImage(Image.open("Final Project Images/Nightmare (with custom watermark).jpg"))
image_label = Label(image=home_image)
image_label.grid(row=1, column=0)

# Home page of widgets
description_label = Label(main, text="This is a collection of some of my work!")
description_label.grid(row=0, column=0)
video_button = Button(main, text="Show videos")
video_button.grid(row=2, column=0)
image_button = Button(main, text="Show images")
image_button.grid(row=3, column=0)
text_button = Button(main, text="Show text and teasers")
text_button.grid(row=4, column=0)
feedback_button = Button(main, text="Show feedback options")
feedback_button.grid(row=5, column=0)
quit_button = Button(main, text="Close Program", command=main.quit)
quit_button.grid(row=6, column=0)

main.mainloop()
