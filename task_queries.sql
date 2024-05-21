-- Task 1: Top 10 highest-scoring games in the last decade
WITH games_with_total_score AS (
    SELECT
        date,
        home_team,
        away_team,
        home_score,
        away_score,
        season,
        (home_score + away_score) AS total_score
    FROM nba_games g
    JOIN nba_teams hteam ON g.home_team = hteam.team_name
    JOIN nba_teams ateam ON g.away_team = ateam.team_name
    WHERE season >= season - 10
)
SELECT
    strftime(date, '%Y-%m-%d') AS date,
    home_team,
    away_team,
    home_score,
    away_score,
    total_score
FROM games_with_total_score
ORDER BY total_score DESC
LIMIT 10;

--Task 2: Win-Loss record for each team over the last decade
SELECT
    t.team_name,
    SUM(CASE WHEN g.home_team = t.team_name AND g.home_score > g.away_score THEN 1 ELSE 0 END +
        CASE WHEN g.away_team = t.team_name AND g.away_score > g.home_score THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN g.home_team = t.team_name AND g.home_score < g.away_score THEN 1 ELSE 0 END +
        CASE WHEN g.away_team = t.team_name AND g.away_score < g.home_score THEN 1 ELSE 0 END) AS losses
FROM nba_games g
JOIN nba_teams t ON g.home_team = t.team_name OR g.away_team = t.team_name
WHERE g.season >= g.season - 10
GROUP BY t.team_name
ORDER BY wins DESC, losses ASC;

--Task 3: Team performance by season (avg points scored by each team per season)
WITH team_points AS (
    SELECT
        home_team AS team,
        season,
        home_score AS points
    FROM nba_games
    WHERE season >= season - 10

    UNION ALL

    SELECT
        away_team AS team,
        season,
        away_score AS points
    FROM nba_games
    WHERE season >= season - 10
),

final_teams AS (
    SELECT
        tp.team,
        tp.season,
        tp.points
    FROM team_points tp
    JOIN nba_teams t ON tp.team = t.team_name
)

SELECT
    team,
    season,
    ROUND(AVG(points), 2) AS avg_points_scored
FROM final_teams
GROUP BY team, season
ORDER BY team, season;

--Task 4: Conference Analysis
WITH team_wins AS (
    SELECT
        CASE WHEN home_score > away_score THEN home_team ELSE away_team END AS team,
        CASE WHEN home_score > away_score THEN 1 ELSE 0 END AS home_win,
        CASE WHEN away_score > home_score THEN 1 ELSE 0 END AS away_win
    FROM nba_games
    WHERE season >= season - 10
),

wins_with_conference AS (
    SELECT
        tw.team,
        t.conference,
        tw.home_win + tw.away_win AS win
    FROM team_wins tw
    JOIN nba_teams t ON tw.team = t.team_name
)

SELECT
    conference,
    SUM(win) AS total_wins
FROM wins_with_conference
GROUP BY conference
ORDER BY total_wins DESC
LIMIT 1;

--Task 5: Detailed Game Analysis
WITH game_margins AS (
    SELECT
        CASE WHEN home_score > away_score THEN home_team ELSE away_team END AS team,
        ABS(home_score - away_score) AS margin_of_victory
    FROM nba_games
    WHERE season >= season - 10
),

team_avg_margins AS (
    SELECT
        g.team,
        ROUND(AVG(g.margin_of_victory), 2) AS avg_margin_of_victory
    FROM game_margins g
    JOIN nba_teams t ON g.team = t.team_name
    GROUP BY g.team
)

SELECT
    team,
    avg_margin_of_victory
FROM team_avg_margins
ORDER BY avg_margin_of_victory DESC
LIMIT 1;

--Task 6: Analyzing Team Performance Over Multiple Seasons
WITH team_points AS (
    SELECT
        home_team AS team,
        season,
        home_score AS team_points,
        away_score AS opponent_points
    FROM nba_games
    WHERE season >= season - 10

    UNION ALL

    SELECT
        away_team AS team,
        season,
        away_score AS team_points,
        home_score AS opponent_points
    FROM nba_games
    WHERE season >= season - 10
),

final_teams AS (
    SELECT
        tp.team,
        tp.season,
        tp.team_points,
        tp.opponent_points
    FROM team_points tp
    JOIN nba_teams t ON tp.team = t.team_name
)

SELECT
    team,
    season,
    ROUND(AVG(team_points), 2) AS avg_points_scored,
    ROUND(AVG(opponent_points), 2) AS avg_points_allowed
FROM final_teams
GROUP BY team, season
ORDER BY team, season;