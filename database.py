import sqlite3

DATABASE = "projects.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            project_title TEXT NOT NULL,
            description TEXT NOT NULL,
            technology TEXT NOT NULL,
            category TEXT NOT NULL,
            email TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_project(student_name, project_title, description,
                technology, category, email):
    conn = get_connection()

    conn.execute("""
        INSERT INTO projects
        (student_name, project_title, description,
         technology, category, email)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (student_name, project_title, description,
          technology, category, email))

    conn.commit()
    conn.close()


def get_approved_projects():
    conn = get_connection()

    projects = conn.execute("""
        SELECT * FROM projects
        WHERE status = 'Approved'
        ORDER BY created_at DESC
    """).fetchall()

    conn.close()
    return projects


def get_all_projects():
    conn = get_connection()

    projects = conn.execute("""
        SELECT * FROM projects
        ORDER BY created_at DESC
    """).fetchall()

    conn.close()
    return projects


def update_project_status(project_id, status):
    conn = get_connection()

    conn.execute("""
        UPDATE projects
        SET status = ?
        WHERE id = ?
    """, (status, project_id))

    conn.commit()
    conn.close()


def delete_project(project_id):
    conn = get_connection()

    conn.execute("""
        DELETE FROM projects
        WHERE id = ?
    """, (project_id,))

    conn.commit()
    conn.close()