from youtube_search import YoutubeSearch
from pytube import YouTube
from moviepy.editor import *
from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_audioclips
import os
import sys

dest = "D:\predictiveAnalysis\Mashup\VidFiles"

def mainScript(singer,num,duration,final):
	downloadVideo(singer,num)
	trimToAudio(duration)
	final = 'MashUp.mp3'
	return final

def downloadVideo(singer,n):
	search = singer + 'songs'
	output = YoutubeSearch(search,max_results = n).to_dict()
	print('Downloading !!!')
	for i in output:
		ytVideo = YouTube('https://www.youtube.com' + i['url_suffix'])
		vid = ytVideo.streams.filter(file_extension = 'mp4').first()
		vid.download(output_path=dest)
	print('Download Complete!!')

def trimToAudio(i):
	print('Trimming the Videos!!')
	clips = []
	for file in os.listdir(dest):
			filePath = os.path.join(dest,file)
			subClip = VideoFileClip(filePath).subclip(0,i)
			Audio = subClip.audio
			clips.append(Audio)
	trimmed = concatenate_audioclips(clips)
	trimmed.write_audiofile('MashUp.mp3')
	print('Trimming Done!!')


def error_Handling(singer,  no_of_videos, duration, final):
    if not singer.strip() :
        sys.exit('Enter Name of singer\n')
    
    elif int(no_of_videos)==0:
            sys.exit('Enter Number of Videos') 
    elif int(duration)==0:
            sys.exit('Enter correct Duration')
    elif final.endswith('.mp3') == False :
            sys.exit("Only .mp3  as output \n")
    return singer, no_of_videos, duration

def main():
    n = len(sys.argv)
    if(n!=5):
        print("Incorrect number of arguments\n")
        return

    singer= sys.argv[1]
    no_of_videos= int(sys.argv[2])
    duration= int(sys.argv[3])
    final= sys.argv[4]
    singer, no_of_videos, duration= error_Handling(singer,  no_of_videos, duration, final)

    mainScript(singer, no_of_videos, duration, final)
    print('MashUp is ready!!')

if __name__ == "__main__":
    main()


