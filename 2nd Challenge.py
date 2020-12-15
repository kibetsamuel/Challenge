import pandas as pd

def get_functional_water_pts(url):
    df = pd.read_json(url)
    pts_comm = {}
    comm_rank = []

   
    number_functional = df['water_point_condition'].value_counts()['functioning']
    
    water_pts_comm = df['communities_villages'].value_counts()
    for k,v in water_pts_comm.items():
        pts_comm[k] = v
    number_water_points = pts_comm
    
    broken_df = df[df['water_point_condition'] == 'broken']
    count_broken = broken_df.groupby('communities_villages').count()['water_point_condition']/len(df) * 100
    count_broken = count_broken.sort_values(ascending=False)


    for k,v in count_broken.items():
        comm_rank.append(k)
    
    
    
    output = {
        'number_functional': number_functional,
        'number_water_points': number_water_points,
        'community_ranking': comm_rank
    }
    
    return output
print(get_functional_water_pts('https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json'))