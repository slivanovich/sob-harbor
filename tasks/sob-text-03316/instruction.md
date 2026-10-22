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
The Eyes of Mystery: The Eyes of Mystery is a lost 1918 American silent mystery film directed by Tod Browning starring Edith Storey.

The Deciding Kiss: The Deciding Kiss is a 1918 American comedy film directed by Tod Browning.  It is not known whether the film currently survives, which suggests that it may be a lost film.

Revenge (1918 film): Revenge is a 1918 American western film directed by Tod Browning.

Which Woman?: Which Woman?  is a 1918 American silent drama film directed by Tod Browning and Harry A. Pollard.  The film stars Ella Hall as a reluctant bride and Priscilla Dean as an adventuress and leader of a gang of thieves.  The story was remade in 1923 as "Nobody's Bride".

Jim Bludso: Jim Bludso is a 1917 American drama film directed by Tod Browning.  It was Browning's first feature film as a director.  Contemporary sources are variable on the matter of whether the direction was a joint effort between Browning and the film's star, Wilfred Lucas.  In their book "Dark Carnival: The Secret World of Tod Browning, Hollywood's Master of the Macabre," David J. Skal and Elias Savada suggest that Lucas' name was added to the credit for contractual reasons, and that Browning directed "Jim Bludso" alone.  As "Jim Bludso" is presumed lost, it is uncertain what the original title card might have read in terms of directorial credit.  The film was produced by the Fine Arts unit within the Triangle Film Corporation, the same studio that made the popular Douglas Fairbanks comedies for Triangle, for whom Browning had previously worked as a scenarist.

London After Midnight (film): London After Midnight, also known as The Hypnotist, was a 1927 American silent mystery film with horror overtones directed by Tod Browning and starring Lon Chaney, Marceline Day, Conrad Nagel, Henry B. Walthall and Polly Moran.  The film was distributed by Metro-Goldwyn-Mayer, and was based on the short story "The Hypnotist" by Tod Browning, who also directed the film.

Tod Browning: Tod Browning (born Charles Albert Browning, Jr.; July 12, 1880 – October 6, 1962) was an American motion picture actor, director and screenwriter.  Browning's career spanned the silent and talkie eras.  Best known as the director of "Dracula" (1931), the cult classic "Freaks" (1932), and classic silent film collaborations with Lon Chaney and Priscilla Dean, Browning directed many movies in a wide range of genres.

The Brazen Beauty: The Brazen Beauty is a 1918 American silent comedy film directed by Tod Browning.  It is not known whether the film currently survives, which suggests that it is a lost film.

The Legion of Death: The Legion of Death is a 1918 American drama film directed by Tod Browning, and released by Metro Pictures Corporation.

Set Free (film): Set Free is a 1918 American silent comedy film directed by Tod Browning.  It is not known whether the film currently survives, which suggests that it is a lost film.

Question: The Deciding Kiss is a 1918 American comedy film directed by Tod Browning, best known as the director of what film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director_name": {
      "type": "string",
      "description": "The name of the director."
    },
    "film_in_question": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film mentioned in the question."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the film mentioned in the question."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film mentioned in the question."
        }
      },
      "required": [
        "title",
        "year",
        "genre"
      ],
      "additionalProperties": false
    },
    "best_known_film_by_director": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film the director is best known for."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the film the director is best known for."
        }
      },
      "required": [
        "title",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "director_name",
    "film_in_question",
    "best_known_film_by_director"
  ],
  "additionalProperties": false
}
