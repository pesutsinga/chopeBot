import pymysql

# CODE TESTING : insert sample data into database

# Connect to the database
db = pymysql.connect("bebong.id", "u7728567", "ikehik3h", "u7728567_chopebot")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# CODE TESTING : insert data according to stored user input from shell
# NEXT : prompt id, uname & pass, facilities priority rank from telegram chat
TelegramID = input('What is your telegram ID? ')
Username = input('What is your NTU Username? ')
Passwords = input('What is your NTU Password? ')
CircularPod = input('Set your facility priority for Circular Pods: ')
LearningPod = input('Set your facility priority for Learning Pods: ')
CollabBooths = input('Set your facility priority for Collab Booths: ')
LearningRoom = input('Set your facility priority for Learning Room: ')
RecordingRoom = input('Set your facility priority for Recording Room: ')

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO LIBCHOP(TELEGRAMID, USERNAME,PASSWORD,
                            CIRCULAR_PODS, LEARNING_PODS,
                            COLLAB_BOOTHS, LEARNING_ROOM,
                            RECORDING_ROOM)
   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

try:
    # Execute the SQL command
    cursor.execute(sql, (TelegramID, Username, Passwords,
                         CircularPod, LearningPod, CollabBooths,
                         LearningRoom, RecordingRoom))
    # Commit change in the database
    db.commit()
except:
    print("The following query has failed")
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
