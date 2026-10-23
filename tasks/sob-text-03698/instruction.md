{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Goodman: John Stephen Goodman (born June 20, 1952) is an American actor.  Early in his career, he was best known for playing Dan Conner on the ABC TV series \"Roseanne\" (1988–1997), for which he won a Golden Globe Award for Best Actor in 1993.  He is also a regular collaborator with the Coen brothers on such films as \"Raising Arizona\" (1987), \"Barton Fink\" (1991), \"The Big Lebowski\" (1998), \"O Brother, Where Art Thou? \" (2000), and \"Inside Llewyn Davis\" (2013).  Goodman's voice roles in animated films include Pacha in Disney's \"The Emperor's New Groove\" (2000), and Sulley in Pixar's \"Monsters, Inc.\" (2001), and \"Monsters University\" (2013).\n\nJohn Gallagher Jr.: John Howard Gallagher Jr. (born June 17, 1984) is an American actor and musician known for originating the role of Moritz Stiefel in Duncan Sheik and Steven Sater's rock musical \"Spring Awakening\", which earned him a Tony Award for Best Featured Actor in a Musical.  He also played Johnny in Green Day's Broadway musical, \"American Idiot\", Lee in the 2011 Broadway production of \"Jerusalem,\" and Edmund in the 2016 Broadway revival of \"Long Day's Journey Into Night\".  He portrayed Jim Harper in Aaron Sorkin's drama series \"The Newsroom\", starred in the HBO mini-series \"Olive Kitteridge\", and played Emmett DeWitt in \"10 Cloverfield Lane\".\n\nDan Trachtenberg: Dan Trachtenberg is an American filmmaker and podcast host.  He directed the 2016 film \"10 Cloverfield Lane\".  Trachtenberg was one of three hosts of \"The Totally Rad Show\" and a former co-host of \"Geekdrome\".  Both programs were hosted at Revision3.  Trachtenberg is also the director of the 2011 short film \"Portal: No Escape\", an episode of \"Black Mirror\" entitled \"Playtest\" and the director of various television commercials and public service announcements.\n\nMary Elizabeth Winstead: Mary Elizabeth Winstead (born November 28, 1984) is an American actress and singer.  She has starred in scream queen roles in the horror films including \"Final Destination 3\" (2006), \"Black Christmas\" (2006), \"Death Proof\" (2007), \"The Thing\" (2011), \"\" (2012), and \"10 Cloverfield Lane\" (2016).  She appeared as John McClane's daughter Lucy in the fourth and fifth films in the \"Die Hard\" franchise (2007, 2013), Ramona Flowers in \"Scott Pilgrim vs. the World\" (2010), Leah in \"The Beauty Inside\" (2012), and Kate Hannah in the Sundance drama \"Smashed\" (2012).\n\nList of Cloverfield characters: The \"Cloverfield\" universe refers to various fiction revolving around the J. J. Abrams-produced \"Cloverfield\", which includes the 2008 film itself, the manga prequel \"Cloverfield/Kishin\", and the 2016 sequel \"10 Cloverfield Lane\".  The films were subject to notably heavy viral marketing campaigns; in fact, \"Cloverfield\" was first publicized with a two-minute teaser trailer that did not advertise the film's title, only its release date: \"01·18·08.\"  Elements of the viral marketing campaign included MySpace pages created for fictional characters, unusually intense secrecy over the film's plot, and websites created for fictional companies alluded to in the film.\n\nBad Robot Productions: Bad Robot Productions (more commonly known as Bad Robot) is an American film and television production company owned by J. J. Abrams and Bryan Burk.  It is responsible for the television series \"Alias\", \"Lost\", \"Fringe\", \"Person of Interest\", \"Revolution\" and \"Westworld\" alongside the feature-length films \"Cloverfield\", \"Star Trek\", \"Super 8\", \"Star Trek Into Darkness\", \"\", \"\", \"\", \"10 Cloverfield Lane\" and most recently, \"Star Trek Beyond\".\n\nCloverfield (franchise): Cloverfield is an American anthology media franchise created and produced by J. J. Abrams consisting of three films, viral marketing websites linking the films together and a tie-in manga to the first film titled \"Cloverfield/Kishin\" (2008). \" Cloverfield\" is a found footage monster horror film released on January 18, 2008, which was well-received by critics. \" 10 Cloverfield Lane\", a spiritual sequel to the first film, is a psychological horror-thriller film that was released on March 11, 2016, and like its predecessor received positive reviews from critics.  A third film in the series, \"God Particle\", is currently scheduled for a 2018 release.\n\n10 Cloverfield Lane: 10 Cloverfield Lane is a 2016 American science fiction psychological thriller film directed by Dan Trachtenberg, produced by J. J. Abrams and Lindsey Weber and written by Josh Campbell, Matthew Stucken and Damien Chazelle.  The film stars John Goodman, Mary Elizabeth Winstead, and John Gallagher, Jr..  It is the second installment in the \"Cloverfield\" franchise.  The film was developed from a script titled \"The Cellar\", but under production by Bad Robot, it was turned into a spiritual successor of the 2008 film \"Cloverfield\".  The film follows a young woman who, after a car crash, wakes up in an underground bunker with two men who insist that an event has left the surface of Earth uninhabitable.\n\nVanilla Sky: Vanilla Sky is a 2001 American science fiction psychological thriller film directed, written, and co-produced by Cameron Crowe.  It is an English-language adaptation of Alejandro Amenábar's 1997 Spanish film \"Open Your Eyes\", which was written by Amenábar and Mateo Gil, with Penélope Cruz reprising her role from the original film.  The film has been described as \"an odd mixture of science fiction, romance and reality warp\".\n\nMat Vairo: Mat Vairo is an American actor originally from Huntington Beach, California.  He can be seen as a series regular on the A&E television series \"The Returned\" in the role of Simon Moran.  He was also seen portraying the role of Connor Bennett on the NBC series \"Revolution\".  Additional television credits include \"\", \"Switched at Birth\" and \"10 Cloverfield Lane\".\n\nQuestion: Which American actor, who is best known for playing Dan Conner, stars in the 2016 American science fiction psychological thriller film 10 Cloverfield Lane?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American actor.\"\n    },\n    \"known_for_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role the actor is best known for.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"genres\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The genres of the film.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film.\"\n        },\n        \"producers\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The producers of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"year\",\n        \"genres\",\n        \"director\",\n        \"producers\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"known_for_role\",\n    \"film_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the American actor."
      },
      "known_for_role": {
        "type": "string",
        "description": "The role the actor is best known for."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "genres": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The genres of the film."
          },
          "director": {
            "type": "string",
            "description": "The director of the film."
          },
          "producers": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The producers of the film."
          }
        },
        "required": [
          "title",
          "year",
          "genres",
          "director",
          "producers"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "known_for_role",
      "film_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
