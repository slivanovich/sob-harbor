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
Paul America: Paul Johnson (February 25, 1944 – October 19, 1982), better known as Paul America, was an American actor who was a member of Andy Warhol's Superstars.  He starred in one Warhol-directed film, "My Hustler" (1965), and also appeared in Edie Sedgwick's final film "Ciao!  Manhattan" (1972).

Rainbow Bridge (film): Rainbow Bridge is a 1971 film directed by Chuck Wein about different countercultural figures interacting on the Hawaiian island of Maui.  He described it as "a kind of space-age "Candid Camera".  We're going to place Pat [New York model Pat Hartley, the protagonist] in all kinds of real-life situtations, and film what happens.  We're going to shoot a lot of film and just see what comes out of it."  Harry Shapiro adds, "the idea was to shoot an antidote to "Easy Rider", showing the positive side of the youth movement."

Chuck Wein: Chuck Wein (March 24, 1939March 18, 2008) was an American promoter and manager of entertainment acts whose celebrity stemmed from his five-year (1964–1969) association with Andy Warhol and from his discovery of Edie Sedgwick who became Warhol Superstar of 1965.

Vinyl (1965 film): Vinyl is a 1965 American black-and-white experimental film directed by Andy Warhol at The Factory.  It is an early adaptation of Anthony Burgess' novel "A Clockwork Orange", starring Gerard Malanga, Edie Sedgwick, Ondine, and Tosh Carillo, and featuring such songs as "Nowhere to Run" by Martha and the Vandellas, "Tired of Waiting for You" by The Kinks, "The Last Time" by The Rolling Stones and "Shout" by The Isley Brothers.

Beauty No. 2: Beauty No. 2 is a 1965 American avant-garde film by directed by Andy Warhol and starring Edie Sedgwick and Gino Piserchio.  Chuck Wein also has a role in the film but never appears onscreen.  Wein wrote the scenario and is also credited as assistant director.

Edie Sedgwick: Edith Minturn "Edie" Sedgwick (April 20, 1943 – November 16, 1971) was an American actress and fashion model.  She is best known for being one of Andy Warhol's superstars.  Sedgwick became known as "The Girl of the Year" in 1965 after starring in several of Warhol's short films in the 1960s.  She was dubbed an "It Girl", while "Vogue" magazine also named her a "Youthquaker".

Horse (1965 film): Horse is a 1965 underground film directed by Andy Warhol, written by Ronald Tavel, and starring Edie Sedgwick, Gregory Battcock, Tosh Carillo, Ondine, Norman Glick, Daniel Cassidy Jr., and Larry Latrae (Latreille).  Warhol himself makes a cameo appearance in the film.

Beauty No. 1: Beauty No. 1 is a 1965 film by Andy Warhol starring Edie Sedgwick, Kip Stagg a.k.a.Bima Stagg, and Chuck Wein.

Poor Little Rich Girl (1965 film): Poor Little Rich Girl is a 1965 underground film by Andy Warhol starring Edie Sedgwick.  "Poor Little Rich Girl" was conceived as the first film in part of a series featuring Sedgwick called "The Poor Little Rich Girl Saga".  The saga was to include other Warhol films: "Restaurant", "Face", and "Afternoon".

Ciao! Manhattan: Ciao!  Manhattan is a 1972 American avant garde film starring Edie Sedgwick, one of Andy Warhol's Superstars.  A scripted drama in which most of the actors play themselves, it centers on a character very closely based on Sedgwick, and deals with the pain of addiction and the lure of fame.

Question: what does Chuck Wein and Edie Sedgwick have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_nationality": {
      "type": "string",
      "description": "The nationality shared by both individuals."
    },
    "shared_professional_contexts": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Professional groups or movements both individuals were associated with."
    },
    "films_with_shared_involvement": {
      "type": "array",
      "items": {
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
          "sedgwick_role": {
            "type": "string",
            "description": "Edie Sedgwick's role in the film."
          },
          "wein_role": {
            "type": "string",
            "description": "Chuck Wein's role in the film."
          }
        },
        "required": [
          "title",
          "year",
          "sedgwick_role",
          "wein_role"
        ],
        "additionalProperties": false
      },
      "description": "Films where both Chuck Wein and Edie Sedgwick had a role."
    },
    "wein_sedgwick_relationship": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The type of direct relationship between them."
        },
        "description": {
          "type": "string",
          "description": "A description of their direct relationship."
        }
      },
      "required": [
        "type",
        "description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "common_nationality",
    "shared_professional_contexts",
    "films_with_shared_involvement",
    "wein_sedgwick_relationship"
  ],
  "additionalProperties": false
}
