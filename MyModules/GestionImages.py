from io import BytesIO
import os
from time import sleep

from fastdownload import download_url
from duckduckgo_search import ddg_images
from fastcore.all import *
from fastai.vision.all import *


# Recherche un type d'image demander
def search_images(pattern, max_images=10):
    return L(ddg_images(pattern, max_results=max_images)).itemgot('image')

# telecharge les image recupere via la fonction du dessus
def download_urls(pattern_name, max_images, path_dest="assets"):
    search_images(f"{pattern_name} photos",max_images=max_images)
    max_images = search_images(f"{pattern_name} photos",max_images=max_images)
    img_paths = []
    for index,item in enumerate(max_images):
        img_path = f"{path_dest}/{pattern_name}/{pattern_name}{index}.jpg"
        img_paths.append(img_path)
        download_url(item, img_path, show_progress=False)
        if index == 10 or 20:
            sleep(10)


# recupere localement une liste d'image dans un dir donné
# il existe la fonction get_images_files present dans fastai.vision.all 
def get_local_paths_img(path):
    my_img_path = []
    try:
        dir = os.listdir(path)
    except FileNotFoundError:
        print(" Le directory n'existe pas! entrez un chemin existant")
    except NotADirectoryError:
        print("Il ne s'agit pas d'un directorie")
    for file in dir:
        my_img_path.append(f"{path}/{file}")
    return my_img_path

# affiche une image donné
def display_local_img(path):
    im = Image.open(path)
    im.to_thumb(256,256) 
    
# affiche une image donné url
def display_url_img(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img.to_thumb(256,256) 


# Nettoie les images 
def clean_imagies(pattern_tuple, parent_path):
    path = Path(parent_path)
    for o in pattern_tuple:
        dest = (path/o) 
        dest.mkdir(exist_ok=True, parents=True)
        resize_images(path/o, max_size=400, dest=path/o)
    failed = verify_images(get_image_files(path))
    failed.map(Path.unlink)
    len(failed)
