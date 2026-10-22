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
The Great Love (1918 film): The Great Love is a 1918 American silent war drama film directed and written by D. W. Griffith who, along with scenario writer Stanner E.V. Taylor, is credited as "Captain Victor Marier".  The film stars George Fawcett and Lillian Gish.  Set during World War I, exterior scenes were shot on location in England.  "The Great Love" is now considered to be a lost film.

Water for Canitoga: Water for Canitoga (German: Wasser für Canitoga) is a 1939 German western film directed by Herbert Selpin and starring Hans Albers, Charlotte Susa and Josef Sieber.  The film is a "Northern", set in Canada in 1905 where an engineer is working to construct a new water supply system despite repeated attempts at sabotage.  It is based on a play by Hans Rehfisch, Otto Eis and Egon Eis.

An Ideal Husband (1935 film): An Ideal Husband (German:Ein idealer Gatte) is a 1935 German comedy film directed by Herbert Selpin and starring Brigitte Helm, Sybille Schmitz and Karl Ludwig Diehl.  It is based on the 1895 play "An Ideal Husband" by Oscar Wilde a sensitive and romantic comedy representing the 19th century.  The adaptation is very faithful to the original work.

The Marriage Swindler: The Marriage Swindler (German:Heiratsschwindler) is a 1938 German drama film directed by Herbert Selpin and starring Eduard von Winterstein, Viktoria von Ballasko and Kurt Waitzmann.  It is sometimes known by the alternative title Die rote Mütze (The Red Cap).  A confidence trickster is released from prison and travels to a village where he blackmails and tricks women out of their savings, before eventually being caught.

Herbert Selpin: Herbert Selpin (29 May 1904 – 1 August 1942) was a German film director and screenwriter of light entertainment during the 1930s and 1940s.  He is best known for his final film, the partly suppressed "Titanic", during the production of which he was arrested by Propaganda Minister Joseph Goebbels.  He was later found dead in his prison cell.

The Green Domino: The Green Domino (French: "Le Domino vert" ) is a 1935 French/German drama film directed by Henri Decoin and Herbert Selpin, based on play by Erich Ebermayer.  It tells the story of a rich heiress who falls in love with an art critic after his wife has been murdered.  It was released on DVD in France on 5 April 2007.

Stanner E.V. Taylor: Stanner E.V. Taylor (28 September 1877 – 23 November 1948) was an American screenwriter and director of the silent era.  He wrote for 108 films between 1908 and 1929.  He was born in St. Louis, Missouri and died in Los Angeles, California.  He was married to Biograph Company actress Marion Leonard.

Scandal at the Fledermaus: Scandal at the Fledermaus (German:Skandal um die Fledermaus) is a 1936 German comedy film directed by Herbert Selpin and starring Viktor de Kowa, Maria Andergast and Adele Sandrock.

Sergeant Berry: Sergeant Berry is a 1938 German comedy western film directed by Herbert Selpin and starring Hans Albers, Toni von Bukovics and Peter Voß.  A tough Chicago policeman is sent to the Mexican–American border on a dangerous mission.  It was based on a novel by Robert Arden.

Gem Motion Picture Company: The Gem Motion Picture Company was an American silent-era film studio.  It was co-founded by filmmaker Stanner E.V. Taylor and his wife, actress Marion Leonard in 1911.  After management issues, the company evolved to primarily act as a producer of short comedies starring Billy Quirk.

Question: Who is a screenwriter from Germany, Stanner E.V. Taylor or Herbert Selpin?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "screenwriter_name": {
      "type": "string",
      "description": "The name of the screenwriter identified."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the identified screenwriter."
    },
    "is_german_screenwriter": {
      "type": "boolean",
      "description": "True if the identified person is a German screenwriter, false otherwise."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why this person was chosen based on the context."
    }
  },
  "required": [
    "screenwriter_name",
    "nationality",
    "is_german_screenwriter",
    "reasoning"
  ],
  "additionalProperties": false
}
