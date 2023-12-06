import sqlite3


class DBHelper:

    def __init__(self, db_name="company.db"):
        self.dbname = f"sqlite3:/{db_name}"
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_database()
        self.insert_categories()

    def create_database(self):
        self.create_all_tables()

    def create_all_tables(self):
        self.create_auth_user_table()
        self.create_address_table()
        self.create_status_table()
        self.create_category_table()
        self.create_material_table()
        self.create_request_table()
        self.create_request_materials_table()

    def insert_categories(self):
        list = ['Сыпучие материалы', 'Электробензоинструменты', 'Инструмент ручной',
                'Расходные материалы', 'Средства индивидуальной защиты', 'Спецтехника']
        for i in list:
            self.insert('category', ['name'], [i])

        list1 = [
            ['Песок', 'Щебень', 'Скальный грунт', 'Отсев'],

            ['Болгарка', 'Перфоратор', 'Молоток отбойный',
             'Шуруповерт', 'Вибротрамбовка', 'Насос электрический',
             'Удленнитель', 'Станок сварочный ПНД', 'Станок сварочный инвертор',
             'Генератор', 'Бензопила'],

            ['Лопата', 'Лом', 'Стропы', 'Монтажка', 'Мастерок', 'Ножовка'],

            ['Бензин', 'Праймер битумный', 'Грунтовка', 'Валики',
             'Кисточки', 'Цемент', 'Диск отрезной', 'Диск шлифовальный',
             'Электроды', 'Раствор', 'Бетон', 'Проволока вязальная'],

            ['Перчатки', 'Каски', 'Очки защитные', 'Респератор', 'Маска сварочная'],

            ['Автокран', 'Самосвал', 'Экскаватор колесный', 'Экскаватор-погрузчик']
        ]
        units = [
            ['тонны/м3', 'тонны/м3', 'тонны/м3', 'тонны/м3'],

            ['шт.',  'шт.', 'шт.', 'шт.', 'шт.', 'шт.', 'шт.', 'шт.', 'шт.', 'шт.', 'шт.'],

            ['шт.', 'шт.', 'шт.', 'шт.', 'шт.', 'шт.'],

            ['литры', 'кг.', 'кг.', 'шт.', 'шт.', 'шт.', 'шт.', 'шт.', 'шт.', 'м3', 'м3', 'м.'],

            ['шт.', 'шт.', 'шт.', 'шт.', 'шт.'],

            ['смены', 'смены', 'смены', 'смены']
        ]

        for i in range(len(list)):
            for j in range(len(list1[i])):
                self.insert('material', ["category_id", "name", "units"], [i + 1, list1[i][j], units[i][j]])

    def create_auth_user_table(self):
        table_name = "auth_user"
        params = ["id", "password", "last_login", "is_superuser", "first_name", "last_name",
                  "second_name", "is_staff", "is_active", "date_joined", "email"]
        types = ["INTEGER PRIMARY KEY AUTOINCREMENT", "VARBINARY(256) NOT NULL", "TEXT NOT NULL",
                 "BOOLEAN NOT NULL", "TEXT NOT NULL", "TEXT NOT NULL", "TEXT DEFAULT NULL",
                 "BOOLEAN NOT NULL", "BOOLEAN NOT NULL", "DATETIME NOT NULL", "TEXT NOT NULL"]
        self.create_table(table_name, params, types, 1, None)
        self.get_unique("auth_user", "unique_user_email", ["email"])

    def create_address_table(self):
        table_name = "address"
        params = ["id", "flat", "building", "city", "street", "is_archieve", "creator_id"]
        types = ["INTEGER PRIMARY KEY AUTOINCREMENT", "INTEGER DEFAULT NULL", "INTEGER", "TEXT", "TEXT", "BOOLEAN", "INTEGER"]
        self.create_table(table_name, params, types, 1, [
            ["creator_id", "auth_user", "id"]
        ])

    def create_request_table(self):
        table_name = "request"
        params = ["id", "user_id", "staff_id", "address_id", "comment", "status_id",
                  "date_creation", "date_selected", "date_actual"]
        types = ["INTEGER PRIMARY KEY AUTOINCREMENT", "INTEGER", "INTEGER DEFAULT NULL", "INTEGER", "TEXT", "INTEGER",
                 "DATETIME", "DATETIME", "DATETIME"]
        self.create_table(table_name, params, types, 1, [
            ["user_id", "auth_user", "id"],
            ["staff_id", "auth_user", "id"],
            ["address_id", "address", "id"],
            ["status_id", "status", "id"]
        ])

    def create_status_table(self):
        table_name = "status"
        params = ["id", "name"]
        types = ["INTEGER PRIMARY KEY AUTOINCREMENT", "TEXT"]
        self.create_table(table_name, params, types, 1, None)
        self.get_unique("status", "unique_status_name", ["name"])

    def create_request_materials_table(self):
        table_name = "request_materials"
        params = ["request_id", "material_id", "count"]
        types = ["INTEGER", "INTEGER", "INTEGER"]
        self.create_table(table_name, params, types, 2, [
            ["request_id", "request", "id"],
            ["material_id", "material", "id"]
        ])

    def create_category_table(self):
        table_name = "category"
        params = ["id", "name"]
        types = ["INTEGER PRIMARY KEY AUTOINCREMENT", "TEXT"]
        self.create_table(table_name, params, types, 1, None)
        self.get_unique("category", "unique_category_name", ["name"])

    def create_material_table(self):
        table_name = "material"
        params = ["id", "category_id", "name", "units"]
        types = ["INTEGER PRIMARY KEY AUTOINCREMENT", "INTEGER", "TEXT", "TEXT"]
        self.create_table(table_name, params, types, 1, [["category_id", "category", "id"]])
        self.get_unique("material", "unique_material_name", ["name"])

    def create_table(self, table_name, params, types, primary_keys_count, foreign_keys):
        column = ""
        keys = ""
        for_keys = ""

        for i in range(0, primary_keys_count - 1):
            keys += params[i] + ", "
        keys += params[primary_keys_count - 1]

        for i in range(len(params) - 1):
            column += params[i] + f" {types[i]}, "
        column += params[len(params) - 1] + f" {types[len(types) - 1]}"

        # foreign keys
        if foreign_keys is not None:
            for i in range(len(foreign_keys) - 1):
                for_keys += f"FOREIGN KEY({foreign_keys[i][0]}) REFERENCES {foreign_keys[i][1]} ({foreign_keys[i][2]}), "
            for_keys += f"FOREIGN KEY({foreign_keys[len(foreign_keys) - 1][0]}) REFERENCES " \
                        f"{foreign_keys[len(foreign_keys) - 1][1]} ({foreign_keys[len(foreign_keys) - 1][2]})"

        new_table = f"CREATE TABLE IF NOT EXISTS {table_name} ({column}" \
                    f"\n {(f', PRIMARY KEY ({keys})', '')[primary_keys_count == 1]}" \
                    f"{(f', {for_keys}', '')[foreign_keys is None]})"
        # print(new_table)
        try:
            print(new_table)
            self.conn.execute(new_table)
            self.conn.commit()
        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            self.conn.rollback()

    def get_unique(self, table_name, name, unique_columns):
        column = ""
        for i in range(len(unique_columns) - 1):
            column += unique_columns[i] + ", "
        column += unique_columns[len(unique_columns) - 1]

        unique = f"CREATE UNIQUE INDEX {name} ON {table_name}({column})"

        try:
            print(unique)
            self.conn.execute(unique)
            print("Выполнилось")
            self.conn.commit()
        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            self.conn.rollback()

    def update(self, table_name, column_arg, arg, column_change, change):
        update = f"UPDATE {table_name} " \
                 f"SET {column_change} = '{change}' " \
                 f"WHERE {column_arg} = '{arg}' "
        try:
            print(update)
            self.conn.execute(update)
            print("Выполнилось")
            self.conn.commit()
        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            self.conn.rollback()

    def delete(self, table_name, column_arg, arg):
        update = f"DELETE FROM {table_name} " \
                 f"WHERE {column_arg} = '{arg}' "
        try:
            # print(new_insert)
            self.conn.execute(update)
            # print("Выполнилось")
            self.conn.commit()
        except sqlite3.Error as err:
            # print('Sql error: %s' % (' '.join(err.args)))
            self.conn.rollback()

    def insert_check(self, table_name, primary_key, primary_value, args):
        arguments = f"'{primary_value}', '"
        for i in range(len(args) - 1):
            arguments += str(args[i]) + "', '"
        arguments += str(args[len(args) - 1]) + "'"
        # print(arguments)

        new_insert = f"INSERT INTO {table_name} SELECT * FROM (SELECT {arguments}) AS tmp " \
                     f"WHERE NOT EXISTS ( SELECT {primary_key} FROM {table_name} WHERE {primary_key} = '{primary_value}'" \
                     f") LIMIT 1"
        try:
            # print(new_insert)
            self.conn.execute(new_insert)
            # print("Выполнилось")
            self.conn.commit()
        except sqlite3.Error as err:
            # print('Sql error: %s' % (' '.join(err.args)))
            self.conn.rollback()

    def insert(self, table_name, column_args, args):
        arguments = "'"
        for i in range(len(args) - 1):
            arguments += str(args[i]) + "', '"
        arguments += str(args[len(args) - 1]) + "'"
        # print(arguments)

        columns = ""
        for i in range(len(column_args) - 1):
            columns += str(column_args[i]) + ", "
        columns += str(column_args[len(column_args) - 1])

        new_insert = f"INSERT INTO {table_name} ({columns}) VALUES ({arguments})"
        # print(new_insert)

        try:
            print(new_insert)
            self.conn.execute(new_insert)
            # print("Выполнилось")
            self.conn.commit()
            return True
        except sqlite3.Error as err:
            print('Sql error: %s' % (' '.join(err.args)))
            self.conn.rollback()
            return False

    def print_info(self, table_name):
        new_get = f"SELECT * FROM {table_name}"
        cursor = self.conn.execute(new_get)

        # print("Выполнилось")

        return [row for row in cursor]

    def get(self, table_name, column_args, args):
        query = ""
        for i in range(len(column_args) - 1):
            query += column_args[i] + " = '" + args[i] + "' AND "
        query += column_args[len(column_args) - 1] + " = '" + args[len(column_args) - 1] + "'"

        new_get = f"SELECT * FROM {table_name} WHERE {query}"
        # print(new_get)

        cursor = self.conn.execute(new_get)

        return [row for row in cursor]

    def rollback(self):
        self.conn.rollback()


    # def update(self, flat_id, updates):

    # def delete(self, flat_id):
