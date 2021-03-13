import pandas as pd
def load(url_or_path_to_csv_file):
    
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"age":"Age"})
        .rename(columns={"sex":"Sex"})
        .rename(columns={"bmi":"BMI"})
        .rename(columns={"children":"Number of Children"})
        .rename(columns={"smoker":"Smoker"})
        .rename(columns={"region":"Place of Residence"})
        .rename(columns={"charges":"Medical Insurance Charges"})
        
    )
    
    return df

def male_only(url_or_path_to_csv_file):
    
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"age":"Age"})
        .rename(columns={"sex":"Sex"})
        .rename(columns={"bmi":"BMI"})
        .rename(columns={"children":"Number of Children"})
        .rename(columns={"smoker":"Smoker"})
        .rename(columns={"region":"Place of Residence"})
        .rename(columns={"charges":"Medical Insurance Charges"}) 
    )
        
    df2 = (
        df
        .drop(df[df.Sex == "female"].index)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2

def female_only(url_or_path_to_csv_file):
    
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"age":"Age"})
        .rename(columns={"sex":"Sex"})
        .rename(columns={"bmi":"BMI"})
        .rename(columns={"children":"Number of Children"})
        .rename(columns={"smoker":"Smoker"})
        .rename(columns={"region":"Place of Residence"})
        .rename(columns={"charges":"Medical Insurance Charges"}) 
    )
        
    df2 = (
        df
        .drop(df[df.Sex == "male"].index)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2

def smokers_only(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"age":"Age"})
        .rename(columns={"sex":"Sex"})
        .rename(columns={"bmi":"BMI"})
        .rename(columns={"children":"Number of Children"})
        .rename(columns={"smoker":"Smoker"})
        .rename(columns={"region":"Place of Residence"})
        .rename(columns={"charges":"Medical Insurance Charges"}) 
    )
        
    df2 = (
        df
        .drop(df[df.Smoker == "no"].index)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2