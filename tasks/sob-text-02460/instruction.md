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
List of female movie actors by name: M: This is an alphabetical list of notable female movie actors with a last name that begins with the letter M.

List of female movie actors by name: L: This is an alphabetical list of notable female movie actors with a last name that begins with the letter L.

Creature from the Black Lagoon (pinball): Creature from the Black Lagoon is a pinball machine designed by John Trudeau ("Dr. Flash") and released by Midway (under the "Bally" brand name).  It is loosely based on the movie of the same name.  The game's theme is 1950's drive-in theater.  The pinball machine was licensed from Universal Studios by Bally so that the backglass artwork, the cabinet artwork, and the creature looked like the original movie actors and monsters.

List of female movie actors by name: T–V: This is an alphabetical list of notable female movie actors with a last name that begins with the letter T, U, or V.

Armand Assante: Armand Anthony Assante Jr. (born October 4, 1949) is an American actor.  He is noted for an Emmy Award-winning role as mobster John Gotti in the 1996 HBO miniseries "Gotti".

List of female movie actors by name: P–Q: This is an alphabetical list of notable female movie actors with a last name that begins with the letter P or Q.

List of female movie actors by name: S: This is an alphabetical list of notable female movie actors with a last name that begins with the letter S.

The Hunley: The Hunley is a 1999 television movie directed by John Gray and starring Armand Assante, Donald Sutherland, Alex Jennings, Michael Dolan and Christopher Bauer.  The film is based on the true story of the "H. L. Hunley" submarine and the Action of 17 February 1864.

List of female movie actors by name: R: This is an alphabetical list of notable female movie actors with a last name that begins with the letter R.

List of female movie actors by name: N–O: This is an alphabetical list of notable female movie actors with a last name that begins with the letter N or O.

Question: What was the name of the TV series that one of the Hunley movie actors won an Emmy for?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who won the Emmy."
    },
    "movie_title": {
      "type": "string",
      "description": "The title of the movie the actor was in."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award won."
        },
        "series_name": {
          "type": "string",
          "description": "The name of the TV series or miniseries for which the award was won."
        },
        "series_type": {
          "type": "string",
          "description": "The type of the series (e.g., miniseries)."
        },
        "award_year": {
          "type": "integer",
          "description": "The year the award-winning series was released or the award was given."
        },
        "role_description": {
          "type": "string",
          "description": "Description of the role for which the award was won."
        }
      },
      "required": [
        "award_name",
        "series_name",
        "series_type",
        "award_year",
        "role_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "movie_title",
    "award_details"
  ],
  "additionalProperties": false
}
