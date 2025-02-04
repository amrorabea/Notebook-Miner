from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

# Load the csv data with debug information
try:
    csv_path = os.path.join(os.path.dirname(__file__), 'static', 'extracted_data.csv')
    print(f"Attempting to load CSV from: {csv_path}")
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        print(f"CSV loaded successfully. Columns: {df.columns.tolist()}")
        print(f"Data shape: {df.shape}")
        print(f"First few rows:\n{df.head()}")
    else:
        print(f"CSV file not found at: {csv_path}")
        df = pd.DataFrame()
except Exception as e:
    print(f"Error loading CSV: {str(e)}")
    df = pd.DataFrame()

@app.route("/")
def index():
    try:
        # Check if DataFrame is empty
        if df.empty:
            return "Error: No data available. The CSV file could not be loaded.", 500

        # Check if required columns exist
        required_columns = ['Category', 'Item', 'Count']
        if not all(col in df.columns for col in required_columns):
            return f"Error: Missing required columns. Available columns: {df.columns.tolist()}", 500

        # Print debug information
        print(f"Unique categories: {df['Category'].unique()}")
        
        # Libraries
        libraries_df = df[df["Category"] == "Libraries"].head(20)
        print(f"Libraries data shape: {libraries_df.shape}")
        
        libraries_fig = px.bar(
            libraries_df,
            x="Count",
            y="Item",
            orientation='h',
            title="Top 20 Most Used Libraries",
            color="Count",
            color_continuous_scale="Viridis",
            height=800
        )
        
        libraries_fig.update_layout(
            yaxis={'categoryorder':'total ascending'},
            font=dict(size=14),
            title=dict(
                font=dict(size=24)
            ),
            margin=dict(l=200),
            showlegend=False,
            xaxis_title="Number of Occurrences",
            yaxis_title="Library Name"
        )

        # Models Distribution
        models_df = df[df["Category"] == "Models"]
        if not models_df.empty:
            models_fig = px.pie(
                models_df,
                values="Count",
                names="Item",
                title="Deep Learning Models Distribution"
            )
        else:
            models_fig = px.pie(pd.DataFrame({'Item': ['No Data'], 'Count': [1]}),
                              values='Count', names='Item', title="No Models Data Available")

        # Data Cleaning Techniques
        cleaning_df = df[df["Category"] == "Data Cleaning Techniques"]
        if not cleaning_df.empty:
            cleaning_fig = px.bar(
                cleaning_df,
                x="Item",
                y="Count",
                title="Data Cleaning Techniques",
                color="Count",
                color_continuous_scale="Viridis"
            )
        else:
            cleaning_fig = px.bar(pd.DataFrame({'Item': ['No Data'], 'Count': [0]}),
                                x='Item', y='Count', title="No Cleaning Techniques Data Available")

        # Architectures
        arch_df = df[df["Category"] == "Architectures"]
        if not arch_df.empty:
            arch_fig = px.bar(
                arch_df,
                x="Item",
                y="Count",
                title="Neural Network Architectures",
                color="Count",
                color_continuous_scale="Viridis"
            )
        else:
            arch_fig = px.bar(pd.DataFrame({'Item': ['No Data'], 'Count': [0]}),
                            x='Item', y='Count', title="No Architecture Data Available")

        # Metrics Comparison
        metrics_df = df[df["Category"] == "Metrics"]
        if not metrics_df.empty:
            metrics_fig = px.bar(
                metrics_df,
                x="Item",
                y="Count",
                title="Evaluation Metrics",
                color="Count",
                color_continuous_scale="Viridis"
            )
        else:
            metrics_fig = px.bar(pd.DataFrame({'Item': ['No Data'], 'Count': [0]}),
                               x='Item', y='Count', title="No Metrics Data Available")

        # Optimizers and Loss Functions
        opt_loss_df = pd.concat([
            df[df["Category"] == "Optimizers"],
            df[df["Category"] == "Loss Functions"]
        ])
        if not opt_loss_df.empty:
            opt_loss_fig = px.bar(
                opt_loss_df,
                x="Item",
                y="Count",
                color="Category",
                title="Optimizers and Loss Functions",
                barmode="group"
            )
        else:
            opt_loss_fig = px.bar(pd.DataFrame({'Item': ['No Data'], 'Count': [0], 'Category': ['None']}),
                                x='Item', y='Count', color='Category', title="No Optimizers/Loss Functions Data Available")

        # Augmentation Techniques
        aug_df = df[df["Category"] == "Augmentation Techniques"]
        if not aug_df.empty:
            aug_fig = px.bar(
                aug_df,
                x="Item",
                y="Count",
                title="Data Augmentation Techniques",
                color="Count",
                color_continuous_scale="Viridis"
            )
        else:
            aug_fig = px.bar(pd.DataFrame({'Item': ['No Data'], 'Count': [0]}),
                           x='Item', y='Count', title="No Augmentation Techniques Data Available")

        # Update layout for all figures
        for fig in [libraries_fig, models_fig, cleaning_fig, arch_fig, 
                   metrics_fig, opt_loss_fig, aug_fig]:
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(size=12),
                margin=dict(l=50, r=50, t=50, b=50)
            )

        graphs = {
            'libraries_graph': libraries_fig.to_html(full_html=False),
            'models_graph': models_fig.to_html(full_html=False),
            'cleaning_graph': cleaning_fig.to_html(full_html=False),
            'arch_graph': arch_fig.to_html(full_html=False),
            'metrics_graph': metrics_fig.to_html(full_html=False),
            'opt_loss_graph': opt_loss_fig.to_html(full_html=False),
            'aug_graph': aug_fig.to_html(full_html=False)
        }

        return render_template("index.html", **graphs)
    
    except Exception as e:
        print(f"Error in route: {str(e)}")
        # Print more debug information
        if not df.empty:
            print(f"DataFrame columns: {df.columns.tolist()}")
            print(f"DataFrame head:\n{df.head()}")
        return f"An error occurred: {str(e)}", 500

# Add a debug route
@app.route("/debug")
def debug():
    try:
        debug_info = {
            "csv_path": os.path.join(os.path.dirname(__file__), 'static', 'extracted_data.csv'),
            "file_exists": os.path.exists(os.path.join(os.path.dirname(__file__), 'static', 'extracted_data.csv')),
            "current_directory": os.getcwd(),
            "directory_contents": os.listdir(os.path.dirname(__file__)),
            "static_contents": os.listdir(os.path.join(os.path.dirname(__file__), 'static')) if os.path.exists(os.path.join(os.path.dirname(__file__), 'static')) else "Static directory not found",
            "dataframe_empty": df.empty if 'df' in globals() else "DataFrame not initialized",
            "dataframe_columns": df.columns.tolist() if 'df' in globals() and not df.empty else "No columns available"
        }
        return debug_info
    except Exception as e:
        return {"error": str(e)}

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)