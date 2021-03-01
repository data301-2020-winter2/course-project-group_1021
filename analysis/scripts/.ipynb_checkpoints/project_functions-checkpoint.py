import pandas as pd
def load_and_process(url_or_path_to_csv_file):
    
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"age":"Age"})
        .rename(columns={"sex":"Sex"})
        .rename(columns={"bmi":"BMI"})
        .rename(columns={"children":"Number of Children"})
        .rename(columns={"smoker":"Smoker"})
        .rename(columns={"region":"Place of Residence"})
        .rename(columns={"charges":"Medical Insurance Charges"})
        .style.set_properties(**{'text-align': 'right'})



        
    )
    
    return df
    
    