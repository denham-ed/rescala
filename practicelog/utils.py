import base64
import io
import os
import urllib.parse
from typing import Any, List, Optional, Union
import matplotlib.pyplot as plt
import pandas as pd
from django.core.files.uploadedfile import UploadedFile
from PIL import Image
from wordcloud import STOPWORDS, WordCloud


stopwords = set(STOPWORDS)

# https://baronchibuike.medium.com/how-to-integrate-wordcloud-to-your-django-web-application-9bb76af0a28
def show_wordcloud(data: Optional[Union[List[str], str]]) -> Optional[Image.Image]:
    """Convert matplotlib data to image."""
    try:
        wordcloud = WordCloud(
            background_color="white",max_words=200,max_font_size=40,
            scale=3,random_state=0,stopwords=stopwords)
        wordcloud.generate(str(data))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        image = io.BytesIO()
        plt.savefig(image, format="png")
        image.seek(0)
        string = base64.b64encode(image.read())
        image_64 = "data:image/png;base64," +   urllib.parse.quote_plus(string)
        return image_64
    except ValueError:
        return None