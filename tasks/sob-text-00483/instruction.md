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
Danny Cannon: John Danny Cannon (born 1968 in Luton, England) is a British film and television writer, director and producer.

Comedians (film): Comedians (Spanish: Cómicos ) is a 1954 Spanish drama film directed by Juan Antonio Bardem.  It was coproduced with Argentina but it is a Spanish film about Spaniards actors on stage.  Bardem confessed to being inspired by "All About Eve".  The film was entered into the 1954 Cannes Film Festival.

The Uninhibited: The Uninhibited (Spanish: Los pianos mecánicos ) is a 1965 Spanish film directed by Juan Antonio Bardem and starring Melina Mercouri, James Mason and Hardy Kruger.  It was entered into the 1965 Cannes Film Festival.

Seven Days in January: Seven Days in January (Spanish: "Siete días de enero" ) is a 1979 Spanish drama film directed by Juan Antonio Bardem about the 1977 Massacre of Atocha.  It was entered into the 11th Moscow International Film Festival where it won the Golden Prize.

La isla misteriosa y el capitán Nemo: L'Ile Mysterieuse / La Isla misteriosa y el capitán Nemo / Die Geheimnisvolle Insel ("The Mysterious Island") is a 1973 European TV miniseries production (300 minutes) adapted from Jules Verne's novel "L'Île mystérieuse".  It was later re-edited into a 96-minute motion picture for theatrical release.  This version was directed by Juan Antonio Bardem and Henri Colpi and featured Omar Sharif as Captain Nemo.

Variety (1971 film): Variety (Spanish:Varietés) is a 1971 Spanish drama film directed by Juan Antonio Bardem and starring Sara Montiel, Vicente Parra and Chris Avram.

Matilde Artero: Matilde Artero is a Spanish actress who appeared in films from 1926 through 1961.  She began her work in silent films, starting with Luis R. Alonso's "La loca de la casa" for Producciones Hornemann.  Her first talkie was as 'Pepita' with Carlos Gardel in the 1933 French-made Les Studios Paramount Spanish musical romance "Espérame", directed by Louis J. Gasnier.  Her final screen appearance was in the production "At Five O'Clock in the Afternoon", a Spanish drama film directed in 1961 by Juan Antonio Bardem.

At Five O'Clock in the Afternoon: At Five O'Clock in the Afternoon (Spanish: A las cinco de la tarde , also released as At Five in the Afternoon) is a 1961 Spanish drama film directed by Juan Antonio Bardem.  The film was selected as the Spanish entry for the Best Foreign Language Film at the 33rd Academy Awards, but was not accepted as a nominee.

Juan Antonio Bardem: Juan Antonio Bardem (] ; 2 June 1922 – 30 October 2002) was a Spanish film director and screen writer.  He was a member of the Communist Party.  Bardem was best known for "Muerte de un ciclista" (1955) which won the FIPRESCI Prize at the 1955 Cannes Film Festival, and "El puente" (1977) which won the Golden Prize at the 10th Moscow International Film Festival.  His 1979 film "Seven Days in January" won the Golden Prize at the 11th Moscow International Film Festival.  In 1981 he was a member of the jury at the 12th Moscow International Film Festival.  In 1993 he was a member of the jury at the 43rd Berlin International Film Festival.  In 1953 he and Luis García Berlanga founded a film magazine, "Objetivo", which existed until 1956.  Bardem is the uncle of actor Javier Bardem.

Vengeance (1958 film): Vengeance (Spanish: La venganza ) is a 1958 Spanish drama film directed by Juan Antonio Bardem.  It was co-produced with Italy, starring Italian Raf Vallone.  Francisco Rabal narrates the film.  It was shown at the 1958 Cannes Film Festival but not released in Spain until the following year.  The film had serious troubles with Spanish censorship.  Bardem even went to prison and it was an international scandal.  It was nominated for the Academy Award for Best Foreign Language Film.

Question: Danny Cannon and Juan Antonio Bardem are both what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_1_name": {
      "type": "string",
      "description": "The name of the first entity."
    },
    "entity_2_name": {
      "type": "string",
      "description": "The name of the second entity."
    },
    "shared_profession": {
      "type": "string",
      "description": "The common profession shared by both entities."
    },
    "entity_1_nationality": {
      "type": "string",
      "description": "The nationality of the first entity."
    },
    "entity_2_nationality": {
      "type": "string",
      "description": "The nationality of the second entity."
    }
  },
  "required": [
    "entity_1_name",
    "entity_2_name",
    "shared_profession",
    "entity_1_nationality",
    "entity_2_nationality"
  ],
  "additionalProperties": false
}
