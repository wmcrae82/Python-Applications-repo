from flask import *
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/majors_add')
def majors_add():
    return render_template('majors_add.html')


@app.route("/save_major", methods=["POST", "GET"])
def save_major():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["Name"]
            with sqlite3.connect('student_info.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Majors (Name) VALUES (?)", (name,))
                conn.commit()
                msg = "Major added Successfully"
        except sqlite3.Error:
            conn.rollback()
            msg = "We can not add this major"
        finally:
            conn.close()
            return render_template('save_major.html', msg=msg)


@app.route('/majors_search')
def majors_search():
    return render_template('majors_search.html')


@app.route('/search_majors_record', methods=["POST"])
def search_majors_record():
    id = request.form["id"]
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM Majors WHERE MajorID == ?', (id,))
    row = cur.fetchone()
    conn.close()
    return render_template('search_majors_record.html', row=row)


@app.route('/majors_update')
def majors_update():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Majors''')
    rows = cur.fetchall()
    conn.close()
    return render_template('majors_update.html', rows=rows)


@app.route("/save_majors_update", methods=["POST", "GET"])
def save_majors_update():
    msg = "msg"
    if request.method == "POST":
        try:
            id = request.form["id"]
            name = request.form["Name"]
            with sqlite3.connect('student_info.db') as conn:
                cur = conn.cursor()
                cur.execute('''UPDATE Majors 
                                SET Name = ?
                                WHERE MajorID == ?''', (name, id))
                conn.commit()
                msg = "Major Updated Successfully"
        except sqlite3.Error:
            conn.rollback()
            msg = "We can not update this major"
        finally:
            conn.close()
            return render_template('save_majors_update.html', msg=msg)


@app.route('/majors_delete')
def majors_delete():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Majors''')
    rows = cur.fetchall()
    conn.close()
    return render_template('majors_delete.html', rows=rows)


@app.route('/delete_majors_record', methods=["POST"])
def delete_majors_record():
    id = request.form["id"]
    with sqlite3.connect('student_info.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM Majors WHERE MajorID == ?', (id,))
            msg = 'Record successfully deleted'
        except sqlite3.Error:
            msg = 'Record can not be deleted'
        finally:
            conn.close()
            return render_template('delete_majors_record.html', msg=msg)


@app.route('/majors_view')
def majors_view():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Majors''')
    rows = cur.fetchall()
    conn.close()
    return render_template('majors_view.html', rows=rows)


@app.route('/dept_add')
def dept_add():
    return render_template('dept_add.html')


@app.route('/save_dept', methods=["POST", "GET"])
def save_dept():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["Name"]
            with sqlite3.connect('student_info.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO Departments (Name) VALUES (?)", (name,))
                conn.commit()
                msg = "Department added Successfully"
        except sqlite3.Error:
            conn.rollback()
            msg = "We can not add this department"
        finally:
            conn.close()
            return render_template('save_dept.html', msg=msg)


@app.route('/dept_search')
def dept_search():
    return render_template('dept_search.html')


@app.route('/search_dept_record', methods=["POST"])
def search_dept_record():
    id = request.form["id"]
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM Departments WHERE DeptID == ?', (id,))
    row = cur.fetchone()
    conn.close()
    return render_template('search_dept_record.html', row=row)


@app.route('/dept_update')
def dept_update():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Departments''')
    rows = cur.fetchall()
    conn.close()
    return render_template('dept_update.html', rows=rows)


@app.route("/save_dept_update", methods=["POST", "GET"])
def save_dept_update():
    msg = "msg"
    if request.method == "POST":
        try:
            id = request.form["id"]
            name = request.form["Name"]
            with sqlite3.connect('student_info.db') as conn:
                cur = conn.cursor()
                cur.execute('''UPDATE Departments 
                                SET Name = ?
                                WHERE DeptID == ?''', (name, id))
                conn.commit()
                msg = "Department Updated Successfully"
        except sqlite3.Error:
            conn.rollback()
            msg = "We can not update this department"
        finally:
            conn.close()
            return render_template('save_dept_update.html', msg=msg)


