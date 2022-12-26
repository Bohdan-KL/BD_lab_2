import psycopg2

username = ''
password = ''
database = ''
host = 'localhost'
port = '5432'

query_1 = '''
SELECT white_id AS player_id, white_rating AS player_rating FROM white
UNION 
SELECT * FROM black; 

'''


query_2 = '''
SELECT victory_status, COUNT(victory_status) FROM game
GROUP BY victory_status;

'''

query_3 = '''
SELECT winner, COUNT(winner) FROM game
GROUP BY winner;

'''

def max_len_x(x):
    max_len = 0
    for i in range(len(x)):
        if len(x[i]) > max_len:
            max_len = len(x[i])
    return max_len

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur1 = conn.cursor()
    cur1.execute(query_1)
    player_id = []
    victory_status_amount = []

    for row in cur1:
        player_id.append(row[0])
        victory_status_amount.append(row[1])

    max_len_name = max_len_x(player_id)
    for i in range(len(player_id)):
        print(player_id[i], ' ' * (max_len_name - len(player_id[i])), '| ', victory_status_amount[i])
    print('\n\n')


    cur2 = conn.cursor()
    cur2.execute(query_2)
    wins = []
    victory_status_amount = []

    for row in cur2:
        wins.append(row[0])
        victory_status_amount.append(row[1])

    max_len_country = max_len_x(wins)
    for i in range(len(wins)):
        print(wins[i], ' ' * (max_len_country - len(wins[i])), '| ', victory_status_amount[i])
    print('\n\n')


    cur3 = conn.cursor()
    cur3.execute(query_3)
    wins = []
    win_nature = []

    for row in cur3:
        wins.append(row[0])
        win_nature.append(row[1])

    max_len_country = max_len_x(wins)
    for i in range(len(wins)):
        print(wins[i], ' ' * (max_len_country - len(wins[i])), '| ', win_nature[i])

    print('\n\n')