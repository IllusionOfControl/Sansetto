accepted_mimetypes = [
    "image/jpeg",
    "image/png",
]


def check_accepted_mimetype(mimetype: str) -> bool:
    return mimetype in accepted_mimetypes
