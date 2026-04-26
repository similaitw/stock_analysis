import pandas as pd
from ui.charts import render_interactive_chart
import plotly.io as pio

# Create mock data
data = {
    'Open': [100, 102, 101, 103, 105] * 10,
    'High': [103, 104, 102, 106, 108] * 10,
    'Low': [99, 101, 100, 102, 104] * 10,
    'Close': [102, 101, 103, 105, 107] * 10,
    'Volume': [1000, 1500, 1200, 1800, 2000] * 10
}
df = pd.DataFrame(data)
df.index = pd.date_range(start='2023-01-01', periods=50)

print("Generating chart...")
try:
    fig = render_interactive_chart(df, "TEST")
    # Save to HTML to manually inspect if needed, or just ensure no error thrown
    pio.write_html(fig, file='test_chart.html', auto_open=False)
    print("Chart saved to test_chart.html. Success.")
except Exception as e:
    print(f"Error: {e}")
