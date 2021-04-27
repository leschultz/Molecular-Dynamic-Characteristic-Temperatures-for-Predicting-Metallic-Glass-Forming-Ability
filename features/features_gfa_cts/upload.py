from foundry import Foundry
import pandas as pd
import json
import os


if __name__ == '__main__':

    # Location information for raw data
    parent = '.'
    df = 'features_gfa_cts.csv'

    metadata = {}
    metadata['inputs'] = ['tg', 'tprime', 'taprime', 'tprimeextrap', 'tstar', 'ta', 'tstarextrap', 'tl']
    metadata['input_descriptions'] = []
    metadata['input_units'] = ['K']*len(metadata['inputs'])
    metadata['outputs'] = ['gfa']
    metadata['output_descriptions'] = ['Glass forming ability']
    metadata['output_units'] = []
    metadata['output_labels'] = ['good', 'poor']

    # Full title of dataset
    title = 'Molecular Dynamic Characteristic Temperatures Classes'

    # Authors list
    authors = [
               'Schultz, Lane E.',
               'Afflerbach, Benjamin',
               'Szlufarska, Izabela',
               'Morgan, Dane',
               ]

    # Shorthand title (optional)
    short_name = 'gfa_classification_original'

    # URL for upload
    data_source = (
                   'https://app.globus.org/file-manager?origin_id'
                   '=962e4716-a384-11eb-8a92-d70d98a40c8d&origin_'
                   'path=%2FC%2FUsers%2FNerve%2FDocuments%2Flmp_cts'
                   '_data_upload%2Fmdf%2Ffeatures%2Ffeatures_gfa_cts%2F'
                   )

    # Create paths
    df = os.path.join(parent, df)

    # Load Data
    df = pd.read_csv(df)
    print(df)

    # Convert to json
    df = df.to_json(orient='index')
    parsed = json.loads(df)

    with open('features_gfa_cts.json', 'w') as outfile:
        json.dump(parsed, outfile, indent=4)

    # Upload
    f = Foundry(no_browser=True, no_local_server=True)
    res = f.publish(
                    metadata,
                    data_source,
                    title,
                    authors,
                    short_name=short_name
                    )
    print(res)
