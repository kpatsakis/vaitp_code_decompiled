# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 898_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 705 bytes


class VulnerableSpotipy:

    def __init__(self):
        self.base_url = "https://api.spotify.com/v1"

    def track(self, track_id):
        url = f"{self.base_url}/tracks/{track_id}"
        return self.make_request(url)

    def make_request(self, url):
        print(f"Making request to: {url}")


vulnerable_spotipy = VulnerableSpotipy()
vulnerable_spotipy.track("../../playlists")

# okay decompiling 898_1.pyc
