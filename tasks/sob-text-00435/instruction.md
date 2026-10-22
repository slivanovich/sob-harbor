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
The Slap (TV series): Filmed in Melbourne, Victoria, the series was produced by Matchbox Pictures' Tony Ayres, Helen Bowden and Michael McMahon, with Penny Chapman serving as executive producer.  The directors; Jessica Hobbs, Matthew Saville, Tony Ayres and Robert Connolly, directed two episodes each.  The writing team included Emily Ballou, Alice Bell, Brendan Cowell, Kris Mrksa and Cate Shortland.

2012 Stockholm International Film Festival: The 23rd Stockholm International Film Festival took place between 7 and 18 November 2012.  American actor Peter Fonda was head of the jury.  The Bronze Horse for best picture was won by the Australian/German film Lore, directed by Cate Shortland.

Cate Shortland: Cate Shortland (born 10 August 1968) is an Australian writer and director of film and television.

Salute to the Marines: Salute to the Marines is a 1943 World War II propaganda war film drama in Technicolor from MGM, produced by John W. Considine, Jr., directed by S. Sylvan Simon, that stars Wallace Beery.  The film co-stars Fay Bainter, Reginald Owen, Ray Collins, Keye Luke, and Marilyn Maxwell.  Beery's older brother Noah Beery, Sr. also appears in the film, which is set in the Philippines just prior to the beginning of the Pacific War.

S. Sylvan Simon: S. Sylvan Simon (March 9, 1910 – May 17, 1951) was an American stage/film director and producer.

Somersault (film): Somersault is a 2004 Australian independent film written and directed by Cate Shortland, featuring Abbie Cornish and Sam Worthington.  Shot in the winter of 2003, the film was released in September 2004 and screened in the Un Certain Regard section at the 2004 Cannes Film Festival.  It also swept the field at the 2004 Australian Film Institute Awards, winning every single feature film award (13 in total).

Berlin Syndrome (film): Berlin Syndrome is a 2017 Australian psychological horror-thriller film directed by Cate Shortland, and written by Shaun Grant, based upon the novel of the same name by Melanie Joosten.  It stars Teresa Palmer and Max Riemelt.

The Kettering Incident: The Kettering Incident is an Australian television drama program, first broadcast on Foxtel's Showcase channel on July 4, 2016.  The series was created by Victoria Madden and Vincent Sheehan, produced by Porchlight Films and Sweet Potato Films, and was written by Victoria Madden, Louise Fox, Cate Shortland and Andrew Knight.  A sneak preview of the series launched at the 2015 "Dark MoFo" festival, with two episodes shown to select audiences at nine locations around Tasmania.

Lore (film): Lore is a 2012 German-British-Australian historical drama based on Rachel Seiffert's much awarded novel "The Dark Room", with the screenplay written by British screenwriter Robin Mukherjee and the film's director, Cate Shortland.

I Love Trouble (1948 film): I Love Trouble is a 1948 American film noir mystery film written by Roy Huggins from his first novel "The Double Take", directed by S. Sylvan Simon, and starring Franchot Tone as Stuart Bailey.  The character of Stuart Bailey was later portrayed by Efrem Zimbalist, Jr. in the television series "77 Sunset Strip".

Question: Are Cate Shortland and S. Sylvan Simon both writers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_writers": {
      "type": "boolean",
      "description": "True if both individuals are writers, false otherwise."
    },
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "is_writer": {
          "type": "boolean",
          "description": "True if the first person is identified as a writer in the context."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles attributed to the first person."
        }
      },
      "required": [
        "name",
        "is_writer",
        "roles"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "is_writer": {
          "type": "boolean",
          "description": "True if the second person is identified as a writer in the context."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles attributed to the second person."
        }
      },
      "required": [
        "name",
        "is_writer",
        "roles"
      ],
      "additionalProperties": false
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the answer based on the roles identified for each person."
    }
  },
  "required": [
    "are_both_writers",
    "person_1",
    "person_2",
    "reasoning"
  ],
  "additionalProperties": false
}
