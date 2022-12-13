
from fastai.vision.all import *

# creer le programme d'entrainement
def training_programme(path):
    dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method='squish')]
    ).dataloaders(path, bs=10)
    return dls

def training(dls: DataBlock):
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(3)
    return learn


def prediction(learn, type_guesting, img):
    is_guesting,_,probs = learn.predict(PILImage.create(img))
    print(f"This is a: {is_guesting}.")
    print(f"Probability it's a {type_guesting}: {probs[0]:.4f}")


path = 'assets'
dls = training_programme(path=path)
learn = training(dls=dls)

prediction(learn,"bird","exam/bird_exam.jpg")