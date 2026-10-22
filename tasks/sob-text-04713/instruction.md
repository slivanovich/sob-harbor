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
Miss USA 1986: Miss USA 1986, the 35th Miss USA pageant, was televised live on May 20 from Miami, Florida on CBS.  The ceremonies were hosted by Bob Barker.  At the conclusion of the final competition, Christy Fichtner of Texas was crowned Miss USA, becoming the second consecutive winner from Texas.

Miss USA 1965: Miss USA 1965, the 14th Miss USA pageant, took place in Miami Beach, Florida on June 4, 1965.  This was the first Miss USA pageant to be televised live (on the CBS network), and the first to be a self-contained production, held several weeks before, and independent of, the Miss Universe pageant.

Miss USA 2008: Miss USA 2008, the 57th Miss USA beauty pageant, was held in Las Vegas, Nevada on April 11, 2008.  At the conclusion of the final night of competition, Crystle Stewart, Miss Texas USA, was crowned the winner by outgoing titleholder, Rachel Smith of Tennessee.  Crystle represented the United States at the Miss Universe 2008 pageant, which was held in Vietnam, where she placed in the Top 10.  This is the first time in Miss USA history that two consecutive women of African-American descent have been crowned.

Miss USA 1964: Miss USA 1964, the 13th Miss USA pageant, took place in Miami Beach, Florida on July 29, 1964.  This was the last Miss USA pageant to be held as an inclusive part of the Miss Universe event.

Olivia Jordan: Olivia Jordan Thomas (born September 28, 1988) is an American actress, model, and beauty pageant titleholder who was crowned Miss USA 2015.  She went on to represent the United States at Miss Universe 2015, where she placed as second runner-up.  Jordan also represented the United States at Miss World 2013, where she finished in the top 20.  She is the first woman from Oklahoma to be crowned Miss USA.

Miss USA 1967: Miss USA 1967, the 16th Miss USA pageant, was won by Sylvia Hitchcock of Alabama.  She was crowned by Miss USA 1966, Maria Remenyi of California.  It took place on the Miami Beach Auditorium in Miami Beach, Florida.  Hitchcock won Miss Universe later and her 2nd runner-up Cheryl Patton later becames Miss USA because the 1st runner-up refused the title.

Miss USA 2010: Miss USA 2010, the 59th Miss USA pageant, was held at the Theatre for the Performing Arts in Planet Hollywood Resort and Casino in Las Vegas, Nevada on May 16, 2010.  Kristen Dalton of North Carolina, crowned her successor, Rima Fakih of Michigan as Miss USA 2010 at the end of this event.

Miss USA 1963: Miss USA 1963, the 12th Miss USA pageant, took place in Miami Beach, Florida on July 17, 1963.  The pageant was won by Marite Ozers of Illinois, who was crowned by outgoing titleholder Macel Leilani Wilson of Hawaii.  Latvian-born Ozers was the first woman born outside the U.S. to take the Miss USA title, and the second delegate from Illinois to do so.  Ozers went on to finish as a Top 15 semi-finalist at Miss Universe 1963.

Miss USA 1962: Miss USA 1962, the 11th Miss USA pageant, took place in Long Beach, California, on July 12, 1962.  The pageant was won by Macel Leilani Wilson of Hawaii, who was crowned by outgoing titleholder Sharon Brown of Louisiana.  Wilson's win gave Hawaii the Miss USA crown at its first attempt, and two days later she was a Top 15 semi-finalist at Miss Universe 1962.  Eleven states did not send a delegate to the 1962 pageant, resulting in the lowest number of contestants since the inaugural pageant of 1952.

Miss USA 2016: Miss USA 2016, was the 65th Miss USA pageant.  It was held at the T-Mobile Arena in Las Vegas, Nevada on June 5, 2016.  All fifty states and the District of Columbia competed.  Olivia Jordan of Oklahoma crowned her successor, Deshauna Barber of the District of Columbia, at the end of the event.  This was the first Miss USA pageant to be broadcast on Fox Network.  Barber represented the USA at the Miss Universe 2016 pageant, where she placed in the Top 9.

Question: What American actress crowned Deschauna Barber in the 65th Miss USA pageant?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "crowned_by_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who performed the crowning."
        },
        "occupation": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Occupations of the person who performed the crowning."
        },
        "crowned_miss_usa_year": {
          "type": "integer",
          "description": "The year the crowner was crowned Miss USA."
        },
        "represented_state": {
          "type": "string",
          "description": "The state the crowner represented."
        }
      },
      "required": [
        "name",
        "occupation",
        "crowned_miss_usa_year",
        "represented_state"
      ],
      "additionalProperties": false
    },
    "pageant_details": {
      "type": "object",
      "properties": {
        "pageant_year": {
          "type": "integer",
          "description": "The year the pageant took place."
        },
        "pageant_number": {
          "type": "integer",
          "description": "The edition number of the Miss USA pageant."
        },
        "crowned_person_name": {
          "type": "string",
          "description": "The name of the person who was crowned."
        },
        "crowned_person_represented_state": {
          "type": "string",
          "description": "The state the crowned person represented."
        }
      },
      "required": [
        "pageant_year",
        "pageant_number",
        "crowned_person_name",
        "crowned_person_represented_state"
      ],
      "additionalProperties": false
    },
    "event_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the pageant was held."
        },
        "state": {
          "type": "string",
          "description": "The state where the pageant was held."
        },
        "venue": {
          "type": "string",
          "description": "The venue where the pageant was held."
        }
      },
      "required": [
        "city",
        "state",
        "venue"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "crowned_by_person",
    "pageant_details",
    "event_location"
  ],
  "additionalProperties": false
}
