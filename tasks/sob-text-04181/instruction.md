{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAloinopsis: Aloinopsis is a genus of ice plants from South Africa.\n\nAloinopsis malherbei: Aloinopsis malherbei is a species of succulent plant, also known as the \"Giant Jewel plant\".  It is native to the Cape Provinces of South Africa, especially the area around Calvinia and Loeriesfontein.  The plant produces a thick tuber and produces yellow flowers.  Unlike other Aloinopsis, it only has tubercles (bumps) at the leaf tips.\n\nCaryocar amygdaliferum: Caryocar amygdaliferum is a plant native to the rain forests of the Choco region of Colombia and Panama.  Its fruit consists of a spiny husk inside which a seed about three times the size of an almond develops.  It has been used for similar purpose as the almond and was traded as a luxury item among the Inca in pre-conquest times and grown in the land of the Chachapoyas.  It is also eaten by some species of bats.\n\nAloinopsis rosulata: Aloinopsis rosulata is a species of succulent plant, native to Southern Africa.  It is a wintergrower, and produces a thick tuber.  The flowers are pale pink with red stripes.\n\nAlmond milk: Almond milk is a plant milk manufactured from almonds with a creamy texture and nutty taste.  It contains neither cholesterol nor lactose, and is often consumed by those who are lactose-intolerant and others who wish to avoid dairy products, including vegans.  Commercial almond milk comes in sweetened, unsweetened, plain, vanilla and chocolate flavors, and is usually enriched with vitamins.  It can also be made at home using a blender, almonds and water.  It is traditionally consumed through much of the Mediterranean.\n\nBinky (polar bear): Binky (1975 – July 20, 1995) was a polar bear who lived at the Alaska Zoo in Anchorage.  He was originally orphaned near Cape Beaufort, close to the Chukchi Sea, but was found by a driller in Northwest Alaska named David Bergsrud.  The area where Binky was located is known to those living outside of Alaska as the North Slope.  Alaska Fish and Game was contacted shortly after Binky's discovery, and arrangements were being made to find a zoo in the Lower 48.  Anchorage had a small zoo at the time, with an elephant that a lady had won and a few other animals.  When word got around that a polar bear cub had been found, folks started hunting for ways to stall the effort of sending Binky outside of Alaska.  Time was needed to find a sponsor to fund an enclosure at the Alaska Children's Zoo for Binky.  Alaska Fish and Game employees came up with the idea of flying Binky to a number of the inland North Slope villages.  School was let out in these villages so all the children could come to the airstrips to see Binky.  These received major news coverage.  Finally things fell into place to allow the Anchorage zoo to take Binky.  Binky quickly became one of its most popular attractions.  He became a local hero and received international news coverage after mauling two zoo visitors in separate incidents in 1994.  Binky died in 1995 from sarcocystosis, a parasitic disease.\n\nAloinopsis setifera: Aloinopsis setifera is a species of succulent plant, native to Southern Africa.\n\nAlmond: The almond (\"Prunus dulcis\", syn.  \"Prunus amygdalus\") is a species of tree native to the Middle East, the Indian subcontinent and North Africa.\n\nMorris Almond: Morris Almond (born February 2, 1985) is an American former professional basketball player.  Almond is the founder of Almond Athletics.  His last professional appearance would be for the Los Angeles D-Fenders of the NBA Development League (D-League).\n\nBrabejum: Brabejum is a genus of a single species of large evergreen tree, Brabejum stellatifolium in the Proteaceae, commonly called wild almond, bitter almond or ghoeboontjie.  It is restricted in the wild to South Africa's Western Cape Province, where it grows in thickets along the banks of streams.  The plant is of botanical interest as being Africa's only member of the large grevilleoid subfamily.  It is a bushy small tree with branches widely at ground level and numerous erect vigorous stems.  Leaves to 6 in (15 cm) long, narrow and bluntly toothed, appear at intervals along the branches, mostly in whorls of 6.  In summer, the plant bears white flowers densely crowded on spikes arising from rusty buds at the leaf axils.  The fruits to 2 in (5 cm) long, magenta to reddish brown, similar to an almond, appear in autumn.  The nut is too bitter to eat; however, in earlier times it was boiled, roasted, and ground to make a \"coffee\" drink.\n\nQuestion: Would you find the Almond plant and Aloinopsis in alaska?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed by the user.\"\n    },\n    \"answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the plants are found in Alaska, false otherwise.\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for the answer based on the provided context.\"\n    },\n    \"plants_information\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each plant mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"plant_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the plant.\"\n          },\n          \"native_regions\": {\n            \"type\": \"array\",\n            \"description\": \"List of native regions for the plant as per context.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          },\n          \"found_in_alaska\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the context states the plant is found in Alaska.\"\n          }\n        },\n        \"required\": [\n          \"plant_name\",\n          \"native_regions\",\n          \"found_in_alaska\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"answer\",\n    \"reasoning\",\n    \"plants_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed by the user."
      },
      "answer": {
        "type": "boolean",
        "description": "True if the plants are found in Alaska, false otherwise."
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for the answer based on the provided context."
      },
      "plants_information": {
        "type": "array",
        "description": "Details about each plant mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "plant_name": {
              "type": "string",
              "description": "The name of the plant."
            },
            "native_regions": {
              "type": "array",
              "description": "List of native regions for the plant as per context.",
              "items": {
                "type": "string"
              }
            },
            "found_in_alaska": {
              "type": "boolean",
              "description": "Indicates if the context states the plant is found in Alaska."
            }
          },
          "required": [
            "plant_name",
            "native_regions",
            "found_in_alaska"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "question_asked",
      "answer",
      "reasoning",
      "plants_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
