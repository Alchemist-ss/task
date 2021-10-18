import pandas as pd

with open('marketing_campaign.csv') as csvfile:
    read_csv = pd.read_csv(csvfile, sep=r'\t', engine='python')



