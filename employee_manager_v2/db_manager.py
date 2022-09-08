import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="nero",
    database="employee_management"
)

cur = db.cursor()

def init_database():
    create_companies_table = 'CREATE TABLE Companies (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL)'
    create_locations_table = 'CREATE TABLE Locations (company INT, FOREIGN KEY (company) REFERENCES Companies(id), name VARCHAR(15) NOT NULL, street VARCHAR(50), city VARCHAR(20), state VARCHAR(2), zip VARCHAR(5), phone VARCHAR(14))'
    create_employees_table = 'CREATE TABLE Employees (id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(15) NOT NULL, last_name VARCHAR(15) NOT NULL, nick_name VARCHAR(15), company INT NOT NULL, FOREIGN KEY (company) REFERENCES Companies(id), location VARCHAR(15) NOT NULL)'
    create_skills_table = 'CREATE TABLE Skills (employee INT NOT NULL, FOREIGN KEY (employee) REFERENCES Employees(id), skill VARCHAR(15) NOT NULL, rating TINYINT NOT NULL)'
    create_availability_table = 'CREATE TABLE Availability (employee INT NOT NULL, FOREIGN KEY (employee) REFERENCES Employees(id), m_start TINYINT NOT NULL, m_end TINYINT NOT NULL, t_start TINYINT NOT NULL, t_end TINYINT NOT NULL, w_start TINYINT NOT NULL, w_end TINYINT NOT NULL,  th_start TINYINT NOT NULL, th_end TINYINT NOT NULL,  f_start TINYINT NOT NULL, f_end TINYINT NOT NULL,  sat_start TINYINT NOT NULL, sat_end TINYINT NOT NULL,  sun_start TINYINT NOT NULL, sun_end TINYINT NOT NULL)'
    cur.execute(create_companies_table)
    cur.execute(create_locations_table)
    cur.execute(create_employees_table)
    cur.execute(create_availability_table)
    cur.execute(create_skills_table)

def create_company(name):
    cur.execute(f'INSERT INTO Companies (name) VALUES ("{name}")')
    return cur.lastrowid

def create_employee(first_name, last_name, company_id, location, nick_name=None):
    cur.execute(f'INSERT INTO Employees (first_name, last_name, nick_name, company, location) VALUES ("{first_name}", "{last_name}", "{nick_name}", {company_id}, "{location}")')
    return cur.lastrowid

def save_db():
    db.commit()

if __name__ == '__main__':
    # init_database()
    create_employee("1234", "Brown", 3, "Cincinatti")
    create_employee("2345", "Brown", 3, "Cincinatti")
    create_employee("3456", "Brown", 3, "Cincinatti")
    create_employee("4567", "Brown", 3, "Cincinatti")
    save_db()