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
The Sound of Fury (film): The Sound of Fury (reissued as Try and Get Me) is a 1950 crime film noir directed by Cy Endfield starring Frank Lovejoy, Kathleen Ryan, and Richard Carlson.  The film is based the 1947 novel "The Condemned" by Jo Pagano, who also wrote the screenplay.

Hide and Seek (1964 film): Hide and Seek is a 1964 British thriller film directed by Cy Endfield.

The Underworld Story: The Underworld Story is a 1950 American film noir crime film directed by Cy Endfield starring Dan Duryea, Herbert Marshall, Gale Storm, Howard Da Silva and Michael O'Shea.  Da Silva plays the loud-mouthed gangster Carl Durham, one of his last roles before becoming blacklisted.

James Cagney: James Francis "Jimmy" Cagney Jr. (July 17, 1899March 30, 1986) was an American actor and dancer, both on stage and in film, though he had his greatest impact in film.  Known for his consistently energetic performances, distinctive vocal style, and deadpan comic timing, he won acclaim and major awards for a wide variety of performances.  He is best remembered for playing multifaceted tough guys in movies such as "The Public Enemy" (1931), "Taxi! " (1932), "Angels with Dirty Faces" (1938), and "White Heat" (1949), and was typecast or limited by this view earlier in his career.  In 1999, the American Film Institute ranked him eighth among its list of greatest male stars of Classic Hollywood Cinema.  Orson Welles said of Cagney, "[he was] maybe the greatest actor who ever appeared in front of a camera", and Stanley Kubrick considered him to be one of the best actors of all time.

Suzannah Olivier: Suzannah Endfield Olivier is an author, journalist, and nutritionist.  She is the author of more than fifteen best-selling books on health and nutrition, including 'The Breast Cancer Prevention and Recovery Diet', 'Natural Hormone Balance', '500 of the Most Stress Busting Techniques You'll Ever Need', 'Food Medicine', 'Healthy Food for Happy Kids', and 'What Should I Feed My Baby?' .  She is the daughter of film director Cy Endfield.

Tarzan's Savage Fury: Tarzan's Savage Fury is a 1952 film starring Lex Barker as Tarzan, Dorothy Hart as Jane, and Patric Knowles.  The movie was directed by Cy Endfield.  While most Tarzan films of the 1930s, 1940s and 1950s presented Tarzan as a very different character from the one in Edgar Rice Burroughs' novels, this movie does make some allusions to the novels.  It was shot in Chatsworth, California's Iverson Ranch.  The film was the last to be directed by Cyril "Cy" Endfield in the US.  Finding himself one of Hollywood's film-makers blacklisted by the House Un-American Activities Committee he moved to Britain.  The film was co-written by Cyril Hume, who'd contributed substantially to the "Tarzan" series back in its bigger budget MGM days.

Sea Fury (film): Sea Fury is a 1958 British action film directed by Cy Endfield and starring Stanley Baker, Victor McLaglen (in his final film), Luciana Paluzzi and Grégoire Aslan.  The film's plot involves a violent rivalry that develops between two tug-boat operators in Spain.  Some of the exteriors were shot in the Costa Brava.  Sea Fury was instrumental in the comeback of director Cy Endfield, who'd been forced to flee Hollywood and seek work in London because of the Hollywood Blacklist.

Sands of the Kalahari: Sands of the Kalahari is a 1965 British adventure film starring Stuart Whitman, Stanley Baker, Susannah York, Harry Andrews and Theodore Bikel, based on the 1960 novel by William Mulvihill.  The screenplay was written by Cy Endfield and William Mulvihill and directed by Cy Endfield.  It was filmed in South-West Africa and Spain and released by Paramount Pictures.

The Argyle Secrets: The Arygle Secrets is a 1948 film directed by Cy Endfield.  It was based on a half-hour radio play by Endfield, originally heard on CBS's "Suspense".  The film was made for the micro-budget of $100,000 and shot in eight days.

Cy Endfield: Cyril Raker Endfield (November 10, 1914 – April 16, 1995) was an American screenwriter, film director, theatre director, author, magician and inventor, based in Britain from 1953.

Question: Were both James Cagney and Cy Endfield magicians?

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
      "description": "True if both individuals were magicians, false otherwise."
    },
    "individuals_involved": {
      "type": "array",
      "description": "Details about each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_magician": {
            "type": "boolean",
            "description": "Indicates if the individual was a magician according to the context."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions attributed to the individual in the context."
          }
        },
        "required": [
          "name",
          "is_magician",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the given answer based on the context."
    }
  },
  "required": [
    "question_asked",
    "answer",
    "individuals_involved",
    "reasoning"
  ],
  "additionalProperties": false
}
