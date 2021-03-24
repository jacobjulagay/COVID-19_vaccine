## About The Project
The goal of this project is to find insights about the Covid-19 vaccine distribution and demographic. Also, I will be talking about how I automated the pulling of data from the CDC Website and Github. 

In order to store all of this data, I used MySQL. Since I am working with a team, I wanted all of us to have the same database. So I decided to learn how to host our MySQL Server onto AWS using their Relational DataBase Service (RDS).

Once, everyone is connected to AWS, we then connect to a data visualiztion software like Tableau or Power BI to find insights within the data. 

I used Python, Pandas, and SqlAlchemy in order fetch data from the CDC API. Once I pulled the data, I converted the datasets into separate dataframes. After, I used the '.to_sql' function in the Pandas library to convert the dataframes to MySQL Tables and connected them to my AWS Server. 
I was able to use the Socrata API to get 3 datasets:
1. J&J Vaccine Results
2. Moderna Vaccine Results
3. Pfizer Vaccine Results

The reason I am using Selenium is because the datasets below do not have an API endpoint. The 3 datasets I am focused on retrieving are: 
1. Race/Ethnicity of People Fully Vaccinated
2. Age Groups of People Fully Vaccinated
3. Sex of People Fully Vaccinated

### Built With
* Python
  * Selenium
  * Pandas
  * SqlAlchemy 
* MySQL
* AWS RDS (Relational Database Service )
* Tableau 
* PowerBI
