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
Peter Chung: Peter Kunshik Chung (born April 19, 1961 in Seoul, South Korea) is a Korean American animator.  He is best known for his unique style of animation, as the creator and director of "Æon Flux", which ran as shorts on MTV's Liquid Television before launching as its own half-hour television series.

The Chronicles of Riddick: Dark Fury: The Chronicles of Riddick: Dark Fury is a 2004 made-for-DVD animated science fiction film.  It was directed by the Korean-American animator Peter Chung, and features Vin Diesel reprising his role of Richard B. Riddick.  It acts as a bridgepoint between "Pitch Black" and "The Chronicles of Riddick".

Drew Neumann: Drew Neumann is an American musician and composer of film and television scores.  He created the soundtrack of the science fiction animated series Æon Flux, and has composed music for many other shows including "The Wild Thornberrys", "Bunnicula", "The Grim Adventures of Billy & Mandy" and "Aaahh!!!  Real Monsters".  He studied film, animation, and composition at the California Institute of the Arts, where he graduated with a BFA (1982).  He has been longtime friends with animator Peter Chung.  He also assisted in the development of, and contributed sound patches and timbres to Moog Music's award-winning Animoog iPad app.

Reign: The Conqueror: Alexander (Japanese: アレクサンダー戦記 , Hepburn: Arekusandā Senki , lit.  "The Alexander War Chronicles") , released in North America as Reign: The Conqueror, is a Korean-Japanese anime first released in 1999.  A re-imagination of the life of Alexander the Great based on the novel of the same name by Hiroshi Aramata, the series was produced by international crew that drew from the resources of the worldwide animation community.  Character and setting design for the show was conceived by Peter Chung, the Korean animator who created the MTV Animated series Æon Flux.  Most of the production work was handled by Korean animators.

Dwayne Cameron: Dwayne Cameron (born 28 October 1981) is a New Zealand born film actor, writer, director and producer.  First and foremost Cameron specializes as a fine arts painter and sculptor.  Most recently as an actor he was cast by Roger Donaldson to star as the title role of Bruce McLaren in Donaldson's feature length doco-drama McLaren and starred in the Amazon TV series .  Globally Cameron is perhaps best known for playing the lead roles of Bray on the teen drama series "The Tribe" and Tyzonn in "Power Rangers Operation Overdrive" and starring as the leading role in feature films "Nice Package", "The Locals" and "Desired".  Recurring lead roles in internationally distributed TV series include "Street Legal", "The Cult", "Mercy Peak", "Shortland Street", "Agent Anna" and "Legend of the Seeker".

Robert Valley: Robert Valley is a Canadian animator and visual graphic artist.  He has a distinct visual style that is influenced by Peter Chung and Gorillaz creator Jamie Hewlett.  Valley was born In Vancouver in 1969.  After completing a four-year animation course in Vancouver, he moved to San Francisco in 1992.

Chris Donaldson: Chris Donaldson (born 26 May 1975 in Auckland, New Zealand) is a New Zealand sprinter who represented his country at the 1996 and 2000 Summer Olympics.  He is the son of film director Roger Donaldson.  He also competed at the 1998 and 2006 Commonwealth Games.  He holds the national record over 200m of 20.42, and was part of the 4 by 100m relay team that set the current national record.  Currently, Chris is the strength and conditioning coach of the NZ National Cricket team.

John Rafter Lee: John Rafter Lee is a British actor, voice actor, professional narrator, playwright and producer who is best known for his portrayal of the mysterious Trevor Goodchild in Peter Chung's "Æon Flux".  Other notable voice credits include Meier Link in both "" and "Vampire Hunter D", Pavlo Zaitsev in episode 16 of "", Jason Wynn in HBO's "Spawn" animated series, and Aristotle in "Reign: The Conqueror"

Roger Donaldson: Roger Donaldson (born 15 November 1945) is an Australian-born New Zealand film director, producer and writer whose films include "The World's Fastest Indian" (2005), acclaimed 1981 relationship drama "Smash Palace", and a run of titles shot in the United States, including the Kevin Costner films "No Way Out" (1987) and "Thirteen Days" (2000), and the 1997 disaster film "Dante's Peak".

Cool Calm Pete: Peter Chung (born March 25, 1979), better known by his stage name Cool Calm Pete, is an Korean American rapper and producer from Seoul, Korea, who is currently based in Queens, New York.  Cool Calm Pete has been profiled in major publications such as URB and XXL.  He is a founding member of the hip hop trio Babbletron.

Question: Who was born the earliest, Roger Donaldson or Peter Chung?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "earliest_born_person_name": {
      "type": "string",
      "description": "The name of the person who was born earliest."
    },
    "earliest_born_person_birth_year": {
      "type": "integer",
      "description": "The birth year of the person who was born earliest."
    },
    "comparison_details": {
      "type": "array",
      "description": "Details of the individuals whose birth years were compared.",
      "items": {
        "type": "object",
        "properties": {
          "person_name": {
            "type": "string",
            "description": "The name of the person."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the person."
          }
        },
        "required": [
          "person_name",
          "birth_year"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "earliest_born_person_name",
    "earliest_born_person_birth_year",
    "comparison_details"
  ],
  "additionalProperties": false
}
