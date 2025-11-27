import pandas as pd
import json

def clone_finder():
    df = pd.read_json('output_file.json', lines=True) #.sort_values(by=["user_id", "timestamp"])
    print(df.head())

'''
    location_count = df.groupby("user_id")["location_id"].nunique()
    multi_loc_filter = location_count[location_count > 1].index
    df_multi = df[df["user_id"].isin(multi_loc_filter)]
    print(df_multi)
'''
clone_finder()