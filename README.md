![UI-DEISGN](https://github.com/parigulmehwish/YouTube-Video-Downloader/assets/153764375/59ca8a53-e117-4d14-8546-1bcf79ba142e)
 This is a Tkinter-based GUI application that allows you to download YouTube videos.

Import necessary libraries: Tkinter, pytube, and moviepy.
Create the main window and set its title, size, and resizability.
Define the download() function to download the YouTube video:
Get the video link from the input field.
Create a YouTube object using the link.
Set the window title to "Downloading".
Filter the video streams and select the first progressive stream with 720p resolution.
Download the video and store it in a variable.
Set the window title to "Successfully Downloaded".
Create a VideoFileClip object from the downloaded video and close it.
Configure the background color of the main window.
Add a YouTube icon to the main window.
Create a frame for the input field and download button.
Add a heading to the frame.
Add a label and input field for the video link.
Add a download button to the frame, which calls the download() function when clicked.
Start the main event loop.
To use this application, enter a YouTube video link in the input field and click the "Download" button. The video will be downloaded with 720p resolution.
