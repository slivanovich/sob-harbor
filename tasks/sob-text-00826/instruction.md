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
Zeitgeist (Levellers album): Zeitgeist is the fourth album by the Levellers.  It was released in 1995 and reached #1 in the UK album charts, making it the band's most successful album.  Two singles were released from the album – "Hope St.", which reached #12 in the UK single charts, and "Fantasy", which reached 16.  Additionally, a re-recorded version of "Just the One" featuring Joe Strummer was released, reaching #12, as well as a live version of "Exodus" from the later "Headlights, White Lines, Black Tar Rivers (Best Live)" album the next year, which reached #24.

Scott Brick: Scott Brick (born (1966--) 30, 1966 in Santa Barbara, California), is an American actor, writer and award-winning narrator of over 800 audiobooks, including popular titles such as "", "Moneyball", "Cloud Atlas (novel)", "A Princess of Mars", "The Bourne Identity (novel)", "The Bourne Supremacy", "The Bourne Ultimatum", "Atlas Shrugged", "Sideways", "Do Androids Dream of Electric Sheep? " (filmed as "Blade Runner"), "I, Robot", "Mystic River (novel)", "Helter Skelter (book)", "Patriot Games", "Bid Time Return" (filmed as "Somewhere in Time (film))", "In Cold Blood", the "Dune (franchise)" series, "Ender's Game", and "Fahrenheit 451".  He has narrated works for a number of high-profile authors, including Tom Clancy, Robert Ludlum, Michael Crichton, John Grisham, Clive Cussler, Stephen J. Cannell, William Faulkner, Nelson DeMille, Brad Meltzer, Harlan Coben, Gregg Hurwitz, David Baldacci, Orson Scott Card, Frank Herbert, Brian Herbert, Kevin J. Anderson, Joseph Finder, Stephen R. Donaldson, Nathaniel Philbrick, Terry Brooks, Steve Berry (novelist), Gene Wilder, Philip K. Dick, Dennis Lehane, Douglas J. Preston, Lincoln Child, Ayn Rand, Justin Cronin and Isaac Asimov, among others.

Headlights, White Lines, Black Tar Rivers (Best Live): Headlights, White Lines, Black Tar Rivers (Best Live)

Life in Cold Blood: Life in Cold Blood is a BBC nature documentary series written and presented by David Attenborough, first broadcast in the United Kingdom from 4 February 2008 on BBC One.

In Cold Blood (Johnny Thunders album): In Cold Blood is a 1983 double album by Johnny Thunders.  The "In Cold Blood" album contains studio recordings and the Live LP contains live recordings.

Cold Blood (band): Cold Blood is a long-standing R&B horn funk band founded by Larry Field in 1968 and was originally based in the East Bay region of the San Francisco Bay Area.  The band has also performed and recorded under the name Lydia Pense and Cold Blood, due to the popularity of their lead singer, Lydia Pense.

Black tar heroin: Black tar heroin is a form of heroin that is sticky like tar or hard like coal.  Its dark color is the result of crude processing methods that leave behind impurities.  Despite its name, black tar heroin can also be dark orange or dark brown in appearance.  It is generally less expensive than other forms of heroin.

Black Tar Heroin (film): Black Tar Heroin: The Dark End of the Street is a 1999 documentary directed by Steven Okazaki.  Filmed from 1995 to 1998 in the Tenderloin, San Francisco, California, the documentary describes the lives of heroin addicts.

Thriller (Cold Blood album): Thriller is a 1973 album by San Francisco funk group Cold Blood.  Lydia Pense and the rest of Cold Blood were backed by The Pointer Sisters.

Mastocarpus papillatus: Mastocarpus papillatus, sometimes called Turkish washcloth, black tar spot, or grapestone is a species of red algae in the Phyllophoraceae family.  It is sometimes confused with the distantly related "Turkish towel" ("Chondracanthus exasperatus") which is of a similar texture but larger.  The specific epithet "papillatus" ('with papillae') is due to the nipple-like projections on the female gametophyte which can give the texture of a terrycloth washcloth found at a Turkish bath.

Question: Was Life in Cold Blood broadcast in the same country that Black Tar Heroin was filmed in? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "entity_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the first entity."
        },
        "broadcast_country": {
          "type": "string",
          "description": "The country where the first entity was broadcast."
        }
      },
      "required": [
        "name",
        "broadcast_country"
      ],
      "additionalProperties": false
    },
    "entity_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the second entity."
        },
        "filming_country": {
          "type": "string",
          "description": "The country where the second entity was filmed."
        }
      },
      "required": [
        "name",
        "filming_country"
      ],
      "additionalProperties": false
    },
    "countries_match": {
      "type": "boolean",
      "description": "True if the broadcast country of entity 1 matches the filming country of entity 2, false otherwise."
    },
    "final_answer": {
      "type": "string",
      "description": "The final answer to the question (yes/no)."
    }
  },
  "required": [
    "question_asked",
    "entity_1",
    "entity_2",
    "countries_match",
    "final_answer"
  ],
  "additionalProperties": false
}
