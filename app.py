from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def swap_case_string():
    try:
        data = request.get_json()
        if "string" not in data or not isinstance(data["string"], str):
            return jsonify({"error": "Invalid input. 'string' parameter not found or not a string."}), 400

        result = data["string"].swapcase()
        return jsonify({"result": result})

    except Exception as e:
        # Handle internal server error
        return jsonify({"error": "Internal Server Error"}), 500
    
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == "__main__":
    app.run()
