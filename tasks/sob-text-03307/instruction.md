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
List of Strike Witches episodes: "Strike Witches" is an anime series released as part of a mixed media project by Humikane Shimada, which also includes light novels and manga.  Taking place in an alternate Earth in the 1940s, the series focuses on the 501st Joint Fighter Wing of Strike Witches, magically powered girls who fight against an alien race known as the Neuroi.  An original video animation was produced by Gonzo and directed by Kunihisa Sugishima and released in Japan on January 1, 2007.  The first season of the anime television series was directed by Kazuhiro Takamura and also produced by Gonzo and aired in between July 3, 2008 and September 18, 2008.  The series was also streamed with English subtitles on YouTube, BOST TV and Crunchyroll.  The uncensored DVDs were released September 26, 2008 and January 30, 2009.  The series was licensed by Funimation Entertainment and was released in a complete box set in North America on March 30, 2010.  The second season, titled "Strike Witches 2" was produced by AIC and again directed by Takamura.  It was broadcast in Japan between July 7, 2010 and September 23, 2010.  It was also simulcast on Crunchyroll and Funimation's anime portal.  This series was also licensed by Funimation and released on Blu-ray Disc and DVD in North America on October 2, 2012.  A film adaptation was released on March 17, 2012.  An original video animation series produced by Silver Link, "Operation Victory Arrow", began release in September 2014.

Lasher (disambiguation): Lasher is the second novel in the Anne Rice series "Lives of the Mayfair Witches".

Anne Rice: Anne Rice (born Howard Allen Frances O'Brien; October 4, 1941) is an American author of gothic fiction, Christian literature, and erotica.  She is perhaps best known for her popular and influential series of novels, "The Vampire Chronicles", revolving around the central character of Lestat.  Books from "The Vampire Chronicles" were the subject of two film adaptations, "Interview with the Vampire" in 1994, and "Queen of the Damned" in 2002.

Merrick (novel): Merrick (2000) is the seventh book in Anne Rice's "The Vampire Chronicles" series.  This book brings together Rice's vampires and the Mayfair Witches.

Lasher: Lasher (1993) by Anne Rice is the second novel in her series "Lives of the Mayfair Witches".

Louis de Pointe du Lac: Louis de Pointe du Lac is a fictional character in Anne Rice's "The Vampire Chronicles" series.  He begins his life as a mortal man and later becomes a vampire.  He is the protagonist who tells his story in "Interview with the Vampire" (the first book of "The Vampire Chronicles").  He also features in "The Vampire Lestat", "The Queen of the Damned", "The Tale of the Body Thief", "Memnoch The Devil", "The Vampire Armand" , "Merrick", "Prince Lestat" and "Prince Lestat and the Realms of Atlantis".

Taltos (Rice novel): Taltos (1994) is the title of the third novel in the trilogy "Lives of the Mayfair Witches" written by Anne Rice.

Blood Canticle: Blood Canticle is a 2003 novel by Anne Rice which incorporates the new characters from her novel "Blackwood Farm" with those from her previous "Vampire Chronicles" and "Mayfair Witches" series.  The novel was originally intended to conclude the saga of Rice's famed vampire Lestat de Lioncourt, but in March 2014 she announced a sequel titled "Prince Lestat".

Blackwood Farm: Blackwood Farm (2002) is the ninth novel in Anne Rice's "The Vampire Chronicles" series and also the fifth in "The Mayfair Witches" series, continuing the unified story introduced in 2000's "Merrick".

The Witching Hour (novel): The Witching Hour (1990) by Anne Rice is the first novel in the "Lives of the Mayfair Witches" series.  It begins the tale of a family of witches, and a spirit that has guided their fortunes for generations.

Question: Which book in "The Mayfair Witches" series includes Lestat?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_title": {
      "type": "string",
      "description": "The title of the book."
    },
    "author": {
      "type": "string",
      "description": "The author of the book."
    },
    "series_information": {
      "type": "array",
      "description": "Details about the series the book belongs to.",
      "items": {
        "type": "object",
        "properties": {
          "series_name": {
            "type": "string",
            "description": "The name of the series."
          },
          "series_position": {
            "type": "string",
            "description": "The book's position within that series (e.g., 'first', 'second', 'fifth')."
          }
        },
        "required": [
          "series_name"
        ],
        "additionalProperties": false
      }
    },
    "character_mentioned": {
      "type": "string",
      "description": "The character whose inclusion in the book was questioned."
    },
    "reason_for_character_inclusion": {
      "type": "string",
      "description": "The reason why the character is included in this specific book, based on the context."
    }
  },
  "required": [
    "book_title",
    "author",
    "series_information",
    "character_mentioned",
    "reason_for_character_inclusion"
  ],
  "additionalProperties": false
}
