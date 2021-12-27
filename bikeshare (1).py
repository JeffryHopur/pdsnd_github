import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input('Which city whould you like to analyze data for? (E.g. chicago, new york city, washington), Washington does not have userdata.\n')
        if city_name.lower() in CITY_DATA:

            city = CITY_DATA[city_name.lower()]
        else:

            print('Sorry the input does not match the cities we have data on please enter chicago, new york city or washington.\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input('Which month would you like to filter the data by? (E.g Please input (all) to apply no month filter or input january, febuary, march,Etc.)\n')
        if month_name.lower() in MONTH_DATA:

            month = month_name.lower()
        else:

            print('sorry we were not able to process the input please input (all) to apply no month filter or input january, febuary, march,Etc.\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input('Which day would you like to filter the data by? (E.g Please input (all) to apply no day filters or input monday, tuesday, wednesday,Etc.)\n')
        if day_name.lower() in DAY_DATA:

            day = day_name.lower()
        else:

            print('sorry we were not able to process the input please input (all) to apply no day filters or input monday, tuesday, wednesday,Etc.)\n')

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
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The filtered data shows the most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The filtered data shows the most common day is: ', common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The filtered data shows the most common hour is: ', str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The filtered data shows the most common start station is: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The filtered data shows the most common end station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "," + df['End Station']).mode()[0]
    print('the most requent combination of start station and end station trip is: ', str(frequent_combination.split(",")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration']
    total_travel_time = trip_duration.sum()
    print('The filtered data shows the total travel time is: \n', str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = trip_duration.mean()
    print('The filtered data shows the mean travel time is: \n', str(mean_travel_time))

    # display max travel time
    max_travel_time = trip_duration.max()
    print('The filtered data shows the max travel time is: \n', str(max_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The filtered data shows the count of user types is: \n', str(user_types))

    if 'Gender' in CITY_DATA:
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n", str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        earliest_birth = birth_year.min()
        most_recent_birth = birth_year.max()
        most_common_birth = birth_year.mode()[0]
        print('The filtered data shows the earliest birth is: {}\n', earliest_birth)
        print('The filtered data shows the most recent birth is: {}\n', most_recent_birth)
        print('The filtered data shows the most common birth is: {}\n', most_common_birth)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the washington database')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    count = 0
    while True:
        raw_data = input('\ntype (yes or no) on if you would like to see the next 5 lines of raw data\n')
        if raw_data.lower() != 'yes':
            return
        count += 5
        print(df.iloc[count:count+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
