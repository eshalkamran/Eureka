import requests

def test_eureka_status():
    print("Testing if Eureka server is accessible at http://localhost:8761/eureka/apps")
    try:
        response = requests.get("http://localhost:8761/eureka/apps")
        print(f"Received status code: {response.status_code}")
        assert response.status_code == 200, "Eureka server is not accessible"
        print("Eureka server is up and running.")

        # Further checks on response content
        json_response = response.json()
        print("Received JSON response from Eureka:")
        print(json_response)
        assert 'applications' in json_response, "No applications key found in response"
    except Exception as e:
        print(f"Test failed with exception: {e}")
        raise

if __name__ == "__main__":
    test_eureka_status()