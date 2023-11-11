"""
Our favorite online shoe store, ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. Help them analyze the data using aggregate measures.
"""
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
#print(ad_clicks.head())

#print(ad_clicks.groupby('utm_source').user_id.count().reset_index())

ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].isnull()

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

#print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  index = 'utm_source',
  columns = 'is_click',
  values = 'user_id'
).reset_index()

#print(clicks_pivot)

clicks_pivot['percent_clicked'] = (clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]))*100
#print(clicks_pivot)

print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())

print(ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().pivot(
  index = 'experimental_group',
  columns = 'is_click',
  values = 'user_id'
).reset_index())


a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
a_clicks_pivot = a_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
).reset_index()
a_clicks_pivot['percent_clicked'] = (a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])) * 100
#print(a_clicks_pivot)

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
b_clicks_pivot = b_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
).reset_index()
b_clicks_pivot['percent_clicked'] = (b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])) * 100
print(b_clicks_pivot)

"""
Compare the results for A and B. What happened over the course of the week? Do you recommend that your company use Ad A or Ad B?
Recomiendo utilizar el anuncio A, ya que ha demostrado tener más clics de manera consistente durante la semana (excepto los martes) en comparación con el anuncio B.
El miércoles, el 30% de las personas hace clic en el anuncio A (el día más débil), mientras que el jueves el porcentaje aumenta al 40% (el día más fuerte).
"""



