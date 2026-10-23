{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBurji La: Burji La (or Burji Pass) is a natural pass in mountains between Skardu and Deosai National Park in Gilgit Baltistan, Pakistan.  Its elevation is 4816 meters.  It is famous especially for its beautiful panoramic view of so many mountain peaks, including that of K2, Nanga Parbat, Masherbrum, Chogolisa, Laila Peak, Golden Peak, Gasherbrum I, Gasherbrum II, Gasherbrum IV and a part of Broad Peak mountain.\n\nThe Dark Glow of the Mountains: The Dark Glow of the Mountains (Gasherbrum - Der Leuchtende Berg) is a TV documentary made in 1984 by German filmmaker Werner Herzog.  It is about an expedition made by freestyle mountain climber Reinhold Messner and his partner Hans Kammerlander to climb Gasherbrum II and Gasherbrum I all in one trip without returning to base camp.  The film is not so much concerned with showing the climb itself or giving guidelines on mountaineering, but seeks to reveal the inner motivation of the climbers.\n\nHassan Sadpara: Hassan Sadpara PP (born Hassan Asad; April 1963 – 21 November 2016) was a Pakistani mountaineer and adventurer from Skardu in GB, Pakistan.  He is the first Pakistani to have climbed six eight-thousanders including the world's highest peak Everest (8848m) besides K2 (8611m), Gasherbrum I (8080m), Gasherbrum II (8034m), Nanga Parbat (8126 m), Broad Peak (8051m).  He is also credited for summiting five of the eight-thousanders without using supplemental oxygen.  Contrary to initial reports, Hassan Sadpara clarified that he used supplemental oxygen during his Everest ascent due to bad weather.  He died due to cancer on 21 November 2016 in Rawalpindi.\n\nNazir Sabir: Nazir Sabir Urdu: نذیر صابر is a Pakistani mountaineer.  He was born in Hunza.  He has climbed Mount Everest and four of the five 8000 m peaks in Pakistan, including the world's second highest mountain K2 in 1981, Gasherbrum II 8035m, Broad Peak 8050m in 1982, and Gasherbrum I (Hidden Peak) 8068m in 1992.  He became the first from Pakistan to have climbed Everest on 17 May 2000 as a team member on the Mountain Madness Everest Expedition led by Christine Boskoff from USA that also included famed Everest climber Peter Habeler of Austria and eight Canadians.\n\nGasherbrum III: Gasherbrum III (Urdu: گاشر برم -3‎ ; ), surveyed as K3a, is a summit in the Gasherbrum massif of the Baltoro Muztagh, a subrange of the Karakoram on the border between Xinjiang, China and Gilgit-Baltistan, Pakistan.  It is situated between Gasherbrum II and IV.\n\nSiguang Ri: Siguang Ri is a mountain in the Mahalangur Himalayas of Tibet, China.  At an elevation of 7308 m it is the 83rd highest peak on Earth.  It is located approximately 6 kilometers NNE of Cho Oyu, the world's 6th highest mountain.\n\nJi Hyeon-ok: Ji Hyeon-ok (Hangul: 지현옥 ) (1959-1999) was a South Korean mountaineer.  Born in Nonsan, she climbed several of the tallest mountains in the world, including Denali (Mount McKinley) in 1988, Mount Everest, in 1993, becoming the first Korean woman to do so, Gasherbrum I, in 1997 and Gasherbrum II, in 1998.\n\nLeila Esfandyari: Leila Esfandyari (Persian: لیلا اسفندیاری‎ ‎ ; Feb 17, 1970 in Karaj, Iran – July 22, 2011, Gasherbrum II, Pakistan) was an Iranian mountain climber.  Esfandyari was the first Iranian woman to scale the summit of Nanga Parbat in the Himalayas, the world’s ninth highest peak with an altitude of 8,125 metres and one of the deadliest peaks.  Esfandyari is regarded as a pioneer in the women’s mountain climbing movement, being one of few women in the world to have completed a similar attempt.\n\nGasherbrum II: Gasherbrum II (Urdu: ‎ ); surveyed as K4, is the 13th highest mountain in the world at 8035 m above sea level.  It is the third-highest peak of the Gasherbrum massif, and is located in the Karakoram, on the border between Gilgit–Baltistan province, Pakistan, and Xinjiang, China.  The mountain was first climbed on July 7, 1956, by an Austrian expedition which included Fritz Moravec, Josef Larch, and Hans Willenpart.\n\nKarakoram: The Karakoram, or Karakorum is a large mountain range spanning the borders of Pakistan, India, and China, with the northwest extremity of the range extending to Afghanistan and Tajikistan.  It is located in the regions of Gilgit–Baltistan (Pakistan), Ladakh (India), and southern Xinjiang (China), and reaches the Wakhan Corridor (Afghanistan).  A part of the complex of ranges from the Hindu Kush to the Himalayan Range, it is one of the Greater Ranges of Asia.  The Karakoram is home to the four most closely located peaks over 8000m in height on earth: K2, the second highest peak in the world at 8611 m , Gasherbrum I, Broad Peak and Gasherbrum II.\n\nQuestion: Siguang Ri and Gasherbrum II, are located in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"mountains\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\"\n          },\n          \"location_countries\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"location_countries\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_location_country\": {\n      \"type\": \"string\"\n    },\n    \"is_border_peak_involved\": {\n      \"type\": \"boolean\"\n    }\n  },\n  \"required\": [\n    \"mountains\",\n    \"common_location_country\",\n    \"is_border_peak_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "mountains": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "location_countries": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "name",
            "location_countries"
          ],
          "additionalProperties": false
        }
      },
      "common_location_country": {
        "type": "string"
      },
      "is_border_peak_involved": {
        "type": "boolean"
      }
    },
    "required": [
      "mountains",
      "common_location_country",
      "is_border_peak_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
