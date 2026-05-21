import requests


BASE_URL = "http://localhost:8000"


def upload_file(uploaded_file):

    files = {

        "file": uploaded_file
    }

    response = requests.post(

        f"{BASE_URL}/upload",

        files=files
    )

    if response.status_code == 200:
        return response.json()

    return {

        "success": False,

        "error": response.text
    }


def get_analytics(file_path):

    response = requests.get(

        f"{BASE_URL}/analyze",

        params={
            "file_path": file_path
        }
    )

    if response.status_code == 200:
        return response.json()

    return {

        "success": False,

        "error": response.text
    }


def get_ai_summary(file_path):

    response = requests.get(

        f"{BASE_URL}/ai-summary",

        params={
            "file_path": file_path
        }
    )

    if response.status_code == 200:
        return response.json()

    return {

        "success": False,

        "error": response.text
    }