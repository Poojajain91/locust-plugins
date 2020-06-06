# How to use VS Code debugger with Locust
from locust import task, HttpUser
from locust.exception import StopUser
from locust_plugins import run_single_user


class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        raise StopUser()


# when executed as a script, run a single locust in a way suitable for the vs code debugger
if __name__ == "__main__":
    MyUser.host = "http://example.edu"
    run_single_user(MyUser)
