{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2014 Indian Super League Final: The 2014 Indian Super League Final was an association football match between the Kerala Blasters and Atlético de Kolkata, played on 20 December 2014, at the DY Patil Stadium in Navi Mumbai.  The match was the final match to determine the inaugural champion of the Indian Super League for the 2014 season.\n\nKerala Blasters FC results by opponent: The Kerala Blasters FC is an Indian football team founded in 2014, after the state of Kerala was awarded a Indian Super League (ISL) franchise.  The team began playing competitive football in the 2014 Indian Super League season.  They plays their home games at the Jawaharlal Nehru Stadium in Kochi.\n\nDimitar Berbatov: Dimitar Ivanov Berbatov (Bulgarian: Димитър Иванов Бербатов ] ; born 30 January 1981) is a Bulgarian professional footballer who plays for Indian Super League club Kerala Blasters.  A striker, he captained the Bulgaria national team from 2006 to 2010, and is the country's all-time leading goalscorer.  He has also won the Bulgarian Footballer of the Year a record seven times, surpassing the number of wins by Hristo Stoichkov.\n\nList of Kerala Blasters FC players: The Kerala Blasters FC are an Indian football team founded in 2014, after the state of Kerala was awarded an Indian Super League (ISL) franchise.  Kerala Blasters began playing competitive football in the 2014 season.  The team plays their home games at the Jawaharlal Nehru Stadium.\n\n2016 Kerala Blasters FC season: The 2016 Kerala Blasters FC season is the third season in the history of the Kerala Blasters, a franchise in the Indian Super League.\n\nFC Dorostol Silistra: FC Dorostol (Bulgarian: ФК Доростол ) is a Bulgarian football club based in Silistra, who currently plays at the North-East Third League, the third division of Bulgarian football.  Its home stadium \"Louis Ayer\" has a capacity of 12 000 seats.  Club colors are blue and white.  The club was officially founded in 1945.  However it exists informally from 1902, which makes it the oldest Bulgarian football club.\n\nList of Kerala Blasters FC managers: Kerala Blasters Football Club is an Indian professional football club based in Kochi, Kerala the club was established on 24 May 2014.  The Blasters compete in the Indian Super League, one of the top leagues of Indian football.The Blasters play home matches at the Jawaharlal Nehru Stadium in Kochi.\n\n2016 Indian Super League Final: The 2016 Indian Super League Final was a football match between Atlético de Kolkata and Kerala Blasters on 18 December 2016 at the Jawaharlal Nehru Stadium in Kochi, Kerala.  It was the final match of the 2016 Indian Super League season, the third season of the Indian Super League.  The match was the second time these two teams played each other in the Indian Super League final after both sides met in the inaugural 2014 final.  Atlético de Kolkata won that final 1–0.\n\nAna-Maria Yanakieva: Ana-Maria Yanakieva (Bulgarian: Ана-Мария Янакиева , born 5 August 1998) is a Bulgarian singer from the music label Virginia Records, the official representative of Sony Music Entertainment for Bulgaria.  She is also a scholar of Dimitar Berbatov Foundation.  Ana-Maria is a finalist from Season 2 of X Factor Bulgaria, which took place in 2013.  She is one of the most talented and promising Bulgarian young singers as considered by many music professionals in Bulgaria.\n\nKerala Blasters FC: Kerala Blasters Football Club is an Indian professional football club based in Kochi, Kerala.  The Blasters compete in the Indian Super League, one of the top leagues of Indian football.  The club was established on 24 May 2014 and began their first professional season a few months later in October 2014.  The team name comes from one of their owners, former Indian cricketer Sachin Tendulkar, who was known as the \"Master Blaster\" during his playing days.\n\nQuestion: For which accomplishment in Bulgarian football is the professional footballer who plays for Indian Super League club Kerala Blasters, and whose name is used for the Foundation where Ana-Maria Yanakieva, a singer from the music label Virginia Records was a scholar, considered the all-time leader?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the professional footballer.\"\n    },\n    \"player_club\": {\n      \"type\": \"string\",\n      \"description\": \"The Indian Super League club the player plays for.\"\n    },\n    \"foundation_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the foundation associated with the player.\"\n    },\n    \"accomplishment_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of accomplishment (e.g., 'national team record').\"\n    },\n    \"accomplishment_detail\": {\n      \"type\": \"string\",\n      \"description\": \"The specific accomplishment for which the player is the all-time leader.\"\n    },\n    \"accomplishment_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country for which the accomplishment is recorded.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"player_club\",\n    \"foundation_name\",\n    \"accomplishment_type\",\n    \"accomplishment_detail\",\n    \"accomplishment_country\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the professional footballer."
      },
      "player_club": {
        "type": "string",
        "description": "The Indian Super League club the player plays for."
      },
      "foundation_name": {
        "type": "string",
        "description": "The name of the foundation associated with the player."
      },
      "accomplishment_type": {
        "type": "string",
        "description": "The type of accomplishment (e.g., 'national team record')."
      },
      "accomplishment_detail": {
        "type": "string",
        "description": "The specific accomplishment for which the player is the all-time leader."
      },
      "accomplishment_country": {
        "type": "string",
        "description": "The country for which the accomplishment is recorded."
      }
    },
    "required": [
      "player_name",
      "player_club",
      "foundation_name",
      "accomplishment_type",
      "accomplishment_detail",
      "accomplishment_country"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
