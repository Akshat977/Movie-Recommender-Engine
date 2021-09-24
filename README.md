
# Movie Recommender Engine

A RECOMMENDER ENGINE WHICH SUGGESTS MOVIES BASED ON FOLLOWING CONDITIONS:
1. SUGGESTING MOVIES WITH THE HIGHEST POPULARITY + RATING (WHICH HAS NOT YET BEEN WATCHED) 
2. SUGGESTING MOVIES BASED ON CONTENT PREVIOUSLY WATCHED AND ALSO PREDICT THE RATING FOR THE NEW MOVIES BASED ON THE USER

- You input the movies watched and then run type1.py or type2.py according to above mentioned conditions. 

The Datasets used in this project can be found using the following links:

[TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)\
[movies](https://file.io/1uykoAQuJpUk)\
[ratings](https://ufile.io/3rxvkow1)
## Working
A) Suggesting movies based on Popularity + Rating:

- Calculating weighted rating (W), which = [(vR+mC)/(v+m)]
Here: 
R: average rating of the movie; 
v: number of votes;  
m: minimum number of votes;
C: mean votes

- Calculating Score = Popularity+W
- Sort score in descending order
- Suggest the top N movies

B) Suggesting movies based on content previously watched and predict ratings:

- Finding the genres of the movies watched from the dataset.
- Forming a user profile according to the genres of movies watched.
- Calculating a score according to number of different genres movies watched and suggesting movies with a new score (Rating).
- Display N movies with highest ratings.




  
## Screenshots
TYPE 1:
![App Screensht](https://i.ibb.co/3dXFtmz/screenshot1.png)
![App Screensht](https://i.ibb.co/grQK7x4/output1.png)

TYPE 2:
![App Screenshot](https://i.ibb.co/N2D9pC1/screenshot2.png)
![App Screenshot](https://i.ibb.co/9hH5tpc/output2.png)

## Deployment

If you want to view movies you have not yet watched based on ratings+popularity:

```bash
  python type1.py
```

If you want similar content (according to your user profile):
```bash
  python type2.py
```

  
## Feedback

If you have any feedback, please reach out me at akshatsaxena977@gmail.com and also reach me at the following links:

  
## Authors

- [AKSHAT SAXENA](https://github.com/Akshat977)

  
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://akshat977.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akshat-saxena-6a3279188/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/AkshatS45989877)

  
## 🛠 Skills 
Statistical Machine Learning, Deployment, Web Scraping...

  