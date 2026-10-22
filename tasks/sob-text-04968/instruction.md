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
The Real Housewives of Miami: The Real Housewives of Miami (abbreviated RHOM) is an American reality television series that aired from February 22, 2011 to November 4, 2013 on Bravo.  Developed as the seventh installment of "The Real Housewives" franchise, following "The Real Housewives of Orange County", "New York City", "Atlanta", "New Jersey", "D.C.", and "Beverly Hills", it aired three seasons and focused on the personal and professional lives of several women living in Miami, Florida.  In 2016, executive producer Andy Cohen confirmed the series had been cancelled.

Mauricio Umansky: Mauricio Umansky (born  1969 ) is an American high-end real estate agent, media personality, and philanthropist.  His wife is "Real Housewives of Beverly Hills" star Kyle Richards and he appears on the show.  He is known for being one of the top real estate agents in the country.

Vanderpump Rules: Vanderpump Rules is an American reality television series airing on Bravo that debuted on January 7, 2013, with the first season originally eight episodes.  A spin-off of "The Real Housewives of Beverly Hills", the series features "The Real Housewives of Beverly Hills" cast member Lisa Vanderpump in the title role and her staff at Vanderpump's West Hollywood, California, restaurant SUR.

Les Vraies Housewives: Les Vraies Housewives (translated The Real Housewives and abbreviated LVH) is a French reality television series that aired on NT1 on March 18, 2013 until April 1, 2013.  Developed as international installment of the "Real Housewives" franchise, it aired only one season and documented the personal and professional lives of several French women residing in Beverly Hills, California.

The Real Housewives of Sydney: The Real Housewives of Sydney (abbreviated RHOS) is an Australian reality television series that airs on Arena.  The show premiered on 26 February 2017.  The series was developed as an international installment of the American "The Real Housewives" franchise and the third installment of "The Real Housewives" franchise by Matchbox Entertainment, following "The Real Housewives of Melbourne" and "Auckland".  "The Real Housewives of Sydney" focuses on the personal and professional lives of several women living in Sydney, Australia.

Kyle Richards: Kyle Richards (born January 11, 1969) is an American actress, television personality, memoirist and philanthropist.  She began her career as a child actress, appearing in a recurring role on "Little House on the Prairie", and in several horror films, including "The Car" (1977), Tobe Hooper's "Eaten Alive" (1977), and John Carpenter's "Halloween" (1978).  Since 2010, she has appeared as a main cast member on "The Real Housewives of Beverly Hills".  She was a contestant on "The New Celebrity Apprentice" (also known as "The Celebrity Apprentice 8"), playing for the charity Children's Hospital Los Angeles.  She was the 5th contestant fired, finishing in 12th place and raising $25,000 for her charity.

List of The Real Housewives cast members: "The Real Housewives" is an American media franchise that consists of several reality television series broadcast on the Bravo cable network.  Each series follows an affluent group of women as they socialize and cope with life's struggles.  The franchise initially began in 2006 with the series of "The Real Housewives of Orange County" that featured Kimberly Bryant, Jo De La Rosa, Vicki Gunvalson, Jeana Keough and Lauri Waring.  Since the premiere of the series, it has grown to include multiple series in different cities and areas across the United States that include: New York City and Atlanta in 2008; New Jersey in 2009; Washington, D.C. and Beverly Hills in 2010; Miami in 2011; Potomac and Dallas in 2016.  The franchise has grown to be successful with several housewives receiving spin-offs of their respective series.

List of Vanderpump Rules episodes: "Vanderpump Rules" is an American reality television series aired on Bravo that debuted on January 7, 2013.  It a spin-off to "The Real Housewives of Beverly Hills".  The series features "The Real Housewives of Beverly Hills" cast member Lisa Vanderpump in the title role and her staff at Vanderpump's West Hollywood, California, restaurant SUR.

The Real Housewives of Beverly Hills: The Real Housewives of Beverly Hills (abbreviated RHOBH) is an American reality television series that premiered on October 14, 2010, on Bravo.  The show was developed as the sixth installment of "The Real Housewives" franchise following "The Real Housewives of Orange County", "New York City", "Atlanta", "New Jersey", and "D.C." It has aired seven seasons and focuses on the personal and professional lives of several women residing in Beverly Hills, California.

Taylor Armstrong: Taylor Armstrong (born Shana Lynette Hughes on June 10, 1971) is an American television personality, memoirist and philanthropist.  She appeared on the reality show "The Real Housewives of Beverly Hills".

Question: Mauricio Umansky's wife on the "Real Housewives of Beverly Hills" is which American actress, television personality, memoirist and philanthropist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the American actress, television personality, memoirist, and philanthropist."
    },
    "relationship_to_mauricio_umansky": {
      "type": "string",
      "description": "The relationship of the person to Mauricio Umansky."
    },
    "occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the person's professions or roles."
    },
    "reality_show_details": {
      "type": "object",
      "properties": {
        "show_name": {
          "type": "string",
          "description": "The name of the reality television series the person appears on."
        },
        "role_on_show": {
          "type": "string",
          "description": "The person's role or status on the reality show."
        }
      },
      "required": [
        "show_name",
        "role_on_show"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "relationship_to_mauricio_umansky",
    "occupations",
    "reality_show_details"
  ],
  "additionalProperties": false
}
