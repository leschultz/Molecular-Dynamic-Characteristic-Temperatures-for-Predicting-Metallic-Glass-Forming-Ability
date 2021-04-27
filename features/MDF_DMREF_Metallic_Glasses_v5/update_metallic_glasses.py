from mdf_connect_client import MDFConnectClient
import pandas as pd
import os


if __name__ == '__main__':

    # Location information for raw data
    parent = '../features'
    df = 'MDF_DMREF_Metallic_Glasses_v5.csv'
    title = 'Metallic Glasses and their Properties'
    authors = [
               'Voyles, Paul M.',
               'Schultz, Lane E.',
               'Morgan, Dane',
               'Carter, Francis'
               ]

    # URL for upload
    url = (
           'https://app.globus.org/file-manager?'
           'origin_id=82f1b5c6-6e9b-11e5-ba47-22'
           '000b92c6ec&origin_path=%2Fmdf_open%2'
           'Fvoyles_mdf_dmref_glasses_v1.3%2FMDF'
           '_DMREF_Metallic_Glasses%2F'
           )
    

    # Create paths
    df = os.path.join(parent, df)

    # Load Data
    df = pd.read_csv(df)

    # Upload
    mdfcc = MDFConnectClient()
    mdfcc.create_dc_block(title=title, authors=authors)
    mdfcc.add_data_source(url)
    mdfcc.add_service('mdf_publish')
    mdfcc.set_test(True)
    print(mdfcc.get_submission())

