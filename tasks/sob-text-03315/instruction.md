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
Custom Killing: Custom Killing is the fourth studio album by the Canadian speed/thrash metal band Razor.  It was released in July 1987 by Toronto based label Fringe Product.  It is more of an experimental approach and was fairly overlooked upon its release.  It also features "Survival of the Fittest" and "Last Rites" which are the band's longest songs ever recorded.  It is the final album to feature Mike Embro on drums and Mike Campagnolo on bass.  The album is currently out of print and has never received an official CD release, however in 2015, High Roller Records re-issued the album on vinyl, limited to 1,000 copies.  It features the original sound and has not been re-mixed or re-mastered.

Open Hostility: Open Hostility is the seventh studio album by Canadian speed/thrash metal band Razor.

Shotgun Justice: Shotgun Justice is the sixth studio album by Canadian speed/thrash metal band Razor.  It is the final album to feature Adam Carlo on bass, Rob Mills on drums and their first with vocalist Bob Reid.  Music videos were made for "Shotgun Justice" and "American Luck".

Charles Bronson: Charles Bronson (born Charles Dennis Buchinsky; Lithuanian: "Karolis Dionyzas Bučinskis" ; November 3, 1921 – August 30, 2003) was an American actor.

Malicious Intent (album): Malicious Intent is the third album released in 1986 by Canadian speed/thrash metal band Razor.  The album contains more honed and intense screaming from frontman Stace McLaren and the tracks on it mostly contains lyrics about heroic fantasy and playing heavy metal.  An exception to this might be "Tear Me to Pieces", with lyrics penned by McLaren about knife fighting.  "Malicious Intent" is known for containing incredibly loud drum rides and overall poor production.  The album itself is an overall turning point for Razor and shows them going from traditional heavy metal and speeding up to a more thrash metal-oriented sound.

Armed &amp; Dangerous (Razor album): Armed And Dangerous is the debut EP release by Canadian speed/thrash metal band Razor, released in 1984.  This EP was limited to 1,200 copies on vinyl and is very rare.

Executioner's Song (album): Executioner's Song is the first studio LP released by Canadian speed/thrash metal band Razor in 1985.  Most of the tracks on the album were first put to tape on the "Escape the Fire" demo, recorded in December 1984.

Decibels (album): Decibels is the eighth studio album by Canadian speed/thrash metal band Razor.  This is the first album in six years and since the band's split in 1992.  It is the only album to feature Rich Oosterbosch on drums and the last with Jon Armstrong on bass.  It is also their most recent to date.

Evil Invaders: Evil Invaders is the second album released in 1985 by Canadian speed/thrash metal band Razor.  The album's art, depicting an evil cyborg of living tissue under a metal endoskeleton, is reminiscent of the title character from the science fiction action film "The Terminator", released one year prior.  A music video was made for "Evil Invaders".

Violent Restitution: Violent Restitution is the fifth full-length album from the Canadian speed/thrash metal band Razor released in 1988.  It is the first album to feature Rob Mills on drums and Dave Carlo's brother Adam on bass and the last one to feature Stace "Sheepdog" McLaren on vocals.  The album is dedicated to late actor Charles Bronson.

Question: Violent Restitution is the fifth full-length album from the Canadian speed/thrash metal band Razor released in 1988, the album is dedicated to the late Charles Bronson, was an American actor, died on which date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "album_release_year": {
      "type": "integer",
      "description": "The year the album was released."
    },
    "dedicated_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person the album is dedicated to."
        },
        "occupation": {
          "type": "string",
          "description": "The occupation of the dedicated person."
        },
        "death_date": {
          "type": "string",
          "description": "The date of death of the dedicated person."
        }
      },
      "required": [
        "name",
        "occupation",
        "death_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_title",
    "album_release_year",
    "dedicated_person"
  ],
  "additionalProperties": false
}
