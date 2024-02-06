import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the .xlsx file
df = pd.read_excel('data.xlsx')

# Define the columns we'll work with
mood_column = 'How frequently do you experience significant changes in your mood, such as feeling very high and excited or very low and depressed? (1 - Rarely, 10 - Constantly)'
duration_column = 'When you experience mood swings, how long do they typically last?'
impact_column = 'Do these mood swings affect your ability to perform daily tasks (e.g., work, study, social activities)?'
factors_column = 'Which, if any, of the following factors do you feel contribute to your mood swings? (Select all that apply)'
treatment_column = 'Have you sought any treatment or support for mood swings?'
notice_changes_column = 'When experiencing a mood swing, do you notice changes in any of the following areas? (Select all that apply)'


# Define a function to draw a trend graph for mood swings and its impact
def draw_trend_graph(dataframe, mood_col, impact_col):
    # Group the data by mood swing frequency and get an average impact score
    impact_map = {'Not at all': 0, 'Only slightly': 1, 'Moderately': 2, 'Severely': 3, 'Completely': 4}
    dataframe[impact_col] = dataframe[impact_col].map(impact_map)
    trend_data = dataframe.groupby(mood_col)[impact_col].mean()

    # Plot the trend data
    fig, ax = plt.subplots(figsize=(10, 5))
    trend_data.plot(kind='line', marker='o', color='b', ax=ax)

    # Set the title and labels
    ax.set_title('Trend of Mood Swing Frequency vs. Impact on Daily Tasks')
    ax.set_xlabel('Mood Swing Frequency (1 - Rarely, 10 - Constantly)')
    ax.set_ylabel('Average Impact on Daily Tasks')

    # Set y-axis to show whole numbers only and range from 0 to 4
    ax.set_yticks(range(5))
    ax.set_ylim(0, 4)

    # Optionally, add custom labels at the top and bottom
    ax.text(-0.1, 4, 'Completely', va='center', ha='right', backgroundcolor='white', fontsize=8,
            transform=ax.get_yaxis_transform())
    ax.text(-0.1, 0, 'Not at all', va='center', ha='right', backgroundcolor='white', fontsize=8,
            transform=ax.get_yaxis_transform())

    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Filter the entries that showed higher frequency of mood swings
high_mood_swing_frequency_df = df[df[mood_column] >= 7]

# Calculate the percentages for each category
total_respondents = len(df)
high_frequency_respondents = len(high_mood_swing_frequency_df)
percentage_high_frequency = (high_frequency_respondents / total_respondents) * 100

# Print out the results to the user
print(f"Percentage of respondents with high mood swing frequency (>=7): {percentage_high_frequency:.2f}%")

# We can add more granularity based on mood swing duration, impact levels, and associated factors
long_duration_df = high_mood_swing_frequency_df[
    high_mood_swing_frequency_df[duration_column].isin(['A week or longer'])]
severe_impact_df = high_mood_swing_frequency_df[
    high_mood_swing_frequency_df[impact_column].isin(['Severely', 'Completely'])]

# As an example, calculate the percentage of those who experience long duration mood swings and those who report severe impacts
percentage_long_duration = (len(long_duration_df) / total_respondents) * 100
percentage_severe_impact = (len(severe_impact_df) / total_respondents) * 100

print(f"Percentage of respondents with long-duration mood swings: {percentage_long_duration:.2f}%")
print(f"Percentage of respondents who report severe impact on daily activities: {percentage_severe_impact:.2f}%")

draw_trend_graph(df, mood_column, impact_column)
