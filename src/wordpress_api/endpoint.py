from enum import Enum


class Endpoint(Enum):
    POSTS = "/wp/v2/posts"
    PAGES = "/wp/v2/pages"
    MEDIA = "/wp/v2/media"
    LOGIN = "/wp-json/api/v1/token"
