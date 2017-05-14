#Eric Xie hx8rc
import psycopg2
import csv

def load_course_database(db_name, csv_filename):
    PG_USER = "postgres"
    PG_USER_PASS = "120995"
    PG_HOST_INFO = ""  # use "" for OS X or Windows
    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + db_name + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)

    print("** Connected to database.")
    cur = conn.cursor()
    with open(csv_filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            asTuple = tuple(row)
            cur.execute("INSERT INTO coursedata (deptID, courseNum, semester, meetingType, seatsTaken, seatsOffered, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s)", asTuple )
        # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()



PG_DATABASE = "course1"

load_course_database(PG_DATABASE , "seas-courses-5years.csv")

