#!/usr/bin/env python
"""Test script - writes results to file"""
import requests
import json
import time

time.sleep(1)

try:
    response = requests.post(
        "http://127.0.0.1:5000/agent",
        json={"text": "hello"},
        timeout=45
    )
    result = {
        "status": response.status_code,
        "reply": response.json().get("reply", "No reply")
    }
except Exception as e:
    result = {
        "error": str(e),
        "type": type(e).__name__
    }

# Write to file so we can see results
with open("d:\\zen\\zen-backend\\test_result.txt", "w") as f:
    f.write(json.dumps(result, indent=2))

print("Test complete - check test_result.txt")
