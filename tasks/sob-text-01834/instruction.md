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
Jimmy (2013 film): Jimmy is a 2013 dramatic family film directed by Mark Freiburger.  It is based on a novel of the same name, by author Robert Whitlow.  The film adaptation was additionally written by director Mark Freiburger, and producer Gary Wheeler.

Sergeant Murphy: Sergeant Murphy is a 1938 American comedy film directed by B. Reeves Eason and written by Sy Bartlett and William Jacobs.  The film stars Ronald Reagan, Mary Maguire, Donald Crisp, Ben Hendricks Jr. and William B. Davidson.  The film was released by Warner Bros. on January 1, 1938.

B. Reeves Eason: B. Reeves Eason (October 2, 1886 – June 9, 1956) was an American film director, actor and screenwriter.  His directorial output was limited mainly to low-budget westerns and action pictures, but it was as a second-unit director and action specialist that he was best known.  He was famous for staging spectacular battle scenes in war films and action scenes in large-budget westerns, but he acquired the nickname "Breezy" for his "breezy" attitude towards safety while staging his sequences—during the famous cavalry charge at the end of "Charge of the Light Brigade" (1936) that Eason directed, so many horses were killed or injured so severely that they had to be euthanized that both the public and Hollywood itself were outraged, resulting in the selection of the American Humane Society by the beleaguered studios to provide representatives on the sets of all films using animals to ensure their safety.

Spy Ship (film): Spy Ship is a 1942 American Warner Bros. B picture drama film directed by B. Reeves Eason and written by Robert E. Kent.  The film, a remake of "Fog Over Frisco" that was based on the short story "The Five Fragments" by George Dyer stars Craig Stevens, Irene Manning (playing a character based on Laura Ingalls), Maris Wrixon, Tod Andrews, Peter Whitney and John Maxwell.  The film was released by Warner Bros. on June 6, 1942.

Service with the Colors: Service with the Colors is a 1940 American short drama film directed by B. Reeves Eason.  It was nominated for an Academy Award at the 13th Academy Awards for Best Short Subject (Two-Reel).

B. Reeves Eason Jr.: Barnes Reeves Eason, better known by his screen name B. Reeves Eason Jr. (November 19, 1914 – October 25, 1921), was an American silent film child actor.  Billed as "Master Breezy Reeves Jr." and "Universal's Littlest Cowboy", and later also known as Breezy Eason Jr., he was the son of motion picture director and actor B. Reeves Eason and his wife, the actress Jimsy Maye.

Mark Freiburger: Stephen Mark Freiburger (born July 16, 1983 in Roanoke, Virginia) is an American filmmaker.  Freiburger grew up in Charlotte, North Carolina, attending Providence High School and the University of North Carolina School of the Arts.  At age 22, Freiburger produced and directed his first feature, "Dog Days of Summer", and at 29 he directed the "Greatest Super Bowl Commercial of All Time" as named by CBS.

The Miracle Rider: The Miracle Rider is a 1935 Mascot movie serial directed by B. Reeves Eason and Armand Schaefer.  The serial stars silent movie cowboy star Tom Mix in his last major film role.

Dog Days of Summer (film): Dog Days of Summer is a 2007 American independent feature film directed by Mark Freiburger and shot on location in Edenton, North Carolina.  It is based on an original screenplay by screenwriters Travis Beacham and Christopher J. Waild.

Competition (1915 film): Competition is a 1915 short film produced by the American Film Manufacturing Company, released by Mutual Film, directed by B. Reeves Eason and Tom Ricketts and starring Charlotte Burton.  It was Eason's directional debut, and he also acted in it.

Question: B. Reeves Eason and Mark Freiburger, have which nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "individuals": {
      "type": "array",
      "description": "List of individuals whose nationality is being queried.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "shared_nationality": {
      "type": "string",
      "description": "The nationality shared by all listed individuals."
    },
    "nationality_source": {
      "type": "string",
      "description": "The source of information for the nationality."
    }
  },
  "required": [
    "individuals",
    "shared_nationality",
    "nationality_source"
  ],
  "additionalProperties": false
}
