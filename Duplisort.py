import pandas as pd

try:
    df = pd.read_csv("TU9.0 general (Responses).csv")

    columns_to_check = ["Event", "Team member name (1)", "Team member name (2)", "Team member name (3)", 
                        "Team member name (4)", "Team member name (5)", "Team member name (6)", 
                        "Team member name (7)", "Team member name (8)", "Team member name (9)", 
                        "Team member name (10)"]
    
    df_no_duplicates = df.drop_duplicates(subset=columns_to_check, keep="first")
    event_dfs = {}
    for event in df_no_duplicates["Event"]:
        event_dfs[event] = df_no_duplicates[df_no_duplicates["Event"] == event]
    with pd.ExcelWriter("sortedTU.xlsx") as writer:
        for event, event_df in event_dfs.items():
            event_df.to_excel(writer, sheet_name=event, index=False)

    print("Velamudinchu pa")
except FileNotFoundError:
    print("File not found. Please provide the correct file path.")
except pd.errors.ParserError:
    print("Incorrect file format. Please provide a CSV file.")
