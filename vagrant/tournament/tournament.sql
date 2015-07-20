-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament;


CREATE TABLE players(
    id serial PRIMARY KEY,
    name varchar(100)
);


CREATE TABLE matches(
    player1_id integer references players(id),
    player2_id integer references players(id),
    winner integer references players(id)
);


--Finding the number of matches each player has played.
CREATE VIEW number_of_matches_by_player AS
    SELECT id, name, COALESCE(number_of_matches, 0) number_of_matches
    FROM players
    LEFT JOIN
    (
        SELECT player_id, COUNT(player_id) number_of_matches
        FROM
        (
            SELECT player1_id as player_id
            FROM matches
            UNION
            SELECT player2_id
            FROM matches
        ) all_players
        GROUP BY player_id
    ) players_matches
    ON players.id = players_matches.player_id;


-- The number of wins for each player.
CREATE VIEW number_of_wins_by_player AS
    SELECT players.id, players.name, COUNT(matches.winner) number_of_wins
    FROM players
    LEFT JOIN matches
    ON players.id = matches.winner
    GROUP BY players.id, players.name, matches.winner;


--The player standings.
CREATE VIEW player_standings AS
    SELECT number_of_wins_by_player.id, number_of_wins_by_player.name, number_of_wins, number_of_matches
    FROM number_of_wins_by_player, number_of_matches_by_player
    WHERE number_of_wins_by_player.id = number_of_matches_by_player.id
    ORDER BY number_of_wins_by_player.number_of_wins DESC;

