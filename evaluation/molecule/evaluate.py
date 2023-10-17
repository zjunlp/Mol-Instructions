import pandas as pd
import selfies as sf
from rdkit import Chem
from sklearn.metrics import mean_absolute_error

def sf_encode(selfies):
    try:
        smiles = sf.decoder(selfies)
        return smiles
    except Exception:
        return None

def convert_to_canonical_smiles(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is not None:
        canonical_smiles = Chem.MolToSmiles(molecule, isomericSmiles=False, canonical=True)
        return canonical_smiles
    else:
        return None
    
def metrics(input_path, output_path, task):
    data = pd.read_table(input_path, sep='\t', on_bad_lines='skip')
    all_data = data.shape[0]
    
    if task == 'property_pred':
        data['output'] = data['output'].astype(str).str.extract(r'(-?\d+\.?\d*)\s*</s>')

        data.dropna(axis=0, how='any', inplace=True)
        data['output'] = pd.to_numeric(data['output'])
        data['ground_truth'] = pd.to_numeric(data['ground_truth'])

        data.dropna(axis=0, how='any', inplace=True)
        
        mae = mean_absolute_error(data['ground_truth'], data['output'])
        print(mae)
        data.to_csv(output_path, index=None, sep='\t', header=True)

    elif task == 'mol_gen':
        data.dropna(axis=0, how='any', inplace=True)
        data['output'] = data['output'].apply(lambda x: x.rsplit(']', 1)[0] + ']' if isinstance(x, str) else x)

        data['output_smiles'] = data['output'].map(sf_encode)
        data.dropna(axis=0, how='any', inplace=True)
        data['output_smiles'] = data['output_smiles'].map(convert_to_canonical_smiles)
        data.dropna(axis=0, how='any', inplace=True)
        data['ground truth'] = data['ground_truth']
        data['ground smiles'] = data['ground_truth'].map(sf_encode)
        data['ground smiles'] = data['ground smiles'].map(convert_to_canonical_smiles)
        data.dropna(axis=0, how='any', inplace=True)
        data.to_csv(output_path, index=None, sep='\t')
        
    else:
        data.dropna(axis=0, how='any', inplace=True)

        data['SELFIES'] = data['description']
        data['SMILES_org'] = data['description'].map(sf_encode)
        data['SMILES'] = data['SMILES_org'].map(convert_to_canonical_smiles)

        data['output'] = data['output'].apply(lambda x: x.rsplit('.', 1)[0] + '.' if isinstance(x, str) else x)
        # data['output'] = data['output'].str.rsplit('.', 1).str[0] + '.'
        data['ground truth'] = data['ground_truth']
        data.dropna(axis=0, how='any', inplace=True)
        data[['SMILES', 'SELFIES', 'ground truth', 'output']].to_csv(output_path, index=None, sep='\t')

        
if __name__ == '__main__':
    input_path = 'property.txt'
    output_path = 'pre_property.txt'
    task = 'property_pred'
    metrics(input_path, output_path, task)