import pandas as pd

def pass_data(sell_df):
    #see all the data for no good reason
    print(sell_df)

    #get the mean price of a specific item across all stores
    item_id_mean_price = sell_df.groupby(['item_id']).mean()
    print(item_id_mean_price['sell_price'])

    #get the standard deviation of the item
    item_id_std_price = sell_df.groupby(['item_id']).std()
    print(item_id_std_price['sell_price'])

    #normalize the deviation by the sales price to put it into percentages
    item_id_norm_price_change = item_id_std_price['sell_price'] / item_id_mean_price['sell_price'] * 100
    print(item_id_norm_price_change)