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
Big Grrrl Small World: Big Grrrl Small World (stylized as Big GRRRL Small World) is the second studio album by American rapper and singer Lizzo.  Recorded at Justin Vernon's April Base Studios in Fall Creek, Wisconsin, it was released on BGSW on December 11, 2015.

Small World (U.S. TV series): Small World was a children's animated anthology show and variety show, which aired on Cartoon Network in the 1990's every Sunday morning, Small World is also aired on BabyFirstTV in the 2000's, after another show aimed at preschoolers "Big Bag".  It sometimes aired on weekday afternoons at 1 PM PST.  It featured several segments from animated TV programs from several countries around the world except for Japan, China, and Korea.  Japan only has anime which only airs on Toonami on Cartoon Network.

Small World (2010 film): Small World (French: Je n'ai rien oublié ) is a 2010 Franco-German drama film directed by Bruno Chiche and adapted from the book "Small World" by Martin Suter.

Son of Flubber: Son of Flubber is the 1963 sequel to the Walt Disney children's sci-fi comedy movie "The Absent-Minded Professor" (1961).  Both films star Fred MacMurray as a scientist who has perfected a high-bouncing substance, Flubber ("flying rubber") that can levitate an automobile and cause athletes to bounce into the sky.  The film co-stars Nancy Olson and Keenan Wynn, and was directed by Robert Stevenson.  Many of the cast members from "The Absent-Minded Professor" also appear in this film, including Elliott Reid and Tommy Kirk.  The film was shot in black and white, but a colorized version was released on VHS in 1997.

Small World (board game): Small World is a board game designed by Philippe Keyaerts, Illustrated by Miguel Coimbra and Cyrille Daujean as graphic designer, and published by Days of Wonder in 2009.  The game is a reworking of Keyaerts' 1999 game "Vinci".  Small World has won several awards, including "Games" magazine 2010 Game of the Year.

Martin Parr: Martin Parr (born 23 May 1952) is a British documentary photographer, photojournalist and photobook collector.  He is known for his photographic projects that take an intimate, satirical and anthropological look at aspects of modern life, in particular documenting the social classes of England, and more broadly the wealth of the Western world.  His major projects have been rural communities (1975–82), "The Last Resort" (1983–85), "The Cost of Living" (1987–89), "Small World" (1987–94) and "Common Sense" (1995–99).

Horse to the Water: "Horse to the Water" is a song written by George Harrison and his son Dhani.  It was originally performed by Jools Holland's Rhythm and Blues Orchestra, featuring Harrison, on the album "Small World, Big Band" (also known as "Jools Holland's Big Band Rhythm & Blues").  Recorded on 2 October 2001, the song is Harrison's last performance on a record.  Harrison only performed vocals on the track, as he was too weak from battling cancer to play guitar, and he died just over eight weeks later on 29 November.  He listed the song's publisher as "R.I.P Music Ltd" instead of his usual music company Harrisongs, which Holland said showed "Harrison's dark sense of humour."  (In the liner notes of some versions of the CD, the credit is "Umlaut Corporation.")

It's a Small World: It's a Small World (currently styled it's a small world) is a water-based dark ride located in the Fantasyland area at the various Walt Disney Parks and Resorts worldwide; these include: Disneyland Park in Anaheim, California, the Magic Kingdom at Walt Disney World Resort in Lake Buena Vista, Florida, Tokyo Disneyland, Disneyland Paris, and Hong Kong Disneyland.  The ride features over 300 audio-animatronic children in traditional costumes from cultures around the world, frolicking in a spirit of international unity, and singing the attraction's title song, which has a theme of global peace.

Medfield College: Medfield College is a fictitious university used as the setting for several films by The Walt Disney Company.  Among them are the two "Professor Brainard" movies, "The Absent-Minded Professor" (1961) and "Son of Flubber" (1963); and the "Dexter Reilly" trilogy: "The Computer Wore Tennis Shoes" (1969), "Now You See Him, Now You Don't" (1972), and "The Strongest Man in the World" (1975); as well as the remake of "The Absent-Minded Professor", "Flubber" (1997).

Philippe Keyaerts: Philippe Keyaerts is a Belgian designer of German-style board games.  His two first published games are "Vinci" and "Evo".  Those two games use the mechanism of allowing the players to spend victory points to improve the characteristics of their play.  He also invented "Space Blast", a small space battle game.  Philippe Keyaerts is best known as the designer of "Small World", a 2009 fantasy-themed board game based upon a remake of "Vinci".

Question: what do It's a Small World and Son of Flubber have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_entity_name": {
      "type": "string",
      "description": "The name of the entity that both items have in common."
    },
    "entity_type": {
      "type": "string",
      "description": "The type of the common entity (e.g., 'Company', 'Creator')."
    },
    "shared_items": {
      "type": "array",
      "description": "A list of items that share the common entity.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the item."
          },
          "item_type": {
            "type": "string",
            "description": "The type of the item (e.g., 'film', 'ride')."
          }
        },
        "required": [
          "title",
          "item_type"
        ],
        "additionalProperties": false
      }
    },
    "commonality_description": {
      "type": "string",
      "description": "A brief description of the commonality."
    }
  },
  "required": [
    "common_entity_name",
    "entity_type",
    "shared_items",
    "commonality_description"
  ],
  "additionalProperties": false
}
