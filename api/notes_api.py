import time

class NotesAPI:

    def __init__(self, client):
        self.client = client

    def get_notes(self):
        start = time.time()

        res = self.client.session.get(
            f"{self.client.base_url}/notes",
            headers=self.client.headers
        )

      
        return res, time.time() - start

    def create_note(self, title, description, category="Home"):
        start = time.time()

        res = self.client.session.post(
            f"{self.client.base_url}/notes",
            json={
                "title": title,
                "description": description,
                "category": category
            },
            headers=self.client.headers
        )

       

        return res, time.time() - start