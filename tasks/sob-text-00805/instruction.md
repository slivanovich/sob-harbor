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
Long Island PGA Championship: The Long Island PGA Championship is a professional golf tournament played on Long Island, New York.  It is sponsored by the Metropolitan section of the PGA of America.  The current title of the event is the MasterCard Long Island PGA Championship.  It was first held in 1935.  Al Brosch won a record nine titles between 1939 and 1960.  In addition to the record-setting success of Brosch, the Long Island PGA Championship has been won by many touring pros, including Jim Albus, Wiffy Cox, Jay Hebert, Tom Nieporte, Bruce Zabriski and others.

2007 PGA Championship: The 2007 PGA Championship was the 89th PGA Championship, played August 9–12 at Southern Hills Country Club in Tulsa, Oklahoma.  Defending champion Tiger Woods won his fourth PGA Championship and 13th major title, two strokes ahead of runner-up Woody Austin.

2016 PGA Championship: The 2016 PGA Championship was the 98th PGA Championship which took place from July 28–31 at Baltusrol Golf Club on the Lower Course in Springfield Township, New Jersey, west of New York City.  This was the ninth major and second PGA Championship at Baltusrol, which last hosted in 2005.  Jimmy Walker won his first major championship title with a score of 14 under par, one shot ahead of 2015 champion Jason Day.

1927 PGA Championship: The 1927 PGA Championship was the 10th PGA Championship, held October 31 to November 5 in Texas at Cedar Crest Country Club in Dallas.  Then a match play championship, Walter Hagen defeated Joe Turnesa 1 up in the finals to win his fourth consecutive PGA Championship, his fifth and final overall, and the ninth of his eleven major titles.

Inwood, New York: Inwood is a hamlet and census-designated place (CDP) in Nassau County, New York, United States.  The population was 9,792 at the 2010 census.

1980 PGA Championship: The 1980 PGA Championship was the 62nd PGA Championship, held August 7–10 at the East Course of Oak Hill Country Club in Rochester, New York.  Jack Nicklaus won his fifth PGA Championship, seven strokes ahead of runner-up Andy Bean.  The victory tied Nicklaus with Walter Hagen, who won five PGA titles in match play competition in the 1920s.

1921 PGA Championship: The 1921 PGA Championship was the fourth PGA Championship, held September 27 to October 1 on Long Island at Inwood Country Club in Inwood, New York.  The match play field of 32 consisted of the defending champion and the top qualifiers from the 1921 U.S. Open.  The competition was five rounds of 36-hole matches in a single-elimination tournament.

1939 PGA Championship: The 1939 PGA Championship was the 22nd PGA Championship, held July 9–15 at Pomonok Country Club in Queens, New York.  Then a match play championship, Henry Picard won his only PGA Championship, defeating Byron Nelson with a birdie at the 37th hole.  It was the second of his two major titles; he won the Masters in 1938.  Nelson won the U.S. Open three months earlier and the next PGA Championship in 1940.  Beginning in 1939, he made five finals in six PGA Championships, and won his second title in 1945.

1926 PGA Championship: The 1926 PGA Championship was the ninth PGA Championship, held September 20–25 at Salisbury Golf Club on Long Island in East Meadow, New York.  Then a match play championship, Walter Hagen defeated Leo Diegel 5 & 3 in the finals to win his third consecutive PGA Championship, his fourth overall, and the eighth of his eleven major titles.

1934 PGA Championship: The 1934 PGA Championship was the 17th PGA Championship, held July 24–29 at Park Country Club in Williamsville, New York, a suburb northeast of Buffalo.  Then a match play championship, Paul Runyan won the first of his two PGA Championship titles, defeating Craig Wood in 38 holes.

Question: Which county in New York held the fourth PGA Championship?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "championship_details": {
      "type": "object",
      "properties": {
        "championship_number": {
          "type": "integer",
          "description": "The sequential number of the PGA Championship."
        },
        "championship_year": {
          "type": "integer",
          "description": "The year the PGA Championship was held."
        }
      },
      "required": [
        "championship_number",
        "championship_year"
      ],
      "additionalProperties": false
    },
    "host_location": {
      "type": "object",
      "properties": {
        "city_or_hamlet": {
          "type": "string",
          "description": "The city or hamlet where the championship was held."
        },
        "state": {
          "type": "string",
          "description": "The state where the championship was held."
        },
        "country_club": {
          "type": "string",
          "description": "The name of the country club that hosted the championship."
        }
      },
      "required": [
        "city_or_hamlet",
        "state",
        "country_club"
      ],
      "additionalProperties": false
    },
    "answer_county": {
      "type": "string",
      "description": "The county in New York where the fourth PGA Championship was held."
    }
  },
  "required": [
    "championship_details",
    "host_location",
    "answer_county"
  ],
  "additionalProperties": false
}
