from flask import Flask, render_template_string
import megaind

app = Flask(__name__)
STACK = 0  # your board index (0 if only one board)

HTML = """
<!doctype html>
<html>
<head>
  <meta http-equiv="refresh" content="1">
  <title>SM-I-001 Input States</title>
  <style>
    .led { display:inline-block; width:25px; height:25px; border-radius:50%; margin:5px; }
    .on { background-color: green; }
    .off { background-color: red; }
    .container { display:flex; flex-wrap: wrap; max-width: 300px; }
    .input-label { margin-right: 10px; font-family: sans-serif; }
  </style>
</head>
<body>
  <h1>SM-I-001 Digital Inputs</h1>
  <div class="container">
    {% for ch, st in inputs %}
      <div>
        <span class="input-label">Input {{ ch }}:</span>
        <span class="led {{ 'on' if st else 'off' }}"></span>
      </div>
    {% endfor %}
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    inputs = []
    for ch in range(1, 9):  # SM-I-001 has 8 opto-isolated inputs
        state = megaind.getOptoCh(STACK, ch)
        inputs.append((ch, state))
    return render_template_string(HTML, inputs=inputs)

if __name__ == "__main__":
    # 0.0.0.0 makes it accessible on your local network
    app.run(host="0.0.0.0", port=5000)
