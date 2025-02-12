import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    view_own_article = views[views['author_id']==views['viewer_id']]['author_id'].unique()
    sorted_authors = sorted(view_own_article)
    sorted_authors =pd.DataFrame(sorted_authors, columns=['id'])
    return sorted_authors
