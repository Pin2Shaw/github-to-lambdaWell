import pandas as pd

def lambda_handler(event, context):
    # TODO implement
    dataTemp = {'col1':[1,2],'col2':[3,4]}
    df = pd.DataFrame(data=dataTemp)
    print(df)
    print('Done')