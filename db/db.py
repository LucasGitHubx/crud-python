import mysql.connector

class DB():
    def __init__(self):
        self.conn = mysql.connector.Connect(
        host="localhost",
        user="root",
        password="55829536",
        db="universidad"
        )
    
    def select(self):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM courses"
            cursor.execute(sql)
            results = cursor.fetchall()

            print("\nThe results will be displayed in the following manner: id-name-capacity-creation_of_the_course")
            for x in results:
                result = "{0} - {1} - {2} - {3}"
                print(result.format(x[0], x[1], x[2], x[3]))
        
        except Exception as e:
            print(e)
    

    def insert(self, name, capacity, creation):
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO courses(name, capacity, creation_date) VALUES(%s, %s, %s)"
            cursor.execute(sql, (name, capacity, creation))
            self.conn.commit()

        except Exception as e:
            print(e)
    

    def update(self, id, name, capacity, creation):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id FROM courses")
            ids = []

            for x in cursor:
                ids.append(x[0])
            
            if id in ids:
                sql = """UPDATE courses 
                     SET name=%s,
                         capacity=%s,
                         creation_date=%s
                     WHERE id=%s"""

                cursor.execute(sql, (name, capacity, creation, id))
                self.conn.commit()

            else:
                print("The id that you gave doesn't exist.")

        except Exception as e:
            print(e)


    def delete(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id FROM courses")
            ids = []

            for x in cursor:
                ids.append(x[0])
            
            if id in ids:
                sql = "DELETE FROM courses WHERE id={0}".format(id)

                cursor.execute(sql, (id))
                self.conn.commit()

            else:
                print("The id that you gave doesn't exist.")

        except Exception as e:
            print(e)
