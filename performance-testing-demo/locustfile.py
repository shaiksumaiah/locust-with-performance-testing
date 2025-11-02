from locust import HttpUser, task, between

class PerformanceTestUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def load_tasks(self):
        self.client.get("/tasks")

    @task(1)
    def load_users(self):
        self.client.get("/users")

    @task(1)
    def get_cache_metrics(self):
        self.client.get("/cache-metrics")
