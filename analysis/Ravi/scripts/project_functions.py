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
        .replace(to_replace='southwest',value='S.W.')
        .replace(to_replace='northwest',value='N.W.')
        .replace(to_replace='southeast',value='S.E.')
        .replace(to_replace='northeast',value='N.E.')
        .replace(to_replace='male',value='Male')
        .replace(to_replace='female',value='Female')
        .replace(to_replace='yes',value='Yes')
        .replace(to_replace='no',value='No')
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

def top50(url_or_path_to_csv_file):
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
        .sort_values(['Medical Insurance Charges'], ascending = False) 
        .head(50)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2

def top10(url_or_path_to_csv_file):
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
        .sort_values(['Medical Insurance Charges'], ascending = False) 
        .head(10)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2

def bot50(url_or_path_to_csv_file):
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
        .sort_values(['Medical Insurance Charges'], ascending = True) 
        .head(50)
        .reset_index()
        .drop(['index'], axis=1)
    )
    return df2

def bot10(url_or_path_to_csv_file):
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
        .sort_values(['Medical Insurance Charges'], ascending = True) 
        .head(10)
        .reset_index()
        .drop(['index'], axis=1)
    )
    return df2

def top30male(url_or_path_to_csv_file):
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
        .sort_values(['Medical Insurance Charges'], ascending = False) 
        .drop(df[df.Sex == "female"].index)
        .head(30)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2
def top30female(url_or_path_to_csv_file):
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
        .sort_values(['Medical Insurance Charges'], ascending = False) 
        .drop(df[df.Sex == "male"].index)
        .head(30)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2

def bot30male(url_or_path_to_csv_file):
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
        .sort_values(['Medical Insurance Charges'], ascending = True) 
        .drop(df[df.Sex == "female"].index)
        .head(30)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2

def bot30female(url_or_path_to_csv_file):
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
        .sort_values(['Medical Insurance Charges'], ascending = True) 
        .drop(df[df.Sex == "male"].index)
        .head(30)
        .reset_index()
        .drop(['index'], axis=1)
    )
    
    return df2

def theory_highest(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"age":"Age"})
        .rename(columns={"sex":"Sex"})
        .rename(columns={"bmi":"BMI"})
        .rename(columns={"smoker":"Smoker"})
        .rename(columns={"charges":"Medical Insurance Charges"}) 
    )
        
    df2 = (
        df
        .loc[(df['Sex']=='male') & 
            (df['Age']<=55) &
            (df['children']<=2) &
            (df['Smoker']=='yes') &
            (df['region']=="southeast") &
            (df['BMI']>=30)]
        .reset_index()
        .drop(['index'], axis=1)
        .rename(columns={"children":"Number of Children"})
        .rename(columns={"region":"Place of Residence"})
    )
    
    return df2

def theory_lowest(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"age":"Age"})
        .rename(columns={"sex":"Sex"})
        .rename(columns={"bmi":"BMI"})
        .rename(columns={"smoker":"Smoker"})
        .rename(columns={"charges":"Medical Insurance Charges"}) 
    )
    

        
    df2 = (
        df
        .loc[(df['Sex']=='female') & 
            (df['Age']<=25) &
            (df['children']>2) &
            (df['Smoker']=='no') &
            (df['region']=="southwest") &
            (df['BMI']<=25)]
        .reset_index()
        .drop(['index'], axis=1)
        .rename(columns={"children":"Number of Children"})
        .rename(columns={"region":"Place of Residence"})
    )
    
    return df2