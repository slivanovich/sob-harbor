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
1970 Tampa Spartans football team: The 1970 Tampa Spartans football team represented the University of Tampa in the 1970 college football season.  It was the Spartans' 34th season and competed as a College Division Independent.  The team was led by head coach Fran Curci, in his third year, and played their home games at Tampa Stadium in Tampa, Florida.  They finished with a record of ten wins and one loss (10–1).

1974 Tampa Spartans football team: The 1974 Tampa Spartans football team represented the University of Tampa in the 1974 college football season.  It was the Spartans' 38th season and competed as a College Division Independent.  The team was led by head coach Dennis Fryzel, in his second year, and played their home games at Tampa Stadium in Tampa, Florida.  They finished with a record of six wins and five losses (6–5).  On February 27, 1975, the University of Tampa Board of Trustees voted to disband the Spartans football program effective for the 1975 season.  Financial hardship was cited as the primary reason for its being disbanded.

1967 Tampa Spartans football team: The 1967 Tampa Spartans football team represented the University of Tampa in the 1967 college football season.  It was the Spartans' 31st season and competed as a member of the NAIA.  The team was led by head coach Sam Bailey, in his fourth year, and played their home games at Phillips Field for their first two home games and then at Tampa Stadium for their final five home games in Tampa, Florida.  They finished with a record of two wins and seven losses (2–7).  The 1967 season is noted for the dedication of Tampa Stadium in the Spartans' 38–0 loss against Tennessee.

1969 Tampa Spartans football team: The 1969 Tampa Spartans football team represented the University of Tampa in the 1969 college football season.  It was the Spartans' 33rd season and competed as a member of the NAIA.  The team was led by head coach Fran Curci, in his second year, and played their home games at Tampa Stadium in Tampa, Florida.  They finished with a record of eight wins and two losses (8–2).  The Spartans opened the season with a loss at <a href="">Akron

1963 Tampa Spartans football team: The 1963 Tampa Spartans football team represented the University of Tampa in the 1963 college football season.  It was the Spartans' 27th season and competed as a member of the NAIA.  The team was led by head coach Fred Pancoast, in his second year, and played their home games at Phillips Field in Tampa, Florida.  They finished with a record of four wins, five losses and one tie (4–5–1).  Pancoast resigned as the Spartans' head coach on January 20, 1964, to take the position of ends coach at Florida.

1961 Tampa Spartans football team: The 1961 Tampa Spartans football team represented the University of Tampa in the 1961 college football season.  It was the Spartans' 25th season and competed as a member of the NAIA.  The team was led by head coach Marcelino Huerta, in his tenth year, and played their home games at Phillips Field in Tampa, Florida.  They finished with a record of eight wins and one loss (8–1).  Huerta resigned as the Spartans' head coach on January 8, 1962, to take the same position at Wichita State.

1968 Tampa Spartans football team: The 1968 Tampa Spartans football team represented the University of Tampa in the 1968 college football season.  It was the Spartans' 32nd season and competed as a member of the NAIA.  The team was led by head coach Fran Curci, in his first year, and played their home games at Tampa Stadium in Tampa, Florida.  They finished with a record of seven wins and three losses (7–3).  Curci was officially hired as the replacement for Sam Bailey as head coach on January 25, 1968, from the Miami Hurricanes, and he won his first game as head coach on the road against UC Santa Barbara.  Other games of note during the season included upsets at Tulane and over Mississippi State, both of the NCAA University Division.

1971 Tampa Spartans football team: The 1971 Tampa Spartans football team represented the University of Tampa in the 1971 college football season.  It was the Spartans' 35th season and first as a University Division Independent.  The team was led by head coach Bill Fulcher, in his first year, and played their home games at Tampa Stadium in Tampa, Florida.  They finished with a record of six wins and five losses (6–5).  Fulcher was hired on January 7, 1971, to serve as the replacement for Fran Curci who resigned to become the head coach at Miami.

University of Tampa: The University of Tampa (UT), is a private co-educational university in Downtown Tampa, Florida, United States.  It is accredited by the Southern Association of Colleges and Schools.  UT offers more than 200 programs of study, including 13 master's degrees and a broad variety of majors, minors, pre-professional programs, and certificates.

1972 Tampa Spartans football team: The 1972 Tampa Spartans football team represented the University of Tampa in the 1972 college football season.  It was the Spartans' 36th season and competed as a College Division Independent.  The team was led by head coach Earle Bruce, in his first year, and played their home games at Tampa Stadium in Tampa, Florida.  They finished with a record of ten wins and two losses (10–2) and with a victory in the Tangerine Bowl over Kent State.  Bruce was hired on February 2, 1972, to serve as the replacement for Bill Fulcher who resigned to become the head coach at Georgia Tech.

Question: The 1974 Tampa Spartans football team represented the University of Tampa (UT), is a private co-educational university in Downtown Tampa, Florida, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "university_name": {
      "type": "string",
      "description": "The name of the university."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the university is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the university is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the university is located."
        }
      },
      "required": [
        "city",
        "state",
        "country"
      ],
      "additionalProperties": false
    },
    "institution_type": {
      "type": "string",
      "description": "The type of educational institution."
    }
  },
  "required": [
    "university_name",
    "location",
    "institution_type"
  ],
  "additionalProperties": false
}
