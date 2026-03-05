import json

def show_dashboard():

    with open("reports/dashboard_metrics.json") as f:
        metrics = json.load(f)

    print("QA Migration Dashboard")
    print("---------------------")

    for k,v in metrics.items():
        print(k,":",v)


if __name__ == "__main__":
    show_dashboard()