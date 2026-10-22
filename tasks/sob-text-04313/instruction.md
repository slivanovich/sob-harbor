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
Marvel Productions: Marvel Productions Ltd., later known as New World Animation Ltd., was the television and film studio subsidiary of the Marvel Entertainment Group, based in Hollywood, Los Angeles, California.  It later became a subsidiary of New World Entertainment and eventually of News Corporation (Fox Entertainment Group).

Vladimir Ignatyuk (icebreaker): Vladimir Ignatyuk (formerly MV Arctic Kalvik) is a diesel icebreaker that was built in 1983 at the Victoria Yard of the Burrard Yarrows Corporation located in Victoria, British Columbia, Canada for "Beaudril Limited", an oil-drilling subsidiary of Gulf Canada Resources Ltd., for use in anchor handling and ice breaking in the Beaufort Sea.  Two other Class 4 icebreakers were built for Beaudril by Burrard Yarrows Co., "Terry Fox" and "Miscaroo".

20th Century Fox: Twentieth Century Fox Film Corporation (known as Twentieth Century-Fox Film Corporation with hyphen from 1935 until 1985, stylized as 20th Century Fox or simply known as Fox or 20th Century Fox Pictures) is an American film studio currently owned by 21st Century Fox.  It is one of the "Big Six" major American film studios and is located in the Century City area of Los Angeles, just west of Beverly Hills.  The studio was owned by News Corporation from 1984 to 2013.

Paramount Pictures: Paramount Pictures Corporation (also known simply as Paramount) is an American film studio based in Hollywood, California, that has been a subsidiary of the American media conglomerate Viacom since 1994.  Paramount is the fifth oldest surviving film studio in the world, the second oldest in the United States, and the sole member of the "Big Six" film studios still located in the Los Angeles neighborhood of Hollywood.  In 1916, film producer Adolph Zukor contracted 22 actors and actresses and honored each with a star on the logo.  These fortunate few would become the first "movie stars."  In 2014, Paramount Pictures became the first major Hollywood studio to distribute all of its films in digital form only.

Austin Young: Austin Young (born April 12, 1966) is an American photographer, film maker and new media artist currently based in Los Angeles.  His work has created an encyclopedic documentation of sub and trans culture in New York, Los Angeles and San Francisco.  Young's photographs have been featured in major publications such as Interview magazine, OK, and Flaunt and have been shown in solo exhibitions and projects at LACMA (Los Angeles, CA), Machine Project (Los Angeles, CA), Hammer Museum (Los Angeles, CA), Berkeley Art Museum (Berkeley, California); and as well as groups shows at Los Angeles Contemporary Exhibitions (Los Angeles, CA) and Stephen Cohen Gallery (Los Angeles, CA).  In addition to photography and film making, Young is co-founder of Fallen Fruit, an art collective who use fruit as a common denominator for public engagement and collaboration.

Wildlife WayStation: The Wildlife WayStation is a 160 acre animal sanctuary in northern Los Angeles County dedicated to rescuing and rehabilitating wild and exotic animals.  A charitable corporation located within the boundaries of Angeles National Forest, the facility was founded in 1976 by animal activist Martine Colette, who still serves as the organization's director.

Universal Studios Hollywood: Universal Studios Hollywood is a film studio and theme park in the San Fernando Valley area of Los Angeles County, California.  About 70% of the studio lies within the unincorporated county island known as Universal City while the rest lies within the city limits of Los Angeles, California.  It is one of the oldest and most famous Hollywood film studios still in use.  Its official marketing headline is "The Entertainment Capital of LA".  It was initially created to offer tours of the real Universal Studios sets and is the first of many full-fledged Universal Studios Theme Parks located across the world.

Find the Lady (1936 film): Find the Lady is a 1936 British comedy film directed by Roland Grillette and starring Jack Melford, Althea Henley and George Sanders.  Its plot involves an American confidence trickster who pretends to be a spiritual healer.  The film was made at Wembley Studios by the British subsidiary of 20th Century Fox.  The sets were designed by art director William Hemsley.

CBS Studio Center: CBS Studio Center is a television and film studio located in the Studio City district of Los Angeles in the San Fernando Valley.  It is located at 4024 Radford Avenue and takes up a triangular piece of land, with the Los Angeles River bisecting the site.  The lot, which is not open to the public for tours, has 18 sound stages from 7,000 to 25000 sqft , 220000 sqft of office space, and 223 dressing rooms.

Universal Pictures: Universal Pictures (also referred to as Universal Studios or simply Universal) is an American film studio owned by Comcast through the Universal Filmed Entertainment Group division of its wholly owned subsidiary NBCUniversal.  The company was founded in 1912 by Carl Laemmle, Mark Dintenfass, Charles O. Baumann, Adam Kessel, Pat Powers, William Swanson, David Horsley, Robert H. Cochrane, and Jules Brulatour, and is the oldest surviving film studio in the United States, the world's fourth oldest after Gaumont, Pathé and Nordisk Film, and the oldest in terms of the overall film market .  Its studios are located in Universal City, California, and its corporate offices are located in New York City.

Question: What is the British subsidiary of the American film studio corporation located in Los Angeles?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "american_film_studio": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the American film studio."
        },
        "location": {
          "type": "string",
          "description": "The location of the American film studio."
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "british_subsidiary": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the British subsidiary."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "A description of the relationship between the American studio and its British subsidiary."
    }
  },
  "required": [
    "american_film_studio",
    "british_subsidiary",
    "relationship_description"
  ],
  "additionalProperties": false
}
