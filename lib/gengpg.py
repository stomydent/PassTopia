from enum import Enum

class KeyType(Enum):
    GPG_KEYTYPE_RSADSA = 0
    GPG_KEYTYPE_DSAELG = 1
    GPG_KEYTYPE_DSA    = 2
    GPG_KEYTYPE_RSA    = 3

class KeySize(Enum):
    GPG_1024 = 0
    GPG_2048 = 1
    GPG_3072 = 2
    GPG_4096 = 3

class KeyExpires(Enum):
    GPG_NEVER = 0
    GPG_CUSTOM = 1
