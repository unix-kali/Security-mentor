
import hashlib
import hmac
import os
import sqlite3


def hash_password(password: str, salt: bytes | None = None) -> tuple[str, str]:
    if salt is None:
        salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
    return digest.hex(), salt.hex()


def init_db(db_path: str = "users.db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def create_user(conn: sqlite3.Connection, username: str, password: str) -> None:
    password_hash, salt = hash_password(password)
    cursor = conn.cursor()
    # Consulta parametrizada com placeholder '?'
    cursor.execute(
        "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
        (username, password_hash, salt),
    )
    conn.commit()


def login(conn: sqlite3.Connection, username: str, password: str) -> bool:
    cursor = conn.cursor()
    # Seguro: consulta parametrizada separa estrutura SQL dos dados de entrada
    query = "SELECT id, username, password_hash, salt FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    row = cursor.fetchone()
    if row is None:
        return False

    _, _, stored_hash, salt_hex = row
    candidate_hash, _ = hash_password(password, bytes.fromhex(salt_hex))
    return hmac.compare_digest(candidate_hash, stored_hash)


if __name__ == "__main__":
    connection = init_db(":memory:")
    create_user(connection, "admin", "segredo123")

    user_input = input("Usuário: ")
    pass_input = input("Senha: ")

    if login(connection, user_input, pass_input):
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha inválidos.")
