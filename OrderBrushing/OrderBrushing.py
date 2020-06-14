import numpy
import pandas as pd

data_frame = pd.read_csv('order_brush_order.csv')

data_frame['year'] = pd.DatetimeIndex(data_frame['event_time']).year
data_frame['month'] = pd.DatetimeIndex(data_frame['event_time']).month
data_frame['day'] = pd.DatetimeIndex(data_frame['event_time']).day
data_frame['hour'] = pd.DatetimeIndex(data_frame['event_time']).hour
data_frame['minute'] = pd.DatetimeIndex(data_frame['event_time']).minute
data_frame['seconds'] = pd.DatetimeIndex(data_frame['event_time']).second
data_frame = data_frame.drop('event_time', axis=1)
data_frame = data_frame.sort_values(by=['shopid', 'orderid'])
data_frame.to_csv('sorted_orders.csv', index=False)
print(data_frame)

data_frame_shopuser = pd.DataFrame(columns=["shopid", "userid", "hour", "minute", "seconds"])

for index, row in data_frame.iterrows():
    repetition = 0
    for index2, row2 in data_frame.iterrows():
        pass

print(data_frame_shopuser)
