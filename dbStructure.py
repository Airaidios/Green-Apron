import sqlite3

def executeSQL(
    db_name,
    sql
    ):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

db_name = "ga.db"

clientTable = """CREATE TABLE IF NOT EXISTS CLIENT
    (client_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    username text,
    address text,
    package integer,
    diet_req text,
    email text,
    level integer,
    password text)"""
executeSQL(db_name, clientTable)

orderTable = """CREATE TABLE IF NOT EXISTS "ORDER"
    (order_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    client_id integer,
    kit_id integer,
    foreign key(client_id) references CLIENT(client_id)on update cascade on delete cascade
    foreign key(kit_id) references KIT(kit_id)on update cascade on delete cascade)"""
executeSQL(db_name, orderTable)

kitTable = """CREATE TABLE IF NOT EXISTS KIT
    (kit_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    kit_name text,
    price float,
    size text)"""
executeSQL(db_name, kitTable)

recipeTable = """CREATE TABLE IF NOT EXISTS RECIPE
    (rec_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    rec_name text,
    culture text
    servings integer,
    prep_time integer,
    kit_id integer,
    foreign key(kit_id) references KIT(kit_id)on update cascade on delete cascade)"""
executeSQL(db_name, recipeTable)

ingredientTable = """CREATE TABLE IF NOT EXISTS INGREDIENT
    (ing_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    ing_name text,
    ing_quant integer,
    allergy text,
    type text,
    rec_id integer,
    foreign key(rec_id) references RECIPE(rec_id)on update cascade on delete cascade)"""
executeSQL(db_name, ingredientTable)

if __name__=="__main__":
    pass
