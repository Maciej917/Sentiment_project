import csv


class CSV_manipulation(object):
    def __init__(self, csv_file_name):
        self.csv_file = csv_file_name

    def read_csv(self, object_number_in_file=0):
        """ Metoda odczytująca plik 'csv_file'. 'object_numner_in_file' służy do wyboru listy z pliku jeżeli jest ich tam więcej """
        csv_list = []
        with open(self.csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            for x in csv_reader:
                csv_list.append(x)
        return csv_list[object_number_in_file]


    def write_csv(self, input):
        """Metoda zapisująca 'input' do 'csv_file' """
        with open(self.csv_file, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ',')
            csv_writer.writerow(input)

