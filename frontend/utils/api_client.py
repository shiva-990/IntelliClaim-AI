import requests

from utils.config import BACKEND_URL


class APIClient:

    def get_claims(self):

        try:
            response = requests.get(
                f"{BACKEND_URL}/api/v1/claims/",
                timeout=5,
            )
            response.raise_for_status()
            return response.json()

        except requests.RequestException:
            return []

    def create_claim(self, payload):

        response = requests.post(
            f"{BACKEND_URL}/api/v1/claims/",
            json=payload,
        )

        return response

    def get_customers(self):

        try:
            response = requests.get(
                f"{BACKEND_URL}/api/v1/customers/",
                timeout=5,
            )
            response.raise_for_status()
            return response.json()

        except requests.RequestException:
            return []

    def get_policies(self):

        try:
            response = requests.get(
                f"{BACKEND_URL}/api/v1/policies/",
                timeout=5,
            )
            response.raise_for_status()
            return response.json()

        except requests.RequestException:
            return []

    def upload_image(self, claim_id, image):

        files = {
            "image": (
                image.name,
                image,
                image.type,
            )
        }

        data = {
            "claim_id": claim_id
        }

        response = requests.post(
            f"{BACKEND_URL}/api/v1/upload/image",
            files=files,
            data=data,
        )

        return response

    def process_claim(self, claim_id):

        response = requests.post(
            f"{BACKEND_URL}/api/v1/process/{claim_id}"
        )

        return response
    def get_report(self, claim_id):

        try:

            response = requests.get(
               f"{BACKEND_URL}/api/v1/reports/report/{claim_id}",
               timeout=60,
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:

            return {
               "error": str(e)
            }
    def get_claim_details(
            self,
            claim_id,
        ):

            try:

                response = requests.get(
                  f"{BACKEND_URL}/api/v1/claims/{claim_id}",
                   timeout=10,
                )

                response.raise_for_status()

                return response.json()

            except requests.RequestException:

                return None


api = APIClient()