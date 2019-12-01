from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from recommender.application import application

if __name__ == "__main__":
  application.run()
