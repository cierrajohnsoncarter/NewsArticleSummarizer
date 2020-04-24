# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import nltk
import nltk.data
from newspaper import Article
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()


# %%
# Get the article
url = 'https://www.washingtonpost.com/technology/2020/04/09/screen-time-rethink-coronavirus/'

article = Article(url)


# %%
# Do some nlp
article.download()
article.parse()
nltk.download('punkt')
article.nlp()


# %%
# Get the article name
title = article.title


# %%
# Get the authors of the article
author1 = article.authors[0]
author2 = article.authors[2]


# %%
# Get the publish data
article.publish_date


# %%
# Get the top image
image = article.top_image


# %%
# Get the article text
print(article.text)


# %%
# Get a summary of the article
print(f'{title.upper()}\n\nBy{author1} and {author2}\n\nHere is a summary of this article:\n\n{article.summary}\n\n\nView the full article:\n\n{url}')
