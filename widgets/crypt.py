import os
import pyAesCrypt
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "$put_a_strong@^#password_here$"

# encrypt
def Encrypt(enc_file):
    with open(enc_file, "rb") as fIn:

        with open(str(enc_file+".aes"), "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# decrypt
def Decrypt(dec_file):
    encFileSize = os.stat(dec_file).st_size
    with open(dec_file, "rb") as fIn:
        try:
            #"decr_"+
            with open(dec_file[:-4], "wb") as fOut:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError:
            # remove output file on error
            os.remove(dec_file[:-4])

# split files : smartly splits files in size of 50MB
def Splitter(spl_file):
    video = VideoFileClip(spl_file)
    vtime = video.duration
    vsize = os.stat(spl_file).st_size/(1024*1024) #size in MB

    time_per_clip = int(50*vtime/vsize)

    if vsize<=50:
        return 
    
    start = 0
    end = time_per_clip
    i=1
    while end<=vtime:
        ffmpeg_extract_subclip(spl_file, start, end, targetname=str(i)+"_"+spl_file)
        start+=time_per_clip
        end+=time_per_clip
        
        i+=1
    if end>vtime and start<vtime:
        ffmpeg_extract_subclip(spl_file, start, vtime,targetname=str(i)+"_"+spl_file)

def Concat(folder_path = os.getcwd()):

    clips = []
    fname=""
    exclude = ['.txt','.pdf','.json','.py']
    for root, directory, filenames in os.walk(folder_path):
        filenames.sort() #to keep video files in proper orders
        for filename in filenames:
            fname=filename
            f = os.path.join(root, filename)

            if os.path.splitext(f)[1] not in exclude:

                clips.append(VideoFileClip(f))

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(fname[2:]) # warning: this assumes no. of clips <10
