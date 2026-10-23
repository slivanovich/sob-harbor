{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMigration to Abyssinia: The Migration to Abyssinia (Arabic: الهجرة إلى الحبشة‎ ‎ , \"al-hijra ʾilā al-habaša\"), also known as the First Hegira (Arabic: هِجْرَة‎ ‎ \"hijrah\"), was an episode in the early history of Islam, where Prophet Muhammad's first followers (the \"Sahabah\") fled from the persecution of the ruling Quraysh tribe of Mecca.  They sought refuge in the Christian Kingdom of Aksum, present-day Ethiopia and Eritrea (formerly referred to as Abyssinia, a name derived from the Arabic \"Al-Habash\"), in 9 BH (613 CE) or 7 BH (615 CE) .  The Aksumite monarch who received them is known in Islamic sources as the Negus (Arabic: نجاشي‎ ‎ \"najāšī\") \"Ashama ibn Abjar\".  Modern historians have alternatively identified him with King Armah and Ella Tsaham.  Some of the exiles returned to Mecca and made the hijra to Medina with Muhammad, while others remained in Abyssinia until they came to Medina in 628.\n\nRobert Browne Hall: Robert Browne Hall (30 June 1858 Bowdoinham, Maine – 8 June 1907), usually known as R. B. Hall, was a leading composer of marches and other music for brass bands.  A principal American composer of marching music, he was born in Bowdoinham, Maine and seldom left his native state during his lifetime, dying in Portland.  His music though has traveled around the world.  He is particularly popular in the United Kingdom, so much so that many lovers of brass band music there mistakenly imagine that Hall is an English composer.  His celebrated march \"Death or Glory\", written in 1895 and dedicated to the Tenth Regiment Band in Albany, New York, is a well-known staple of brass band concerts and competitions all over the UK.\n\nJakuren: Jakuren (寂蓮 ) (also known as Fujiwara no Sadanaga (藤原定長) before becoming a monk) (1139–1202) was a Japanese Buddhist priest and poet.  He was adopted by the noted poet Fujiwara no Shunzei upon the death of Shunzei's younger brother.  Shunzei originally intended for Sadanaga to be his heir; however, he subsequently had two male offspring of his own, and Sadanaga was forced to step aside in favor of Fujiwara no Sadaie.  As was common practice at the time, he became a monk, and acquired the religious name of Jakuren.  Taking Saigyo as his model, he traveled around the country, composing poems of his travels.  He was well regarded in his time and frequently associated with Fujiwara no Teika.  He was one of the six compilers of the eighth imperial \"waka\" anthology, the famous \"Shin Kokin Wakashū\", and thirty-five of his poems were selected for the work.  Before he died, he adopted Fujiwara no Ietaka, pupil to Shunzei.  One of his poems was included in the famous poetry anthology \"Hyakunin Isshu.\"\n\nPrajnatara: Prajñātārā, also known as Keyura, was the twenty-seventh Brahmin patriarch of Indian Buddhism according to Chan Buddhism and the head of the Sarvastivada sect of early Buddhist schools.  She traveled around East India preaching Buddhism.  Prajñātārā was Bodhidharma's teacher.\n\nRobert Edison Fulton Jr.: Robert Edison Fulton Jr. (April 15, 1909 – May 7, 2004) was an American inventor and adventurer.  He is known for having traveled around the world on a motorcycle and for several aviation-related inventions, among his 70 patents.  Fulton was also a professional photographer.\n\nEthiopian Empire: The Ethiopian Empire (Amharic: ), also known as Abyssinia (derived from the Arabic \"al-Habash\"), was a kingdom that spanned a geographical area in the current state of Ethiopia.  It existed from approximately 1137 (beginning of Zagwe dynasty) until 1974, when the Solomonic dynasty was overthrown in a coup d'état.\n\nItalo-Yemeni Treaty: The Italo-Yemeni Treaty of 1926 (also known as the Treaty of San'a) was a treaty between the Kingdom of Italy and Mutawakkilite Kingdom of Yemen.  The treaty was signed in September 1926 and was described as a friendship treaty.  At the time, Italy was ruled by the fascist National Fascist Party with Benito Mussolini as head of government.  The treaty recognized Imam Yahya Muhammad Hamid ed-Din as King of Yemen and acknowledged his claims to Aden.  The treaty was renewed on October 15, 1937, after Italy had annexed Abyssinia (present-day Ethiopia).\n\nMansfield Parkyns: Mansfield Parkyns (16 February 1823 – 12 January 1894) was an English traveller, known for his travel book \"Life in Abyssinia: being notes collected during three years' residence and travels in that country\" (1853).  In this book he described his experiences and observations during three years (1843–1846) travels in Abyssinia, the modern territories of Eritrea and Ethiopia.\n\nSecond Italo-Ethiopian War: The Second Italo-Ethiopian War, also referred to as the Second Italo-Abyssinian War, was a colonial war from 3 October 1935 to 5 May 1936 between the armed forces of the Kingdom of Italy and those of the Ethiopian Empire (also known as Abyssinia).  Ethiopia was defeated, annexed and subjected to military occupation until the defeat of Italy in East Africa in 1941, during the East African Campaign of the Second World War.\n\nSizwe Zakho: Sizwe Zakho is a South African born music producer, he is known for producing artists like Rebecca Malope, Israel Mosehla and worked with a whole host of other gospel.  He also traveled around the continent of Africa hosting workshops on gospel music.  Zakho's distinct style of producing has seen a massive turn around in the South African gospel scene in such a way that many upcoming musicians aspired to work with him.\n\nQuestion: What was the kingdom that Mansfield Parkyns traveled around and is also known as Abyssinia?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"traveler_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who traveled.\"\n    },\n    \"kingdom_name\": {\n      \"type\": \"string\",\n      \"description\": \"The official name of the kingdom or empire.\"\n    },\n    \"alternative_kingdom_name\": {\n      \"type\": \"string\",\n      \"description\": \"Another name by which the kingdom was known.\"\n    },\n    \"travel_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"duration_years\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of years the traveler spent in the country.\"\n        },\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the travel period.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the travel period.\"\n        },\n        \"book_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the book written about the travels.\"\n        }\n      },\n      \"required\": [\n        \"duration_years\",\n        \"start_year\",\n        \"end_year\",\n        \"book_title\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"traveler_name\",\n    \"kingdom_name\",\n    \"alternative_kingdom_name\",\n    \"travel_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "traveler_name": {
        "type": "string",
        "description": "The name of the person who traveled."
      },
      "kingdom_name": {
        "type": "string",
        "description": "The official name of the kingdom or empire."
      },
      "alternative_kingdom_name": {
        "type": "string",
        "description": "Another name by which the kingdom was known."
      },
      "travel_details": {
        "type": "object",
        "properties": {
          "duration_years": {
            "type": "integer",
            "description": "The number of years the traveler spent in the country."
          },
          "start_year": {
            "type": "integer",
            "description": "The start year of the travel period."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of the travel period."
          },
          "book_title": {
            "type": "string",
            "description": "The title of the book written about the travels."
          }
        },
        "required": [
          "duration_years",
          "start_year",
          "end_year",
          "book_title"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "traveler_name",
      "kingdom_name",
      "alternative_kingdom_name",
      "travel_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
