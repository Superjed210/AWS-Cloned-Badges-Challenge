import pandas as pd

json_path = 'output_file.json'


def cloned_user(path):

    df = pd.read_json(path, lines=True)
    df = df.sort_values(by=['user_id', 'timestamp'])

    location_counts = df.groupby('user_id')['location_id'].nunique()
    multi_location_users = (location_counts[location_counts > 1].index).tolist()

    df_multi = df[df['user_id'].isin(multi_location_users)]
    df_multi['time_diff'] = df_multi.groupby('user_id')['timestamp'].diff()

    df_multi['clone'] = (
    (df_multi['time_diff'] < pd.Timedelta(hours=4)) &
    (df_multi['location_id'] != df_multi.groupby('user_id')['location_id'].shift()))

    cloned_users = df_multi[df_multi['clone']]['user_id'].unique()
    return cloned_users




print(cloned_user(json_path))