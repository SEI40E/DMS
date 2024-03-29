import psycopg2
from psycopg2 import sql

# List of database connection strings
DATABASE_URLS = [
    "postgres://pbcusqgz:glJ53RAC-vj2evae_dZVSPnQqI8e_Nui@bubble.db.elephantsql.com/pbcusqgz",
    "postgres://hzypcrnd:5jE78MKpt6885VDIbxRkuI0aBteqqpey@bubble.db.elephantsql.com/hzypcrnd",
    "postgres://nchemrjv:CRSus5sf-6lyOuVx7987xohUWIymuo34@bubble.db.elephantsql.com/nchemrjv"
]

# SQL command to create the "bike" table
create_table_command = sql.SQL("""
CREATE TABLE IF NOT EXISTS bike (
    bike_id SERIAL PRIMARY KEY,
    bike_model VARCHAR(255) NOT NULL,
    bike_price DECIMAL(10, 2)
)
""")

# Function to create table in a given database
def create_table_in_database(db_url):
    try:
        # Connect to the database using the database URL
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        # Execute the create table command
        cur.execute(create_table_command)
        
        # Commit the changes
        conn.commit()
        
        print("Table 'bike' created successfully in database:", db_url)
        
    except psycopg2.DatabaseError as e:
        print(f"An error occurred in database {db_url}: {e}")
    finally:
        # Close communication with the database
        if cur: cur.close()
        if conn: conn.close()

# Iterate over each database URL and create the table
for db_url in DATABASE_URLS:
    create_table_in_database(db_url)
