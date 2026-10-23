{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGasherbrum I: Gasherbrum I (Urdu: ‎ ; ), surveyed as K5 and also known as Hidden Peak, is the 11th highest mountain in the world at 8080 m above sea level.  It is located on the Pakistani–Chinese border in Gilgit–Baltistan region of Pakistan and Xinjiang region of China.  Gasherbrum I is part of the Gasherbrum massif, located in the Karakoram region of the Himalaya.  Gasherbrum is often claimed to mean \"Shining Wall\", presumably a reference to the highly visible face of the neighboring peak Gasherbrum IV; but in fact it comes from \"rgasha\" (beautiful) + \"brum\" (mountain) in Balti, hence it actually means \"beautiful mountain.\"\n\nCastle Rock Mountain: Castle Rock Mountain (12406 ft ) is in the Beartooth Mountains in the U.S. state of Montana.  The peak is one of the tallest in the Beatooth Mountains, the tenth-tallest in Montana and is in the Absaroka-Beartooth Wilderness, on the border of Custer and Gallatin national forests.  The nearest taller mountain to Castle Rock Mountain is Castle Rock Spire, 0.65 mi east.  Castle Rock Mountain is flanked by the Sundance Glacier to the north and the Castle Rock Glacier to the south.\n\nK2: K2 (Urdu: ‎ ), also known as Mount Godwin-Austen or Chhogori (Balti and Urdu: ‎ ), is the second highest mountain in the world, after Mount Everest, at 8611 m above sea level.  It is located on the China-Pakistan border between Baltistan, in the Gilgit-Baltistan region of northern Pakistan, and the Taxkorgan Tajik Autonomous County of Xinjiang, China.  K2 is the highest point of the Karakoram range and the highest point in both Pakistan and Xinjiang.\n\nGasherbrum: Gasherbrum (Urdu: گاشر برم‎ ) is a remote group of peaks located at the northeastern end of the Baltoro Glacier in the Karakoram range of the Himalaya on the border of the Chinese-administered Shaksgam Valley and the Gilgit-Baltistan territory of Pakistan.  The massif contains three of the world's 8,000 metre peaks (if Broad Peak is included).  Although the word \"Gasherbrum\" is often claimed to mean \"Shining Wall\", presumably a reference to the highly visible face of Gasherbrum IV, it comes from \"rgasha\" (beautiful) + \"brum\" (mountain) in Balti, hence it actually means \"beautiful mountain\".\n\nBurji La: Burji La (or Burji Pass) is a natural pass in mountains between Skardu and Deosai National Park in Gilgit Baltistan, Pakistan.  Its elevation is 4816 meters.  It is famous especially for its beautiful panoramic view of so many mountain peaks, including that of K2, Nanga Parbat, Masherbrum, Chogolisa, Laila Peak, Golden Peak, Gasherbrum I, Gasherbrum II, Gasherbrum IV and a part of Broad Peak mountain.\n\nGasherbrum III: Gasherbrum III (Urdu: گاشر برم -3‎ ; ), surveyed as K3a, is a summit in the Gasherbrum massif of the Baltoro Muztagh, a subrange of the Karakoram on the border between Xinjiang, China and Gilgit-Baltistan, Pakistan.  It is situated between Gasherbrum II and IV.\n\nMachulo La: Machulo La is a mountain view point which is considered the most easiest way to view some of the most highest peaks of Himalayas and Karakoram mountains in a single glance such as K2, Broad Peak, Gasherbrum-I, Gasherbrum-II, Gasherbrum III, Gasherbrum IV, K7, K6 and Nanga Parbat.\n\nHassan Sadpara: Hassan Sadpara PP (born Hassan Asad; April 1963 – 21 November 2016) was a Pakistani mountaineer and adventurer from Skardu in GB, Pakistan.  He is the first Pakistani to have climbed six eight-thousanders including the world's highest peak Everest (8848m) besides K2 (8611m), Gasherbrum I (8080m), Gasherbrum II (8034m), Nanga Parbat (8126 m), Broad Peak (8051m).  He is also credited for summiting five of the eight-thousanders without using supplemental oxygen.  Contrary to initial reports, Hassan Sadpara clarified that he used supplemental oxygen during his Everest ascent due to bad weather.  He died due to cancer on 21 November 2016 in Rawalpindi.\n\nNazir Sabir: Nazir Sabir Urdu: نذیر صابر is a Pakistani mountaineer.  He was born in Hunza.  He has climbed Mount Everest and four of the five 8000 m peaks in Pakistan, including the world's second highest mountain K2 in 1981, Gasherbrum II 8035m, Broad Peak 8050m in 1982, and Gasherbrum I (Hidden Peak) 8068m in 1992.  He became the first from Pakistan to have climbed Everest on 17 May 2000 as a team member on the Mountain Madness Everest Expedition led by Christine Boskoff from USA that also included famed Everest climber Peter Habeler of Austria and eight Canadians.\n\nKarakoram: The Karakoram, or Karakorum is a large mountain range spanning the borders of Pakistan, India, and China, with the northwest extremity of the range extending to Afghanistan and Tajikistan.  It is located in the regions of Gilgit–Baltistan (Pakistan), Ladakh (India), and southern Xinjiang (China), and reaches the Wakhan Corridor (Afghanistan).  A part of the complex of ranges from the Hindu Kush to the Himalayan Range, it is one of the Greater Ranges of Asia.  The Karakoram is home to the four most closely located peaks over 8000m in height on earth: K2, the second highest peak in the world at 8611 m , Gasherbrum I, Broad Peak and Gasherbrum II.\n\nQuestion: Which is a taller mountain, K2 or Gasherbrum III?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"mountains_compared\": {\n      \"type\": \"array\",\n      \"description\": \"List of mountains being compared for height.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the mountain.\"\n          },\n          \"height_meters\": {\n            \"type\": \"integer\",\n            \"description\": \"The height of the mountain in meters, if available in the context.\"\n          }\n        },\n        \"required\": [\n          \"name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"taller_mountain\": {\n      \"type\": \"object\",\n      \"description\": \"Details of the mountain determined to be taller.\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the taller mountain.\"\n        },\n        \"height_meters\": {\n          \"type\": \"integer\",\n          \"description\": \"The height of the taller mountain in meters.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"height_meters\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"comparison_conclusion\": {\n      \"type\": \"string\",\n      \"description\": \"A summary of the height comparison.\"\n    }\n  },\n  \"required\": [\n    \"mountains_compared\",\n    \"taller_mountain\",\n    \"comparison_conclusion\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "mountains_compared": {
        "type": "array",
        "description": "List of mountains being compared for height.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the mountain."
            },
            "height_meters": {
              "type": "integer",
              "description": "The height of the mountain in meters, if available in the context."
            }
          },
          "required": [
            "name"
          ],
          "additionalProperties": false
        }
      },
      "taller_mountain": {
        "type": "object",
        "description": "Details of the mountain determined to be taller.",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the taller mountain."
          },
          "height_meters": {
            "type": "integer",
            "description": "The height of the taller mountain in meters."
          }
        },
        "required": [
          "name",
          "height_meters"
        ],
        "additionalProperties": false
      },
      "comparison_conclusion": {
        "type": "string",
        "description": "A summary of the height comparison."
      }
    },
    "required": [
      "mountains_compared",
      "taller_mountain",
      "comparison_conclusion"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
