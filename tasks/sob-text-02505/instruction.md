{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOrson Welles Commentaries: Orson Welles Commentaries (1945–46) is an ABC radio series produced and directed by Orson Welles.  Featuring commentary by Welles, with reminiscences and readings from literature, the 15-minute weekly program aired Sunday afternoons at 1:15 p.m. ET beginning September 16, 1945.  Lear Radio sponsored the program through the end of June 1946 when it failed to find a larger audience.  The series was continued by ABC as a sustaining show through October 6, 1946.  \"Orson Welles Commentaries\" was the last of Welles's own radio shows.\n\nComedy Theatre (New York City): The Comedy Theatre was a Broadway theatre located at 110 West 41st Street in Manhattan that opened in 1909.  It presented the first Broadway appearances of Katharine Cornell and Ruth Draper, as well as Eugene O'Neill's first Broadway play.  Shuttered in the wake of the Depression, it reopened in 1937 as the Mercury Theatre — the venue for Orson Welles's groundbreaking adaptation of Shakespeare's \"Julius Caesar\" and other productions for the Mercury Theatre repertory company.  In 1939 it began presenting classic Yiddish theatre.  The building was demolished in 1942.\n\nOrson Welles: George Orson Welles ( ; May 6, 1915 – October 10, 1985) was an American actor, director, writer, and producer who worked in theatre, radio, and film.  He is remembered for his innovative work in all three: in theatre, most notably \"Caesar\" (1937), a Broadway adaptation of William Shakespeare's \"Julius Caesar\"; in radio, the legendary 1938 broadcast \"The War of the Worlds\"; and in film, \"Citizen Kane\" (1941), consistently ranked as one of the greatest films ever made.\n\nTom Powers: Tom Powers (July 7, 1890 – November 9, 1955) was an American actor in theatre, films, radio and television.  A veteran of the Broadway stage, notably in plays by George Bernard Shaw, he created the role of Charles Marsden in Eugene O'Neill's \"Strange Interlude\".  He succeeded Orson Welles in the role of Brutus in the Mercury Theatre's debut production, \"Caesar\".  In films, he was a star of Vitagraph Pictures and later became best known for his role as the victim of scheming wife Barbara Stanwyck and crooked insurance salesman Fred MacMurray in the film noir classic, \"Double Indemnity\" (1944).\n\nOrson Welles Show (radio): Orson Welles Show (1941–42), also known as The Orson Welles Theater, Orson Welles and his Mercury Theater and the Lady Esther Show (after its sponsor), is a live CBS Radio series produced, directed and hosted by Orson Welles.  Broadcast Mondays at 10 p.m. ET, it made its debut September 15, 1941.  Its last broadcast was February 2, 1942.\n\nRichard France (writer): Richard France (born May 5, 1938) is an American playwright, author, and film and drama critic.  He is a recognized authority on the stage work of American filmmaker Orson Welles.  His publication, \"The Theatre of Orson Welles\", which received a CHOICE Outstanding Academic Book Award in 1979, has been called \"a landmark study\" and has been translated into Japanese.  His 1990 companion volume, \"Orson Welles on Shakespeare\" has been praised by Welles critics and biographers.\n\nCaesar (Mercury Theatre): Caesar is the title of Orson Welles's innovative 1937 adaptation of William Shakespeare's \"Julius Caesar\", a modern-dress bare-stage production that evoked comparison to contemporary Fascist Italy and Nazi Germany.  Considered Welles's highest achievement in the theatre, it premiered November 11, 1937, as the first production of the Mercury Theatre, an independent repertory theatre company that presented an acclaimed series of productions on Broadway through 1941.\n\nThis is Orson Welles: This is Orson Welles is a 1992 book by Orson Welles (1915–1985) and Peter Bogdanovich that comprises conversations between the two filmmakers recorded over several years, beginning in 1969.  The wide-ranging volume encompasses Welles's life and his own stage, radio and film work as well as his insights on the work of others.  The interview book was transcribed by Bogdanovich after Welles's death, at the request of Welles's longtime companion and professional collaborator, Oja Kodar.  Welles considered the book his autobiography.\n\nThe Orson Welles Almanac: The Orson Welles Almanac (also known as Radio Almanac and The Orson Welles Comedy Show) is a 1944 CBS Radio series directed and hosted by Orson Welles.  Broadcast live on the Columbia Pacific Network, the 30-minute variety program was heard Wednesdays at 9:30 p.m. ET January 26 – July 19, 1944.  The series was sponsored by Mobilgas and Mobiloil.  Many of the shows originated from U.S. military camps, where Welles and his repertory company and guests entertained the troops with a reduced version of \"The Mercury Wonder Show\".  The performances of the all-star jazz band that Welles brought together for the show were an important force in the revival of traditional New Orleans jazz in the 1940s.\n\nMe and Orson Welles: Me and Orson Welles is a 2008 British-American period drama film directed by Richard Linklater and starring Zac Efron, Christian McKay, and Claire Danes.  Based on Robert Kaplow's novel of the same name, the story, set in 1937 New York, tells of a teenager hired to perform in Orson Welles's groundbreaking stage adaptation of William Shakespeare's \"Julius Caesar\".  He becomes attracted to a career-driven production assistant.\n\nQuestion: Which role did Tom Powers play in the Orson Welles's 1937 adaptation of William Shakespeare's \"Julius Caesar\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"role_played\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role the actor played.\"\n    },\n    \"play_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the play adaptation.\"\n        },\n        \"original_work\": {\n          \"type\": \"string\",\n          \"description\": \"The original work the play was adapted from.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the play.\"\n        },\n        \"year_of_production\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the play was produced.\"\n        },\n        \"theatre_company\": {\n          \"type\": \"string\",\n          \"description\": \"The theatre company that produced the play.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"original_work\",\n        \"director\",\n        \"year_of_production\",\n        \"theatre_company\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"role_played\",\n    \"play_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "role_played": {
        "type": "string",
        "description": "The specific role the actor played."
      },
      "play_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the play adaptation."
          },
          "original_work": {
            "type": "string",
            "description": "The original work the play was adapted from."
          },
          "director": {
            "type": "string",
            "description": "The director of the play."
          },
          "year_of_production": {
            "type": "integer",
            "description": "The year the play was produced."
          },
          "theatre_company": {
            "type": "string",
            "description": "The theatre company that produced the play."
          }
        },
        "required": [
          "title",
          "original_work",
          "director",
          "year_of_production",
          "theatre_company"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "role_played",
      "play_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
