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
Leo Kahn (entrepreneur): Leo Kahn (December 31, 1916 – May 11, 2011) was an American reporter and businessman.  He is credited as the co-founder of Staples Inc. Kahn is also considered a pioneer of the natural and health food supermarket industry, founding the Fresh Fields and Nature's Heartland chains, which are now part of Whole Foods Market.

Kim Fields: Kim Victoria Fields (born May 12, 1969) is an American actress and television director.  Fields is known for her roles as Dorothy "Tootie" Ramsey on the NBC sitcom "The Facts of Life" (1979–88), and as Regina "Regine" Hunter on the Fox sitcom "Living Single" (1993–98).  Fields is the daughter of actress/director Chip Fields and older sister of actress Alexis Fields.

Julia McKenzie: Julia Kathleen McKenzie (born 17 February 1941) is an English actress, singer, presenter, and theatre director.  On television, she is known for her BAFTA Award nominated role as Hester Fields in the sitcom "Fresh Fields" (1984–86) and its sequel "French Fields" (1989–91), and as Miss Marple in "Agatha Christie's Marple" (2008–13).

Fresh Fields: Fresh Fields is a British sitcom starring Julia McKenzie and Anton Rodgers.  A ratings success at the time, it was written by John Chapman and produced by Thames Television for ITV, running for four series between 7 March 1984 and 23 October 1986.

Anton Rodgers: Anthony "Anton" Rodgers (10 January 1933 – 1 December 2007) was an English actor and occasional director.  He performed on stage, in film, in television dramas and sitcoms.  He starred in the sitcoms "Fresh Fields" (ITV, 1984-86), as well its sequel series "French Fields" (ITV, 1989-91) and "May to December" (BBC, 1989-94).

British Comedy Guide: British Comedy Guide or BCG (formerly the British Sitcom Guide or BSG) is a British website covering all forms of British comedy, across all media.  At the time of writing, BCG has published guides to more than 7,000 individual British comedies - primarily TV and radio situation comedy, sketch shows, comedy dramas, satire, variety and panel games.  Other notable features on BCG include a news section, a message board, interviews with comedians and actors, a series of comment and opinion articles, a searchable merchandise database, and a section offering advice to aspiring comedy writers.  The website also runs "The Comedy.co.uk Awards" and hosts several podcast series, some of which have won awards.

Vol-au-vent (film): Vol-au-vent is a 1996 British comedy film directed by John McKenzie and starring Tim Mills, Dennis Waterman, Julia McKenzie and Lisa Coleman.  Its plot concerns an upper-middle class wedding that is interrupted by three jewel thieves on the run from the law.

Jon Iles: Jon Iles (born 17 May 1954 in Ripon, North Yorkshire) is an English actor who is best known for playing DC Mike Dashwood in "The Bill" from 1984 to 1992.  He returned to the series in 1996, promoted to DS for the antiques squad.  As well as a prolific stage career, Jon's other TV credits include "To the Manor Born", "The Dick Emery Show", "Doctors", "Crown Court", "Law and Disorder", "Never the Twain" and "Fresh Fields".

French Fields: French Fields is a British sitcom.  It is a sequel/continuation of the series "Fresh Fields" and ran for 19 episodes from 5 September 1989 to 8 October 1991.  It was written by John T. Chapman (who created and wrote all the episodes of "Fresh Fields") and Ian Davidson and was produced by Thames Television for ITV.

List of Fresh Fields episodes: This is a list of episodes for the British television series "Fresh Fields".

Question: What actress, nominated as Hester Fields in the sitcom "Fresh Fields" was in the 1996 British comedy Vol-au-vent?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "role_in_fresh_fields": {
      "type": "string",
      "description": "The character played by the actress in the sitcom 'Fresh Fields'."
    },
    "award_nomination": {
      "type": "string",
      "description": "The award for which the actress was nominated for her role in 'Fresh Fields'."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film the actress starred in."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    }
  },
  "required": [
    "actress_name",
    "role_in_fresh_fields",
    "award_nomination",
    "film_title",
    "film_year",
    "film_genre"
  ],
  "additionalProperties": false
}
