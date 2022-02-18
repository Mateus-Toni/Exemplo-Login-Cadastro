import mysql.connector

import parameters



def open_db(user, password, host, database):
    try:
        db = mysql.connector.connect(user=user, password=password,
                                     host=host, database=database)
        cursor = db.cursor(dictionary=True)
    except:
        return None, None
    else:
        return db, cursor
    
    
def save_user(nome, sobrenome, email, telefone, senha):
    db, cursor = open_db(parameters.NAME, parameters.PASSWORD, parameters.HOST, parameters.DB_NAME)
    if db:
        cursor.execute(f"""insert into users values (default, '{nome}', '{sobrenome}','{email}','{telefone}', '{senha}')""")
        db.commit()
        db.close()


def delete_user(id_user):
    db, cursor = open_db(parameters.NAME, parameters.PASSWORD, parameters.HOST, parameters.DB_NAME)
    if db:
        cursor.execute(f"""delete from users where id_user = '{id_user}';""")
        db.commit()
        db.close        


def verify_items(email, telefone):
    db, cursor = open_db(parameters.NAME, parameters.PASSWORD, parameters.HOST, parameters.DB_NAME)
    if db:
        cursor.execute(f"""select * from users where email = '{email}' or telefone = '{telefone}';""")
        if has := cursor.fetchall():
            return False
        return True


def get_items(email):
    db, cursor = open_db(parameters.NAME, parameters.PASSWORD, parameters.HOST, parameters.DB_NAME)
    if db:
        cursor.execute(f"""select nome, senha from users where email = '{email}'""")
        values = cursor.fetchall()
        for dict_values in values:
            return dict_values
        
