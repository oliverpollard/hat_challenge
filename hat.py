import random
from google_images_download import google_images_download
from PIL import Image, ImageDraw, ImageFilter


def load_nouns():
	nouns_file = "nouns.txt"
	with open(nouns_file) as f:
		nouns = f.read().splitlines()
	nouns = [x for x in nouns if (x.startswith("h") or x.startswith("a") or x.startswith("t"))]

	return nouns

def random_nouns(nouns, number):
	random_noun_list = []

	picked = 0
	while picked < number:
		picked_noun = random.choice(nouns)
		if picked_noun not in random_noun_list:
			random_noun_list.append(picked_noun)
			picked = picked + 1

	return random_noun_list

def main():
	nouns = load_nouns()
	random_noun_list = random_nouns(nouns, number=60)

	response = google_images_download.googleimagesdownload()
	download_arguments = {"save_source":"source","format": "jpg", "limit": 1, "print_urls": True, "size": "medium"}
	for noun in random_noun_list:
		download_arguments["keywords"] = noun
		response.download(download_arguments)
		source_file = "downloads/source.txt"
	with open(source_file) as f:
		sources = f.read().splitlines()

	
	#990,660
	basewidth = 100
	
	hat_image = Image.open("hat_source.jpg")
	for source in sources:
		image_location = source.split()[0]
		image = Image.open(image_location)
		wpercent = (basewidth/float(image.size[0]))
		hsize = int((float(image.size[1])*float(wpercent)))
		image = image.resize((basewidth,hsize), Image.ANTIALIAS)
		back_im = hat_image.copy()
		x_pos = random.randint(300,700)
		y_pos = random.randint(100,500)
		back_im.paste(image, (x_pos, y_pos))
		back_im.save('hat.jpg', quality=95)
		hat_image = Image.open("hat.jpg")

	print(random_noun_list)

if __name__ == "__main__":
	main()