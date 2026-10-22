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
Burning Daylight (1920 film): Burning Daylight is a 1920 silent film drama directed by Edward Sloman with Mitchell Lewis, Helen Ferguson and William V. Mong starring.  It was distributed by Metro Pictures.

His People: His People (aka; Proud Heart) is a 1925 silent film about a young, Jewish boxer growing up on the Lower East Side of Manhattan directed by Edward Sloman.  According to film historian Lester Friedman, “Sloman’s compelling vision of the painful depths and joyous heights of immigrant life endow the film with an exuberant vitality that captivates modern filmgoers and enlightens film historians.”

Puttin' On the Ritz (film): Puttin' On the Ritz is a 1930 musical film directed by Edward Sloman and starring Harry Richman, Joan Bennett, and James Gleason.  The screenplay was written by Gleason and William K. Wells based on a story by John W. Considine, Jr. It was the first of many films to feature the popular song "Puttin' On the Ritz", which was written and published by Irving Berlin in 1929.

A Dog of Flanders (1935 film): A Dog of Flanders is a 1935 American drama film directed by Edward Sloman, based on a screenplay by Ainsworth Morgan from the story by Dorothy Yost, which she adapted from the 1872 novel of the same name by Ouida.  The film stars Frankie Thomas, appearing in only his second film (the first being "Wednesday's Child").

The Mutiny of the Elsinore (1920 film): The Mutiny of the Elisnore is a 1920 American silent action film directed by Edward Sloman and starring Mitchell Lewis, Helen Ferguson, and Noah Beery Jr. It is an adaptation of the Jack London novel "The Mutiny of the Elsinore".  It is not known whether the film currently survives.

Edward Sloman: Edward Sloman (19 July 1886, London - 29 September 1972, Woodland Hills, California) was an English silent film director, actor, screenwriter and radio broadcaster.  He directed over 100 films and starred in over 30 films as an actor between 1913 and 1938.

Alias the Deacon: Alias the Deacon is a 1928 silent film produced and released by Universal Pictures.  Based on a stage play of the same name, it was directed by Edward Sloman and is preserved at the Library of Congress Packard Campus for Audio-Visual Conservation.

Phil Rosen: Phil Rosen (May 8, 1888 – October 22, 1951) was an American film director and cinematographer.  He directed 142 films between 1915 and 1949.

His Woman: His Woman is a 1931 American romance drama film directed by Edward Sloman and starring Gary Cooper and Claudette Colbert.  Based on the novel "His Woman" by Dale Collins, the story is about a tough sea captain who discovers a baby aboard his freighter and hires a tramp, masquerading as a missionary's daughter, to care for the infant on their passage to New York.

The Kibitzer: The Kibitzer is a 1930 American comedy film directed by Edward Sloman and written by Marion Dix, Sam Mintz, Edward G. Robinson, Viola Brothers Shore and Jo Swerling.  The film stars Harry Green, Mary Brian, Neil Hamilton, Albert Gran, David Newell, Guy Oliver and Tenen Holtz.  The film was released on January 11, 1930, by Paramount Pictures.

Question: Who was born first, Phil Rosen or Edward Sloman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_born_first": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "person_born_second": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "earliest_birth_year": {
      "type": "integer"
    },
    "answer": {
      "type": "string"
    }
  },
  "required": [
    "person_born_first",
    "person_born_second",
    "earliest_birth_year",
    "answer"
  ],
  "additionalProperties": false
}
