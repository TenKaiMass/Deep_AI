import os
import xml.etree.ElementTree as ET

# fonction de calcul merci internet !
def convert_box(size, box):
    dw, dh = 1. / size[0], 1. / size[1]
    x, y, w, h = (box[0] + box[1]) / 2.0 - 1, (box[2] + box[3]) / 2.0 - 1, box[1] - box[0], box[3] - box[2]
    return x * dw, y * dh, w * dw, h * dh

def convert_for_yolo(path,list_of_xml,labels):
    for image in list_of_xml:
        get_image_informations(path,image,labels)
       

def xml_to_txt(path,image):
    # Verifie qu'on prend bien les fichier xml (clean anomalie)
    if image.split('.')[1] == 'xml':
        # recupère le nom des images
        image_name = image.split('.')[0]
        # Ajoute les version txt vide
        return open(f'{path}{image_name}.txt', 'w')
        

def get_image_informations(path,image,labels):
    # conversion xml to txt
    file_gestor = xml_to_txt(path,image)
    
    # On configure le curseur pour se balader dans le fichier et recuperer les information
    start = ET.parse(os.path.join('data','labels', image))
    curseur = start.getroot()       
    width = int(curseur.find('size') .find('width').text)
    height = int(curseur.find('size') .find('height').text)
    for objet in curseur.iter('object'):
        label = objet.find('name').text
        if label in labels and objet.find('difficult').text != '1':
            bndbox = objet.find('bndbox')
            # Nous faisons des calculs sur la taille de l'item grace au position
            bb = convert_box((width, height), [float(bndbox.find(x).text) for x in ('xmin', 'xmax', 'ymin', 'ymax')])
            label_id = labels.index(label)  # class id
            # ajout des infos dans un txt au meme nom
            file_gestor.write(" ".join([str(a) for a in (label_id, *bb)]) + '\n')


