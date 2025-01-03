def paginate_dataframe(df, page_size=5, page_num=0):
    """Return a slice of the dataframe based on pagination parameters."""
    total_pages = len(df) // page_size + (1 if len(df) % page_size > 0 else 0)
    start_idx = page_num * page_size
    end_idx = start_idx + page_size
    
    # Preserve original index when slicing
    return df.iloc[start_idx:end_idx].copy(), total_pages 