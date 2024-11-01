import pandas as pd 

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv", header = 0)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = round(df["race"].value_counts(),1)
    
    # What is the average age of men?
    average_age_men = round(df.loc[ df["sex"]=="Male","age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education']=='Bachelors', "age"].count() / df.iloc[:,0].count() * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    percentage_advanced = round(df.loc[ ((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')) & (df["salary"] == '>50K'), "education" ].value_counts() / df.loc[ ((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')) & (df["salary"] == '>50K'), "education" ].count() * 100,1)
    
    # What percentage of people without advanced education make more than 50K?
    percentage_50k = round(df.loc[ (df["salary"] == '>50K'), "education"].count()  /  df.loc[ ((df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')), "education"].count() * 100,1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education =  round(df.loc[ ((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')), "education"].count() /df.iloc[:,0].count() * 100,1)
    lower_education = round(df.loc[ ((df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')), "education"].count() /df.iloc[:,0].count() * 100, 1)
    
    total_count = df.iloc[:,0].count()
    
    rich_count =  df.loc[ (df["salary"] == '>50K'), "education"].count()
    
    # percentage with salary >50K
    higher_education_rich = round(df.loc[ (((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate' )) & (df["salary"]==">50K") ), "education"].count() / df.loc[ ((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')), "education"].count() * 100,1)
    lower_education_rich = round(df.loc[ (((df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')) & (df["salary"]==">50K") ), "education"].count() / df.loc[ ((df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')), "education"].count()* 100,1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.loc[ : , "hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[ (df["hours-per-week"]== min_work_hours), "salary" ].count() 

    rich_percentage = round(df.loc[ ( (df["hours-per-week"]== min_work_hours) & (df["salary"] ==">50K")),"salary"].count() / df.loc[ (df["hours-per-week"]== min_work_hours), "salary" ].count() * 100,1)

    # What country has the highest percentage of people that earn >50K?
    
    highest_earning_country_percentage = round((df.loc[ df["salary"] ==">50K", "native-country" ].value_counts() / df.loc[: , "native-country" ].value_counts()).max() * 100,1)
    highest_earning_country = (df.loc[ df["salary"] ==">50K", "native-country" ].value_counts() / df.loc[: , "native-country" ].value_counts()).idxmax()
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[ ((df["native-country"]=="India") & (df["salary"]==">50K")), "occupation" ].value_counts().sort_values(ascending=False).idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    
