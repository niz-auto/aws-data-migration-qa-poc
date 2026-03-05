def compare_counts(source_df, target_df):

    if len(source_df) == len(target_df):
        print("Row count validation passed")
    else:
        print("Row count mismatch")