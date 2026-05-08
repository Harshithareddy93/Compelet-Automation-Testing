import csv
import os
from datetime import datetime


class PerformanceLogger:

    FILE_PATH = "performance_logs/performance.csv"

    @staticmethod
    def log(test_name, elapsed):

        os.makedirs("performance_logs", exist_ok=True)

        file_exists = os.path.isfile(
            PerformanceLogger.FILE_PATH
        )

        with open(
            PerformanceLogger.FILE_PATH,
            mode="a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Timestamp",
                    "Test Name",
                    "Execution Time"
                ])

            writer.writerow([
                datetime.now(),
                test_name,
                elapsed
            ])