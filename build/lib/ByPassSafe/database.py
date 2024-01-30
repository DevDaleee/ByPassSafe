# database.py
import psycopg2
from psycopg2 import sql
import bcrypt

from ByPassSafe.account import Account


class Database:
    DATABASE_URL = "postgres://lfusjels:57VUWL0RGqHFJEsJuYX8L3iuesufDE4n@kesavan.db.elephantsql.com/lfusjels"

    @staticmethod
    def save_account(account):
        try:
            connection = psycopg2.connect(Database.DATABASE_URL)
            cursor = connection.cursor()

            create_account_query = sql.SQL(
                "INSERT INTO accounts (master_id, username, password, email) VALUES ({}, {}, {}, {})"
            ).format(
                sql.Literal(account.master_id),
                sql.Literal(account.username),
                sql.Literal(account.password),
                sql.Literal(account.email),
            )

            cursor.execute(create_account_query)
            connection.commit()

            print("Conta salva com sucesso.")

        except Exception as e:
            print(f"Erro ao salvar conta: {e}")

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_accounts_by_master_id(master_id):
        connection = psycopg2.connect(Database.DATABASE_URL)
        cursor = connection.cursor()

        select_accounts_query = "SELECT * FROM accounts WHERE master_id = %s"
        cursor.execute(select_accounts_query, (master_id,))
        accounts = cursor.fetchall()

        cursor.close()
        connection.close()

        return accounts

    def authenticate_user(email, password):
        connection = psycopg2.connect(Database.DATABASE_URL)
        cursor = connection.cursor()

        select_master_query = "SELECT * FROM masters WHERE email = %s"
        cursor.execute(select_master_query, (email,))
        master = cursor.fetchone()

        cursor.close()
        connection.close()

        if master is not None and bcrypt.checkpw(
            password.encode("utf-8"), master[2].encode("utf-8")
        ):
            return master[0]
        else:
            return None

    @staticmethod
    def get_account_by_username(master_id, username):
        connection = psycopg2.connect(Database.DATABASE_URL)
        cursor = connection.cursor()

        select_account_query = (
            "SELECT * FROM accounts WHERE master_id = %s AND username = %s"
        )
        cursor.execute(select_account_query, (master_id, username))
        account_data = cursor.fetchone()

        cursor.close()
        connection.close()

        if account_data:
            account = Account(
                account_data[0], account_data[2], account_data[3], account_data[4]
            )
            return account
        else:
            return None
