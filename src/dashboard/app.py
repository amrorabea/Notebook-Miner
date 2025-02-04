from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

# Load the csv data
try:
    # Adjust the path to be relative to the static folder
    df = pd.read_csv(os.path.join('static', 'extracted_data.csv'))
except FileNotFoundError:
    print("Error: Could not find the CSV file.")
    df = pd.DataFrame()
    
@app.route("/")
def index():
    try:
        # Libraries
        libraries_df = df[df["Category"] == "Libraries"].head(20)
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
        models_fig = px.pie(
            df[df["Category"] == "Models"],
            values="Count",
            names="Item",
            title="Deep Learning Models Distribution"
        )

        # Data Cleaning Techniques
        cleaning_fig = px.bar(
            df[df["Category"] == "Data Cleaning Techniques"],
            x="Item",
            y="Count",
            title="Data Cleaning Techniques",
            color="Count",
            color_continuous_scale="Viridis"
        )

        # Architectures
        arch_fig = px.bar(
            df[df["Category"] == "Architectures"],
            x="Item",
            y="Count",
            title="Neural Network Architectures",
            color="Count",
            color_continuous_scale="Viridis"
        )

        # Metrics Comparison
        metrics_fig = px.bar(
            df[df["Category"] == "Metrics"],
            x="Item",
            y="Count",
            title="Evaluation Metrics",
            color="Count",
            color_continuous_scale="Viridis"
        )

        # Optimizers and Loss Functions
        opt_loss_df = pd.concat([
            df[df["Category"] == "Optimizers"],
            df[df["Category"] == "Loss Functions"]
        ])
        opt_loss_fig = px.bar(
            opt_loss_df,
            x="Item",
            y="Count",
            color="Category",
            title="Optimizers and Loss Functions",
            barmode="group"
        )

        # Augmentation Techniques
        aug_fig = px.bar(
            df[df["Category"] == "Augmentation Techniques"],
            x="Item",
            y="Count",
            title="Data Augmentation Techniques",
            color="Count",
            color_continuous_scale="Viridis"
        )

        # Update layout for all figures to ensure proper display
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
        print(f"Error occurred: {str(e)}")  # For logging
        return f"An error occurred while generating the dashboard: {str(e)}"

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Health check endpoint
@app.route("/health")
def health_check():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    # Get port from environment variable or default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    # Development server configuration
    if os.environ.get("FLASK_ENV") == "development":
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        app.run(host='0.0.0.0', port=port)