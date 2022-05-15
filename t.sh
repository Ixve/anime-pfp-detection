#!/bin/bash
url="https://api.imgbb.com/1/upload?expiration=600&key=IMGBB_KEY_HERE"
temp_file="$XDG_DATA_HOME/animeface-ruby/temp_out.png"

imageurl=$(curl -X POST "$url" -F "image=@"$temp_file)
echo $imageurl > /tmp/upload.json
cat /tmp/upload.json | jq -r ".data" > ./data1.json
cat ./data1.json | jq -r ".url" > ./data.json

