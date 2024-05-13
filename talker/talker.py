#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dora import Node

node = Node()

event = node.next()
if event["type"] == "INPUT":
    print(
        f"""Node received:
    id: {event["id"]},
    value: {event["value"]},
    metadata: {event["metadata"]}"""
    )
    node.send_output("speech", b"hello world or something", None)
