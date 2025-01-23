import os
import google.generativeai as genai

genai.configure(api_key=["AIzaSyAooNcS_-7pgX0JbX4rAc3p1pr5ryHJUOQ"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  upload_to_gemini("image_croissant.jpeg", mime_type="image/jpeg"),
]

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        files[0],
        "Given this image:\n\n1. First, describe the image\n2. Then, detail the recipe to bake this item in JSON format. Include item names and quantities for the recipe",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Certainly! Here's the analysis and recipe based on the image you provided.\n\n**1. Image Description:**\n\nThe image showcases a close-up, slightly high-angle view of a basket filled with freshly baked croissants. The croissants are a rich golden brown, indicating they've been baked to perfection. They are flaky, layered, and have the classic curved shape, with some displaying a more pointed end and others more rounded. The light glistens off their surface, enhancing their appealing, buttery texture. They are densely packed within the basket, creating a sense of abundance and warmth. The basket itself appears to be a light-colored woven material, providing a neutral background that highlights the golden hues of the croissants. There's also a slight depth of field effect, with the background slightly blurred, which puts the focus directly on the croissants in the foreground.\n\n**2. Recipe in JSON format:**\n\n```json\n{\n  \"recipe_name\": \"Classic French Croissants\",\n  \"description\": \"A recipe for making flaky, buttery croissants.\",\n  \"ingredients\": [\n    {\n      \"item\": \"All-purpose flour\",\n      \"quantity\": \"500 grams\"\n    },\n    {\n      \"item\": \"Instant dry yeast\",\n      \"quantity\": \"10 grams\"\n    },\n    {\n      \"item\": \"Granulated sugar\",\n      \"quantity\": \"50 grams\"\n    },\n    {\n      \"item\": \"Salt\",\n      \"quantity\": \"10 grams\"\n    },\n    {\n      \"item\": \"Whole milk\",\n      \"quantity\": \"250 ml\"\n    },\n    {\n       \"item\": \"Water\",\n       \"quantity\":\"120 ml\"\n    },\n    {\n      \"item\": \"Unsalted butter (cold)\",\n      \"quantity\": \"350 grams\"\n    },\n    {\n      \"item\": \"Egg\",\n      \"quantity\": \"1 large (for egg wash)\"\n    }\n   \n  ],\n   \"instructions\": [\n    \"In a large bowl, whisk together flour, instant dry yeast, sugar, and salt.\",\n    \"In a saucepan, heat milk and water until lukewarm. Add this to the flour mixture.\",\n      \"Mix to form a shaggy dough. Transfer the dough onto a floured surface and knead for about 8-10 minutes, or until smooth. Form it into a ball, place in a lightly greased bowl, cover and let rise at room temperature for about 1 hour, until doubled.\",\n    \"Gently press out the dough to deflate. Shape into a rectangle. Wrap the dough in plastic wrap and chill in the refrigerator for 2 hours.\",\n      \"Take out the cold butter, place in between plastic wrap and with a rolling pin, shape it into a rectangle, about 2/3 the size of the dough.\",\n    \"Place the butter on the middle of the dough rectangle. Fold the sides of the dough over the butter to seal it in. Pinch the edges to avoid butter from escaping\",\n    \"Roll the dough out to a long rectangle. Fold the dough in thirds. This completes the first 'turn'.\",\n     \"Wrap the dough in plastic wrap and refrigerate for 30-45 minutes. \",\n     \"Repeat the rolling and folding process two more times for a total of three turns, chilling the dough between each turn. After the last turn, wrap the dough and refrigerate for 2-3 hours or overnight.\",\n    \"Remove the dough from the refrigerator and roll out to about 4-5 mm thick. Cut into triangles using a knife or a pizza cutter.\",\n     \"Beginning at the base of each triangle, gently roll them up into croissant shape. Place on a baking sheet lined with parchment paper, leaving room between the croissants.\",\n    \"Lightly beat the egg, and use a brush to coat the tops of the croissants evenly. Let proof at room temperature for 1-2 hours, or until puffed up.\",\n    \"Preheat the oven to 200°C (400°F).\",\n    \"Bake for 15-20 minutes, or until golden brown. Let cool slightly before serving.\"\n\n  ],\n    \"notes\": \"Ensure butter is cold to create layers. The chilling is important for best results. Adjust baking time based on your oven.\"\n}\n```\n\nLet me know if you have any other requests!",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)