@app.route('/dept_delete')
def dept_delete():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Departments''')
    rows = cur.fetchall()
    conn.close()
    return render_template('dept_delete.html', rows=rows)


@app.route('/delete_dept_record', methods=["POST"])
def delete_dept_record():
    id = request.form["id"]
    with sqlite3.connect('student_info.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM Departments WHERE DeptID == ?', (id,))
            msg = 'Record successfully deleted'
        except sqlite3.Error:
            msg = 'Record can not be deleted'
        finally:
            conn.close()
            return render_template('delete_dept_record.html', msg=msg)


@app.route('/dept_view')
def dept_view():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Departments''')
    rows = cur.fetchall()
    conn.close()
    return render_template('dept_view.html', rows=rows)


@app.route('/student_add')
def student_add():
    return render_template('student_add.html')


@app.route('/save_student', methods=["POST", "GET"])
def save_student():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["Name"]
            major = request.form["MajorID"]
            dept = request.form["DeptID"]
            with sqlite3.connect('student_info.db') as conn:
                cur = conn.cursor()
                cur.execute('''INSERT INTO Students (Name, MajorID, DeptID) VALUES (?,?,?)''',
                            (name, major, dept,))
                conn.commit()
                msg = "Student added Successfully"
        except sqlite3.Error:
            conn.rollback()
            msg = "We can not add this student"
        finally:
            conn.close()
            return render_template('save_student.html', msg=msg)


@app.route('/student_search')
def student_search():
    return render_template('student_search.html')


@app.route('/search_student_record', methods=["POST"])
def search_student_record():
    id = request.form["id"]
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys=ON')
    cur.execute('''SELECT 
                        Students.StudentId,
                        Students.Name,
                        Majors.Name,
                        Departments.Name
                    FROM
                        Students, Majors, Departments
                    WHERE
                        Students.StudentID == ? AND
                        Students.MajorID == Majors.MajorID AND
                        Students.DeptID == Departments.DeptID''', (id,))

    row = cur.fetchone()
    conn.close()
    return render_template('search_student_record.html', row=row)


@app.route('/student_update')
def student_update():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Students''')
    rows = cur.fetchall()
    conn.close()
    return render_template('student_update.html', rows=rows)


@app.route("/save_student_update", methods=["POST", "GET"])
def save_student_update():
    msg = "msg"
    if request.method == "POST":
        try:
            id = request.form["id"]
            name = request.form["Name"]
            major_id = request.form["MajorID"]
            dept_id = request.form["DeptID"]
            with sqlite3.connect('student_info.db') as conn:
                cur = conn.cursor()
                cur.execute('''UPDATE Students 
                                SET Name = ?,
                                    MajorId = ?,
                                    DeptID = ?
                                WHERE StudentID == ?''', (name, major_id, dept_id, id))
                conn.commit()
                msg = "Student Updated Successfully"
        except sqlite3.Error:
            conn.rollback()
            msg = "We can not update this student"
        finally:
            conn.close()
            return render_template('save_student_update.html', msg=msg)


@app.route('/student_delete')
def student_delete():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''SELECT 
                        Students.StudentId,
                        Students.Name,
                        Majors.Name,
                        Departments.Name
                    FROM
                        Students, Majors, Departments
                    WHERE
                        Students.MajorID == Majors.MajorID AND
                        Students.DeptID == Departments.DeptID''')

    rows = cur.fetchall()
    conn.close()
    return render_template('student_delete.html', rows=rows)


@app.route('/delete_student_record', methods=["POST"])
def delete_student_record():
    id = request.form["id"]
    with sqlite3.connect('student_info.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM Students WHERE StudentID == ?', (id,))
            msg = 'Record successfully deleted'
        except sqlite3.Error:
            msg = 'Record can not be deleted'
        finally:
            conn.close()
            return render_template('delete_student_record.html', msg=msg)


@app.route('/student_view')
def student_view():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('PRAGMA foreign_keys=ON')
    cur.execute('''SELECT 
                        Students.StudentId,
                        Students.Name,
                        Majors.Name,
                        Departments.Name
                    FROM
                        Students, Majors, Departments
                    WHERE
                        Students.MajorID == Majors.MajorID AND
                        Students.DeptID == Departments.DeptID''')

    rows = cur.fetchall()
    conn.close()
    return render_template('student_view.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)

