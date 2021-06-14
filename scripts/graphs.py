import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('processed/data_collection_2/US_IT_BigCompanies.xlsx')
df.columns = ['Job Seniorities', 'Any Gender', 'Female', 'Male', 'Any Gender 2', 'Female 2', 'Male 2', 'Any Gender 3', 'Female 3', 'Male 3', 'female', 'male', 'male:female']
df = df.drop([0, 1])
print(df.head())

df['Job Seniorities']
df['male:female']
df['female']

fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Job Seniorities')
ax1.set_ylabel('male:female', color=color)
ax1.plot(df['Job Seniorities'], df['male:female'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('%\female', color=color)  # we already handled the x-label with ax1
ax2.plot(df['Job Seniorities'], df['female'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

# plt.plot(df['Job Seniorities'],df['male:female'])
# plt.title('Job Seniorities vs. male:female')
# plt.xlabel('Job Seniorities')
# plt.ylabel('male:female')
# plt.show()

# Program will only end when plt.show returns, which is after you closed all figures.
plt.show(block=True)


# fig, ax1 = plt.subplots()

# ax1.set_xlabel('time (s)')
# ax1.set_ylabel('exp', color=color)
# ax1.plot(t, data1, color=color)
# ax1.tick_params(axis='y', labelcolor=color)

# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:blue'
# ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
# ax2.plot(t, data2, color=color)
# ax2.tick_params(axis='y', labelcolor=color)

# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.show()