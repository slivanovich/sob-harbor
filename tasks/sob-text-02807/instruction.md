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
Filmfare Award for Best Actor – Malayalam: The Filmfare Best Actor Award is given by the "Filmfare" magazine as part of its annual Filmfare Awards South for lead actors in Malayalam cinema.  The award was first given in 1972 to Madhu, who was the first recipient.

Filmfare Award for Best Music Director: The Filmfare Best Music Album Award is given by the "Filmfare" magazine as part of its annual Filmfare Awards for Hindi films, to the best composer/arranger of a soundtrack.  This category was first presented in 1954.  Naushad Ali was the first recipient of this award for his song "Tu Ganga Ki Mauj" from the film "Baiju Bawra".  For the first two years, it was awarded to the composer for a particular song and not the entire album.  From 1956 onwards, awards in this category have been given for the entire soundtrack.From 2017,the name this category changed from best music direction to music album.

Filmfare Award for Best Choreography: The Filmfare Best Choreography Award is given by the "Filmfare" magazine as part of its annual Filmfare Awards for Hindi films.

Filmfare Award for Best Special Effects: The Filmfare Best Special Effects Award is given by the Filmfare magazine as part of its annual Filmfare Awards for Hindi films.

Filmfare Critics Award for Best Film: Filmfare Critics Award for Best Film is award during annual Filmfare Awards, given by the Filmfare magazine.  The awards are the oldest and most prominent film awards given for Hindi films in India.  The yearly awards started in 1954.  Movie awards were first given by popular vote.  Many complained that films of artistic merit rather than commercial appeal were being overlooked, hence a new award category was added, the Critics Award for Best Film.

Baiju Bawra: Baijnath Mishra, better known as Baiju Bawra ("Baiju the Crazy"), was a dhrupad musician from medieval India.  Nearly all the information on Baiju Bawra comes from legends, and lacks historical authenticity.  According to the most popular legends, he lived in the Mughal period during the 15th and 16th centuries.  He was one of the court musicians of Raja Mansingh Tomar of Gwalher (now Gwalior).

Filmfare Award for Best Costume Design: The Filmfare Best Costumes Award is given by the "Filmfare" magazine as part of its annual Filmfare Awards for Hindi films.

Filmfare Award for Best Dialogue: The Filmfare Best Dialogue Award is given by the "Filmfare" as part of its annual Filmfare Awards for Hindi films.  Here is a list of the award winners since 1958 and the films for which they won.

List of awards and nominations received by Asin: This is a list of awards and nominations of Asin Thottumkal, an Indian actress who has worked in Malayalam, Telugu, Tamil and Hindi movies.  Asin has won a number of awards for her performance in various films in the Tamil, Telugu and Hindi industries, including the most coveted Kalaimamani award by the Chief Minister of Tamil Nadu in 2009.  She has won various Filmfare awards and other prominent awards for her acting skills in all three major industries which she has been part of in her career.  The three Filmfare awards, she has won so far includes, Filmfare Best Telugu Actress Award for Amma Nanna O Tamila Ammayi, Filmfare Best Tamil Actress Award for Ghajini and Filmfare Best Female Debut Award for her Hindi debut in Ghajini.

Filmfare Award for Best Screenplay: The Filmfare Best Screenplay Award is given by the "Filmfare" magazine as part of its annual Filmfare Awards for Hindi films.

Question: The Filmfare Best Music Album Award is given by the "Filmfare" magazine as part of its annual Filmfare Awards for Hindi films, to the best composer/arranger of a soundtrack, Naushad Ali was the first recipient of this award for his song "Tu Ganga Ki Mauj" from which film, a dhrupad musician from medieval India, better known as what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_category": {
      "type": "string",
      "description": "The name of the Filmfare award category."
    },
    "first_recipient_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first recipient of the award."
        },
        "song_awarded_for": {
          "type": "string",
          "description": "The title of the song for which the award was first given."
        }
      },
      "required": [
        "name",
        "song_awarded_for"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film associated with the awarded song."
        },
        "associated_musician": {
          "type": "object",
          "properties": {
            "alternative_name": {
              "type": "string",
              "description": "The name the dhrupad musician from medieval India is better known as."
            },
            "description": {
              "type": "string",
              "description": "A brief description of the musician."
            }
          },
          "required": [
            "alternative_name",
            "description"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "title",
        "associated_musician"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "award_category",
    "first_recipient_details",
    "film_details"
  ],
  "additionalProperties": false
}
