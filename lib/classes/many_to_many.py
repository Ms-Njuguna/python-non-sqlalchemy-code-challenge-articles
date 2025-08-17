class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    def __setattr__(self, key, value):
        if key == "title":
            if not isinstance(value, str):
                return  
            if hasattr(self, "title"):
                return  
        super().__setattr__(key, value)
        
        
class Author:
    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        if key == "name":
            if not isinstance(value, str):
                return  
            if hasattr(self, "name"):
                return  
        super().__setattr__(key, value)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass