import sys
import os
import requests

try:
    vid_url = sys.argv[1]
except IndexError:
    sys.exit("\n\tError: \'py yt_thumb.py\' must be followed by a Youtube URL argument")

std_yt_url = "https://www.youtube.com/watch?v="
short_yt_url = "https://www.youtu.be/"

if std_yt_url not in vid_url and short_yt_url not in vid_url:
    sys.exit("\n\tError: Invalid URL")

try:
    vid_id_begin_index = vid_url.find("watch?v=") + 8
    vid_id_end_index = vid_id_begin_index + 11
    vid_id = vid_url[vid_id_begin_index:vid_id_end_index]
except IndexError:
    sys.exit("\n\tError: Failed to parse Youtube video ID")

if len(vid_id) < 11:
    sys.exit("\n\tError: Failed to parse Youtube video ID")

yt_thumb_url = "https://i.ytimg.com/vi/" + vid_id + "/hqdefault.jpg"
print(yt_thumb_url)

default_thumbnail_dir = os.getcwd() + "\YT_Thumbnails"

if not os.path.exists(default_thumbnail_dir):
    os.makedirs(default_thumbnail_dir)

default_thumb_name = "Youtube_Thumbnail-" + vid_id + ".jpg"
default_save_path = default_thumbnail_dir + '\\' + default_thumb_name

if os.path.exists(default_save_path):
    sys.exit("\n\tError: \"" + default_thumb_name + "\" already exists in " + default_thumbnail_dir)

with open(default_save_path, "wb") as f:
    f.write(requests.get(yt_thumb_url).content)

sys.exit("\n\tSuccess: \"" + default_thumb_name + "\" saved to " + default_thumbnail_dir)