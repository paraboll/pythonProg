from ParseCSV import ParseCSV

filepath = r'C:/******/TB_burden_countries_2020-07-29.csv'
db_string = "postgresql://postgres:admin@localhost:5432/Test"
myClass = ParseCSV(filepath, db_string)
data = myClass.CSVtoTable(filepath)
myClass.TableToDB(data, db_string)
res = myClass.DBtoConsole(db_string)
myClass.printDB(res)