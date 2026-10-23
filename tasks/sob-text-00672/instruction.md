{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTakri alphabet: The Takri script (sometimes called \"Tankri\") is an abugida writing system of the Brahmic family of scripts.  It is closely related to, and derived from, the Sharada script employed by Kashmiri.  It is also related to the Gurmukhī script used to write Punjabi.  Until the late 1940s, And adopted version script of Takri (called Dogri, Dogra or Dogra Akhtar)was the official script for writing the Dogri in the state of Jammu and Kashmir and Kangri, Cahmbeali, Mandeali in Himachal Pradesh.  There are some record of using Takri script in the history of Nepali (Khas Kura).  Takri has historically been used by a number of Western Pahari, Garhwali and Dardic languages in the Western Himalayas, such as Gaddi or Gaddki (the language of the Gaddi ethnic group), Kashtwari (the dialect centered on the Kashtwar or Kishtwar region of Jammu and Kashmir) and Chamiyali (the language of the Chamba region of Himachal Pradesh).  Takri used to be most prevalent script for business records and communication in various parts of Himachal Pradesh including Chintpurni, Una, Kangra, Bilaspur and Hamirpur regions.  The aged businessmen can still be found using Takri in these areas, but newer generation has now shifted to Devanagari and even English (Roman).  This shift can be traced to have happened during the period ranging from 1950s to 1980s.\n\nMountains of Bhutan: The mountains of Bhutan are some of the most prominent natural geographic features of the kingdom.  Located on the southern end of the Eastern Himalaya, Bhutan has one of the most rugged mountain terrains in the world, whose elevations range from 160 m to more than 7,000 m above sea level, in some cases within distances of less than 100 km of each other.  Bhutan's highest peak, at 7,554 m above sea level, is north-central Kula Kangri, close to the border with China; the second highest peak, Jomolhari, overlooking the Chumbi Valley in the west, is 7,314 m above sea level; nineteen other peaks exceed 7,000 m .  Weather is extreme in the mountains: the high peaks have perpetual snow, and the lesser mountains and hewn gorges have high winds all year round, making them barren brown wind tunnels in summer, and frozen wastelands in winter.  The blizzards generated in the north each winter often drift southward into the central highlands.\n\nChangtse: Changtse (Tibetan: \"north peak\") is a mountain situated between the Main Rongbuk and East Rongbuk Glaciers in Tibet, China, immediately north of Mount Everest.  It is connected to Mount Everest via the North Col.\n\nMishmi Hills: The Mishmi Hills, known in China as the Qilinggong Mountains (), are a southern extension of the Kangri Garpo mountains and are claimed by India and China.  The distinction between the Mishmi Hills and the Kangri Garpo is not well-defined, and may follow the McMahon Line.  On the Indian side, the Mishmi Hills are located at the northeastern tip of the country, in central Arunachal Pradesh.  On the Chinese side, they form the southern parts of Nyingchi Prefecture in the Tibet Autonomous Region.\n\nTeram Kangri: The Teram Kangri group is a mountain massif in the remote Siachen Muztagh, a subrange of the Karakoram range.  The high point of the group, and of the Siachen Muztagh, is Teram Kangri I.  The peak lies on the boundary between China and the disputed Siachen Glacier region near the line of control between India and Pakistan.  The northeast side of the peak is in Chinese-controlled territory, the southwest side in the disputed Siachen area currently controlled by India.\n\nKangri Garpo: Kangri Garpo () is a mountain range in eastern Tibet, located primarily in Nyingchi Prefecture as well as a portion of Qamdo Prefecture in the Tibet Autonomous Region, China.  The mountain range lies to the east of the Himalayas and to the west of the Hengduan Mountains.  The mountains are geographically a southern extension of the eastern Transhimalayas.\n\nNarendra Kumar (mountaineer): Colonel Narendra \"Bull\" Kumar (also spelled \"Narinder\"; born 8 December 1933) is an Indian soldier-mountaineer.  He is known for the mountaineering reconnaissance expedition he undertook in Teram Kangri, Siachen Glacier and Saltoro Range for Indian Army in 1978 at the age of 45.  If he had not undertaken this expedition, all of Siachen Glacier would be Pakistan's.  That is an area covering almost 10000 km2 , but because of his expedition, India conquered all the entire area.  Kumar crossed seven mountain ranges—Pir Panjal Range, Himalayas, Zanskar, Ladakh, Saltoro, Karakoram and Agil—to give India Siachen.\n\n1950 Assam–Tibet earthquake: The 1950 Assam–Tibet earthquake, also known as the Assam earthquake, occurred on 15 August and had a moment magnitude of 8.6.  The epicentre was located in the Mishmi Hills, known in Chinese as the Qilinggong Mountains (祁灵公山), south of the Kangri Garpo and just east of the Himalayas in the North-East Frontier Agency part of Assam, India.  This area, south of the McMahon Line and now known as Arunachal Pradesh, is today disputed between China and India.  The earthquake was destructive in both Assam (India) and Tibet (China), and approximately 4,800 people were killed.  The earthquake is notable as being the largest recorded quake caused by continental collision rather than subduction, and is also notable for the loud noises produced by the quake and reported throughout the region.\n\nKangri dialect: Kangri is a dialect spoken in northern India, predominantly in the Kangra, Hamirpur, Bilaspur, Una districts and some parts of Mandi and Chamba district of Himachal Pradesh and in the Pathankot, Gurdaspur and Hoshiarpur districts in the Punjab state.  It is associated with the people of the Kangra Valley.  It is an Indo-Aryan dialect, closely related to Dogri and today classified as one of the Western Pahari (पहाड़ी) group of languages, with some influence in vocabulary Standard Punjabi (Majhi).  which is spoken to the west in the state of Punjab.  Kangri, along with Dogri, has been classified as a dialect of Punjabi by linguists but since the 1960s, both have been recognised as dialects of a separate language group called Pahari.\n\nGhent Kangri: Ghent Kangri (or Mount Ghent, Ghaint I) is a high peak near the north end of the Saltoro Mountains, a subrange of the Karakoram range.  It is located west of the Siachen Glacier in an area under Pakistan control, but very close to the Actual Ground Position Line with India.\n\nQuestion: Are Changtse and Teram Kangri both related to mountains?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_entities\": {\n      \"type\": \"array\",\n      \"description\": \"List of entities mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"Name of the entity.\"\n          },\n          \"type\": {\n            \"type\": \"string\",\n            \"description\": \"Classification of the entity based on the context (e.g., mountain, mountain massif).\"\n          },\n          \"is_mountain_related\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the entity is explicitly described as a mountain or part of a mountain range.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"type\",\n          \"is_mountain_related\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"all_entities_are_mountain_related\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if all specified entities are related to mountains, false otherwise.\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation of why the entities are or are not related to mountains.\"\n    }\n  },\n  \"required\": [\n    \"question_entities\",\n    \"all_entities_are_mountain_related\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_entities": {
        "type": "array",
        "description": "List of entities mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "Name of the entity."
            },
            "type": {
              "type": "string",
              "description": "Classification of the entity based on the context (e.g., mountain, mountain massif)."
            },
            "is_mountain_related": {
              "type": "boolean",
              "description": "Indicates if the entity is explicitly described as a mountain or part of a mountain range."
            }
          },
          "required": [
            "name",
            "type",
            "is_mountain_related"
          ],
          "additionalProperties": false
        }
      },
      "all_entities_are_mountain_related": {
        "type": "boolean",
        "description": "True if all specified entities are related to mountains, false otherwise."
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation of why the entities are or are not related to mountains."
      }
    },
    "required": [
      "question_entities",
      "all_entities_are_mountain_related",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
