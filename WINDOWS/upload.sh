auth="63c5bdfc-d10f-43da-a6db-e8b408f37f9d"
url="https://api.has-cool.pics/upload"

temp_file="./out.png"

image_url=$(curl -X POST -F "file=@"$temp_file -H "Authorization: Bearer "$auth -v "$url" 2>/dev/null)
echo $image_url > ./data.json

cat ./data.json | jq -r ".data.fileLink" > ./data1.json

#ill convert this to batch tommorow.
