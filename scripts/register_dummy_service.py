import requests
import json

def register_dummy_service():
    print("Registering a dummy service with Eureka server...")
    registration_data = {
        "instance": {
            "hostName": "dummy-service.localhost",
            "app": "DUMMY-SERVICE",
            "ipAddr": "127.0.0.1",
            "status": "UP",
            "port": {"$": 8080, "@enabled": "true"},
            "vipAddress": "dummy-service.localhost",
            "dataCenterInfo": {
                "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                "name": "MyOwn"
            }
        }
    }

    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.post(
            "http://localhost:8761/eureka/apps/DUMMY-SERVICE",
            data=json.dumps(registration_data),
            headers=headers
        )
        print(f"Registration response status code: {response.status_code}")
        assert response.status_code == 204, "Failed to register the dummy service"
        print("Dummy service successfully registered.")
    except Exception as e:
        print(f"Registration failed with exception: {e}")
        raise

if __name__ == "__main__":
    register_dummy_service()
