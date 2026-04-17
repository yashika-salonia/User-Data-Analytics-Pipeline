import matplotlib.pyplot as plt

def plot_data(df1, df2):

    color1= "#932ED6"
    color2 = "#E7224C"

    # Graph 1
    plt.figure(figsize=(8,5))
    plt.bar(df1["subject"], df1["avg_session"], color=color1)
    plt.xlabel("Subject")
    plt.ylabel("Avg Session Time")
    plt.title("Avg Session Time per Subject")
    plt.savefig("output/charts/sql_subject.png")
    plt.close()

    # Graph 2
    plt.figure(figsize=(8,5))
    plt.scatter(df2["distraction_count"], df2["avg_time"], color=color2, marker='o')
    plt.plot(df2["distraction_count"], df2["avg_time"], color=color2, linestyle='--', alpha=0.5)
    plt.xlabel("Distraction Count")
    plt.ylabel("Avg Session Time")
    plt.title("Distraction vs Avg Session Time")
    plt.savefig("output/charts/sql_distraction.png")
    plt.close()

    print("Charts created")