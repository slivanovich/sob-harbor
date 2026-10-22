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
Proving Ground (Star Trek: Enterprise): "Proving Ground" is the thirteenth episode from the third season of the television series "".  It's the sixty-fifth episode of the series, first airing on January 21, 2004.  The episode continues the Xindi story arc, opening with a montage of scenes from previous shows.  Archer and the re-occurring character, the Andorian Captain Shran take on the Xindi in an uncertain dalliance.

Mike Farrell: Michael Joseph Farrell, Jr. (born February 6, 1939) is an American actor, best known for his role as Captain B.J. Hunnicutt on the television series "M*A*S*H" (1975–83).  He is an activist for various political causes.

Welcome to Korea: "Welcome to Korea" was a 2-episode story arc, the 73rd and 74th episodes of the "M*A*S*H" television series, and first two episodes of the fourth season of the series.  First aired on September 12, 1975, the series' first 60 minute episode (double the normal time) was most notable for its off-screen departure of the character of Captain Trapper John McIntyre (played by Wayne Rogers), and his replacement by the freshly drafted Captain B.J. Hunnicutt (played by Mike Farrell).

Titties and Dragons: "Titties and Dragons" is the ninth episode in the seventeenth season of the American animated television series "South Park".  The 246th episode of the series overall, it premiered on Comedy Central in the United States on December 4, 2013.  It is the conclusion of a three-episode story arc that began with "Black Friday", and continued with "A Song of Ass and Fire".  The story centers upon the children of South Park, role playing as characters from "Game of Thrones", split into two factions over whether to collectively purchase bargain-priced Xbox One or PlayStation 4 video game consoles at an upcoming Black Friday sale at the local mall, where Randy Marsh has been made the Captain of mall security.  The episode received critical acclaim.

Villain of the week: "Villain of the week" (or, depending on genre, "monster of the week", "freak of the week" or "alien of the week") is an antagonist that only appears on one episode of a work of fiction.  A villain of the week is commonly seen in American and Japanese genre-based television series.  As many shows of this type air episodes weekly at a rate of ten to twenty new episodes per year, there is often a new antagonist in the plot of each week's episode.  The main characters usually confront and vanquish these characters, often leaving them never to be seen again (as in "Charmed", "Smallville" and "Scooby-Doo").  Some series alternate between using such antagonists and furthering the series' ongoing plotlines (as in "Buffy the Vampire Slayer", "Supernatural", "Fringe" and "The X-Files", where fandom is often divided over preference for one type of episode versus the other), while others use these one-time foes as pawns of the recurring adversaries (as in "Kamen Rider", "Sailor Moon", "Super Sentai" and their American equivalent, "Power Rangers").  On other occasions, these villains return reformed, becoming invaluable allies or gaining a larger role in the story.  The American action drama "Burn Notice" focuses on short-lived antagonists, but the final portion of every episode is committed to developing a larger story arc.  The British sci-fi programme "Torchwood" used this format in its first two series, before switching to a continuous story format.

Paradise Island Lost (comics): "Paradise Island Lost" is the name to two-part story arc written by Phil Jimenez who also did the artwork, featured in "Wonder Woman (Vol.  2)" #168-169.  This was Jimenez' second story arc under his run on Wonder Woman, with the first being the "Gods of Gotham" four-issue story arc from "Wonder Woman (Vol.  2)" #164-167.  Just like "Gods of Gotham" where he was a co-writer with J. M. DeMatteis, he co-wrote this story arc with George Pérez, best known to have rebooted Wonder Woman in 1987 first with the "Gods and Mortals" story arc, that marked his return to the book since 1992.  It wouldn't be until issue #171 where Jimenez became the book's sole writer.  The story's name is taken from an epic poem of the same name by John Milton.

Xindi (Star Trek): The Xindi is the collective term for six fictional races in the science fiction television series "".  The entire , broadcast in 2003 to 2004, centered on this group of previously unknown aliens.  They are native to the planet Xindus in a region of space known as the Delphic Expanse.  They consist of five species resembling familiar Earth animals (a rarity for alien races in "Star Trek") and a sixth resembling humans.  At first they appeared as violent enemies wanting no interaction with humanity, but common ground gradually emerged as the crew of the "Enterprise" discovered that the Xindi were being manipulated into this enmity by their Guardians.  Some Xindi became important recurring characters as the 24-episode story arc unfolded.

Penumbra (Star Trek: Deep Space Nine): "Penumbra" is the 167th episode of the television series "", the 17th episode of the .  It is the first episode of the series' final 10-episode story arc.  The title refers to the shadow effect of the same name.

Castle (season 4): The fourth season of American crime-comedy-drama television series "Castle" was ordered on January 10, 2011, by ABC.  The season aired from September 19, 2011, to May 7, 2012.  The fourth season initially contained 22 episodes, but on December 8, 2011, ABC ordered an additional episode, bringing the total episode count to 23 episodes.  Penny Johnson Jerald joined the cast as the new captain, Victoria "Iron" Gates for the fourth season.

A Song of Ass and Fire: "A Song of Ass and Fire" is the eighth episode in the seventeenth season of the American animated television series "South Park".  The 245th episode of the series overall, it first aired on Comedy Central in the United States on November 20, 2013.  The episode serves as a continuation of the previous episode, "Black Friday", in which the children of South Park, role-playing as characters from "Game of Thrones", are split into two factions over whether to collectively purchase bargain-priced Xbox One or PlayStation 4 video game consoles at an upcoming Black Friday sale at the local mall, where Randy Marsh has been made the Captain of mall security.  The story arc concludes with the following episode, "Titties and Dragons".

Question: Name the American actor, best known for his role as Captain B.J. Hunnicutt in a television series which included a 2-episode story arc where we see the departure of Captain Trapper and his replacement by this new Captain? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the American actor."
    },
    "actor_nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "best_known_role": {
      "type": "object",
      "properties": {
        "character_name": {
          "type": "string",
          "description": "The name of the character the actor is best known for."
        },
        "series_name": {
          "type": "string",
          "description": "The name of the television series where the character appeared."
        }
      },
      "required": [
        "character_name",
        "series_name"
      ],
      "additionalProperties": false
    },
    "related_story_arc": {
      "type": "object",
      "properties": {
        "story_arc_name": {
          "type": "string",
          "description": "The name of the 2-episode story arc."
        },
        "episode_count": {
          "type": "integer",
          "description": "The number of episodes in the story arc."
        },
        "key_events": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key events that occurred during the story arc."
        }
      },
      "required": [
        "story_arc_name",
        "episode_count",
        "key_events"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "actor_nationality",
    "best_known_role",
    "related_story_arc"
  ],
  "additionalProperties": false
}
