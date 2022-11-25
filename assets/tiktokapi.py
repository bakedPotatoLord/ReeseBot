import ffmpeg
import yt_dlp as youtube_dl
import os
import discord
import os

def video(name):
	ff = name.split("/")[-1].strip("-")
	if ff == "":
		ff = name.split("/")[-2].strip("-")
	if "tube" in name:
		os.system(f"yt-dlp -f \"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best\" -v -o {ff}video.mp4 " + name)
	else:
		print(ff)
		os.system(f"yt-dlp {name} -o {ff}video.mp4 ")
	os.system(f"mv {ff}video.mp4 compme{ff}.mp4")
	while not os.path.exists(f"finished{ff}.mp4"):
		pass
	print("done")
	file = discord.File(f"finished{ff}.mp4")
	return file, ff


def compress_video(video_full_path):
        if len(video_full_path.split("/")) == 1:
                output_file_name = video_full_path[6:]
        else:
                output_file_name = ("/".join(s.split("/")[:-1]) + s.split("/")[-1][6:])
        if os.path.exists(output_file_name):
                return
        target_size = 8000
        # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
        min_audio_bitrate = 32000
        max_audio_bitrate = 256000
        probe = ffmpeg.probe(video_full_path)
        # Video duration, in s.
        duration = float(probe['format']['duration'])
        # Audio bitrate, in bps.
        audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
        # Target total bitrate, in bps.
        target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)
        # Target audio bitrate, in bps
        if 10 * audio_bitrate > target_total_bitrate:
                audio_bitrate = target_total_bitrate / 10
                if audio_bitrate < min_audio_bitrate < target_total_bitrate:
                        audio_bitrate = min_audio_bitrate
                elif audio_bitrate > max_audio_bitrate:
                        audio_bitrate = max_audio_bitrate
        # Target video bitrate, in bps.
        video_bitrate = target_total_bitrate - audio_bitrate
        i = ffmpeg.input(video_full_path)
        ffmpeg.output(i, os.devnull,**{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}).overwrite_output().run()
        ffmpeg.output(i, output_file_name,**{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}).overwrite_output().run()
        os.system(f"mv {output_file_name} finished{output_file_name}")
        os.system(f"rm {video_full_path}")


def compress_forever():
	while True:
		for file in os.listdir():
			if file.split(".")[-1] == "mp4":
				if "compme" in file:
					print("compressing video")
					try:
						compress_video(file)
					except Exception as e:
						print(e)
						compressed_something = False



