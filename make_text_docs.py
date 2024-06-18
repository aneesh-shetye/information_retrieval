import os 
from get_dataset import get_dataframe
from utils import get_text

if __name__ == "__main__": 

    df_proce = get_dataframe()
    df = df_proce[:100].copy()

    output_folder = 'text_docs'
    #os.makedirs(output_folder, exist_ok=True)

    indices_to_skip = []
    for index, row in df.iterrows():
        url = row['url']
        text = get_text(url)

        if text is not None:
            file_name = os.path.join(output_folder, f'{index}.txt')
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(text)
        else:
            indices_to_skip.append(index)

    df.drop(indices_to_skip, inplace=True)

    print(f'Text saved in folder: {output_folder}')
    print(f'Skipped {len(indices_to_skip)} indices')
    print(f'New dataframe length: {len(df)}')


