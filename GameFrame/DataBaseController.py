import os
import sqlite3


class DataBaseController:
    """
    Controller class for managing SQLite database connections and queries.

    Attributes:
        app_db (sqlite3.Connection): The SQLite database connection object.
        app_cursor (sqlite3.Cursor): The cursor object for executing SQL queries.
    """

    def __init__(self, dbase_file_name: str):
        """
        Initializes the DataBaseController with the specified database file.

        Args:
            dbase_file_name (str): The name of the SQLite database file.
        """
        app_file_path = os.path.join(os.path.dirname(__file__), dbase_file_name)
        self.app_db = sqlite3.connect(app_file_path)
        self.app_cursor = self.app_db.cursor()

    def close(self):
        """
        Closes the database connection.
        """
        self.app_db.close()

    # ------------------------------ #
    # -- This is an example query -- #
    # ------------------------------ #
'''
    def get_lesson(self, topic):
        """
        Retrieves the lesson for a given topic from the Topic table.

        Args:
            topic (str): The name of the topic.

        Returns:
            str: The lesson associated with the topic.
        """
        self.app_cursor.execute(
            """
                SELECT lesson
                FROM Topic
                WHERE name = :topic
            """,
            {'topic': topic}
        )
        return self.app_cursor.fetchone()[0]
'''
