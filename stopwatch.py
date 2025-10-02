import time

def stopwatch():
    input("⏱️ Press Enter to start the stopwatch...")
    start_time = time.time()

    input("🛑 Press Enter to stop the stopwatch.")
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"⏲️ Elapsed Time: {round(elapsed_time, 2)} seconds")

if __name__ == "__main__":
    stopwatch()
