from django.db import models


class Blogger:
    def __init__(self, name, category, description, social_links):
        self.name = name
        self.category = category
        self.description = description
        self.social_links = social_links


bloggers = [
    Blogger("John Doe", "Tech", "Tech enthusiast and blogger",
            {"Twitter": "https://twitter.com/johndoe"}),
    Blogger("Jane Smith", "Lifestyle", "Lifestyle blogger", {
            "Instagram": "https://instagram.com/janesmith"}),
]
