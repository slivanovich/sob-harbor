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
Angel's Son: "Angel's Son" is a song written by Mikey Doling, Clint Lowery, Morgan Rose, Lajon Witherspoon of Sevendust and performed by Witherspoon and two fellow Sevendust members (drummer Morgan Rose and guitarist/vocalist Clint Lowery) and ex-Snot band member (now ex-Sevendust guitarist) Sonny Mayo, for the post-mortem compilation CD in honor of James Lynn Strait known as "Strait Up".  This was the only single track from the tribute album.

Lajon Witherspoon: Lajon "LJ" Jermaine Witherspoon (born October 3, 1972) is an American musician best known as the vocalist for the Atlanta-based alternative metal band Sevendust.

Reese Witherspoon: Laura Jeanne Reese Witherspoon ( ; born March 22, 1976) is an American actress, producer, and entrepreneur.  Born in New Orleans and raised in Tennessee, she began her career as a child actress, making her professional screen debut in "The Man in the Moon" (1991), for which she was nominated for a Young Artist Award.  Following breakout roles in "" (1992) and "Jack the Bear" (1993), she starred in the comedy-drama "Pleasantville" (1998), for which she won the Young Hollywood Award for Breakthrough Performance.  Her leading role of Tracy Flick in "Election" (1999) was nominated for a Golden Globe Award.

Moon Hee-joon: Moon Hee-joon (; or spelled Moon Hee-jun; born March 14, 1978) is a South Korean pop-rock singer-songwriter signed under SidusHQ.  He initially rose to fame as the leader of former boy band H.O.T. under SM Entertainment.

Sevendust: Sevendust is an American alternative metal band from Atlanta, Georgia, formed in 1994 by bassist Vince Hornsby, drummer Morgan Rose and guitarist John Connolly.  After their first demo, lead vocalist Lajon Witherspoon and guitarist Clint Lowery joined the group.  Following a few name changes, the members settled on the name Sevendust and released their self-titled debut album on April 15, 1997.  They have attained success with three consecutive RIAA gold certified albums and have sold millions of albums worldwide.

Seasons (Sevendust album): Seasons is the fourth studio album by American heavy metal band Sevendust.  It would be the band's final album with TVT Records and was dedicated to the memory of Reginald Witherspoon (Lajon Witherspoon's younger brother) and Dave Williams (Drowning Pool's original singer), the former was murdered in November 2002 and the latter died of cardiomyopathy in August 2002.

Moment of Impact (album): Moment of Impact is the debut studio album by American rock group Eye Empire.  A Limited Edition 1000 copies were released on December 12, 2010 with a full release on September 14, 2011.  It features guest appearances from singer Lajon Witherspoon and drummer Morgan Rose of Sevendust.  It was later released as an expanded edition double album, with the title shortened to "Impact".

Prodigal Son (Sevendust song): Prodigal Son is the first single by the heavy metal band Sevendust from their seventh studio album "" and was written by vocalist Lajon Witherspoon and drummer Morgan Rose.  The song premiered on Active and Mainstream Rock radio on February 10, 2008.

The Past (song): "The Past" is the second single from the "" album produced by the American heavy metal band Sevendust.  This power ballad, with lead vocals from Lajon Witherspoon and featuring guest vocals by lead vocalist of the band "Daughtry", Chris Daughtry, is a bit of a departure for the band, falling more into the post-grunge category than what fans have come to expect from Sevendust.  "Sorrow", another song found on "", is similar in tone and also contains guest vocals, this time by Myles Kennedy.  Sevendust has not yet created a music video for "The Past".

100 People, 100 Songs: 100 People, 100 Songs () was a 2014 South Korean singing competition program presented by Kim Sung-joo, Jang Yun-jeong and Moon Hee-joon.  It aired on JTBC from October 31, 2014 to September 27, 2015.

Question: Who was born most recently, Moon Hee-joon or Lajon Witherspoon?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_comparison": {
      "type": "object",
      "properties": {
        "person_1": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the first person being compared."
            },
            "birth_date": {
              "type": "string",
              "format": "date",
              "description": "The full birth date of the first person (YYYY-MM-DD)."
            },
            "birth_year": {
              "type": "integer",
              "description": "The birth year of the first person."
            }
          },
          "required": [
            "name",
            "birth_date",
            "birth_year"
          ],
          "additionalProperties": false
        },
        "person_2": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the second person being compared."
            },
            "birth_date": {
              "type": "string",
              "format": "date",
              "description": "The full birth date of the second person (YYYY-MM-DD)."
            },
            "birth_year": {
              "type": "integer",
              "description": "The birth year of the second person."
            }
          },
          "required": [
            "name",
            "birth_date",
            "birth_year"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "person_1",
        "person_2"
      ],
      "additionalProperties": false
    },
    "most_recently_born_person_name": {
      "type": "string",
      "description": "The name of the person who was born most recently."
    },
    "most_recent_birth_year": {
      "type": "integer",
      "description": "The birth year of the most recently born person."
    }
  },
  "required": [
    "person_comparison",
    "most_recently_born_person_name",
    "most_recent_birth_year"
  ],
  "additionalProperties": false
}
