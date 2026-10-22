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
2016 Stockton ATP Challenger: The 2016 Stockton ATP Challenger was a professional tennis tournament played on hard courts.  It was the first edition of the tournament which was part of the 2016 ATP Challenger Tour.  It took place in Stockton, United States between 1 October and 9 October 2016.

Happy Valley, South Australia: Happy Valley is a metropolitan suburb of Adelaide, South Australia.  It is located 20 km south of the Central Business District of Adelaide.

2016 Poprad-Tatry ATP Challenger Tour: The 2016 Poprad-Tatry ATP Challenger Tour was a professional tennis tournament played on clay courts.  It was the second edition of the tournament which was part of the 2016 ATP Challenger Tour.  It took place in Poprad, Slovakia between 13 and 18 June 2016.

2016 Santaizi ATP Challenger: The 2016 Santaizi ATP Challenger was a professional tennis tournament played on indoor carpet courts.  It was the third edition of the tournament which was part of the 2016 ATP Challenger Tour.  It took place in Taipei, Taiwan between 25 April and 1 May.

2016 Gemdale ATP Challenger: The 2016 Gemdale ATP Challenger was a professional tennis tournament played on hard courts.  It was the third edition of the tournament which was part of the 2016 ATP Challenger Tour.  It took place in Shenzhen, China between 21 and 27 March 2016.

2016 ATP Challenger Torino: The 2016 ATP Challenger Torino was a professional tennis tournament played on clay courts.  It was the second edition of the tournament which was part of the 2016 ATP Challenger Tour.  It took place in Turin, Italy between 18 and 24 April.

2016 City of Onkaparinga ATP Challenger: The 2016 City of Onkaparinga ATP Challenger was a professional tennis tournament played on hard courts.  It was the second edition of the tournament which was part of the 2016 ATP Challenger Tour.  It took place in Happy Valley, Australia between 2–10 January 2016.

2016 Latrobe City Traralgon ATP Challenger: The 2016 Latrobe City Traralgon ATP Challenger is a professional tennis tournament played on outdoor hard court.  It is the fifth edition of the tournament which was part of the 2016 ATP Challenger Tour.  It took place in Traralgon, Australia between 24–30 October 2016.

2015 City of Onkaparinga ATP Challenger: The 2015 City of Onkaparinga ATP Challenger was a professional tennis tournament played on hard courts.  It was the first edition of the tournament which was part of the 2015 ATP Challenger Tour.  It took place in Happy Valley, Australia between 3–11 January 2015.

2017 City of Onkaparinga ATP Challenger: The 2017 City of Onkaparinga ATP Challenger was a professional tennis tournament played on hard courts.  It was the third edition of the tournament and part of the 2017 ATP Challenger Tour.  It took place in Happy Valley, Australia from 2 to 8 January 2017.

Question: The 2016 City of Onkaparinga ATP Challenger took place in a metropolitan suburb how far south of the Central Business District of Adelaide?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tournament_name": {
      "type": "string",
      "description": "The name of the tennis tournament."
    },
    "location_suburb": {
      "type": "string",
      "description": "The suburb where the tournament took place."
    },
    "distance_from_adelaide_cbd_km": {
      "type": "integer",
      "description": "The distance in kilometers from the Central Business District of Adelaide."
    },
    "direction_from_adelaide_cbd": {
      "type": "string",
      "description": "The cardinal direction from the Central Business District of Adelaide."
    }
  },
  "required": [
    "tournament_name",
    "location_suburb",
    "distance_from_adelaide_cbd_km",
    "direction_from_adelaide_cbd"
  ],
  "additionalProperties": false
}
