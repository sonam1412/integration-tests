#/bin/bash


#get all the related images here
relImgs=$(cat catalog.yaml | yq '.relatedImages[].image' | sed 's/---//')
echo "These are related images: $relimgs"
# cycle through those and show outputs
for i in ${relImgs// /}
do
	skopeo inspect --no-tags docker://$i
done
