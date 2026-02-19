<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />


  <!-- Google Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
    }

    body {
      background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
      color: #fff;
      line-height: 1.6;
    }

    .container {
      max-width: 1000px;
      margin: auto;
      padding: 20px;
    }

    header {
      text-align: center;
      padding: 60px 20px;
    }

    header h1 {
      font-size: 3rem;
      font-weight: 700;
      letter-spacing: 1px;
    }

    header p {
      margin-top: 10px;
      font-size: 1.2rem;
      color: #cfd8dc;
    }

    section {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(10px);
      padding: 25px;
      margin-bottom: 25px;
      border-radius: 12px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }

    section h2 {
      margin-bottom: 15px;
      font-weight: 600;
      color: #00e5ff;
    }

    ul {
      padding-left: 20px;
    }

    li {
      margin-bottom: 8px;
    }

    .skills {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 15px;
    }

    .card {
      background: rgba(0,0,0,0.35);
      padding: 15px;
      border-radius: 10px;
      transition: transform 0.25s ease, background 0.25s ease;
    }

    .card:hover {
      transform: translateY(-6px);
      background: rgba(0,0,0,0.6);
    }

    footer {
      text-align: center;
      padding: 30px 10px;
      color: #b0bec5;
    }

    a {
      color: #00e5ff;
      text-decoration: none;
      font-weight: 500;
    }

    a:hover {
      text-decoration: underline;
    }

    @media (max-width: 600px) {
      header h1 { font-size: 2.2rem; }
    }
  </style>
</head>
<body>
  <div class="container">

  <header>
      <h1>Harsh Tiwari</h1>
      <p>Aspiring Data Scientist • Python Developer • Trader</p>
    </header>

  <section>
      <h2>About Me</h2>
      <p>
        Hey! I'm Harsh Tiwari, an 18-year-old student who isn’t interested in traditional academics. I’m fascinated by dark, unsettling topics — the kind of stories that scare people, make them emotional, and keep them awake at night. I’m also passionate about trading in the forex and crypto markets. I’ve been consistently profitable in my paper trading accounts, achieving my target monthly profit of 20% within the first 12–13 working days, with an accuracy rate of around 60%.
      </p>
    </section>

  <section>
      <h2>Academics</h2>
      <ul>
        <li><strong>10th:</strong> 82.66% (Math: 87, Science: 83, English: 71)</li>
        <li><strong>12th:</strong> 67.67% (Math: 60, Physics: 64, Chemistry: 76)</li>
      </ul>
    </section>

  <section>
      <h2>Skills</h2>
      <div class="skills">
        <div class="card">Python (NumPy, Pandas, Matplotlib, Seaborn, Tkinter)</div>
        <div class="card">HTML & CSS</div>
        <div class="card">JavaScript (Beginner)</div>
        <div class="card">Trading & Market Analysis</div>
      </div>
    </section>

  <section>
      <h2>Contact</h2>
      <p>Email: harsh.tiwari7112@gmail.com</p>
      <p>
        Instagram: <a href="https://www.instagram.com/geld_zuerst/" target="_blank">@geld_zuerst</a><br>
        GitHub: <a href="https://github.com/Harsh7112" target="_blank">Harsh7112</a>
      </p>
    </section>

  <footer>
      <p>© 2026 Harsh Tiwari — Built with ambition 🚀</p>
    </footer>

  </div>
</body>
</html>
