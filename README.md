
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>iPhone IPSW Helper</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #10131a;
      color: white;
      padding: 30px 16px;
      max-width: 600px;
      margin: auto;
    }
    .panel {
      background: #1d2330;
      padding: 22px;
      border-radius: 14px;
      margin-top: 18px;
    }
    button, input {
      width: 100%;
      box-sizing: border-box;
      padding: 13px;
      margin-top: 12px;
      border-radius: 8px;
    }
    button {
      background: #3984ff;
      color: white;
      border: 0;
      font-weight: bold;
      cursor: pointer;
    }
    .note { color: #bbc5d6; line-height: 1.5; }
    #result { overflow-wrap: anywhere; }
  </style>
</head>
<body>
  <h1>iPhone IPSW Helper</h1>
  <p class="note">Firmware file checker for iPhone 12 Pro Max.</p>

  <div class="panel">
    <h2>1. Select your IPSW</h2>
    <input type="file" id="ipsw" accept=".ipsw">
    <button onclick="checkFile()">Check firmware file</button>
    <p id="result" aria-live="polite">No file selected.</p>
  </div>

  <div class="panel">
    <h2>2. Before restoring</h2>
    <p class="note">
      • iPhone 12 Pro Max identifier: iPhone13,4<br>
      • Apple must still be signing the chosen iOS version.<br>
      • Restoring can erase your data.<br>
      • Activation Lock will remain after restoring.
    </p>
    <button onclick="window.open(
      'https://ipsw.me/iPhone13,4', '_blank', 'noopener'
    )">Check firmware listings</button>
    <button onclick="window.open(
      'https://support.apple.com/118106', '_blank', 'noopener'
    )">Apple restore instructions</button>
  </div>

  <script>
    function checkFile() {
      const file = document.getElementById("ipsw").files[0];
      const result = document.getElementById("result");

      if (!file) {
        result.textContent = "Please select an IPSW file first.";
        return;
      }

      result.textContent =
        "Selected: " + file.name +
        "\nFile size: " +
        (file.size / (1024 ** 3)).toFixed(2) + " GB" +
        "\nThis checks the filename and size only. " +
        "It does not verify the firmware or signing status.";
    }
  </script>
</body>
</html>
