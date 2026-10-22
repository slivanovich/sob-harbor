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
Chinatown After Dark: Chinatown After Dark is a 1931 American Pre-Code drama film directed by Stuart Paton.  The film costars several favorites from the silent film era.

The Alamo: Shrine of Texas Liberty: The Alamo: Shrine of Texas Liberty is a 1938 American black-and-white war film directed by Stuart Paton and produced by H. W. Kier and Norman Sheldon.  The film was a two-reel short produced in a couple of weeks San Antonio, Texas.  The film was done in pantomime and audio was done by narration and organ music.

Reputation (1921 film): Reputation is a lost 1921 American silent drama film produced and distributed by the Universal Film Manufacturing Company and directed by Stuart Paton.  Priscilla Dean stars in what was considered one of her finest performances.

In Old Cheyenne (1931 film): In Old Cheyenne is a 1931 western film directed by Stuart Paton.  It is a re-make of the 1930 film "Phantom of the Desert".

Stuart Paton: Stuart Paton (23 July 1883 – 16 December 1944) was a British director, screenwriter and actor of the silent era.  He directed 67 films between 1915 and 1938.  He also wrote for 24 films between 1914 and 1927.  Despite a sizable list of credits, Paton was never well-regarded, especially as a director.

Beloved Jim: Beloved Jim is a lost 1917 American silent drama film produced and released by Universal Film Manufacturing Company.  It was directed by Stuart Paton and starred Priscilla Dean.

The Border Raiders: The Border Raiders is a 1918 American silent western film directed by Stuart Paton and starring Betty Compson and George Larkin.

20,000 Leagues Under the Sea (1916 film): 20,000 Leagues Under the Sea is a 1916 silent film directed by Stuart Paton.  The film's storyline is based on the novel "Twenty Thousand Leagues Under the Sea" by Jules Verne.  It also incorporates elements from Verne's "The Mysterious Island".

Bryan Singer: Bryan Jay Singer (born September 17, 1965) is an American film director, film producer, writer, and actor.  He is the founder of Bad Hat Harry Productions and he has produced or co-produced almost all of the films he has directed.

Clipped Wings (1937 film): Clipped Wings is a 1937 American crime and aviation Kier-Phillips production for National pictures, directed by Stuart Paton from an original story and screenplay by Paul Willett.  The film stars Lloyd E. Hughes, Rosalind Keith and William Janney.

Question: Were both Bryan Singer and Stuart Paton actors and directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "answer": {
      "type": "boolean",
      "description": "The boolean answer to the question."
    },
    "individuals_roles": {
      "type": "array",
      "description": "Details about each individual mentioned in the question and their roles.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_director": {
            "type": "boolean",
            "description": "True if the individual was a director, false otherwise."
          },
          "is_actor": {
            "type": "boolean",
            "description": "True if the individual was an actor, false otherwise."
          }
        },
        "required": [
          "name",
          "is_director",
          "is_actor"
        ],
        "additionalProperties": false
      }
    },
    "all_individuals_were_directors": {
      "type": "boolean",
      "description": "True if all individuals mentioned were directors, false otherwise."
    },
    "all_individuals_were_actors": {
      "type": "boolean",
      "description": "True if all individuals mentioned were actors, false otherwise."
    }
  },
  "required": [
    "question_asked",
    "answer",
    "individuals_roles",
    "all_individuals_were_directors",
    "all_individuals_were_actors"
  ],
  "additionalProperties": false
}
