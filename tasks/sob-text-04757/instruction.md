{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSubhash Shinde: Subhash Shinde is an Indian make-up artist.  Subhash Shinde has worked with many leading actresses in Bollywood, including Priyanka Chopra in the film \"Mary Kom\".  Stars including Sridevi, Aishwarya Rai Bachchan, Priyanka Chopra, Radhika Apte, Shraddha Kapoor in the film \"Haseena\" have worked with him.  Although he usually does makeup for women.  Subhash Shinde is known as the prosthetics king as it is not commonly used amongst Indian Make-up Artists\n\nRohan Mapuskar: Rohan Mapuskar is a Mumbai based casting director and associate director who has cast actors for movies like 3 idiots, Ferrari ki Sawaari, Shivaay and .  He has worked with Vinod Chopra Films for 9 years.  Mapuskar is credited with the casting for Ventilator, directed by Rajesh Mapuskar, and featuring more than 100 actors including Jitendra Joshi and Ashutosh Gowariker.  The film was produced by Priyanka Chopra and Dr. Madhu Chopra.\n\nDon (soundtrack): Don is the soundtrack album to 2006 Hindi film of the same name, directed by Farhan Akhtar starring Shahrukh Khan, Priyanka Chopra and Boman Irani.  The music was released on 26 August on T-Series and sold over 10,000 copies in India.\n\nIn My City: \"In My City\" is the debut single by Indian recording artist and actress Priyanka Chopra, featuring American rapper will.i.am.  The song was produced by RedOne, Rush and Brian Kennedy, and was co-written by Ester Dean, who provides additional vocals.  The demo version of \"In My City\" was first played by will.i.am to Chopra, who was impressed with the track and decided to record it.  The song is a homage to Chopra's nomadic childhood and journey from being a small-town girl to being a successful actor.  \"In My City\" premiered on 13 September 2012, at the NFL Network's \"Thursday Night Football\".  The next day, the song was released for digital downloads to Nokia Music Store along with CD single.\n\nPriyanka Chopra: Priyanka Chopra (] ; born 18 July 1982) is an Indian actress, singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.  One of India's highest-paid and most popular celebrities, Chopra has received numerous awards, including a National Film Award and five Filmfare Awards.  In 2016, the Government of India honoured her with the Padma Shri, the fourth highest civilian award, and \"Time\" magazine named her one of the 100 most influential people in the world.\n\nDeewana Main Deewana: Deewana Main Deewana is a 2013 Bollywood romantic comedy film starring Govinda, Priyanka Chopra, Kader Khan, Prem Chopra, Johnny Lever and Shakti Kapoor directed by K. C. Bokadia.  The film was released worldwide on 1 February 2013.  This film was shot approximately in 2003 but release was delayed.The film is a Hindi remake of Tamil film Priyamudan directed by Vincent Selva.\n\nExotic (song): \"Exotic\" is the second single by Indian recording artist Priyanka Chopra featuring American rapper Pitbull.  \"Exotic\" is to be featured on Chopra's upcoming debut studio album; the song was released by Interscope Records on July 9, 2013 as the lead single from the album.  \"Exotic\" was written by Chopra, Pitbull and RedOne, who also produced the song.  It contains both English and Hindi lyrics.\n\nBam Bam Bol Raha Hai Kashi: Bam Bam Bol Raha Hai Kashi is a 2016 Indian, bhojpuri language film directed by Santosh Mishra And Produced By Dr.Madhu Chopra,Priyanka Chopra.\n\nPriyanka Chopra filmography: Priyanka Chopra is an Indian actress who has established herself as a leading actress of Indian cinema.  She made her Bollywood debut in 2003 spy thriller \"\".  The same year, Chopra's role in the box-office hit musical \"Andaaz\" won her the Filmfare Award for Best Female Debut.  In 2004, she starred in the highly successful comedy \"Mujhse Shaadi Karogi\" and garnered critical acclaim for her breakthrough role in the thriller \"Aitraaz\" which earned her the Filmfare Award for Best Performance in a Negative Role and a second Best Supporting Actress nomination.  Chopra starred in six films in 2005, including \"\" and \"Bluffmaster! \".  In 2006, she starred in two of the highest-grossing films of the yearthe superhero film \"Krrish\" and the action thriller \"Don\".\n\nMannara Chopra: Mannara Chopra (born 29 March 1991) is an Indian film actress and model who predominantly works in Hindi and Telugu films.  She is the cousin of Bollywood actresses Priyanka Chopra, Parineeti Chopra, and Meera Chopra.  She made her Bollywood debut with the film \"Zid\" (2014).\n\nQuestion: What country is home to both Don and Priyanka Chopra?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the country that is home to both entities.\"\n    },\n    \"associated_entities\": {\n      \"type\": \"array\",\n      \"description\": \"A list of entities (person, film, etc.) associated with the country.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"entity_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the entity.\"\n          },\n          \"entity_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of the entity (e.g., 'person', 'film', 'soundtrack').\"\n          }\n        },\n        \"required\": [\n          \"entity_name\",\n          \"entity_type\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"reasoning_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A brief summary of the reasoning for identifying the country.\"\n    }\n  },\n  \"required\": [\n    \"country_of_origin\",\n    \"associated_entities\",\n    \"reasoning_summary\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "country_of_origin": {
        "type": "string",
        "description": "The name of the country that is home to both entities."
      },
      "associated_entities": {
        "type": "array",
        "description": "A list of entities (person, film, etc.) associated with the country.",
        "items": {
          "type": "object",
          "properties": {
            "entity_name": {
              "type": "string",
              "description": "The name of the entity."
            },
            "entity_type": {
              "type": "string",
              "description": "The type of the entity (e.g., 'person', 'film', 'soundtrack')."
            }
          },
          "required": [
            "entity_name",
            "entity_type"
          ],
          "additionalProperties": false
        }
      },
      "reasoning_summary": {
        "type": "string",
        "description": "A brief summary of the reasoning for identifying the country."
      }
    },
    "required": [
      "country_of_origin",
      "associated_entities",
      "reasoning_summary"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
