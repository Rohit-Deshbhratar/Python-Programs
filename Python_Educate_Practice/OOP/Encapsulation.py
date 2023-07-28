class Movie:
  def __init__(self):
    self.title = ""
    self.year = -1
    self.genre = ""

  def __init__(self, title, year, genre):
    self.title = title
    self.year = year
    self.genre = genre

  # getters setters
  def get_title(self):
    return self.title

  def set_title(self, title):
    self.title = title

  def get_year(self):
    return self.year

  def set_year(self, year):
    self.year = year

  def get_genre(self):
    return self.genre

  def set_genre(self, genre):
    self.genre = genre

  def print_details(self):
    print(f"Title: {self.title}, Year: {self.year}, Genre: {self.genre}")

def main(): 
  movie = Movie("The Lion King", 1994, "Adventure")
  movie.print_details()

  print("---")  
  movie.set_title("Forrest Gump")
  print(f"New title: {movie.get_title()}")  

if __name__ == "__main__":
    main()