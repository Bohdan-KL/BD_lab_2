SELECT * FROM black;
SELECT * FROM white;
SELECT * FROM game;

SELECT white_id AS player_id, white_rating AS player_rating FROM white
UNION 
SELECT * FROM black;

SELECT victory_status, COUNT(victory_status) FROM game
GROUP BY victory_status;

SELECT winner, COUNT(winner) FROM game
GROUP BY winner;
