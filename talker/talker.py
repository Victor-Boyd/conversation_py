from dora import DoraStatus
import pyarrow as pa

class Operator:
    """
    Template docstring
    """

    def __init__(self):
        """Called on initialisation"""
        pass
        self.num = 0

    def on_event(
        self,
        dora_event,
        send_output,
    ) -> DoraStatus:

        if dora_event["type"] == "INPUT":
            self.num += 1
            print(
                f"Received input {dora_event['id']}, with data: {dora_event['value']}"
            )
            
            try:
                output_data = pa.array([f"hello {self.num}"], type=pa.string())
                send_output("speech", output_data)
            except Exception as e:
                print(f"Error sending output: {e}")

        return DoraStatus.CONTINUE

    def __del__(self):
        """Called before being deleted"""
        pass
