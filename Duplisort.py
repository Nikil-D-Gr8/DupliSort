import pandas as pd

# Read the original CSV file
df = pd.read_csv("TU9.0 general (Responses).csv")

# Remove duplicates based on the "Event" column
df_no_duplicates = df.drop_duplicates(subset=["Event"])

# Create a dictionary to store dataframes for each unique event
event_dfs = {}
for event in df_no_duplicates["Event"]:
    event_dfs[event] = df[df["Event"] == event]

# Write each event dataframe to a separate spreadsheet
with pd.ExcelWriter("sortedTU.xlsx") as writer:
    for event, event_df in event_dfs.items():
        event_df.to_excel(writer, sheet_name=event, index=False)

# Combine all event dataframes into one dataframe
combined_df = pd.concat(event_dfs.values())

# Write the combined dataframe to a single CSV file
combined_df.to_csv("sortedTU.csv", index=False)

print("Duplicates removed and events sorted successfully!")
