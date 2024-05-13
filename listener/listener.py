#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dora import Node
import pyarrow as pa

node = Node()

event = node.next()
if event["type"] == "INPUT":
    message_list = event["value"].to_pylist()
    message_bytes = bytes(message_list)
    formatted_message = message_bytes.decode("utf-8")
    print(
        f"""I heard {formatted_message}"""
    )
