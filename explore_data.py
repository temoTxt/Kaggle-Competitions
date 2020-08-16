import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
import scipy

def pass_data(sell_df):
    #see all the data for no good reason
    print(sell_df)

    item_id_stats = pd.DataFrame()
    #get the mean price of a specific item across all stores
    item_id_stats['mean'] = sell_df.groupby(['item_id'])['sell_price'].mean()
    print(item_id_stats['mean'])

    #get the standard deviation of the item
    item_id_stats['std'] = sell_df.groupby(['item_id'])['sell_price'].std()
    print(item_id_stats['std'])

    #normalize the deviation by the sales price to put it into percentages
    item_id_stats['norm_change'] = item_id_stats['std'] / item_id_stats['mean'] * 100
    print(item_id_stats['norm_change'])

    print(item_id_stats.head)

    ax1 = item_id_stats.plot.scatter(x='mean',

                          y='norm_change',

                          c='DarkBlue')

    plt.pyplot.show()

    #TODO Iterate over item_id groups and pass them into test_stat_dist function
    #for group in item_id_stats:
    #    test_and_stat_dist(group)


def test_and_stat_dist(df_input_group):
    #from here https://pythonhealthcare.org/2018/05/03/81-distribution-fitting-to-data/

    #TODO need to create specific array from dataframe into y
    y = df_input_group.data[:, 0]

    # Create an index array (x) for data

    x = np.arange(len(y))
    size = len(y)



    sc = StandardScaler()
    yy = y.reshape(-1, 1)
    sc.fit(yy)
    y_std = sc.transform(yy)
    y_std = y_std.flatten()
    y_std
    del yy

    dist_names = ['beta',
                  'expon',
                  'gamma',
                  'lognorm',
                  'norm',
                  'pearson3',
                  'triang',
                  'uniform',
                  'weibull_min',
                  'weibull_max']

    # Set up empty lists to stroe results
    chi_square = []
    p_values = []

    # Set up 50 bins for chi-square test
    # Observed data will be approximately evenly distrubuted aross all bins
    percentile_bins = np.linspace(0, 100, 51)
    percentile_cutoffs = np.percentile(y_std, percentile_bins)
    observed_frequency, bins = (np.histogram(y_std, bins=percentile_cutoffs))
    cum_observed_frequency = np.cumsum(observed_frequency)

    # Loop through candidate distributions

    for distribution in dist_names:
        # Set up distribution and get fitted distribution parameters
        dist = getattr(scipy.stats, distribution)
        param = dist.fit(y_std)

        # Obtain the KS test P statistic, round it to 5 decimal places
        p = scipy.stats.kstest(y_std, distribution, args=param)[1]
        p = np.around(p, 5)
        p_values.append(p)

        # Get expected counts in percentile bins
        # This is based on a 'cumulative distrubution function' (cdf)
        cdf_fitted = dist.cdf(percentile_cutoffs, *param[:-2], loc=param[-2],
                              scale=param[-1])
        expected_frequency = []
        for bin in range(len(percentile_bins) - 1):
            expected_cdf_area = cdf_fitted[bin + 1] - cdf_fitted[bin]
            expected_frequency.append(expected_cdf_area)

        # calculate chi-squared
        expected_frequency = np.array(expected_frequency) * size
        cum_expected_frequency = np.cumsum(expected_frequency)
        ss = sum(((cum_expected_frequency - cum_observed_frequency) ** 2) / cum_observed_frequency)
        chi_square.append(ss)

    # Collate results and sort by goodness of fit (best at top)

    results = pd.DataFrame()
    results['Distribution'] = dist_names
    results['chi_square'] = chi_square
    results['p_value'] = p_values
    results.sort_values(['chi_square'], inplace=True)

    # Report results

    print('\nDistributions sorted by goodness of fit:')
    print('----------------------------------------')
    print(results)



