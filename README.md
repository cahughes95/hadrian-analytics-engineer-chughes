
# Hadrian NBA Analytics Project
## Chris Hughes, Analytics Engineer

This project is designed to extract, transform, and analyze NBA team and game data. The primary goals are to load NBA data from [API-Sports NBA](https://api-sports.io/documentation/nba/v2#section/Introduction) into a DuckDB database, transform it into a usable format, and run various SQL queries to derive insights for the specified questions in the NBA project document. The project requirements are located in the `SQL Test for Analytics Engineer.docx` file.

## Project Structure

```
.
├── elt
|   |── api/
│       ├── __init__.py
│       ├── client.py
|   ├── lib/
│       ├── __init__.py
│       ├── settings.py
|   |── models/
│       ├── __init__.py
│       ├── db.py
│       ├── games.py
│       ├── teams.py
|   |── __init__.py
├── .gitignore
├── README.md
|── SQL Test for Analytics Engineer.docx
|── build_db.py
|── main.py
├── nba_data.db
├── requirements.txt
└── task_queries.sql
```

### Notes About Structure

- The SQL queries for the project tasks are located in the `task_queries.sql` file in the root directory.
- The `build_db.py` script handles the data extraction and transformation in the DuckDB database. The client for requesting data from the API and the models for the DuckDB database are located in the `elt` folder.
- The `main.py` script runs the SQL queries and prints the results for the specified tasks.

## Getting Started

### 1. Prerequisites

- Python 3.8 or higher
- DuckDB
- `requests` library
- `pandas` library
- `tabulate` library

### 2. Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/cahughes95/hadrian-analytics-engineer-chughes
    cd hadrian-analytics-engineer-chughes
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your API key in a `.env` file:
    ```sh
    echo "API_KEY=your_api_key_here" > lib/.env
    ```

### 3. Building the Database

Run the `build_db.py` script to fetch the data from the API, save it to staging tables in a DuckDB database, and transform it into the final schema:

```sh
python build_db.py
```

### 4. Running SQL Queries for the Requested Tasks

To run the provided SQL queries and obtain the results, execute the `main.py` script:

```sh
python main.py
```

## SQL Query Results (Task Answers)

Below are the results from each SQL query I wrote and executed.

### Task 1: Top 10 Highest-Scoring Games in the Last Decade

This query calculates the total score for each game and selects the top 10 highest-scoring games in the last decade.


Result:
```
+------------+-----------------------+-----------------------+------------+------------+-------------+
|    date    |       home_team       |       away_team       | home_score | away_score | total_score |
+------------+-----------------------+-----------------------+------------+------------+-------------+
| 2023-02-25 |      LA Clippers      |   Sacramento Kings    |    175     |    176     |     351     |
| 2019-03-02 |     Atlanta Hawks     |     Chicago Bulls     |    161     |    168     |     329     |
| 2019-10-31 |  Washington Wizards   |    Houston Rockets    |    158     |    159     |     317     |
| 2022-02-26 |  Washington Wizards   |   San Antonio Spurs   |    153     |    157     |     310     |
| 2023-11-22 |     Atlanta Hawks     |    Indiana Pacers     |    152     |    157     |     309     |
| 2020-08-01 |   Dallas Mavericks    |    Houston Rockets    |    149     |    153     |     302     |
| 2024-01-04 |       Utah Jazz       |    Detroit Pistons    |    154     |    148     |     302     |
| 2019-01-11 |   San Antonio Spurs   | Oklahoma City Thunder |    154     |    147     |     301     |
| 2018-12-23 |  Washington Wizards   |     Phoenix Suns      |    149     |    146     |     295     |
| 2019-02-23 | Oklahoma City Thunder |       Utah Jazz       |    148     |    147     |     295     |
+------------+-----------------------+-----------------------+------------+------------+-------------+
...
```

### Task 2: Win-Loss Record for Each Team Over the Last Decade

This query calculates the win-loss record for each team over the last decade.


Result (top 10 included here, execute `main.py` to see full results):
```
+-----------------------+------+--------+
|       team_name       | wins | losses |
+-----------------------+------+--------+
| Golden State Warriors | 563  |  316   |
|    Boston Celtics     | 562  |  329   |
|    Milwaukee Bucks    | 505  |  344   |
|    Denver Nuggets     | 497  |  351   |
|    Toronto Raptors    | 492  |  355   |
|      Miami Heat       | 479  |  388   |
|      LA Clippers      | 476  |  351   |
|       Utah Jazz       | 450  |  365   |
|  Philadelphia 76ers   | 444  |  388   |
| Oklahoma City Thunder | 439  |  377   |
+-----------------------+------+--------+
...
```

### Task 3: Team Performance by Season (Average Points Scored)

This query calculates the average points scored by each team per season over the last decade.


Result (first 10 included here, execute `main.py` to see full results):
```
+----------------+--------+-------------------+
|      team      | season | avg_points_scored |
+----------------+--------+-------------------+
| Atlanta Hawks  |  2015  |      101.88       |
| Atlanta Hawks  |  2016  |      102.93       |
| Atlanta Hawks  |  2017  |      102.93       |
| Atlanta Hawks  |  2018  |       113.3       |
| Atlanta Hawks  |  2019  |      110.63       |
| Atlanta Hawks  |  2020  |      112.23       |
| Atlanta Hawks  |  2021  |      112.71       |
| Atlanta Hawks  |  2022  |      117.99       |
| Atlanta Hawks  |  2023  |       117.7       |
| Boston Celtics |  2015  |      104.86       |
+----------------+--------+-------------------+
...
```

### Task 4: Conference Analysis

This query calculates the total number of wins for each conference over the last decade and selects the conference with the most wins.


Result:
```
+------------+------------+
| conference | total_wins |
+------------+------------+
|    West    |    6266    |
+------------+------------+
```

### Task 5: Detailed Game Analysis

This query calculates the average margin of victory for each team over the last decade and selects the team with the highest average margin of victory.

Result:
```
+-----------------------+-----------------------+
|         team          | avg_margin_of_victory |
+-----------------------+-----------------------+
| Golden State Warriors |         14.1          |
+-----------------------+-----------------------+
```

### Task 6: Analyzing Team Performance Over Multiple Seasons

This query calculates the average points scored and allowed by each team per season over the last decade.


Result (first 10 included here, execute `main.py` to see full results):
```
+----------------+--------+-------------------+--------------------+
|      team      | season | avg_points_scored | avg_points_allowed |
+----------------+--------+-------------------+--------------------+
| Atlanta Hawks  |  2015  |      101.88       |       99.04        |
| Atlanta Hawks  |  2016  |      102.93       |       103.31       |
| Atlanta Hawks  |  2017  |      102.93       |       108.23       |
| Atlanta Hawks  |  2018  |       113.3       |       119.18       |
| Atlanta Hawks  |  2019  |      110.63       |       119.15       |
| Atlanta Hawks  |  2020  |      112.23       |       110.91       |
| Atlanta Hawks  |  2021  |      112.71       |       111.49       |
| Atlanta Hawks  |  2022  |      117.99       |       117.91       |
| Atlanta Hawks  |  2023  |       117.7       |       120.03       |
| Boston Celtics |  2015  |      104.86       |       101.65       |
+----------------+--------+-------------------+--------------------+
...
```

## Assumptions and Notes

- Notes about the NBA teams data pulled: 
    - Used the `league=standard` query parameter for the API request.
    - Only standard league and NBA teams are considered.  
- Notes about the NBA games data pulled:
    - Used the `league=standard` and `season=YYYY` query parameters for the API requests. 
    - I looped through seasons to pull all available season data for the last 10 seasons.
    - Initially attempted to use asyncio to send concurrent requests to API, but had issues with the rate limit (hence the "for loop" for the season requests).
- When writing the SQL queries, I joined the `nba_teams` table on to the `nba_games` data to ensure only games for NBA teams were included in my final results. When I pulled the games data from the API, I couldn't filter out All-Star teams, so I joined my final teams table to exclude those All-Star teams from appearing.

## Conclusion

This project demonstrates how to extract, transform, and analyze NBA data using Python and SQL. By following the setup instructions, you can recreate the DuckDB database and run the provided queries to gain insights into NBA team performances over the last decade.

Thank you for your time and consideration! :)
