from pytube import YouTube

# https://www.youtube.com/watch?v=ZbIzZD_YNsA&pp=ygUKMm1pbiB2aWRlbw%3D%3D
link = input("Enter Video Link Here==>>>")
yt = YouTube(link) 
print(f'Video Title==>>> {yt.title}')
print(f'Video Caption==>>> {yt.captions}')
print(f'Video Description==>>> {yt.description}')
# print(f'Video Stream==>>> {yt.streams}')
stream = yt.streams.filter(progressive=True)
video_index = list(enumerate(stream))

for i in video_index:
    print(i)

index = int(input("Enter Your Video's Index==>>>"))
stream[index].download()
print("====================SUCCESS===================")