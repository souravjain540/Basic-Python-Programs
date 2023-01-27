import pytube

url = input("Enter Video url: ")

# Take Path Manually By User.
path = input("Enter path of storage: ")

# Specify the storage path of video.
# path = "D:"

pytube.YouTube(url).streams.get_highest_resolution().download(path)
