{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRavi Teja: Ravi Teja (born 26 January 1967 ) and popularly referred to as \"Mass Maharaja\" is an Indian film actor known for his work in Telugu cinema.  He is widely considered one of the most popular and highest paid actors of Telugu cinema, who has appeared in over sixty films.  He won the Nandi Special Jury Award in 1999 and 2002 for his performance in the films \"Nee Kosam\" (1999) and \"Khadgam\" (2002) and also won the state Nandi Award for best actor for his film \"Neninthe\" in 2008.\n\nRam Charan: Ram Charan is an Indian film actor, dancer, producer, businessman and entrepreneur, who works in Telugu cinema.  He won two Nandi Awards, two South Filmfare awards, two CineMAA Awards, and two Santosham Best Actor Awards. Charan is one of the highest paid actors in Tollywood.\n\nWu Xiubo: Wu Xiubo (), (born 5 September 1968), is a Chinese actor, musician and producer.  He is perhaps most widely known as Xinjie Liu, the protagonist in the TV series \"Before the Dawn\", for which he received several awards.  Other prominent dramas in which he had a starring role include \"The Wedding Gown\", \"Sword & Spy\", \"To the Oak\", \"The Brotherhood\", \"Road May Say\", and \"Invincible Love\".  He is currently one of the highest paid actors on Chinese television.\n\nIrtiqa: Irtiqa (Urdu: ارتقاء, literal English translation: \"evolution\") is the debut album by the Pakistani rock band, Entity Paradigm.  It was originally slated for a 25 September 2003 release date, but was delayed to 1 October.  Entity Paradigm released singles from \"Irtiqa\" which were \"Hamesha,\" \"Hamein Aazma\", \"Kahan Hai Tu\", \"Aghosh\", \"Waqt\" and \"Irtiqa III\"; the videos for \"Waqt\" and \"Irtiqa III\" were directed by Xulfi himself.\n\nList of awards and nominations received by Rekha: Rekha is an Indian film actress who primarily works in Hindi films. Hailed as one of India's finest actresses, she made her debut as a child artist in 1966 and went on to appear in lead roles in the early 1970s.  Since her debut as a leading actress she has acted in over 180 films.  Rekha has often portrayed strong female characters, while also acting in some arthouse films besides numerous mainstream cinema.  She has won four Filmfare Awards; two Best Actress Awards—resulting from seven nominations, one Best Supporting Actress Award—resulting from six nominations, and a Lifetime Achievement Award.  The first award came in 1981 for the Hrishikesh Mukherjee-directed \"Khubsoorat\" where she was cast in a comic role.  Her portrayal of a classical courtesan in \"Umrao Jaan\" (1981) fetched her the National Film Award for Best Actress in 1982.  Rekha received her second Filmfare award in 1989 for \"Khoon Bhari Maang\".  She portrayed the role of a widow who sets out to take revenge on her lover.  Her negative role in \"Khiladiyon Ka Khiladi\" was highly appreciated by the critics and earned her a Filmfare Award in the Best Supporting Actress category.  In 2003, she was presented with the Lifetime Achievement Award.  In 2010, Rekha was awarded the Padma Shri, the 4th highest civilian honour in India.  Other awards won by her include International Indian Film Academy Awards, Bengal Film Journalists' Association Awards, Star Screen Awards, Zee Cine Awards, Stardust Awards and Bollywood Movie Awards.\n\nKajol: Kajol (born Kajol Mukherjee; 5 August 1974), also known by her married name Kajol Devgan, is an Indian film actress, who predominantly works in Hindi cinema.  Born in Mumbai to the Mukherjee-Samarth family, she is the daughter of actress Tanuja Samarth and late filmmaker Shomu Mukherjee.  One of India's most successful and highest paid actresses in the 90s, Kajol is the recipient of numerous accolades, including six Filmfare Awards, among twelve nominations.  Along with her late aunt Nutan, she holds the record for most Best Actress wins at Filmfare, with five.  In 2011, the Government of India awarded her with the Padma Shri, the fourth highest civilian honour of the country.\n\nShor Macha: \"Shor Macha\" (Urdu: شور مچا, literal English translation: \"make noise\") is a song by the Pakistani rock band Entity Paradigm.  It is the overall seventh single release by the band, and also being the first single since their comeback in 2009.  On August 13, 2010, Entity Paradigm released \"Shor Macha\" as the first single from their upcoming second studio album, the music video of the song was a dedication to all Pakistanis.  The music video of the song was sponsored by djuice and directed by Bilal Lashari.\n\nFawad Khan: Fawad Afzal Khan (born 29 November 1981) is a Pakistani actor, model and singer who appears in Pakistani films, previously being appeared widely in Pakistani dramas and also in Hindi films.  He is one of the highest paid actors in the industry and is the recipient of several awards including a Filmfare Award, 3 Lux Style Awards, and 6 Hum Awards.\n\nBrahmanandam: Brahmanandam Kanneganti (born 1 February 1956) is an Indian film actor and comedian, known for his works predominantly in Telugu cinema.  He currently holds the Guinness World Record for the most screen credits for a living actor.  He was honoured with the Padma Shri, for his contribution to Indian cinema in 2009.  Brahmanandam is regarded as one of the finest comic actors of India, noted particularly for his comic expressions.  He has acted in more than 1100 films till date and has been one of the highest paid comedy actors in Indian Cinema.  Brahmanandam has garnered five state Nandi Awards, one Filmfare Award South, six CineMAA Awards, and three South Indian International Movie Awards for best comedy.  Race Gurram (2014) was his 987th film.\n\nAjab Tamasha: \"Ajab Tamasha\" (literal English translation: \"Strange Circus\") is a song by the Pakistani rock band Entity Paradigm.  The song along with the music video was released on 21 December 2012 as part of the band's tenth anniversary.This is the first single released after the departure of Fawad Khan, who left to focus on his acting career and Drummer ‘’’Waqar Khan’’’ who left because he moved from Lahore to Islamabad.\n\nQuestion: Who is one of the highest paid actors in the industry and is the recipient of several awards including a Filmfare Award, who left Entity Paradigm before the release of \"Strange Circus\" ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor.\"\n    },\n    \"is_highest_paid_actor\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the actor is one of the highest paid in the industry.\"\n    },\n    \"awards_summary\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"has_filmfare_award\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the actor has received a Filmfare Award.\"\n        },\n        \"other_awards_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The total count of other specific awards mentioned.\"\n        },\n        \"other_award_names\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of names of other specific awards received by the actor.\"\n        }\n      },\n      \"required\": [\n        \"has_filmfare_award\",\n        \"other_awards_count\",\n        \"other_award_names\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"band_affiliation\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"band_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band the actor was previously affiliated with.\"\n        },\n        \"departure_event\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the event or release that occurred after the actor's departure from the band.\"\n        },\n        \"departure_reason\": {\n          \"type\": \"string\",\n          \"description\": \"The stated reason for the actor's departure from the band.\"\n        }\n      },\n      \"required\": [\n        \"band_name\",\n        \"departure_event\",\n        \"departure_reason\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"is_highest_paid_actor\",\n    \"awards_summary\",\n    \"band_affiliation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor."
      },
      "is_highest_paid_actor": {
        "type": "boolean",
        "description": "Indicates if the actor is one of the highest paid in the industry."
      },
      "awards_summary": {
        "type": "object",
        "properties": {
          "has_filmfare_award": {
            "type": "boolean",
            "description": "Indicates if the actor has received a Filmfare Award."
          },
          "other_awards_count": {
            "type": "integer",
            "description": "The total count of other specific awards mentioned."
          },
          "other_award_names": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of names of other specific awards received by the actor."
          }
        },
        "required": [
          "has_filmfare_award",
          "other_awards_count",
          "other_award_names"
        ],
        "additionalProperties": false
      },
      "band_affiliation": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band the actor was previously affiliated with."
          },
          "departure_event": {
            "type": "string",
            "description": "The name of the event or release that occurred after the actor's departure from the band."
          },
          "departure_reason": {
            "type": "string",
            "description": "The stated reason for the actor's departure from the band."
          }
        },
        "required": [
          "band_name",
          "departure_event",
          "departure_reason"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "is_highest_paid_actor",
      "awards_summary",
      "band_affiliation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
