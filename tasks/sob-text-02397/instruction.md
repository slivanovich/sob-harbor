Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Jordan at the 2002 Asian Games: Jordan participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Jordan won overall two medals, all bronze, and clinched 34th spot in the medal table.

Macau at the 2002 Asian Games: Macau participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Macau won overall four medals, and clinched 29th spot in the medal table.

Laos at the 2002 Asian Games: Laos participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Laos won overall two medals, all bronze, and clinched 34th spot in the medal table.

2002 Asian Games medal table: The 2002 Asian Games (officially known as the 14th Asian Games) was a multi-sport event held in Busan, South Korea from September 29 to October 14, 2002.  Busan was the second South Korean city to host the Games, after Seoul in 1986.  A total of 6,572 athletes—4,605 men and 1,967 women—from 44 Asian National Olympic Committees (NOCs) participated in 38 sports divided into 419 events.  The number of competing athletes was higher than the 1998 Asian Games, in which 6,544 athletes from 41 NOCs participated.  It was the first time in the history of the Asian Games that all 44 member nations of the Olympic Council of Asia (OCA) participated in the Games.  Afghanistan returned after the fall of the Taliban government in the midst of ongoing war; East Timor, newest member of the OCA made its debut; and North Korea competed for the first time in an international sporting event hosted by South Korea.  Both nations marched together at the opening ceremony with a Korean Unification Flag depicting the Korean Peninsula as United Korea.

Hong Kong at the 2002 Asian Games: Hong Kong participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Hong Kong won overall 21 medals (including four golds), and clinched 16th spot in the medal table.

Mongolia at the 2002 Asian Games: Mongolia participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Mongolia won overall 14 medals (including one gold), and clinched 26th spot in the medal table.

Vietnam at the 2002 Asian Games: Vietnam participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Vietnam won overall 18 medals (including four golds), and clinched 15th spot in the medal table.

Lebanon at the 2002 Asian Games: Lebanon participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Lebanon won only one gold, and clinched 27th spot in the medal table.

Singapore at the 2002 Asian Games: Singapore participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Singapore won overall 17 medals (including five golds), and clinched 13th spot in the medal table.

Qatar at the 2002 Asian Games: Qatar participated in the 2002 Asian Games held in Busan, South Korea, from September 29 to October 14, 2002.  Athletes from Qatar won overall 17 medals (including four golds), and clinched 17th spot in the medal table.

Question: Mongolia at the 2002 Asian Games clinched the 26th spot in this multi sport event held where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The official name of the multi-sport event."
    },
    "participating_nation": {
      "type": "string",
      "description": "The nation whose performance is being queried."
    },
    "medal_table_rank": {
      "type": "integer",
      "description": "The rank of the participating nation in the medal table."
    },
    "host_city": {
      "type": "string",
      "description": "The city where the event was held."
    },
    "host_country": {
      "type": "string",
      "description": "The country where the event was held."
    }
  },
  "required": [
    "event_name",
    "participating_nation",
    "medal_table_rank",
    "host_city",
    "host_country"
  ],
  "additionalProperties": false
}
