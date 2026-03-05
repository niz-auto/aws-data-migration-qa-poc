from datetime import datetime

def generate_report(results):

    report = f"""
    Data Migration Validation Report
    --------------------------------

    Timestamp: {datetime.now()}

    Row Count Match: {results['row_count']}
    Duplicate Records: {results['duplicates']}
    Null Values: {results['nulls']}
    """

    with open("reports/validation_report.txt", "w") as f:
        f.write(report)

    print("Report generated.")