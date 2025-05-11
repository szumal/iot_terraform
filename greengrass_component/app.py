import time

def mock_local_processing():
    while True:
        print("[Greengrass] Processing sensor data locally...")
        time.sleep(10)

if __name__ == "__main__":
    mock_local_processing()