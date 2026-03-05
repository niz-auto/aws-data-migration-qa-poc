def check_pipeline_status(logs):

    if "ERROR" in logs:
        print("Pipeline failure detected")
    else:
        print("Pipeline completed successfully")