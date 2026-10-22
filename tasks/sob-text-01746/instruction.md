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
819th Strategic Aerospace Division: The 819th Strategic Aerospace Division is an inactive United States Air Force organization.  Its last assignment was with Second Air Force of Strategic Air Command (SAC) at Dyess Air Force Base, Texas, where it was inactivated on 2 July 1966.

825th Strategic Aerospace Division: The 825th Strategic Aerospace Division is an inactive United States Air Force organization.  Its last assignment was with Strategic Air Command (SAC), assigned to Second Air Force at Little Rock Air Force Base, Arkansas, where it was inactivated on 1 January 1970.

820th Strategic Aerospace Division: The 820th Strategic Aerospace Division is an inactive United States Air Force organization.  Its last assignment was with Strategic Air Command (SAC)'s Eighth Air Force at Plattsburgh Air Force Base, New York, where it was inactivated on 25 June 1965.

4080th Strategic Reconnaissance Wing: The 4080th Strategic Reconnaissance Wing is a discontinued United States Air Force (USAF) wing last assigned to the 12th Strategic Aerospace Division of Strategic Air Command (SAC) at Davis-Monthan AFB, Arizona.  It was SAC's high altitude reconnaissance wing for its existence and was the first USAF wing to operate the Lockheed U-2.  It was discontinued as part of a program to replace operational units controlled by major commands with those controlled by USAF whose lineages could be continued,

818th Strategic Aerospace Division: The 818th Strategic Aerospace Division is an inactive United States Air Force organization.  Its last assignment was with Strategic Air Command at Lincoln Air Force Base, Nebraska, where it was inactivated on 25 March 1965.

Plattsburgh Air Force Base: Plattsburgh Air Force Base is a former United States Air Force Strategic Air Command (SAC) base covering 3,447 acres (13.7 km²) in the extreme northeast corner of New York, 20 miles (32 km) south of the Canada–United States border, located on the western shore of Lake Champlain opposite Burlington, Vermont, in the city of Plattsburgh, New York.

810th Strategic Aerospace Division: The 810th Strategic Aerospace Division is an inactive United States Air Force organization.  Its last assignment was with Strategic Air Command (SAC), assigned to Fifteenth Air Force at Minot Air Force Base, North Dakota, where it was inactivated on 30 June 1971.

395th Strategic Missile Squadron: The 395th Strategic Missile Squadron is an inactive United States Air Force unit.  Its last assignment was with the 1st Strategic Aerospace Division, based at Vandenberg AFB, California.  It was inactivated on 31 December 1969.

450th Bombardment Wing: The 450th Bombardment Wing is an inactive United States Air Force (USAF) unit.  It was last assigned to the 810th Strategic Aerospace Division of Strategic Air Command at Minot Air Force Base, North Dakota.  It was inactivated on 25 July 1968.

556th Strategic Missile Squadron: The 556th Strategic Missile Squadron (551 SMS) is an inactive United States Air Force unit.  It was last assigned to the 820th Strategic Aerospace Division, stationed at Plattsburgh AFB, New York.

Question: In which city did the 820th Strategic Aerospace Division occur?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "division_name": {
      "type": "string",
      "description": "The name of the strategic aerospace division."
    },
    "location": {
      "type": "object",
      "properties": {
        "base_name": {
          "type": "string",
          "description": "The name of the Air Force Base."
        },
        "city": {
          "type": "string",
          "description": "The city where the division was located."
        },
        "state": {
          "type": "string",
          "description": "The state where the division was located."
        }
      },
      "required": [
        "base_name",
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "inactivation_date": {
      "type": "string",
      "description": "The date when the division was inactivated."
    }
  },
  "required": [
    "division_name",
    "location",
    "inactivation_date"
  ],
  "additionalProperties": false
}
