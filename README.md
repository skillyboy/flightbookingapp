                +------------------+       +-----------------+       +--------------+
                |     Airport      |       |     Airline     |       |   Aircraft   |
                +------------------+       +-----------------+       +--------------+
                | id: Integer      |1     *| id: Integer     |1     *| id: Integer  |
                | name: String     |<----- *| name: String    |<-----| airline_id:  |
                | city: String     |        +-----------------+       |   Integer    |
                | country: String  |                                  | model:       |
                +------------------+                                  |   String     |
                        |                                             | registration|
                        |                                             |   _number:   |
                        |                                             |   String     |
                        |                                             +--------------+
                        |                                                            |
                +------------------+                                                |
                |       User       |                                                |
                +------------------+                                                |
                | id: Integer      |                                                |
                | username: String |                                                |
                | email: String    |                                                |
                | password: String |                                                |
                +------------------|------------------------------------------------+
                        |                                                        |
                        |                                                        |
                +------------------+                                                |
                |      Flight      |                                                |
                +------------------+                                                |
                | id: Integer      |                                                |
                | airline_id:      |                                                |
                |     Integer      |                                                |
                | aircraft_id:     |                                                |
                |     Integer      |                                                |
                | flight_number:   |                                                |
                |     String       |                                                |
                | origin_id:       |                                                |
                |     Integer      |                                                |
                | destination_id:  |                                                |
                |     Integer      |                                                |
                | departure_datetime: |                                             |
                |     DateTime     |                                                |
                | arrival_datetime: |                                               |
                |     DateTime     |                                                |
                | available_seats: |                                                |
                |     Integer      |                                                |
                +------------------+------------------------------------------------+
                        |                                                        |
                        |                                                        |
                +------------------+                                                |
                |     Booking      |                                                |
                +------------------+                                                |
                | id: Integer      |                                                |
                | user_id: Integer |                                                |
                | flight_id:       |                                                |
                |     Integer      |                                                |
                | date: DateTime   |                                                |
                +------------------+------------------------------------------------+
