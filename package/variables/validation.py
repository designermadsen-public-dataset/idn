batch_size = 32

crop_aspect_ratio = False
follow_links = False
shuffle = True

seed = 232323

split_at = 0.25

width = 256
height = 256


def get_batch_size() -> int:
    global batch_size
    return batch_size


def get_crop_aspect_ratio() -> bool:
    global crop_aspect_ratio
    return crop_aspect_ratio


def get_follow_links() -> bool:
    global follow_links
    return follow_links


def get_seed() -> int:
    global seed
    return seed


def get_height() -> int:
    global height
    return height


def get_width() -> int:
    global width
    return width


def get_split_at() -> float:
    global split_at
    return split_at


def set_split_at(value: float) -> None:
    global split_at
    split_at = value


def set_batch_size(value: int) -> None:
    global batch_size
    batch_size = value


def set_crop_aspect_ratio(value: bool) -> None:
    global crop_aspect_ratio
    crop_aspect_ratio = value


def set_follow_links(value: bool) -> None:
    global follow_links
    follow_links = value


def set_seed(value: int) -> None:
    global seed
    seed = value


def set_height(value: int) -> None:
    global height
    height = value


def set_width(value: int) -> None:
    global width
    width = value
