import requests
import pandas as pd
from bs4 import BeautifulSoup

def la_liga_stats():
    url = "https://fbref.com/es/comps/12/Estadisticas-de-La-Liga"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    table = soup.select('table.stats_table')[1]
    table_data = []

    # Loop through the rows of the table
    for row in table.find_all("tr"):
        # Create a list to hold the row data
        row_data = []
        # Loop through the cells of the row
        for cell in row.find_all("td"):
            # Add the cell data to the row data list
            row_data.append(cell.text.strip())
        # Add the row data to the table data list
        table_data.append(row_data)

    # Create a pandas DataFrame from the table data
    df = pd.DataFrame(table_data)

    header=[ "equipo","PJh","PGh","PEh","PPh","GFh","GCh","DGh","Ptsh","Pts/PJh","xGh","xGAh","xGDh","xGD/90h","PJv","PGv","PEv","PPv","GFv","GCv","DGv","Ptsv","Pts/PJv","xGv","xGAv","xGDv","xGD/90v"]

    df.columns = header
    df = df.dropna()

    return df

    
def premier_stats():
    url = "https://fbref.com/es/comps/9/Estadisticas-de-Premier-League"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    table = soup.select('table.stats_table')[1]
    table_data = []

    # Loop through the rows of the table
    for row in table.find_all("tr"):
        # Create a list to hold the row data
        row_data = []
        # Loop through the cells of the row
        for cell in row.find_all("td"):
            # Add the cell data to the row data list
            row_data.append(cell.text.strip())
        # Add the row data to the table data list
        table_data.append(row_data)

    # Create a pandas DataFrame from the table data
    df = pd.DataFrame(table_data)

    header=[ "equipo","PJh","PGh","PEh","PPh","GFh","GCh","DGh","Ptsh","Pts/PJh","xGh","xGAh","xGDh","xGD/90h","PJv","PGv","PEv","PPv","GFv","GCv","DGv","Ptsv","Pts/PJv","xGv","xGAv","xGDv","xGD/90v"]

    df.columns = header
    df = df.dropna()

    return df




def ligue1_stats():
    url = "https://fbref.com/es/comps/13/Estadisticas-de-Ligue-1"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    table = soup.select('table.stats_table')[1]
    table_data = []

    # Loop through the rows of the table
    for row in table.find_all("tr"):
        # Create a list to hold the row data
        row_data = []
        # Loop through the cells of the row
        for cell in row.find_all("td"):
            # Add the cell data to the row data list
            row_data.append(cell.text.strip())
        # Add the row data to the table data list
        table_data.append(row_data)

    # Create a pandas DataFrame from the table data
    df = pd.DataFrame(table_data)

    header=[ "equipo","PJh","PGh","PEh","PPh","GFh","GCh","DGh","Ptsh","Pts/PJh","xGh","xGAh","xGDh","xGD/90h","PJv","PGv","PEv","PPv","GFv","GCv","DGv","Ptsv","Pts/PJv","xGv","xGAv","xGDv","xGD/90v"]

    df.columns = header
    df = df.dropna()

    return df

def bundes_stats():
    url = "https://fbref.com/es/comps/20/Estadisticas-de-Bundesliga"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    table = soup.select('table.stats_table')[1]
    table_data = []

    # Loop through the rows of the table
    for row in table.find_all("tr"):
        # Create a list to hold the row data
        row_data = []
        # Loop through the cells of the row
        for cell in row.find_all("td"):
            # Add the cell data to the row data list
            row_data.append(cell.text.strip())
        # Add the row data to the table data list
        table_data.append(row_data)

    # Create a pandas DataFrame from the table data
    df = pd.DataFrame(table_data)

    header=[ "equipo","PJh","PGh","PEh","PPh","GFh","GCh","DGh","Ptsh","Pts/PJh","xGh","xGAh","xGDh","xGD/90h","PJv","PGv","PEv","PPv","GFv","GCv","DGv","Ptsv","Pts/PJv","xGv","xGAv","xGDv","xGD/90v"]

    df.columns = header
    df = df.dropna()

    return df



def eredivisie_stats():
    url = "https://fbref.com/es/comps/23/Estadisticas-de-Eredivisie"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    table = soup.select('table.stats_table')[1]
    table_data = []

    # Loop through the rows of the table
    for row in table.find_all("tr"):
        # Create a list to hold the row data
        row_data = []
        # Loop through the cells of the row
        for cell in row.find_all("td"):
            # Add the cell data to the row data list
            row_data.append(cell.text.strip())
        # Add the row data to the table data list
        table_data.append(row_data)

    # Create a pandas DataFrame from the table data
    df = pd.DataFrame(table_data)

    header=[ "equipo","PJh","PGh","PEh","PPh","GFh","GCh","DGh","Ptsh","Pts/PJh","xGh","xGAh","xGDh","xGD/90h","PJv","PGv","PEv","PPv","GFv","GCv","DGv","Ptsv","Pts/PJv","xGv","xGAv","xGDv","xGD/90v"]

    df.columns = header
    df = df.dropna()

    return df


def serieA_stats():
    url = "https://fbref.com/es/comps/11/Estadisticas-de-Serie-A"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    table = soup.select('table.stats_table')[1]
    table_data = []

    # Loop through the rows of the table
    for row in table.find_all("tr"):
        # Create a list to hold the row data
        row_data = []
        # Loop through the cells of the row
        for cell in row.find_all("td"):
            # Add the cell data to the row data list
            row_data.append(cell.text.strip())
        # Add the row data to the table data list
        table_data.append(row_data)

    # Create a pandas DataFrame from the table data
    df = pd.DataFrame(table_data)

    header=[ "equipo","PJh","PGh","PEh","PPh","GFh","GCh","DGh","Ptsh","Pts/PJh","xGh","xGAh","xGDh","xGD/90h","PJv","PGv","PEv","PPv","GFv","GCv","DGv","Ptsv","Pts/PJv","xGv","xGAv","xGDv","xGD/90v"]

    df.columns = header
    df = df.dropna()

    return df