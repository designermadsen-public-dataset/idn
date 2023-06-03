from package.variables.training import get_batch_size
from package.variables.validation import get_batch_size

from keras.preprocessing import image_dataset_from_directory

training_object = None
validation_object = None


def training_set( path_to_dataset: str ):
    global training_object

    if not(training_object is None):
        return training_object
    
    dataset = image_dataset_from_directory(
        path_to_dataset, 
        color_mode='rgb',
        batch_size=32,
        image_size=(256, 256),
        validation_split=0.25,
        shuffle=True,
        seed=23232,
        subset='training',
        follow_links=True,
        crop_to_aspect_ratio=True
    )
    training_object = dataset
    
    return dataset
    


def validation_set( path_to_dataset: str ):
    global validation_object

    if not(validation_object is None):
        return validation_object
    
    dataset = image_dataset_from_directory(
        path_to_dataset, 
        color_mode='rgb',
        batch_size=32,
        image_size=(256, 256),
        validation_split=0.25,
        shuffle=True,
        seed=23232,
        subset='validation',
        follow_links=True,
        crop_to_aspect_ratio=True
    )
    validation_object = dataset

    return dataset
    
    

