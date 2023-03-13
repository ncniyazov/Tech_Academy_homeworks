import os

# Open the .m3u file containing the list of channels
with open("Tural_playlist.m3u8", "r", encoding="utf-8") as f:
    data = f.readlines()

# Create folders for SD and HD channels if they don't already exist
if not os.path.exists("SD"):
    os.makedirs("SD")
if not os.path.exists("HD"):
    os.makedirs("HD")

# Loop through each line in the file
for line in data:
    # If the line starts with #EXTINF, it contains channel information
    if line.startswith("#EXTINF"):
        # Add the channel link to the appropriate file
        if "HD" not in line:
            with open("SD/SD.m3u", "a", encoding="utf-8") as f:
                f.write(line)
        elif "HD" in line:
            with open("HD/HD.m3u", "a", encoding="utf-8") as f:
                f.write(line)
    else:
        # Add the channel link to the appropriate file
        if "SD" in line:
            with open("SD/SD.m3u", "a", encoding="utf-8") as f:
                f.write(line)
        elif "HD" in line:
            with open("HD/HD.m3u", "a", encoding="utf-8") as f:
                f.write(line)
