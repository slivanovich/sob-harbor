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
Léonce Perret: Léonce Joseph Perret (14 March 1880 – 12 August 1935) was a prolific and innovative French film actor, director and producer.  He also worked as a stage actor and director.  Often described as avant-garde for his unorthodox directing methods, Léonce Perret introduced innovative camera, lighting and film scoring techniques to French cinema.

The Orchid Dancer: The Orchid Dancer (French:La danseuse Orchidée) is a 1928 French silent film directed by Léonce Perret and starring Louise Lagrange, Ricardo Cortez and Xenia Desni.

Beauty Spot (film): Beauty Spot (French: Grains de beauté) is a 1932 French musical comedy film directed by Pierre Caron and Léonce Perret and starring Simone Cerdan, Marfa d'Hervilly and Doris Morrey.  It is a remake of the 1931 German film "Opera Ball" and is part of the operetta film genre.

Léonce Perret filmography (actor): A definitive filmography for Léonce Perret would be virtually impossible given that he wrote, acted in, directed or produced more than 400 films.  Of those more than 400 films, only roughly one third are still available today.  The remaining copies are stored mostly at the Gaumont Film Library, the French Film Library, the National Cinematography Film Archives and in several other European film libraries such as the Nederlands Filmmuseum in Amsterdam.

The Silent Master: The Silent Master is a 1917 American drama film directed by Léonce Perret and starring Robert Warwick.  The film is an adaption of "The Court of St. Simon" by E. Phillips Oppenheim.

The Nude Woman (1926 film): The Nude Woman (French: La femme nue) is a 1926 French silent drama film directed by Léonce Perret and starring Iván Petrovich, Louise Lagrange and Nita Naldi.  Based on a play by Henry Bataille, it was remade as a sound film in 1932.

Larry Cohen: Lawrence G. "Larry" Cohen (born July 15, 1941) is an American film producer, director, and screenwriter.  He is best known as a B-Movie auteur of horror and science fiction films – often containing a police procedural element – during the 1970s and 1980s.  He has since concentrated mainly on screenwriting including the Joel Schumacher thriller "Phone Booth" (2002), "Cellular" (2004) and "Captivity" (2007).  In 2006 Cohen returned to the directing chair for Mick Garris' "Masters of Horror" TV series (2006); he directed the episode "Pick Me Up".

Léonce Perret filmography (director): A definitive filmography for Léonce Perret would be virtually impossible given that he wrote, acted in, directed or produced more than 400 films.  Of those, only roughly one third are still available today.  The remaining copies are stored mostly at the Gaumont Film Library, the French Film Library, the National Cinematography Film Archives and in several other European film libraries such as the Nederlands Filmmuseum in Amsterdam.

Tarnished Reputations: Tarnished Reputations is a 1920 American silent adventure drama film directed by Herbert Blache, Alice Guy-Blaché, and Léonce Perret and starring Dolores Cassinelli, Alan Roscoe, and Georges Deneubourg.  It is presumed to be a lost film.

Madame Sans-Gêne (1925 film): Madame Sans-Gêne was a 1925 American silent romantic costume comedy-drama film directed by Léonce Perret and starring Gloria Swanson.  Based on the play of the same name by Victorien Sardou and Émile Moreau, the film is now considered lost.

Question: What do Léonce Perret and Larry Cohen have in common in the film industry?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the individuals being compared."
    },
    "shared_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Roles that both individuals have in common in the film industry."
    },
    "industry": {
      "type": "string",
      "description": "The industry in which the commonalities are found."
    }
  },
  "required": [
    "person_names",
    "shared_roles",
    "industry"
  ],
  "additionalProperties": false
}
