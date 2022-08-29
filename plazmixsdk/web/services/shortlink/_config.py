import os


class ShortLinkConfig:
    ENDPOINT = os.getenv('PX_SHORT_LINK_ENDPOINT') or 'https://plzm.xyz/api/'
    API_TOKEN = os.getenv('PX_SHORT_LINK_API_TOKEN') or 'token'
