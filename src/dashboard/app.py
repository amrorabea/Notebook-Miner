from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load the csv data
df = pd.read_csv("../data/extracted_data.csv")

@app.route("/")
def index():
    
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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
