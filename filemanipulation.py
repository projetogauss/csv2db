from connection import Connectionpg

con = Connectionpg.createconnection()
cursor = con.cursor()

sql_statement = """INSERT INTO TAB_CAD (DATA, VALOR) VALUES (%s,%s)"""

list_rows = []

def main():
    try:
        with open('datasets/champagne_sales.csv','r') as file:
            for line in file.readlines():
                striped_line = line.strip()
                spliped_line = striped_line.split(',')
                list_rows.append(spliped_line)
            for row in list_rows[1:]:
                records = (row[0],row[1])
                cursor.execute(sql_statement, records)
                print('Inserindo registro: {} e {}'.format(row[0],row[1]))
            con.commit()
            cursor.close()
            con.close()
    except FileNotFoundError as error:
        print(error)


if __name__ == '__main__':
    main()
    