import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_data(path):
    df = pd.read_csv(path)

    color = "#4F46E5"  # consistent color

    # STYLE
    plt.style.use('ggplot')

    # 📊 1. Bar Chart
    subject_focus = df.groupby("subject")["focus_score"].mean()

    plt.figure(figsize=(8,5))
    subject_focus.plot(kind="bar", color=color)

    plt.title("Average Focus Score per Subject", fontsize=14, fontweight='bold')
    plt.xlabel("Subject")
    plt.ylabel("Focus Score")
    plt.xticks(rotation=30)
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("output/charts/subject_focus.png")
    plt.close()

    # 📉 2. Scatter Plot

    z = np.polyfit(df["distraction_count"], df["focus_score"], 1)
    p = np.poly1d(z)

    plt.plot(df["distraction_count"], p(df["distraction_count"]), color="red")
    plt.figure(figsize=(8,5))
    plt.scatter(df["distraction_count"], df["focus_score"], color=color, alpha=0.7)

    plt.title("Distraction vs Focus Score", fontsize=14, fontweight='bold')
    plt.xlabel("Distraction Count")
    plt.ylabel("Focus Score")
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("output/charts/distraction_vs_focus.png")
    plt.close()

    print("Analysis Completed with improved visuals")