This is a very basic API covering Le Mans winners by year and was built as an exercise to build an API in Flask
        The database contains the following information:
            <ul>
                <li>Year</li>
                <li>Team</li>
                <li>Car</li>
                <li>Drivers</li>
                <li>Laps</li>
                <li>Distance</li>
            </ul>
    
    
    </p>
    To access the api add  /api/v1/resources/winners to the URL. This will bring back everything
    You can filter on the following headings: Team,Year, Car and Drivers. So to search by year and driver
    
     /api/v1/resources/winners?year=2018&driver=Fernando%20Alonso