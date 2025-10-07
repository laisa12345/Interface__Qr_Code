from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interface Kelompok 10</title>
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(to right, #83a4d4, #b6fbff);
      text-align: center;
      padding: 50px;
    }
    h1 {
      color: #222;
      margin-bottom: 30px;
    }
    table {
      margin: 0 auto;
      border-collapse: collapse;
      width: 60%;
      background: #fff;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    th, td {
      padding: 15px;
      border-bottom: 1px solid #ddd;
    }
    th {
      background-color: #007bff;
      color: white;
    }
    tr:hover {
      background-color: #f2f2f2;
    }
    footer {
      margin-top: 40px;
      font-size: 14px;
      color: #555;
    }
  </style>
</head>
<body>
  <h1>Interface Kelompok 10</h1>
  <table>
    <tr>
      <th>No</th>
      <th>NIM</th>
      <th>Nama Anggota</th>
    </tr>
    <tr>
      <td>1</td>
      <td>2318047</td>
      <td>Laisa Imama Fajarina</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2318055</td>
      <td>Rayhan Ainurron Falaqi</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2318062</td>
      <td>Shabrina Dwiputri</td>
    </tr>
  </table>

  <footer>
    © 2025 Kelompok 10 - Informatika
  </footer>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
