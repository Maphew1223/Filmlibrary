import random
from datetime import date

class film:
  
  def __init__(self, title, year, genre, views=0):
      self.title = title
      self.year = year
      self.genre = genre
      self.views = views
    
  def play(self):
      self.views += 1
    
  def __str__(self):
    return f"{self.title} ({self.year})"
    
class series:
  
  def __init__(self, title, year, genre, episode, season, views=0):
    self.title = title
    self.year = year
    self.genre = genre
    self.episode = episode
    self.season = season
    self.views = views
    
  def play(self):
    self.views += 1
    
  def __str__(self):
    return f"{self.title} S{self.season:02}E{self.episode:02}"
    
library = [
  film("Jackass - świry w akcji", 2002, "Akcja", 0),
  film("Blade Runner 2049", 2017, "Science-fiction", 0),
  film("Diuna", 2021, "Science-fiction", 0),
  film("Władca mroku", 2023, "Horror", 0),
  film("Czarny telefon", 2021, "Horror", 0),
  series("Chłopaki z baraków", 2001, "Sitcom", 5, 1),
  series("Rick i Morty", 2013, "Sitcom", 2, 3),
  series("Bojack Horseman", 2014, "Sitcom", 4, 2),
  series("Ed, Edd i Eddy", 1999, "Cartoon", 1, 1),
  series("Nie ma jak w rodzinie", 2015, "Sitcom" , 2, 2),       
]

def get_movies():
  return sorted([title for title in library if isinstance(title, film)], key=lambda x: x.title)
  
def get_series():
  return sorted([title for title in library if isinstance(title, series)], key=lambda x: x.title)
  
def top_titles(n):
  return sorted(library, key=lambda x: x.views, reverse=True)[:n]
print("Biblioteka filmów\nFilmy:")

for m in get_movies():
    print(m)
print("\nSeriale:")

for s in get_series():
    print(s)
  
def generate_views():
  title = random.choice(library)
  title.views += random.randint(1, 100)
  
def generate_views_multiple(n):
  for v in range(n):
      generate_views()
    
date = date.today()
format_date = date.strftime("%d.%m.%Y")

print("\nGenerowanie odtworzeń...")
generate_views_multiple(10)

print(f"\nNajpopularniejsze filmy i seriale dnia {format_date}:")
for title in top_titles(3):
    print(f"{title}: {title.views} odtworzeń")
  