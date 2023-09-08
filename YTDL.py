try:
    from pytube import YouTube
except:
    print("Installing pytube...")
    import os
    os.system("pip install pytube")
    print("Ready for use.")
    
try:
    from json import loads
except:
    print("Installing json lib...")
    import os
    os.system("pip install json")
    print("Ready for use.")

url = input("Paste the URL of the video to download: ")

try:
    v = YouTube(url)
except:
    print("An error occurred loading the video.")
    quit()
    
print("Fetching video details...")
try:
    video_streams = v.streams
except pytube.exceptions.AgeRestrictedError:
    print("The video you have requested is age-restricted.")
    quit()
    
data = []

for i in video_streams:
    i = str(i)
    i = i.split("<Stream: ")
    n = i[1]
    n = "{" + n + "}"
    n = n.replace(">", "")
    n = n.replace(" ", ",")
    n = n.replace("=", ":")
    n = n.replace("'", '"')
    
    n = n.replace("itag", '"itag"')
    n = n.replace("mime_type", '"mime"')
    n = n.replace("progressive", '"isProg"')
    n = n.replace("res", '"resolution"')
    n = n.replace("fps:", '"FPS":')
    n = n.replace("vcodec", '"vcodec"')
    n = n.replace("acodec", '"acodec"')
    n = n.replace("type", '"type"')
    n = n.replace("abr", '"abr"')
    
    data.append(loads(n))
    
print('')
for i in range(len(data)):
    try:
        print("ID " + str(data[i]["itag"]) + " | Type: " + data[i]["mime"] + ", Resolution: " + data[i]["resolution"] + ", FPS: " + data[i]["FPS"])
    except:
        print("ID " + str(data[i]['itag']) + " | Type: " + data[i]["mime"] + ", Bitrate: " + data[i]["abr"])
    
fname = input("\nEnter a name for the download: ")
while True:
    try:
        response = input("Enter the ID of your desired video/audio: ")

        print("Searching for the ID...")
        video_streams = v.streams.get_by_itag(int(response))
        print("ID found!")
        break
    except:
        print("ID not found. Try another.")

print("Downloading your file, please wait...")
try:
    open(str("/home/tyler/Downloads/YTDL/" + fname), "w+")
    video_streams.download(filename = fname)
    print("Video downloaded successfully.")
    quit()
except Exception:
    print("Video download failed. Please try again.")