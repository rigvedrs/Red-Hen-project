import pandas as pd
import requests
import os
from PIL import Image
import argparse
from tqdm import tqdm


# Parsing arguments
parser = argparse.ArgumentParser()

parser.add_argument('--csv_loc', type=str, default='B1_final_data.csv', help='File path to the content image')
parser.add_argument('--num', type=int, default=5, help='Number of images to download, 0 for all, and any other number for otherwise')
parser.add_argument('--output_dir', type=str, default='Style_images/', help='File path to output directory')

args = parser.parse_args()

# Read the file 
file_path = args.csv_loc
df = pd.read_csv(file_path)
assert args.num < len(df), f"Number entered is more than length of df ({len(df)})"


# Download the images
os.makedirs(args.output_dir, exist_ok=True)

# Download and save the selected images
if args.num == 0:
	for c, row in tqdm(df.iterrows(),total=len(df)):
		image_link = row['IMAGE_LINK']
		title = row['TITLE']
		technique = row['TECHNIQUE']
		file_name = f"Style_images/{title}_{technique}.jpg"  

		response = requests.get(image_link)

		# Saving Image
		with open(file_name, 'wb') as file:
			file.write(response.content)
			print(f"Image saved: {file_name}")

else:
	for c, row in tqdm(df.iterrows(),total=args.num):
		if c == args.num:
			break
		image_link = row['IMAGE_LINK']
		title = row['TITLE']
		technique = row['TECHNIQUE']
		file_name = f"Style_images/{title}_{technique}.jpg"  

		response = requests.get(image_link)

		# Saving Image
		with open(file_name, 'wb') as file:
			file.write(response.content)
			print(f"Image saved: {file_name}")

