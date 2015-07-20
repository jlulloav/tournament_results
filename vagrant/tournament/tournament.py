#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

from itertools import izip_longest

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def delete_matches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM matches")
    db.commit()
    db.close()


def delete_players():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM players")
    db.commit()
    db.close()


def count_players():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    number_of_players = int(cursor.fetchone()[0])
    db.close()
    return number_of_players


def register_player(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    db.commit()
    db.close()


def player_standings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM player_standings")
    player_standing = cursor.fetchall()
    db.close()
    return player_standing


def report_match(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO matches (player1_id, player2_id, winner) VALUES (%s, %s, %s)", (winner, loser, winner,))
    db.commit()
    db.close()


def swiss_pairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    iterator = iter(player_standings())
    player_standings_iterator = list(izip_longest(*[iterator] * 2, fillvalue=None))
    swiss_pairings_list = [(player[0][0], player[0][1], player[1][0], player[1][1]) for player in
                           player_standings_iterator]
    return swiss_pairings_list
