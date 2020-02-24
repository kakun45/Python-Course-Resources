"""
blacklist.py

This file just contains the list of the JWT_tokens that are imported by
app and the logout resource so that tokens can be added to the blacklist when the
user logs out.
"""

BLACKLIST = set()
