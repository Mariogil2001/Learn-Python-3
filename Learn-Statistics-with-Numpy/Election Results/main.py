import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']
total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print total_ceballos
percentage_ceballos = 100 * total_ceballos/len(survey_responses)
print percentage_ceballos
survey_responses = len(survey_responses)
print survey_responses
possible_surveys = np.random.binomial(70, 0.54, 10000) / 70.
print possible_surveys
plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.title('Binomial Election Results')
plt.xlabel('Voter Percentage')
plt.ylabel('Frequency')
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print ceballos_loss_surveys
#ceballos_loss_surveys = 21.6%
large_survey = np.random.binomial(7000, 0.54, 10000) / 7000.
print large_survey
ceballos_loss_new = np.mean(large_survey < 0.5)
print ceballos_loss_new
#With more data, 
#0% is the calculated percentage that ceballos will loose the election. 
#The advice would be to assess the signifigance of your sample size 
#prior to drawing conclusions from the survey data.