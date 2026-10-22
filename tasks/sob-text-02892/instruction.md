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
Frontier of the Stars: Frontier of the Stars is a lost 1921 American drama silent film directed by Charles Maigne and written by Charles Maigne and Albert Payson Terhune.  The film stars Thomas Meighan, Faire Binney, Alphonse Ethier, Edward Ellis, Gus Weinberg and Florence Johns.  The film was released January 20, 1921, by Paramount Pictures.

The Invisible Bond: The Invisible Bond is a lost 1919 American silent drama film directed by Charles Maigne and written by Charles Maigne based upon the novel "The See-Saw: A Story of To-day" by Sophie Kerr.  The film stars Irene Castle, Huntley Gordon, Claire Adams, Fleming Ward, George Majeroni, and Helen Greene.  The film was released on November 23, 1919, by Paramount Pictures.

Hush Money (1921 film): Hush Money is a lost 1921 American silent drama film directed by Charles Maigne and written by Charles Maigne and Samuel Merwin.  The film stars Alice Brady, George Fawcett, Larry Wheat, Harry Benham, and Jerry Devine.  The film was released in November 1921, by Paramount Pictures.

The Golden Fetter: The Golden Fetter is a 1917 American romance silent film directed by Edward LeSaint and written by Charles Tenney Jackson and Charles Maigne.  The film stars Wallace Reid, Anita King, Tully Marshall, Guy Oliver, Walter Long and Mrs. Lewis McCord.  The film was released on January 25, 1917, by Paramount Pictures.

Women (1985 film): Women is a 1985 Hong Kong drama film directed by Stanley Kwan in his directorial debut.  Like Kwan's following films, "Women" focuses on female characters and their efforts to overcome cultural restrictions.  The cast includes Cora Miao, Chow Yun-fat, Cherie Chung and Elaine Jin.  It was nominated for nine Hong Kong Film Awards including Best Picture.

Stanley Kwan: Stanley Kwan (; born October 9, 1957) is a Hong Kong Second Wave Hong Kong film director and producer.

Drums of Fate: Drums of Fate is a 1923 American silent drama film directed by Charles Maigne and written by Will M. Ritchey and Stephen French Whitman.  The film stars Mary Miles Minter, Maurice 'Lefty' Flynn, George Fawcett, Robert Cain, Casson Ferguson, Bertram Grassby, and Noble Johnson.  The film was released on January 14, 1923, by Paramount Pictures.  It is not known whether the film currently survives.

The Cowboy and the Lady (1922 film): The Cowboy and the Lady is a 1922 American silent Western film directed by Charles Maigne and stars Mary Miles Minter and Tom Moore.  Distributed by Paramount Pictures, the film is based on the Clyde Fitch Broadway stage play of the same name which starred Maxine Elliott and her then-husband Nat C. Goodwin.  It was the last silent version of the many silent filming of the play and Minter's third to last motion picture.  It is not known whether the film currently survives.

Kwan Pun Leung: Kwan Pun Leung (關本良) is a Hong Kong cinematographer.  After starting his career as a photographer in the local arts and culture scene, he made his motion picture debut as director of photography on director Stanley Kwan’s 1997 film "Hold You Tight".  Kwan then worked on Ann Hui’s films "July Rhapsody" (2002) and "The Postmodern Life of My Aunt" (2006), as well as Wong Kar-wai’s 2004 film "2046".

Charles Maigne: Charles Maigne (November 11, 1879 – November 28, 1929) was an American screenwriter and film director of the silent era.  He wrote for 32 films between 1916 and 1928.  He also directed 18 films between 1918 and 1923.

Question: What type of profession does Charles Maigne and Stanley Kwan have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "professions"
      ],
      "additionalProperties": false
    },
    "person_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "professions"
      ],
      "additionalProperties": false
    },
    "common_profession": {
      "type": "string"
    }
  },
  "required": [
    "person_one",
    "person_two",
    "common_profession"
  ],
  "additionalProperties": false
}
