# Eric Xie hx8rc
import psycopg2

def instructor_numbers(dept_id):
    PG_USER = "postgres"
    PG_USER_PASS = "120995"
    PG_HOST_INFO = ""  # use "" for OS X or Windows
    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + "course1" + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    cur = conn.cursor()
    cur.execute("SELECT * FROM coursedata WHERE deptID = \'%s\'" % dept_id)
    allEntries = cur.fetchall()
    ret = {}
    for entry in allEntries:
        if entry[6] not in ret.keys():
            ret[entry[6]] = 0
        ret[entry[6]] += entry[4]
        print(entry)
    return ret
dict = instructor_numbers("APMA")
for instructor in dict:
    print(instructor,":",dict[instructor])