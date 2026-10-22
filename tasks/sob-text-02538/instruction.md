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
2016 Bethune–Cookman Wildcats football team: The 2016 Bethune–Cookman Wildcats football team represented Bethune–Cookman University in the 2016 NCAA Division I FCS football season.  They were led by second-year head coach Terry Sims and played their home games at Municipal Stadium.  They were a member of the Mid-Eastern Athletic Conference (MEAC).  They finished the season 4–6, 4–4 in MEAC play to finish in a two-way tie for fifth place.

Bethune–Cookman Wildcats women's basketball: The Bethune–Cookman Wildcats women's basketball team represents Bethune-Cookman University in the sport of basketball.  The Wildcats competes in the NCAA Division I and the Mid-Eastern Athletic Conference (MEAC).  They play their home games in Moore Gymnasium on Bethune-Cookman University campus in Daytona Beach, Florida.

Bethune–Cookman Wildcats football: The Bethune–Cookman Wildcats football team represents Bethune-Cookman University in the sport of American football.  The Wildcats compete in the Football Championship Subdivision (FCS) of the National Collegiate Athletics Association (NCAA) and the south division of the Mid-Eastern Athletic Conference (MEAC).  They play their home games at Municipal Stadium (Daytona Beach).  The Wildcats have won two black college football national championships and seven MEAC titles in the history of their football program.

Bethune–Cookman University: Bethune–Cookman University (B–CU), formerly Bethune–Cookman College (B–CC), is a private, co-ed, historically black university located in Daytona Beach, Florida, United States.  The primary administration building, White Hall, and the Mary McLeod Bethune Home have been added to the US National Register of Historic Places.

2010 Bethune–Cookman Wildcats football team: The 2010 Bethune–Cookman Wildcats football team represented Bethune-Cookman University in the 2010 NCAA Division I FCS football season.  The Wildcats were led by first year head coach Brian Jenkins and played their home games at Municipal Stadium.  They are a member of the Mid-Eastern Athletic Conference.  They finished the season 10–2, 7–1 in MEAC play to finish in first place.

2011 Bethune–Cookman Wildcats football team: The 2011 Bethune–Cookman Wildcats football team represented Bethune-Cookman University in the 2011 NCAA Division I FCS football season.  The Wildcats were led by fifth year head coach Brian Jenkins and played their home games at Municipal Stadium.  They are a member of the Mid-Eastern Athletic Conference.  They finished the season 8–3, 6–2 in MEAC play to finish in second place.

Bethune–Cookman Wildcats: The Bethune–Cookman Wildcats are the athletic teams that represent Bethune–Cookman University in Daytona Beach, Florida.  They compete as a member of the National Collegiate Athletic Association Division I level (Football Championship Subdivision) primarily competing in the Mid-Eastern Athletic Conference (MEAC) for all sports.

2017 Bethune–Cookman Wildcats football team: The 2017 Bethune–Cookman Wildcats football team represents Bethune–Cookman University in the 2017 NCAA Division I FCS football season.  They are led by third-year head coach Terry Sims and play their home games at Municipal Stadium.  They are a member of the Mid-Eastern Athletic Conference (MEAC).

2012 Bethune–Cookman Wildcats baseball team: The 2012 Bethune–Cookman Wildcats baseball team represents Bethune-Cookman University in the sport of baseball during the 2012 college baseball season.  The Wildcats competed in Division I of the National Collegiate Athletic Association (NCAA) and the Southern Division of the Mid-Eastern Athletic Conference (MEAC).  The team is coached by Jason Beverlin, who entered his first season at Bethune-Cookman.  The Wildcats won the MEAC Tournament and moved on to the NCAA Tournament and participated in the Gainesville Regional, where they were beat 0-2.

2015 Bethune–Cookman Wildcats baseball team: The 2015 Bethune–Cookman Wildcats baseball team represents Bethune-Cookman University in the sport of baseball during the 2015 college baseball season.  The Wildcats competed in Division I of the National Collegiate Athletic Association (NCAA) and the Southern Division of the Mid-Eastern Athletic Conference (MEAC).  The team is coached by Jason Beverlin, who is entering his fifth season at Bethune-Cookman.

Question: The Bethune–Cookman Wildcats are athletic teams that represent a private, co-ed, historically black university located where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "university_name": {
      "type": "string",
      "description": "The full name of the university."
    },
    "university_attributes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key characteristics of the university."
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
    }
  },
  "required": [
    "university_name",
    "university_attributes",
    "location"
  ],
  "additionalProperties": false
}
