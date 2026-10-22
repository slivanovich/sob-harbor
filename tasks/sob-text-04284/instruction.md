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
Simon (game): Simon is an electronic game of memory skill invented by Ralph H. Baer and Howard J. Morrison, with software programming by Lenny Cope.  The device creates a series of tones and lights and requires a user to repeat the series.  If the user succeeds the series becomes progressively longer and more complex.  Once the user fails, the game is over.  The original version was manufactured and distributed by Milton Bradley but after they went out of business, the product was taken over by Hasbro.  Much of the assembly language was written by Charles Kapps , who taught computer science at Temple University and also wrote one of the first books on the theory of computer programming.  "Simon" was launched in 1978 at Studio 54 in New York City and was an immediate success, becoming a pop culture symbol of the 1970s and 1980s.

Old Broadway Theatre: The Broadway Theatre (September 27, 1847 – April 2, 1859), called the Old Broadway Theatre since its demise, was at 326–30 Broadway, between Pearl and Anthony (now Worth) Streets in Manhattan.  With over 4000 seats, it was the largest theater ever built in New York when it opened.  During its brief existence, many prominent performers of the era appeared on its stage.  It presented plays, opera, ballet, hippodrama, and circus performances in a space that was reconfigured several times.  The operators always struggled to make money, however, and after twelve years the Broadway Theatre was replaced by a more profitable building, for the textile trade.

The Theatre Museum: The Theatre Museum (TTM) is located at 30 Worth Street in Manhattan, New York City.  Its mission is to preserve, protect and perpetuate the legacy of theatre, including Broadway theatre.  The Theatre Museum continues the legacy of The Broadway Theatre Institute begun in 1995 by presenting Awards for Excellence in Theatre History Preservation and Theatre Arts Education.  It currently functioning as a museum-at-large and is not open to the public.

Tony Award: The Antoinette Perry Award for Excellence in Broadway Theatre, more commonly known as Tony Award, recognizes the excellence in live Broadway theatre.  The awards are presented by the American Theatre Wing and The Broadway League at an annual ceremony in New York City.  The awards are given for Broadway productions and performances, and an award is given for regional theatre.  Several discretionary non-competitive awards are also given, including a Special Tony Award, the Tony Honors for Excellence in Theatre, and the Isabelle Stevenson Award.  The awards are named after Antoinette "Tony" Perry, co-founder of the American Theatre Wing.

Merlin (game): Merlin (sometimes known as Merlin, the Electronic Wizard) was a handheld electronic game first made by Parker Brothers in 1978.  The game was invented by former NASA employee Bob Doyle, his wife Holly, and brother-in-law Wendl Thomis.  Merlin is notable as one of the earliest and most popular handheld games, selling over 5 million units during its initial run, as well as one of the most long-lived, remaining popular throughout the 1980s.  A version of the game was re-released in 2004 by the Milton Bradley Company.

Broadway Theatre (53rd Street): The Broadway Theatre (formerly Universal's Colony Theatre, B.S. Moss' Broadway Theatre, Earl Carroll's Broadway Theatre, and Ciné Roma) is a Broadway theatre located in midtown Manhattan.  It has a large seating capacity of 1,761, and unlike most Broadway theaters, it is actually located on Broadway, at number 1681.

Jules Podell: Jules Podell (died 1973) was a former nightclub operator who ran the Copacabana nightclub in New York City.  Although it was opened in 1940 by Monte Proser, Podell was put in place by mob boss Frank Costello, Proser's partner.  By 1950 Podell was making all the decisions and Proser was gone.  Podell ran the club until he died in 1973.

Electronic game: An electronic game is a game that employs electronics to create an interactive system with which a player can play.  Video game is the most common form today, and for this reason the two terms are often mistakenly used synonymously.  Other common forms of electronic game include such products as handheld electronic games, standalone systems (e.g. pinball, slot machines, or electro-mechanical arcade games), and exclusively non-visual products (e.g. audio games).

Broadway theatre: Broadway theatre, commonly known as Broadway, refers to the theatrical performances presented in the 41 professional theatres with 500 or more seats located in the Theater District and Lincoln Center along Broadway, in Midtown Manhattan, New York City.  Along with London's West End theatre, Broadway theatre is widely considered to represent the highest level of commercial theatre in the English-speaking world.

Studio 54: Studio 54 is a former nightclub and currently a Broadway theatre, located at 254 West 54th Street, between Eighth Avenue and Broadway in Manhattan, New York City.  The building, originally built as the Gallo Opera House, opened in 1927, after which it changed names several times, eventually becoming CBS radio and television Studio 52.

Question: The electronic game of memory skill, Simon, was launched in 1978 at what former nightclub that is currently a Broadway theatre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_name": {
      "type": "string",
      "description": "The name of the electronic game."
    },
    "launch_year": {
      "type": "integer",
      "description": "The year the game was launched."
    },
    "launch_venue": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the venue where the game was launched."
        },
        "venue_type_at_launch": {
          "type": "string",
          "description": "The type of venue at the time of the game's launch."
        },
        "current_venue_type": {
          "type": "string",
          "description": "The current type of the venue."
        },
        "city": {
          "type": "string",
          "description": "The city where the venue is located."
        }
      },
      "required": [
        "name",
        "venue_type_at_launch",
        "current_venue_type",
        "city"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "game_name",
    "launch_year",
    "launch_venue"
  ],
  "additionalProperties": false
}
