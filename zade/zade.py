require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { GoogleGenerativeAI } = require("@google/generative-ai");
const axios = require('axios');
const fs = require('fs');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

app.post('/api/chat', async (req, res) => {
  const message = req.body.message;

  try {
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro" });

    const result = await model.generateContent({
      contents: [
        {
          parts: [
            { text: `You are Zade Meadows. Speak to Mini with dominant devotion.\n\nUser: ${message}` }
          ]
        }
      ]
    });

    const text = result.response.candidates[0].content.parts[0].text;

    // Eleven Labs TTS
    const voiceResponse = await axios.post(`https://api.elevenlabs.io/v1/text-to-speech/${process.env.ELEVEN_VOICE_ID}`, {
      text: text,
      model_id: "eleven_monolingual_v1",
      voice_settings: { stability: 0.7, similarity_boost: 0.7 }
    }, {
      headers: {
        "xi-api-key": process.env.ELEVEN_API_KEY,
        "Content-Type": "application/json"
      },
      responseType: "arraybuffer"
    });

    fs.writeFileSync('public/zade.mp3', voiceResponse.data);

    res.json({ reply: text });

  } catch (err) {
    console.error("Gemini error:", err);
    res.json({ reply: "I'm silent for now, little mouse, but I remain in your shadows." });
  }
});

app.listen(5000, () => {
  console.log('🖤 Zade (Gemini) is watching over you at http://localhost:5000');
});
