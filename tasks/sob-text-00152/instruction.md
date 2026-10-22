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
Define the Great Line: Define the Great Line is the fifth album by American metalcore band Underoath.  The album was released in the United States on June 20, 2006, along with a limited edition version containing exclusive artwork and DVD.  For the recording of this album, Underoath's usual producer, James Paul Wisner, was replaced by Adam Dutkiewicz of Killswitch Engage and Matt Goldman.  The album debuted at No. 2 on the "Billboard" 200 charts selling over 98,000 copies in its first week, and within a week of its release it became the highest charting Christian album on the "Billboard" 200 since 1997.

Loving You Tonight: "Loving You Tonight" is the fourth single released from Squeeze's tenth album, "Some Fantastic Place".  Lead vocals on the song are by Paul Carrack.  The only other time Carrack sang lead on a Squeeze track was in 1981, on the better-known "Tempted."

Rewired (Mike + The Mechanics album): Rewired is the sixth studio album by Mike + The Mechanics, released in 2004.  This was the first album released by the band following the death of the co-lead singer Paul Young.  Partly because of this, the album was credited to "Mike + The Mechanics + Paul Carrack".  It is the only Mike + The Mechanics album to date with only one lead vocalist.

Some Fantastic Place: Some Fantastic Place is a 1993 album by the British new wave group Squeeze.  It was the band's tenth studio album, and it marked the departure of drummer Gilson Lavis, the only band member besides Chris Difford and Glenn Tilbrook who had appeared on every Squeeze album to this point (Lavis was replaced by Pete Thomas).  This record also marked the brief return of keyboardist/vocalist Paul Carrack.  Carrack had last appeared on 1981's "East Side Story", performing the lead vocals on one of Squeeze's most popular early singles, "Tempted."  "Loving You Tonight" became only the second Squeeze song cut in thirteen years to feature Carrack singing a lead part.  Additionally, bassist Keith Wilkinson wrote and sang "True Colours (The Storm)", the first song on a Squeeze album not written by Glenn Tilbrook, Chris Difford, Jools Holland, or any combination of those three.  The record was produced by Squeeze and Peter Smith.

Paul Carrack: Paul Melvyn Carrack (born 22 April 1951) is an English singer, songwriter, composer and multi-instrumentalist who has recorded as both a solo artist and as a member of several popular bands.  The BBC dubbed Carrack "The Man with the Golden Voice", while "Record Collector" remarked: "If vocal talent equalled financial success, Paul Carrack would be a bigger name than legends such as Phil Collins or Elton John."

The Changing of Times: The Changing of Times is the third album by American metalcore band Underoath.  The album was released on February 26, 2002, through Solid State Records.  It is the last Underoath recording to feature vocalist Dallas Taylor and guitarist Octavio Fernandez, but is the first to include guitarist Timothy McTague.  The album is the best-selling Solid State debut.  It is also the only album to feature William Nottke on bass.  The opening track "When the Sun Sleeps" was released as Underoath's first music video.

Spencer Chamberlain: Spencer Chamberlain (born January 4, 1983) is an American musician, best known for being the current lead vocalist for the metalcore band Underoath.  Before fronting Underoath, Chamberlain was the vocalist for the band This Runs Through in which his brother, Phil Chamberlain, was the drummer (who is also the drummer for To Speak of Wolves).  He is currently the vocalist of Sleepwave.

Underoath: Underoath (stylized as Underøath or UnderOath) is an American Christian post-hardcore band from Tampa, Florida.  Founded by Dallas Taylor and Luke Morton on November 30, 1997, in Ocala, Florida, subsequently its additional members were from Tampa, Florida.

Dallas Taylor (vocalist): Dallas Taliaferro Taylor (born May 17, 1980) is an American musician who is the vocalist for the Southern metal band Maylene and the Sons of Disaster.  He is the former vocalist and founder of the American metalcore band Underoath.  He performed on three Underoath albums: "Act of Depression", "Cries of the Past", and "The Changing of Times".  In 2003, Dallas left Underoath, and was replaced by Spencer Chamberlain.  He was born in Ocala, Florida.

They're Only Chasing Safety: They're Only Chasing Safety is the fourth album by American post-hardcore band Underoath.  The album was released on June 15, 2004, through Solid State Records.  Prior to recording, it was ready to be recorded with Underoath founder and frontman Dallas Taylor, but instead was replaced with the band's current lead vocalist Spencer Chamberlain.  It is also the first record to feature bassist Grant Brandell, who replaced William Nottke shortly after the release of "The Changing of Times", and James Smith, who replaced Octavio Fernandez on rhythm guitar.

Question: Which of the following is the former vocalist and founder of the band Underoath: Paul Carrack or Dallas Taylor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_entity": {
      "type": "string",
      "description": "The band that the question is about."
    },
    "role_in_band": {
      "type": "string",
      "description": "The specific role being inquired about within the band."
    },
    "candidate_options": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The list of names provided as options in the question."
    },
    "identified_person": {
      "type": "string",
      "description": "The person identified as matching the role based on the context."
    },
    "person_details": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the identified person."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the identified person."
        },
        "birth_place": {
          "type": "string",
          "description": "The birth place of the identified person."
        },
        "founding_date": {
          "type": "string",
          "description": "The date the person co-founded the band."
        },
        "albums_performed_on": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of albums the person performed on for the band."
        },
        "departure_year": {
          "type": "integer",
          "description": "The year the person left the band."
        },
        "replacement_vocalist": {
          "type": "string",
          "description": "The name of the person who replaced the identified vocalist."
        }
      },
      "required": [
        "full_name",
        "birth_date",
        "birth_place",
        "founding_date",
        "albums_performed_on",
        "departure_year",
        "replacement_vocalist"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "question_entity",
    "role_in_band",
    "candidate_options",
    "identified_person",
    "person_details"
  ],
  "additionalProperties": false
}
