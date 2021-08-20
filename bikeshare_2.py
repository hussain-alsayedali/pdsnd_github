import time
import pandas as pd
import numpy as np
mm=['all', 'january' ,'february', 'march', 'april', 'may', 'june']
dd=['all', 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday']
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('specify a city to analyze!')
    print('either chicago, new york city or washington ')
    city=input().lower()
    while city != 'chicago' and city != 'new york city' and city !=  'washington':
        print('type another city ,this city is not valid')
        city = input().lower()
    # get user input for month (all, january, february, ... , june)
    print('specify a month to analyze!')
    print('either january ,february, march, april, may or june')
    print('if you want to see all type ALL')
    month = input().lower()
    while month not in mm:
        print('this month is not valid type another month')
        month = input().lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('specify a day to analyze!')
    day = input().lower()
    while day not in dd :
        print('this day is not valid type another day')
        day = input().lower()

    print('-'*40)
    return city, month, day





def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('themost common month Hour is:', popular_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_month = df['day_of_week'].mode()[0]
    print('the most common day of week is:', popular_month)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station is', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('most commonly used end station is', popular_end_station)

    # display most frequent combination of start station and end station trip

    popular_end_start_station = (df['Start Station'] + ' -/- ' + df['End Station']).mode()[0]
    print('most frequent combination of start station and end station trip is',popular_end_start_station )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time =df['Trip Duration'].sum()
    print('total travel time is :',total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time is :',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user types are :',user_types)

    # Display counts of gender
    if 'gender' in df:
        Gender_types = df['Gender'].value_counts()
        print('gender types are :' ,Gender_types )

    # Display earliest, most recent, and most common year of birth
        birth_year_max = df['Birth Year'].max()
        print('the most recent birth year is :' , birth_year_max)
        birth_year_min = df['Birth Year'].min()
        print('the earliest birth year is :', birth_year_min)
        birth_year_mean =df['Birth Year'].mode()[0]
        print('the most common birth year is :', birth_year_mean)
    else:
        print('washington does not have data about birthyear or genders')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        see = input('\nWould you like to see more data type yes or no \n').lower()
        while see != 'yes' and see!= 'no':
            print('type yes or no')
            see=input().lower()
        num = 0
        while True :
            if see == 'yes':
                columns=df.iloc[num: num + 5]
                num = num + 5
                print(columns)
                see = input('\nWould you like to see more data type yes or no \n').lower()
                while see != 'yes' and see != 'no':
                    print('type yes or no')
                    see = input().lower
            else:
                break
        restart = input(' do you want to restart')
        while restart != 'yes' and restart != 'no':
            print('type yes or no')
            restart = input()
        if restart.lower() == 'yes':
            print('have a nice day')
            break



if __name__ == "__main__":
	main()
