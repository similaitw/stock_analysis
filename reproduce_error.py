try:
    from ui.charts import render_interactive_chart
    import pandas as pd
    print("Import successful.")
    
    df = pd.DataFrame({
        'Open': [10, 11], 'High': [12, 13], 'Low': [9, 10], 'Close': [11, 12], 'Volume': [100, 200]
    }, index=pd.date_range('20230101', periods=2))
    
    print("Calling render_interactive_chart...")
    render_interactive_chart(df, "TEST", overlays=['MA5'], indicators=['RSI'])
    print("Success.")
except Exception as e:
    print(f"Error: {e}")
