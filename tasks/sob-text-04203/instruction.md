{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCorey Reynolds: Corey Reynolds is an American musical theatre, television, and film actor known for originating the role of Seaweed in the Broadway adaptation of \"Hairspray\", and for the TNT crime show \"The Closer\".\n\nA. J. Reynolds: Alfred John \"AJ\" Reynolds is a Canadian performer, entertainer, and radio personality, best known for his internationally syndicated radio show Canada's Top 20 Countdown.  Reynolds is also co-founder of Positive Number Productions and is the current host of \"AJ Reynolds ON Air\" heard on stations across Canada.\n\nCarl Beukes: Carl Beukes (born 3 October 1976) is a South African actor best known for his roles as Paul McPherson in \"Isidingo\" and as the archangel Gabriel in \"Dominion\".  Beukes is a graduate of The National School of the Arts, where he studied Speech & Drama.  In addition to his credited film, television, and other screen roles, Beukes has also been in the cast of the stage productions \"Macbeth, Certified Male, Amadeus, Popcorn, Art, Black Dog\", and \"Tape\".\n\nDavid Rhodes (guitarist): David Rhodes (born 2 May 1956) is an English guitarist, singer, and songwriter best known for his long-time association with Peter Gabriel.  He was the guitarist and vocalist for the British rock band Random Hold from 1979–1982, and has been the principal studio and touring guitarist for Gabriel since 1980.  Rhodes has released two solo albums.\n\nDonald Hewlett: Donald Hewlett (30 August 19204 June 2011) was an English actor, born in Northenden, Manchester, Lancashire, and best known for his sitcom roles as Colonel Charles Reynolds in \"It Ain't Half Hot Mum\" and Lord Meldrum in \"You Rang, M'Lord? \", both written by Jimmy Perry and David Croft.  He also had a number of parts in British film and television productions.\n\nHit (album): Hit, also known as Peter Gabriel: The Definitive Two CD Collection, is a 2003 compilation album of songs by the English rock musician Peter Gabriel.  It reached No. 29 in the UK album charts and No. 100 in the U.S..  Disc one is labelled \"Hit\" and disc two \"Miss\", reflecting the first disc which comprises Gabriel's best known chart singles and the second featuring his more obscure material.\n\nDavid Gabriel: Detective Sergeant David Gabriel is a fictional character featured in TNT's \"The Closer\", portrayed by Corey Reynolds.  Gabriel was a Sergeant in the Los Angeles Police Department's (LAPD) Priority Homicide Division.  He was promoted to Detective during season five.  He is seen as Deputy Chief Brenda Leigh Johnson's right-hand man.\n\nAnthony George: Anthony George (born Ottavio Gabriel George, January 29, 1921 – March 16, 2005) was an American actor mostly seen on television.  He is best known for roles of Don Corey in CBS's \"Checkmate\", Burke Devlin #2 and Jeremiah Collins on ABC's \"Dark Shadows\", as Dr. Tony Vincente on Columbia Broadcasting System's \"Search for Tomorrow\", and Dr. Will Vernon #3 on ABC's \"One Life to Live\".\n\nCorey Sevier: Corey Daniel Sevier (born July 3, 1984) is a Canadian actor.  He is perhaps best known for his role on the Fox television series \"North Shore\" as Gabriel McKay and as Timmy Cabot in \"Lassie\".\n\nBetty Noyes: Elizabeth Noyes Hand (October 11, 1912 – December 24, 1987) was a singer and actress best known for dubbing two of Debbie Reynolds' numbers in the 1952 film \"Singin' in the Rain.\"  Today, this is a well-known example of dubbing in a movie musical; ironically, Reynolds's character in \"Singin' in the Rain\" was supposedly dubbing for another character.\n\nQuestion: Corey Reynolds is best known for his roles as David Gabriel and Seaweed from which two productions?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"known_roles_and_productions\": {\n      \"type\": \"array\",\n      \"description\": \"A list of roles the actor is known for and the productions they appeared in.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"role_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the character or role.\"\n          },\n          \"production_name\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the production.\"\n          },\n          \"production_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of production (e.g., 'Broadway adaptation', 'TV show').\"\n          }\n        },\n        \"required\": [\n          \"role_name\",\n          \"production_name\",\n          \"production_type\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"total_known_productions\": {\n      \"type\": \"integer\",\n      \"description\": \"The total count of productions listed for the actor's known roles.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"known_roles_and_productions\",\n    \"total_known_productions\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "known_roles_and_productions": {
        "type": "array",
        "description": "A list of roles the actor is known for and the productions they appeared in.",
        "items": {
          "type": "object",
          "properties": {
            "role_name": {
              "type": "string",
              "description": "The name of the character or role."
            },
            "production_name": {
              "type": "string",
              "description": "The title of the production."
            },
            "production_type": {
              "type": "string",
              "description": "The type of production (e.g., 'Broadway adaptation', 'TV show')."
            }
          },
          "required": [
            "role_name",
            "production_name",
            "production_type"
          ],
          "additionalProperties": false
        }
      },
      "total_known_productions": {
        "type": "integer",
        "description": "The total count of productions listed for the actor's known roles."
      }
    },
    "required": [
      "actor_name",
      "known_roles_and_productions",
      "total_known_productions"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
