#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Zen Voice Assistant - Flask Backend"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sys
import io
import traceback

# Fix Windows encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', line_buffering=True)

# Import AI and executor
try:
    from ollama_brain import ask_ollama
    from executor import execute_plan
except ImportError as e:
    print(f"ERROR importing modules: {e}")
    traceback.print_exc()
    sys.exit(1)

# Initialize Flask
app = Flask(__name__)
CORS(app)

print("\n" + "="*60)
print("ZEN AUTOGPT AGENT STARTING...")
print("="*60 + "\n")

@app.route("/")
def home():
    """Serve the voice.html UI"""
    try:
        return render_template("voice.html")
    except Exception as e:
        print(f"ERROR serving home: {e}")
        traceback.print_exc()
        return f"Error: {e}", 500

@app.route("/test", methods=["POST"])
def test():
    """Test endpoint - no Ollama required"""
    try:
        user_text = request.json.get("text", "")
        print(f"[TEST] Received: {user_text}")
        return jsonify({"reply": f"Test OK: {user_text}"})
    except Exception as e:
        print(f"[TEST ERROR] {e}")
        traceback.print_exc()
        return jsonify({"reply": f"Error: {e}"}), 500

@app.route("/agent", methods=["POST"])
def agent():
    """Main agent endpoint - processes voice commands"""
    try:
        # Get text from request
        user_text = request.json.get("text", "").strip()
        
        if not user_text:
            print("[AGENT] Empty request")
            return jsonify({"reply": "Please say something"}), 400
        
        print(f"\n[AGENT] USER SAID: {user_text}")
        print(f"[AGENT] Processing...")
        
        # Get AI plan
        try:
            plan = ask_ollama(user_text)
            print(f"[AGENT] Plan received: {plan}")
        except Exception as e:
            print(f"[AGENT ERROR] Ollama failed: {e}")
            traceback.print_exc()
            return jsonify({"reply": f"AI error: {e}"}), 500
        
        # Execute plan
        try:
            result = execute_plan(plan)
            print(f"[AGENT] Result: {result}")
        except Exception as e:
            print(f"[AGENT ERROR] Execution failed: {e}")
            traceback.print_exc()
            return jsonify({"reply": f"Execution error: {e}"}), 500
        
        # Return response
        response = {"reply": result if result else "Done"}
        print(f"[AGENT] Returning: {response}")
        return jsonify(response)
        
    except Exception as e:
        error_msg = f"Agent error: {type(e).__name__}: {e}"
        print(f"\n[AGENT CRITICAL ERROR] {error_msg}")
        traceback.print_exc()
        return jsonify({"reply": error_msg}), 500

@app.before_request
def log_request():
    """Log all requests"""
    print(f"[REQUEST] {request.method} {request.path}")

@app.after_request
def log_response(response):
    """Log all responses"""
    print(f"[RESPONSE] Status: {response.status_code}\n")
    return response

if __name__ == "__main__":
    print("Starting Flask server on http://127.0.0.1:5000\n")
    try:
        app.run(debug=True, use_reloader=False, threaded=True, port=5000)
    except Exception as e:
        print(f"FATAL ERROR: {e}")
        traceback.print_exc()
        sys.exit(1)
