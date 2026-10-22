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
Dilkon, Arizona: Dilkon (Navajo: ) is a census-designated place (CDP) in Navajo County, Arizona, United States.  The population was 1,265 at the 2000 census.  The name of the town is said to be derived from the Navajo phrase "smooth black rock" or "bare surface".

Oljato-Monument Valley, Arizona: Oljato-Monument Valley (Navajo: ) is a census-designated place (CDP) in Navajo County, Arizona, United States.  The population was 155 at the 2000 census.

Phoenix, Arizona: Phoenix ( ) is the capital and most populous city of the U.S. state of Arizona.  With 1,615,017 people (as of 2016 ), Phoenix is the fifth most populous city nationwide, the most populous state capital in the United States, and the only state capital with a population of more than one million residents.

Pinon, Arizona: Pinon (Navajo: ) is a census-designated place (CDP) in Navajo County, Arizona, United States, and on the Navajo Nation.  The population was 1,190 at the 2000 census.

Shonto, Arizona: Shonto (Navajo: ) is a census-designated place (CDP) in Navajo County, Arizona, United States.  The population was 568 at the 2000 census.

Keams Canyon, Arizona: Keams Canyon (Hopi: Pongsikya or Pongsikvi; Navajo: ) is a census-designated place (CDP) in Navajo County, Arizona, United States.  The population was 260 at the 2000 census.

Jeddito, Arizona: Jeddito (Navajo: ) is a census-designated place (CDP) in Navajo County, Arizona, United States.  The population was 390 at the 2000 census.

Kayenta, Arizona: Kayenta (Navajo: ) is a U.S. census-designated place (CDP) which is part of the Navajo Nation and is in Navajo County, Arizona.  The population was 5,189 at the 2010 census.  Kayenta is located 25 mi south of Monument Valley and contains a number of hotels and motels which service visitors to Monument Valley.  Like other places on the Navajo Nation, it is illegal to serve alcohol.  Arizona does not observe Daylight Time; however, the Navajo reservation does.

Greasewood, Arizona: Greasewood (Navajo: ) is a census-designated place (CDP) in Navajo County, Arizona, United States.  The population was 581 at the 2000 census.

Heber-Overgaard, Arizona: Heber-Overgaard is a census-designated place (CDP) in Navajo County, Arizona, United States.  Situated atop the Mogollon Rim, the community lies at an elevation of 6,627 ft .  The town is located approximately 144 miles (231.74 km) north of Phoenix, at the junction of SR 260 and SR 277, between Payson and Show Low, Arizona.  The population was 2,822 at the 2010 census.

Question: What U.S. state capitol has a population of more than one million residents and is 144 miles south of a census-designated place (CDP) in Navajo County?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "state_capital": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the U.S. state capital."
        },
        "population": {
          "type": "integer",
          "description": "The population of the state capital."
        },
        "population_exceeds_one_million": {
          "type": "boolean",
          "description": "True if the state capital's population is more than one million residents."
        }
      },
      "required": [
        "name",
        "population",
        "population_exceeds_one_million"
      ],
      "additionalProperties": false
    },
    "related_cdp": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the census-designated place (CDP)."
        },
        "county": {
          "type": "string",
          "description": "The county where the CDP is located."
        }
      },
      "required": [
        "name",
        "county"
      ],
      "additionalProperties": false
    },
    "distance_to_cdp_miles": {
      "type": "integer",
      "description": "The distance in miles between the state capital and the CDP."
    },
    "direction_from_cdp": {
      "type": "string",
      "enum": [
        "north",
        "south",
        "east",
        "west"
      ],
      "description": "The cardinal direction of the state capital relative to the CDP."
    }
  },
  "required": [
    "state_capital",
    "related_cdp",
    "distance_to_cdp_miles",
    "direction_from_cdp"
  ],
  "additionalProperties": false
}
