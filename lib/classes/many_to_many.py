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
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        categories = {article.magazine.category for article in self.articles()}
        if categories:
           return list(categories)
        else:
            return None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass