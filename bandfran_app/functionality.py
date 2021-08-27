from random import randrange

def populate_stats(stats, users):
    stats['pop'] = randrange(10, 30)
    stats['unique'] = randrange(40, 60)
    stats['users'] = randrange(1, 5)
    select_user = randrange(0, len(users))
    stats['user_name'] = users[select_user]['first_name'] + " " + users[select_user]['last_name']
    stats['user_email'] = users[select_user]['email']
    return stats