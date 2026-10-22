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
Paris Honeymoon: Paris Honeymoon is a 1939 American musical film directed by Frank Tuttle and written by Frank Butler and Don Hartman.  The film stars Bing Crosby, Franciska Gaal, Akim Tamiroff, Shirley Ross, Edward Everett Horton and Ben Blue.  Filming took place in Hollywood from May 23 to July 1938 and the film was released on January 27, 1939 by Paramount Pictures.

Hostages (1943 film): Hostages is a war film produced by Paramount Pictures and released in 1943.  It was directed by Frank Tuttle from a script by Frank Butler and Lester Cole based on the 1942 novel of the same name by Stefan Heym.  The film stars Luise Rainer, Arturo de Cordova, William Bendix and Paul Lukas and features Katina Paxinou and Oskar Homolka.

Something Always Happens (1928 film): Something Always Happens is a 1928 American comedy silent film directed by Frank Tuttle and written by Raymond Cannon, Herman J. Mankiewicz, Florence Ryerson and Frank Tuttle.  The film stars Esther Ralston, Neil Hamilton, Sôjin Kamiyama, Charles Sellon, Roscoe Karns, Lawrence Grant and Mischa Auer.  The film was released on March 24, 1928, by Paramount Pictures.

Varsity (film): Varsity is a lost 1928 American comedy silent film directed by Frank Tuttle and written by Howard Estabrook, George Marion Jr. and Wells Root.  The film stars Charles 'Buddy' Rogers, Mary Brian, Chester Conklin, Phillips Holmes, Robert Ellis and John Westwood.  The film was released on October 27, 1928, by Paramount Pictures.

Frank Tuttle: Frank Wright Tuttle (August 6, 1892 – January 6, 1963) was a Hollywood film director and writer who directed films from 1922 ("The Cradle Buster") to 1959 ("Island of Lost Women").

Easy Come, Easy Go (1928 film): Easy Come, Easy Go is a 1928 American comedy silent film directed by Frank Tuttle and written by Owen Davis, George Marion Jr. and Florence Ryerson.  The film stars Richard Dix, Nancy Carroll, Charles Sellon, Frank Currier, Arnold Kent and Christian J. Frank.  The film was released on April 21, 1928, by Paramount Pictures.

The Kentuckians: The Kentuckians is a lost 1921 American silent drama film directed by Charles Maigne and written by Frank Tuttle based upon the novel of the same name by John Fox, Jr..  The film stars Monte Blue, Wilfred Lytell, Diana Allen, Francis Joyner, J.H. Gilmour, John Miltern, and Thomas S. Brown.  The film was released on February 20, 1921, by Paramount Pictures.

The Studio Murder Mystery: The Studio Murder Mystery is a 1929 American mystery film directed by Frank Tuttle and written by Ethel Doherty, A. Channing Edington, Carmen Ballen Edington, Joseph L. Mankiewicz and Frank Tuttle.  The film stars Neil Hamilton, Doris Hill, Warner Oland, Fredric March, Chester Conklin, Florence Eldridge and Guy Oliver.  The film was released on June 1, 1929, by Paramount Pictures.

John English (director): John Wilkinson English (25 June 1903 – 11 October 1969) was a British film editor and film director.  He is most famous for the film serials he co-directed with William Witney for Republic Pictures such as "Zorro's Fighting Legion" and "Drums of Fu Manchu".

Don Juan Quilligan: Don Juan Quilligan is a 1945 American comedy film directed by Frank Tuttle and written by Frank Gabrielson and Arthur Kober.  The film stars William Bendix, Joan Blondell, Phil Silvers, Anne Revere, B.S. Pully and Mary Treen.  The film was released on June 1, 1945, by 20th Century Fox.

Question: Frank Tuttle and John English, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "occupations": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "occupations"
      ],
      "additionalProperties": false
    },
    "person_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "occupations": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "occupations"
      ],
      "additionalProperties": false
    },
    "mutual_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "number_of_mutual_occupations": {
      "type": "integer"
    }
  },
  "required": [
    "person_a",
    "person_b",
    "mutual_occupations",
    "number_of_mutual_occupations"
  ],
  "additionalProperties": false
}
