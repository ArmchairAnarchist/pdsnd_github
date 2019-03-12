import time
import pandas as pd
import numpy as np

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
    """ user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs """
    while True:
        city = input('Enter the city of choice: ').lower()
        if (city in ['chicago', 'new york city', 'washington']):
            print ('Thanks for entering: {}'.format(city))
            break
        else:
            print('Please enter: chicago, new york city or washington!')


    """ user input for month (all, january, february, ... , june)"""
    while True:
        month = input('Enter the month of choice (or all): ').lower()
        if (month in ['january', 'February', 'march', 'april', 'may', 'june', 'all']):
            print('Thanks for entering: {}'.format(month))
            break
        else:
            print('Please enter: all, january, february, ... , june !')

    """ user input for day of week (all, monday, tuesday, ... sunday) """

    while True:
        day = input('Enter the day of choice (or all): ').lower()
        if (day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']):
            print ('Thanks for entering: {}'.format(day))
            break
        else:
            print('Please enter: all, monday, tuesday, ... sunday!')
            continue



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

    """ load data file into a dataframe """
    df = pd.read_csv(CITY_DATA[city])

    """ converted Start Time column to datetime """
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    """ extracted month and day of week from Start Time to create new columns """
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    """ filter by month if applicable """
    if month != 'all':
        """ use the index of the months list to get the corresponding int """
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        """ filter by month to create the new dataframe """
        df = df[df['month'] == month]

    """ filter by day of week if applicable """
    if day != 'all':
        """ filter by day of week to create the new dataframe """
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times, dates and days of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """ the most common month """
    common_month = df['month'].mode()[0]

    print('Most Popular Month:', common_month)

    """ the most common day of week """
    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Day:', popular_day)

    """ the most common start hour """
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:',popular_hour,'.00')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    """" most commonly used start station """
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(start_station))

    """ most commonly used end station """
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(end_station))
    """ most frequent combination of start station and end station trip """
    most_common_stations = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station: {},{}"\
    .format(most_common_stations[0], most_common_stations[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """ total travel time """
    tot_time = df['Trip Duration'].sum()/3600
    trip_count = df['Trip Duration'].count()
    print('The total time travelled was: {} hours.'.format(tot_time))
    print('Count: {}.'.format(trip_count))
    """ mean travel time """
    avg_trip = df['Trip Duration'].mean()/60
    print('The mean average trip time was {} minutes'.format(avg_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    """ counts of user types """
    user_types = df['User Type'].value_counts()
    print('The breakdown of users...')
    print(user_types)

    """ counts of gender """
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print('Gender not recorded')

    """ earliest, most recent, and most common year of birth """
    if 'Birth Year' in df.columns:
        print('The oldest user was:', df['Birth Year'].min())

    else:
        print('DOB not recorded.')

    if 'Birth Year' in df.columns:
        print('The youngest user was:', df['Birth Year'].max())

    else:
        print('DOB not recorded.')

    if 'Birth Year' in df.columns:
        print('The most common year of birth was:', df['Birth Year'].min())

    else:
        print('DOB not recorded.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
""" Ask the user if they want to see raw data and keeps showing them this until they say no"""
def display_data (df):
    user_input = input('\nWhat would you like to see raw data?\nPlease enter yes or no\n').lower()
    if user_input in ('yes', 'y'):
        i = 0
    while True:
        print(df.iloc[i:i+5])
        i += 5
        more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
        if more_data not in ('yes', 'y'):
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
