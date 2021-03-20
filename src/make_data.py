import requests
import zipfile

def _download_data(data_fn='raw_data'):
    '''Download data from Kaggle'''
    # Request the file 
    #url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00270/driftdataset.zip'
    # Unzip the file
    #r = requests.get(url, allow_redirects=True)
    #open('data/raw/{}.zip'.format(data_fn), 'wb').write(r.content)

def _unzip_data(data_fn='raw_data'):

    #with zipfile.ZipFile('data/raw/{}.zip'.format(data_fn), 'r') as zipObj:
        #zipObj.extractall('data/raw/')
    pass

def make_data(data_fn):
    pass
    
