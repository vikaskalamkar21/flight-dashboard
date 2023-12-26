import mysql.connector

class DB:
    def __init__(self):
        #connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='indigo')
            self.mycursor = self.conn.cursor()
            print('connection established')
        except:
            print('connection error')

    def fetch_city_names(self):

        city= []
        self.mycursor.execute("""
        SELECT DISTINCT(destination) from indigo.flights
        UNION
        SELECT DISTINCT(Source) from indigo.flights""" )

        data = self.mycursor.fetchall()

        print(data)

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self,source,destination):

        self.mycursor.execute('''SELECT Airline,Route,Dep_time,Duration,Price FROM indigo.flights
                                WHERE Source = '{}' AND Destination = '{}'
                                '''.format(source,destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
                            SELECT airline , count(*) FROM indigo.flights
                            group by airline""")

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

    def busy_airport(self):
        city = []
        frequency1 = []

        self.mycursor.execute("""
                                select source,count(*) from (select source from indigo.flights
								union all 
								select destination from indigo.flights) t
                                group by t.source
                                order by count(*) desc
                                """)
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency1.append(item[1])

        return city, frequency1

    def daily_frequency(self):
                date = []
                frequency2 = []

        self.mycursor.execute("""
            SELECT date_of_journey,count(*) from indigo.flights
            group by date_of_journey""")
        data = self.mycursor.fetchall()

        for item in data:
                date.append(item[0])
                frequency2.append(item[1])

        return date, frequency2