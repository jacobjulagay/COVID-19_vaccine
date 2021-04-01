import pandas as pd
from sodapy import Socrata
from sqlalchemy import create_engine
import credentials
import requests


# Credentials for AWS
un = credentials.login['username']
pw = credentials.login['pw']
endpoint = credentials.login['endpoint']

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cdc.gov", None)

# Pfizer results: CDC
pfizer_results = client.get("saz5-9hgg")
pfizer_results_df = pd.DataFrame.from_records(pfizer_results)
pfizer_results_df2 = pfizer_results_df.assign(manufacturer = 'pfizer')

# J&J results: CDC
jj_results = client.get("w9zu-fywh")
jj_results_df = pd.DataFrame.from_records(jj_results)
jj_results_df2 = jj_results_df.assign(manufacturer = 'jj')

# Moderna results: CDC
moderna_results = client.get("b7pe-5nws")
moderna_results_df = pd.DataFrame.from_records(moderna_results)
moderna_results_df2 = moderna_results_df.assign(manufacturer = 'moderna')

# us_state_vaccinations.csv from Github: owid/covid-19-data
us_state_vaccinations_url = "https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/us_state_vaccinations.csv?raw=true"
us_state_vaccinations_df = pd.read_csv(us_state_vaccinations_url)
print(us_state_vaccinations_df)

# age_groups_of_people_fully_vaccinated: CDC
age_groups_of_people_fully_vaccinated_df = pd.read_csv('C:\\Users\\jacob\\Documents\\Talent_Path\\Covid-Vaccine-Project\\age_groups_of_people_fully_vaccinated.csv', skiprows=3)
# race_ethnicity_of_people_fully_vaccinated: CDC
race_ethnicity_of_people_fully_vaccinated_df = pd.read_csv('C:\\Users\\jacob\\Documents\\Talent_Path\\Covid-Vaccine-Project\\race_ethnicity_of_people_fully_vaccinated.csv', skiprows=3)
# sex_of_people_fully_vaccinated: CDC
sex_of_people_fully_vaccinated_df = pd.read_csv('C:\\Users\\jacob\\Documents\\Talent_Path\\Covid-Vaccine-Project\\sex_of_people_fully_vaccinated.csv', skiprows=3)

    
# Connecting to AWS w/ sqlalchemy
engine = create_engine('mysql://{}:{}@{}'.format(un,pw,endpoint))

# Transforming DataFrames to MySQL Tables
pfizer_results_df2.to_sql('pfizer_vaccine', con = engine, if_exists= 'replace', index = False)
jj_results_df2.to_sql('jj_vaccine', con = engine, if_exists= 'replace', index = False)
moderna_results_df2.to_sql('moderna_vaccine', con = engine, if_exists= 'replace', index = False)
us_state_vaccinations_df.to_sql('us_state_vaccinations', con=engine, if_exists = 'replace', index=False)
age_groups_of_people_fully_vaccinated_df.to_sql('age_groups_of_people_fully_vaccinated',con=engine, if_exists = 'replace', index=False)
race_ethnicity_of_people_fully_vaccinated_df.to_sql('race_ethnicity_of_people_fully_vaccinated',con=engine, if_exists = 'replace', index=False)
sex_of_people_fully_vaccinated_df.to_sql('sex_of_people_fully_vaccinated',con=engine, if_exists = 'replace', index=False)