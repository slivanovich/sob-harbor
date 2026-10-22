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
The Dark Horse (1932 film): The Dark Horse is a 1932 American pre-Code political comedy film, starring Warren William and Bette Davis.  The movie was directed by Alfred E. Green.

Warren Low: Warren Low (born 1906; died in Woodland Hills, Los Angeles on July 27, 1989) was a noted American film editor who worked on "Now, Voyager", "Out of the Fog", and others.  He was an originator for what became the American Cinema Editors and received awards from them.

Cerium hexaboride: Cerium hexaboride (CeB, also called cerium boride, CeBix, CEBIX, and (incorrectly) CeB) is an inorganic chemical, a boride of cerium.  It is a refractory ceramic material.  It has low work function and one of the highest electron emissivity known, and is stable in vacuum.  The principal use of cerium hexaboride is a coating of hot cathodes, or hot cathodes made of cerium hexaboride crystals.  It usually operates at temperature of 1450 °C.

Lanthanum hexaboride: Lanthanum hexaboride (LaB, also called lanthanum boride and LaB) is an inorganic chemical, a boride of lanthanum.  It is a refractory ceramic material that has a melting point of 2210 °C, and is insoluble in water and hydrochloric acid.  It has a low work function and one of the highest electron emissivities known, and is stable in vacuum.  Stoichiometric samples are colored intense purple-violet, while boron-rich ones (above LaB) are blue.  Ion bombardment changes its color from purple to emerald green.

Fashions of 1934: Fashions of 1934 is a 1934 American pre-Code musical comedy film directed by William Dieterle with musical numbers created and directed by Busby Berkeley.  The screenplay by F. Hugh Herbert and Carl Erickson was based on the story "The Fashion Plate" by Harry Collins and Warren Duff.  The film stars William Powell, Bette Davis, Hugh Herbert and Frank McHugh, and has songs by Sammy Fain (music) and Irving Kahal (lyrics).  (Sometime after the initial release, the title "Fashions of 1934" was changed to "Fashions", replacing the original title with an insert card stating William Powell in "Fashions").

It's Love I'm After: It's Love I'm After is a 1937 American comedy film directed by Archie Mayo and starring Leslie Howard, Bette Davis, and Olivia de Havilland.  Based on the story "Gentlemen After Midnight" by Maurice Hanline, with a screenplay by Casey Robinson, the film is about a couple who have postponed their marriage eleven times and who continue to plot and scheme their way to marriage.  The film marked the third on-screen pairing of Leslie Howard and Bette Davis, following "Of Human Bondage" and "The Petrified Forest".

Safetica Technologies: Safetica Technologies is a European data loss prevention software (DLP) vendor.  Safetica DLP is designed for contextual protection of data at the endpoint level.  It blocks erroneous or malicious actions which might lead to sensitive files leaving a company.  Safetica can also identify wasted costs connected with low work productivity or ineffective use of software licenses or wasted print.

The Star (1952 film): The Star is a 1952 American drama film directed by Stuart Heisler and starring Bette Davis, Sterling Hayden and Natalie Wood.  The plot tells the story of an aging, washed up actress who is desperate to restart her career.  Even though the film was a critical and commercial failure, Bette Davis received an Academy Award nomination for Best Actress.

Now, Voyager: Now, Voyager is a 1942 American drama film starring Bette Davis, Paul Henreid, and Claude Rains, and directed by Irving Rapper.  The screenplay by Casey Robinson is based on the 1941 novel of the same name by Olive Higgins Prouty.

Baby Jane Hudson: Baby Jane Hudson is a fictional character and the antagonist of Henry Farrell's 1960 novel "What Ever Happened to Baby Jane? " She was portrayed by Bette Davis in the 1962 film adaptation and by Lynn Redgrave in the 1991 made-for-TV remake.  The 1962 production is the better-known, with Bette Davis earning an Academy Award nomination for her performance.  The character is portrayed by Susan Sarandon,who plays Bette Davis, in the TV anthology "Feud: Bette and Joan" aired in 2017.

Question: Which movie staring Bette Davis did Warren Low work on?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the movie was released."
    },
    "main_actors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the main actors starring in the movie."
    },
    "crew_members": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the crew member."
          },
          "role": {
            "type": "string",
            "description": "The role of the crew member in the film production."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "description": "A list of key crew members and their roles, including Warren Low."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why this movie fits the criteria of starring Bette Davis and having Warren Low work on it."
    }
  },
  "required": [
    "movie_title",
    "release_year",
    "main_actors",
    "crew_members",
    "reasoning"
  ],
  "additionalProperties": false
}
