import csv

def sortCSVFile(inputFileName, outputFileName, sortColumn=0):
    with open(inputFileName, 'r') as inputFile:
        inputFileReader = csv.reader(inputFile)
        header = next(inputFileReader)
        
        sortedRows = sorted(inputFileReader, key=lambda row: row[sortColumn])

        with open(outputFileName, 'w', newline='') as outputFile:
            outputFileWriter = csv.writer(outputFile)
            outputFileWriter.writerow(header)
            outputFileWriter.writerows(sortedRows)

def main():
    inputFileName = "grades.csv"
    outputFileName = "sortedgrades.csv"

    sortColumn = 0
    sortCSVFile(inputFileName, outputFileName, sortColumn)

if __name__ == "__main__":
    main()
