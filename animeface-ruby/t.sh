#!/bin/bash
url="https://api.imgbb.com/1/upload?expiration=600&key=e81290c4b32a22b16aa1d0d6b8b7e582"
temp_file="/home/synth/animeface-2009/animeface-ruby/temp_out.png"
content_type="image/png"

imageurl=$(curl -X POST "$url" -F "image=@"$temp_file)
echo $imageurl > /tmp/upload.json
cat /tmp/upload.json | jq -r ".data" > ./data1.json
cat ./data1.json | jq -r ".url" > ./data.json

