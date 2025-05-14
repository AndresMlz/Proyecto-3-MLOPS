from locust import HttpUser, task, between
import random

class InferenceUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def predict(self):
        payload = {
            "instances": [
                {
                    "time_in_hospital": random.randint(1, 14),
                    "num_lab_procedures": random.randint(20, 80),
                    "num_procedures": random.randint(0, 6),
                    "num_medications": random.randint(1, 20),
                    "number_outpatient": random.randint(0, 5),
                    "number_emergency": random.randint(0, 3),
                    "number_inpatient": random.randint(0, 3),
                    "number_diagnoses": random.randint(1, 16),
                    "age": random.choice([25, 35, 45, 55, 65, 75, 85, 95])
                }
            ]
        }
        self.client.post("/predict", json=payload) 