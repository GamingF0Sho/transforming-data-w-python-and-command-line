# Project: Transforming Data from Hacker News

### Overview

In this project, we'll be working with Hacker News (http://news.ycombinator.com/) from 2006 to 2015.  At Hacker News, users submit articles about technology, startups, etc., and others can "upvote" the articles, if they like them.  The dataset was compiled by Arnaud Drizard using the Hacker News API, and can be found here: https://github.com/arnauddri/hn

We will write scripts to answer the following:

- What words appear most often in headlines?
- What domains were submitted most often?
- At what time of day are most articles submitted?

### Data & Files

- **count.py** -- *Determines what words appear most often in the headlines.*
- **domains.py** -- *Determines which domains were submitted most often.*
- **read.py** -- *Loads dataset and does initial processing.  Has a function that allows other scripts to import the code to read in the dataset.*
- **times.py** -- *What hour of the day are the most articles are submitted.*
- **hn_stories.csv** -- *10,000 randomly sampled rows including the following four columns:**
  - **submission_time** -- *When the story was submitted.*
  - **upvotes** -- *Number of upvotes the submission got.*
  - **url** -- *The base domain of the submission.*
  - **headline** -- *The headline of the submission which users can edit.*
 
  
