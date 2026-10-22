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
Monika Absolonová: Monika Absolonová (born 27 September 1976) is a Czech singer and actress.  In 2002, she performed the title role in the famous Czech musical, Kleopatra, at Prague's Broadway Theatre.  Absolonová performed her first solo concert in Prague's Broadway Theatre in 2010.  She took part in the Czech version of "Dancing with the Stars" in 2010.  In 2013, she became the Czech singing voice of Elsa in Frozen.

Broadway Theatre (Cape Girardeau, Missouri): Broadway Theater, also known as the New Broadway Theatre, Fox Broadway, Kerasotes Broadway Theatre, is a historic vaudeville house and movie theater located at Cape Girardeau, Missouri.  It built in 1921, and is a two-story, red brick building with a white, glazed brick façade.  The building consists of the theatre/storefront zone on the first level and a second zone with office space on the second level.

Old Broadway Theatre: The Broadway Theatre (September 27, 1847 – April 2, 1859), called the Old Broadway Theatre since its demise, was at 326–30 Broadway, between Pearl and Anthony (now Worth) Streets in Manhattan.  With over 4000 seats, it was the largest theater ever built in New York when it opened.  During its brief existence, many prominent performers of the era appeared on its stage.  It presented plays, opera, ballet, hippodrama, and circus performances in a space that was reconfigured several times.  The operators always struggled to make money, however, and after twelve years the Broadway Theatre was replaced by a more profitable building, for the textile trade.

Studio 54: Studio 54 is a former nightclub and currently a Broadway theatre, located at 254 West 54th Street, between Eighth Avenue and Broadway in Manhattan, New York City.  The building, originally built as the Gallo Opera House, opened in 1927, after which it changed names several times, eventually becoming CBS radio and television Studio 52.

Gershwin Theatre: The Gershwin Theatre is a Broadway theatre located at 222 West 51st Street in midtown-Manhattan in the Paramount Plaza building.  The theatre is named after brothers George Gershwin, a composer, and Ira Gershwin, a lyricist.  It has the largest seating capacity of any Broadway theatre with 1,933 seats.

Tony Award: The Antoinette Perry Award for Excellence in Broadway Theatre, more commonly known as Tony Award, recognizes the excellence in live Broadway theatre.  The awards are presented by the American Theatre Wing and The Broadway League at an annual ceremony in New York City.  The awards are given for Broadway productions and performances, and an award is given for regional theatre.  Several discretionary non-competitive awards are also given, including a Special Tony Award, the Tony Honors for Excellence in Theatre, and the Isabelle Stevenson Award.  The awards are named after Antoinette "Tony" Perry, co-founder of the American Theatre Wing.

Broadway Theatre (53rd Street): The Broadway Theatre (formerly Universal's Colony Theatre, B.S. Moss' Broadway Theatre, Earl Carroll's Broadway Theatre, and Ciné Roma) is a Broadway theatre located in midtown Manhattan.  It has a large seating capacity of 1,761, and unlike most Broadway theaters, it is actually located on Broadway, at number 1681.

Paul Marantz: Paul Marantz is an American architectural lighting designer, whose work includes the discothèque Studio 54, the Times Square Ball, the Tribute in Light, the Barnes Foundation,

Broadway theatre: Broadway theatre, commonly known as Broadway, refers to the theatrical performances presented in the 41 professional theatres with 500 or more seats located in the Theater District and Lincoln Center along Broadway, in Midtown Manhattan, New York City.  Along with London's West End theatre, Broadway theatre is widely considered to represent the highest level of commercial theatre in the English-speaking world.

The Theatre Museum: The Theatre Museum (TTM) is located at 30 Worth Street in Manhattan, New York City.  Its mission is to preserve, protect and perpetuate the legacy of theatre, including Broadway theatre.  The Theatre Museum continues the legacy of The Broadway Theatre Institute begun in 1995 by presenting Awards for Excellence in Theatre History Preservation and Theatre Arts Education.  It currently functioning as a museum-at-large and is not open to the public.

Question: Paul Marantz work includes which nightclub that is currently a Broadway theatre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "theatre_name": {
      "type": "string",
      "description": "The name of the theatre/nightclub."
    },
    "current_status": {
      "type": "string",
      "description": "The current function or status of the establishment."
    },
    "former_status": {
      "type": "string",
      "description": "The previous function or status of the establishment."
    },
    "designer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the designer."
        },
        "role": {
          "type": "string",
          "description": "The role or profession of the designer."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "location_city": {
      "type": "string",
      "description": "The city where the theatre is located."
    }
  },
  "required": [
    "theatre_name",
    "current_status",
    "former_status",
    "designer_details",
    "location_city"
  ],
  "additionalProperties": false
}
