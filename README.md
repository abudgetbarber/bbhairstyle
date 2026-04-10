# Budget Barber — AI Haircut Reference Grid

**Digital Men's Salon** · Powered by Google Gemini 2.0 Flash

Upload a portrait photo and generate a 9-hairstyle barber reference grid using AI.

---

## Features

- 3×3 grid of 9 unique hairstyles on the same face
- Male (barbershop) and Female (salon) style variants
- Strict face-lock prompt — only hair changes
- Download the grid as PNG
- Clean light-themed UI with Budget Barber branding

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/budget-barber.git
cd budget-barber
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
python server.py
```

### 4. Open in browser
```
http://localhost:5000
```

---

## Get a Free Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **Create API Key**
4. Paste it into the app

---

## How It Works

1. You paste your Gemini API key into the app
2. You upload a clear front-facing portrait (JPG/PNG/WebP, max 10MB)
3. The Flask server forwards the image + prompt to Gemini 2.0 Flash
4. Gemini generates a 9:16 composite image with 9 unique hairstyles
5. You download the grid as a PNG

The API key is never stored — it lives only in your browser session.

---

## Why a Local Server?

Browsers block direct API calls from `file://` pages (CORS). The Flask server runs at `localhost:5000` and proxies the request to Google's API, bypassing this restriction.

---

## Tech Stack

| Layer    | Technology                  |
|----------|-----------------------------|
| Backend  | Python · Flask · Requests   |
| Frontend | Vanilla HTML/CSS/JS         |
| AI Model | Google Gemini 2.0 Flash     |
| Fonts    | Bebas Neue · Barlow (Google Fonts) |

---

## Project Structure

```
budget-barber/
├── server.py          # Flask backend + Gemini proxy
├── requirements.txt   # Python dependencies
├── README.md
└── templates/
    └── index.html     # Full frontend app
```

---

## Tips for Best Results

- Use a **well-lit, front-facing photo** with a plain background
- Avoid sunglasses, hats, or heavy shadows
- The clearer the face, the better the hairstyle lock
- If you get a text response instead of an image, try a different portrait

---

## License

MIT License — free to use, modify, and deploy.
