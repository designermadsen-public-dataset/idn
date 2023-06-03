from os.path \
    import \
        realpath, \
        dirname, \
        isdir, \
        join

from package.dataset import \
    training_set, \
    validation_set

def script_location() -> str:
    return dirname(
        realpath(
        __file__
        )
    )

def dataset_path_exist() -> bool:
    return isdir(
        dataset_location()
    )

def dataset_location() -> str:
    return join(
        script_location(), 
        'dataset'
    )

def numbers_training_dataset():
    if dataset_path_exist():
        return training_set(
            dataset_location()
        )


def numbers_validation_dataset():
    if dataset_path_exist():
        return validation_set(
            dataset_location()
        )

