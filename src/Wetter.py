import pandas as pd
import csv
import re
import os


class Value109:
    '''
    Diese Klasse beinhaltet eine Spalte eines .109-Wetterdatensatzes.
    
    Funktionen:
        printInfoString()
        
    
    Diese Funktion ist im Rahmen meiner Masterarbeit zum Thema 'Robust Bauen' entstanden.

    Author:
    Roman Ficht
    Version 0.1
    Datum 16.03.2022
    '''
    def __init__(self):
        self.var = 'IBEAM_M'
        self.col = 2
        self.interp = 0
        self.add = 0
        self.mult = 1
        self.samp = 0
        self.docstring = '!...to get radiation in W/m2'
        self.data = []

    def printInfoString(self):
        return f'<var>   {self.var} <col>  {self.col}  <interp> {self.interp}  <add>  {self.add}  <mult>  {self.mult}  <samp>   {self.samp}'

    def __repr__(self):
        return f'109-Variable <{self.var}>'
    def __call__(self):
        return self.data

class weather109:
    '''
    
    Diese Klasse kann Wetterdatensätze vom Dateiformat .109 einlesen, bearbeiten und exportieren
    
    Funktionen:

        read_file(path):
            Liest eine .109-Wetterdatei ein und 
    
    Diese Funktion ist im Rahmen meiner Masterarbeit zum Thema 'Robust Bauen' entstanden.

    Author:
    Roman Ficht
    Version 0.1
    Datum 16.03.2022

    '''
    def __init__(self):
        self.name = 'WeatherFile'
        self.userdefined = ''
        self.longitude = 0 # east of greenwich: negative; (shift for use of TYPE 16: -2.50   )
        self.latitude = 0
        self.gmt = 0 # time shift from GMT, east: positive (hours), solar = solartime
        self.interval = 1 # Data file time interval between consecutive lines
        self.firsttime = 1 # Time corresponding to first data line (hours)
        self.Variables = {}
        self.year = ''
    
    def read_file(self, path = r'C:\Users\Roman\workspace\thesis\src\wetterdaten\weatherfile_munich.109', year=2010):
        self.name = os.path.basename(path).rsplit('.',1)[0]
        self.year = year
        with open(path, mode='r', encoding='latin-1') as data:
            data = data.read().splitlines()
            lines = []
            for l, line in enumerate(data):
                if '!' in line:
                    for p, part in enumerate(line.split()):
                        if '!' in part:
                            line = line.split()[:p]
                else:
                    line = line.split()
                if len(line) > 0:
                    lines.append(line)
                    find = re.search(r'<([^\)\s]+)>', line[0])
                    if find:
                        if hasattr(self,find[1]):
                            if len(line) == 2:
                                setattr(self, find[1], line[1])
                            if len(line) == 1:
                                setattr(self, find[1], '')
                        if find[1] == 'var':
                            v = Value109()
                            for i, item in enumerate(line):
                                find2 = re.search(r'<([^\)\s]+)>', item)
                                if find2:
                                    if hasattr(v,find2[1]):
                                        setattr(v,find2[1], line[i+1])
                            self.Variables[int(v.col)] = v
                        if find[1] == 'data':
                            data = l
        data = lines[data+1:]
        data = list(map(list, zip(*data)))
        if len(data) == len(self.Variables) + 1:
            self.Period = data[0]
            for key, item in self.Variables.items():
                item.data = pd.Series(list(map(float, data[key-1])), self.Period, name=item.var)

        self.df = pd.concat([v() for col, v in self.Variables.items()],axis=1)

    def _writeheader(self): 
        data = [f'<userdefined>   {self.userdefined}', f'<longitude>   {self.longitude}',f'<latitude>   {self.latitude}',f'<gmt>   {self.gmt}',f'<interval>   {self.interval}',f'<firsttime>   {self.firsttime}']
        return data
    def _writedataheader(self):
        head = []
        for key, item in self.Variables.items():
            head.append(item.printInfoString())
        return head
    def _writedata(self):
        data = ['<data>']
        for i, row in self.df.iterrows():
            row = [i] + row.to_list()
            data.append('   '.join(map(str,row)))
        return data
    def printFile(self,dest = r'./sim/robust-inputs'):
        data = self._writeheader() + self._writedataheader() + self._writedata()
        data = '\n'.join(data)
        self.filename = os.path.join(dest, f'{self.name}.109')
        with open(self.filename, 'w+') as f:
            f.write(data)
        print(f'Wetterdatei {self.filename} wurde erfolgreich gespeichert"')

class epw():
    """A class which represents an EnergyPlus weather (epw) file
    """
    
    def __init__(self):
        """
        """
        self.headers={}
        self.df=pd.DataFrame()
            
    
    def read(self,fp):
        """Reads an epw file 
        
        Arguments:
            - fp (str): the file path of the epw file   
        
        """
        
        self.headers=self._read_headers(fp)
        self.df=self._read_data(fp)
                
        
    def _read_headers(self,fp):
        """Reads the headers of an epw file
        
        Arguments:
            - fp (str): the file path of the epw file   
            
        Return value:
            - d (dict): a dictionary containing the header rows 
            
        """
        
        d={}
        with open(fp, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                if row[0].isdigit():
                    break
                else:
                    d[row[0]]=row[1:]
        return d
    
    
    def _read_data(self,fp):
        """Reads the climate data of an epw file
        
        Arguments:
            - fp (str): the file path of the epw file   
            
        Return value:
            - df (pd.DataFrame): a DataFrame comtaining the climate data
            
        """
        
        names=['Year',
               'Month',
               'Day',
               'Hour',
               'Minute',
               'Data Source and Uncertainty Flags',
               'Dry Bulb Temperature',
               'Dew Point Temperature',
               'Relative Humidity',
               'Atmospheric Station Pressure',
               'Extraterrestrial Horizontal Radiation',
               'Extraterrestrial Direct Normal Radiation',
               'Horizontal Infrared Radiation Intensity',
               'Global Horizontal Radiation',
               'Direct Normal Radiation',
               'Diffuse Horizontal Radiation',
               'Global Horizontal Illuminance',
               'Direct Normal Illuminance',
               'Diffuse Horizontal Illuminance',
               'Zenith Luminance',
               'Wind Direction',
               'Wind Speed',
               'Total Sky Cover',
               'Opaque Sky Cover (used if Horizontal IR Intensity missing)',
               'Visibility',
               'Ceiling Height',
               'Present Weather Observation',
               'Present Weather Codes',
               'Precipitable Water',
               'Aerosol Optical Depth',
               'Snow Depth',
               'Days Since Last Snowfall',
               'Albedo',
               'Liquid Precipitation Depth',
               'Liquid Precipitation Quantity']
        
        first_row=self._first_row_with_climate_data(fp)
        df=pd.read_csv(fp,
                       skiprows=first_row,
                       header=None,
                       names=names)
        return df
        
        
    def _first_row_with_climate_data(self,fp):
        """Finds the first row with the climate data of an epw file
        
        Arguments:
            - fp (str): the file path of the epw file   
            
        Return value:
            - i (int): the row number
            
        """
        
        with open(fp, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i,row in enumerate(csvreader):
                if row[0].isdigit():
                    break
        return i
        
        
    def write(self,fp):
        """Writes an epw file 
        
        Arguments:
            - fp (str): the file path of the new epw file   
        
        """
        
        with open(fp, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for k,v in self.headers.items():
                csvwriter.writerow([k]+v)
            for row in self.dataframe.itertuples(index= False):
                csvwriter.writerow(i for i in row)