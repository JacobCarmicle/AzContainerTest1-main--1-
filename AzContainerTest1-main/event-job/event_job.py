from azure.storage.queue import QueueClient
import os

queue_name = os.environ.get("AZURE_STORAGE_QUEUE_NAME")
connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")

def main():
    queue_client = QueueClient.from_connection_string(connection_string, queue_name)
    messages = queue_client.receive_messages(messages_per_page=1)
    for msg in messages:
        print(f"Processing message: {msg.content}")
        queue_client.delete_message(msg.id, msg.pop_receipt)

if __name__ == "__main__":
    print("Event job started...")
    main()
    print("Event job completed.")
