# Tournament Results

Tournament Results keeps track of players and matches in a game tournament.

## Table of contents

- [Installation](#installation)
- [Dependencies](#dependencies)

## Dependencies
As a first step, make sure you have the following dependencies installed:
- [Python 2.7.x](https://www.python.org/downloads/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)

On the links above you'll find the necessary documentation to install each one of the required dependencies.

## Installation

### What's included

Within the download you'll find the following files. You'll see something like this:

```
|-- vagrant
  |-- tournament
    |-- tournament.py
    |-- tournament.sql
    |-- tournament_test.py
```

### Running the application test

1. [Download the latest version](https://github.com/jlulloav/tournament_results/archive/master.zip).
2. From the vagrant folder, you can run this command to start the virtual machine:
```$ vagrant up```
3. Run this command to go inside the virtual machine:
```$ vagrant ssh```
4. Run this command to install the database:
```$ psql```
```$ \i /vagrant/tournament/tournament.sql```
```$ \q```
5. Run this command to run the application test:
```$ python /vagrant/tournament/tournament_test.py```
6. If everything is fine, You will see this.  
```1. Old matches can be deleted.```
```2. Player records can be deleted.```
```3. After deleting, count_players() returns zero.```
```4. After registering a player, count_players() returns 1.```
```5. Players can be registered and deleted.```
```6. Newly registered players appear in the standings with no matches.```
```7. After a match, players have updated standings.```
```8. After one match, players with one win are paired.```
```Success!  All tests pass!```