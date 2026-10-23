{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCougar Town (season 3): The third season of \"Cougar Town\", an American sitcom that airs on ABC, began airing on February 14, 2012 and concluded on May 29, 2012 with a 1-hour episode.  Season three regular cast members include Courteney Cox, Christa Miller, Busy Philipps, Brian Van Holt, Dan Byrd, Ian Gomez, and Josh Hopkins.  The sitcom was created by Bill Lawrence and Kevin Biegel.  This is the final season to air on ABC before it moved to TBS.\n\nStar Trek: Enterprise (season 1): Season one of \"\", an American television series, began airing on September 26, 2001, on UPN.  The season concluded after 26 episodes on May 22, 2002.  The series was developed by Rick Berman and Brannon Braga, who also served as executive producers.  Season one regular cast members include Scott Bakula, Jolene Blalock, Connor Trinneer, Dominic Keating, Linda Park, Anthony Montgomery and John Billingsley.\n\nCougar Town (season 1): The first season of \"Cougar Town\", an American television series, began airing on September 23, 2009 and concluded on May 19, 2010.  Season one regular cast members include Courteney Cox, Christa Miller, Busy Philipps, Brian Van Holt, Dan Byrd, Ian Gomez, and Josh Hopkins.  The sitcom was created by Bill Lawrence and Kevin Biegel.\n\nJosh Hopkins: William Joshua \"Josh\" Hopkins (born September 12, 1970) is an American actor and amateur musician.  Hopkins was born in Lexington, Kentucky.  He has participated in many TV series and films.  He is the writer and performer of the song \"\"Feigning Interest\"\", a humoristic music video about dating that went viral in 2007.  In 2015, he starred in the ABC thriller \"Quantico\" as Liam O'Connor.\n\nCougar Town (season 2): The second season of \"Cougar Town\", an American television series, began airing on September 22, 2010 and concluded on May 25, 2011.  Season two regular cast members include Courteney Cox, Christa Miller, Busy Philipps, Brian Van Holt, Dan Byrd, Ian Gomez, and Josh Hopkins.  The sitcom was created by Bill Lawrence and Kevin Biegel.\n\nCold Case (season 1): Season one of Cold Case, an American television series, began airing on September 28, 2003.  Cold Case is a drama about Lilly Rush, an enigmatic and highly effective detective on the Philadelphia Homicide Squad.  Rush's instinctive understanding of the criminal mind and her singular passion for uncovering the truth makes her the perfect fit for investigating cold cases, yester-crimes that have remained unsolved – some only a few months old, others going back decades.  Rush and her team use their wits to take on aging evidence and witnesses with buried secrets, uncovering fresh clues, digging into old wounds and doggedly pursuing the truth.  Joining Rush on her mission are a team of talented detectives: Scotty Valens, Rush's confident and street-smart partner; Nick Vera, rough around the edges but a sharp investigator; Will Jeffries, an experienced veteran who's been around the block; Kat Miller, no-nonsense and resourceful; and Lieutenant John Stillman, Rush's mentor and sometime father figure.  With their assistance, Rush is able to take on the toughest cases, giving voice to victims unable to speak for themselves – making sure none is ever forgotten.  Season one regular cast members include Kathryn Morris, Danny Pino, John Finn, Thom Barry and Jeremy Ratchford.  In 3 episodes, Justin Chambers had played Chris Lassing, Lilly's partner on the Philadelphia Homicide Squad, but left the show to star as Alex Karev in ABC's hit drama show \"Grey's Anatomy\".\n\nCougar Town (season 4): The fourth season of \"Cougar Town\", an American sitcom that airs on TBS, began airing on January 8, 2013.  Season four regular cast members include Courteney Cox, Christa Miller, Busy Philipps, Brian Van Holt, Dan Byrd, Ian Gomez, and Josh Hopkins.  The sitcom was created by Bill Lawrence and Kevin Biegel.  This is the first season to air on TBS.\n\nCougar Town (season 5): The fifth season of \"Cougar Town\", an American sitcom that airs on TBS, began airing on January 7, 2014.  Season five regular cast members include Courteney Cox, Christa Miller, Busy Philipps, Brian Van Holt, Dan Byrd, Ian Gomez, and Josh Hopkins.  The sitcom was created by Bill Lawrence and Kevin Biegel.\n\nMen at Work (season 1): The first season of the TBS sitcom Men at Work premiered on May 24, 2012 and ended July 12, 2012.  A total of ten episodes were produced.  Season one regular cast members include Danny Masterson, Michael Cassidy, Adam Busch, Meredith Hagner and James Lesure.\n\nStargate Atlantis (season 4): The fourth season of \"Stargate Atlantis\", an American-Canadian television series, began airing on September 28, 2007 on the US-American Sci Fi Channel.  The fourth season concluded after 20 episodes on March 7, 2008 on Sci Fi.  The series was developed by Brad Wright and Robert C. Cooper, who also served as executive producers.  Amanda Tapping (Col. Samantha Carter) joins the cast as a regular for 14 episodes, Jewel Staite (Dr. Jennifer Keller) was a recurring character for eleven episodes, while regular cast member Torri Higginson (Dr. Elizabeth Weir) was a recurring cast member for four episodes.  Other season four regular cast members include Joe Flanigan, David Hewlett, Rachel Luttrell and Jason Momoa.\n\nQuestion: What season one regular cast member of \"Cougar Town\" was also in \"Quantico\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"cougar_town_role\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"season_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The season number of Cougar Town the actor was a regular cast member in.\"\n        },\n        \"series_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the series.\"\n        },\n        \"cast_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of cast member (e.g., regular).\"\n        }\n      },\n      \"required\": [\n        \"season_number\",\n        \"series_title\",\n        \"cast_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"other_series_appearance\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"series_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the other series the actor appeared in.\"\n        },\n        \"role_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character played in the other series.\"\n        }\n      },\n      \"required\": [\n        \"series_title\",\n        \"role_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"cougar_town_role\",\n    \"other_series_appearance\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "cougar_town_role": {
        "type": "object",
        "properties": {
          "season_number": {
            "type": "integer",
            "description": "The season number of Cougar Town the actor was a regular cast member in."
          },
          "series_title": {
            "type": "string",
            "description": "The title of the series."
          },
          "cast_type": {
            "type": "string",
            "description": "The type of cast member (e.g., regular)."
          }
        },
        "required": [
          "season_number",
          "series_title",
          "cast_type"
        ],
        "additionalProperties": false
      },
      "other_series_appearance": {
        "type": "object",
        "properties": {
          "series_title": {
            "type": "string",
            "description": "The title of the other series the actor appeared in."
          },
          "role_name": {
            "type": "string",
            "description": "The name of the character played in the other series."
          }
        },
        "required": [
          "series_title",
          "role_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "cougar_town_role",
      "other_series_appearance"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
