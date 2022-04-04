# Project Proposal

## What is the end service that your project will provide? What is the purpose of the system you plan to build?

To provide housing recommendations in NYC to the user based on user-input 

## Who is your client and how will that client benefits from your end service?

Client = Individual investors looking to purchase a new home
Benefit = Ability to make an informed decision and get the best value per dollar

### What does your end-to-end data pipeline look like? 

Data ingestion: BigQueryData set obtained from Google's BigQuery Public data (export data points from Google Cloud Platform) --> Data storage with SQL --> Processing with python scripts  --> Deployment to web app (Heroku) 

#### What dataset(s) do you plan to use, and how will you obtain the data? Please include a link! (The link can be to the dataset you’re downloading, the site you’re scraping, etc.)

Obtaining data from Google's BigQuery Public data on housing. The host is [housecanary](https://www.housecanary.com/contact-us/), and they require that I contact them to get access to the full dataset. I've submitted the request form already and hopefully will speak with someone tomorrow. If I can not get access, I will change the project. 

#### Do you plan to be able to automatically pull in new data at a regular cadence (e.g with Airflow or a cron job)?

Not sure at the moment as I do not know how complex it will be to set this part of the project up. 

#### What is an individual sample/unit of analysis in this project? In other words, what does one row or observation of the data represent? 

Features I will work with: Zip code, square footage, address, property features, dollar/sqr foot, valuation, property type. 

#### How do you intend to meet the tools requirements of the project (data storage solution and at least one tool for cloud computing, big data handling, or web deployment)?

SQL for storage 
Google Cloud Platform for cloud computing and big data handling
Heroku for web deployment

#### Are you planning in advance to need or use additional tools beyond those required?
python scripts
OOP
