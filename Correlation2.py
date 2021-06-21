import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):

    student_marks = []
    days_present = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            student_marks.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))
    return {
        'x': student_marks,
        'y': days_present
    }  
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Correlation is ', correlation[0,1])

def setup():
    data_path = 'Student Marks vs Days Present.csv'
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setup()