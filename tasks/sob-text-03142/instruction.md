{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBlood In Blood Out: Blood In Blood Out (also known as Bound by Honor) is a 1993 American crime-drama film directed by Taylor Hackford.  It follows the intertwining lives of three Chicano relatives from 1972 to 1984.  They start out as members of a street gang in East Los Angeles, and as dramatic incidents occur, their lives and friendships are forever changed.  \"Blood In Blood Out\" was filmed in 1991 throughout the Spanish-speaking areas of Los Angeles and inside California's San Quentin State Prison.\n\nThe Gentleman from Nowhere: The Gentleman from Nowhere is a 1948 American crime-drama film directed by William Castle.\n\nBugsy: Bugsy is a 1991 American crime-drama film directed by Barry Levinson which tells the story of mobster Bugsy Siegel and his relationship with Virginia Hill.  It stars Warren Beatty as Siegel and Annette Bening as Hill, as well as Harvey Keitel, Ben Kingsley, Elliott Gould, and Joe Mantegna.  The screenplay was written by James Toback from research material by Dean Jennings' 1967 book \"We Only Kill Each Other\".\n\nPrison Break (film): Prison Break is a 1938 American crime-drama film directed by Arthur Lubin and starring Barton MacLane, Glenda Farrell and Paul Hurst.  The film was based on the story \"Walls of San Quentin\" by Norton S. Parker.  It was released by Universal Pictures on July 12, 1938.  A fisherman confesses to a murder he didn't commit to protect a friend.  Determined to keep out of trouble in prison, but another convict makes things difficult for him.\n\nDeath in the Desert (film): Death in the Desert is a 2015 American crime-drama film directed and produced by Josh Evans and starring Michael Madsen and Shayla Beesley, with John Palladino, Paz de la Huerta, and Roxy Saint appearing in supporting roles.  Principal filming completed in February 2014 in Las Vegas, Nevada.  It is the second film collaboration between Madsen and Evans, who produced \"The Price of Air\" in which Madsen starred.\n\nGood Time (film): Good Time is a 2017 American crime-drama film directed by Ben and Josh Safdie and written by Josh Safdie and Ronald Bronstein.  The film stars Robert Pattinson, Barkhad Abdi and Jennifer Jason Leigh.  Its original soundtrack was composed by electronic musician Oneohtrix Point Never.\n\nThe Funeral (1996 film): The Funeral is a 1996 American crime-drama film directed by Abel Ferrara and starring Christopher Walken, Chris Penn, Annabella Sciorra, Isabella Rossellini, Vincent Gallo, Benicio del Toro and Gretchen Mol.\n\nAmerican Pastoral (film): American Pastoral is a 2016 American crime-drama film directed by Ewan McGregor and written by John Romano, based on the 1997 novel of the same name by Philip Roth.  The film stars McGregor, Jennifer Connelly, Dakota Fanning, Peter Riegert, Rupert Evans, Uzo Aduba, Molly Parker and David Strathairn.  Principal photography began on September 21, 2015, in Pittsburgh.\n\nI Am a Thief: I Am a Thief is a 1934 American crime-drama film directed by Robert Florey.\n\nPeter Riegert: Peter Riegert (born April 11, 1947) is an American actor, screenwriter and film director, best known for his roles as Donald \"Boon\" Schoenstein in \"Animal House\" (1978), \"Mac\" MacIntyre in \"Local Hero\" (1983), fast-talking gangster Aldo in \"Oscar\" (1991), tough, no-nonsense Lt. Kellaway in \"The Mask\" (1994), newspaper editor Delbert McGinty in \"We Bought a Zoo\" (2011) and glove manufacturer Lou Levov in \"American Pastoral\" (2016).  He directed the short film \"By Courier\" (2000) and, along with producer Ericka Frederick, was nominated for the Academy Award for Best Live Action Short Film.\n\nQuestion: What film star of the 2016 American crime-drama film directed by Ewan McGregor was best known for his role in \"Animal House?\"\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film in question.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who fits the criteria.\"\n    },\n    \"actor_role_in_film\": {\n      \"type\": \"string\",\n      \"description\": \"The role the actor played in the specified film.\"\n    },\n    \"actor_known_for_film\": {\n      \"type\": \"string\",\n      \"description\": \"The film the actor is best known for, as per the question.\"\n    },\n    \"actor_known_for_role\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role in the 'known for' film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_director\",\n    \"actor_name\",\n    \"actor_role_in_film\",\n    \"actor_known_for_film\",\n    \"actor_known_for_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film in question."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_director": {
        "type": "string",
        "description": "The director of the film."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who fits the criteria."
      },
      "actor_role_in_film": {
        "type": "string",
        "description": "The role the actor played in the specified film."
      },
      "actor_known_for_film": {
        "type": "string",
        "description": "The film the actor is best known for, as per the question."
      },
      "actor_known_for_role": {
        "type": "string",
        "description": "The specific role in the 'known for' film."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_director",
      "actor_name",
      "actor_role_in_film",
      "actor_known_for_film",
      "actor_known_for_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
