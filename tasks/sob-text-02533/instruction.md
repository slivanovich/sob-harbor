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
Zak Ové: Zak Ové (born 1966) is a British visual artist who works between sculpture, film and photography, living in London, UK, and Trinidad.  His themes reflect "his documentation of and anthropological interest in diasporic and African history, specifically that which is explored through Trinidadian carnival."  In work that is "filtered through his own personal and cultural upbringing, with a black Trinidadian father and white Irish mother", he has exhibited widely in Europe, the United States and Africa, participating in international museum shows in London, Dakar, Paris, Dubai, Prague, Berlin, Johannesburg, Bamako and New York City.  His father is the filmmaker Horace Ové and his sister is the actress Indra Ové.

Pressure (film): Pressure is a 1976 British drama film and the first feature-length fiction film directed by a Black film-maker in Britain.  Directed by Horace Ové, and co-written by him with Samuel Selvon, "Pressure" is a powerful portrait of inter-generational tensions between first- and second-generation West Indian migrants in London's Notting Hill area.  According to Julia Toppin,

Thrill of a Romance: Thrill of a Romance (also known as "Thrill of a New Romance") was an American romance film released by Metro-Goldwyn-Mayer in 1945, starring Van Johnson, Esther Williams and Carleton G. Young, with musical performances by opera singer Lauritz Melchior.  The film was directed by Richard Thorpe and written by Richard Connell and Gladys Lehman.

Jerry Thorpe: Richard Jerome "Jerry" Thorpe (born 1926) is an American TV and film director and producer.  He is the son of actor Richard Thorpe.

Playing Away: Playing Away is a 1987 TV comedy film directed by Horace Ové, from a screenplay by Caryl Phillips.  In the story, an English cricket team, fictitiously named "Sneddington" (based in Lavenham, Suffolk), invites a team of West Indian heritage based in Brixton (South London) to play a charity game in support of their "Third World Week."  According to Screenonline, "The gentle comedy of manners and unexpected reversal of white and black stereotypes in "Playing Away" contrasts sharply with the stylistic experimentation and the militant denunciations of racial prejudice in director Horace Ové's earlier feature, "Pressure" (1975)." " New York Times" reviewer Vincent Canby called it "witty and wise without being seriously disturbing for a minute".

Richard Thorpe: Richard Thorpe (February 24, 1896 – May 1, 1991) was an American film director best known for his long career at Metro-Goldwyn-Mayer.

Horace Ové: Horace Ové, CBE (born 1939), is a British filmmaker, photographer, painter and writer, one of the leading black independent film-makers to emerge in Britain since the post-war period.  Ové holds the "Guinness World Record" for being the first black British film-maker to direct a feature-length film, "Pressure" (1975).  In its retrospective history, "100 Years of Cinema", the British Film Institute (BFI) declared: "Horace Ové is undoubtedly a pioneer in Black British history and his work provides a perspective on the Black experience in Britain."

Black Hand (1950 film): Black Hand is a 1950 American film noir directed by Richard Thorpe and starring Gene Kelly as an Italian immigrant fighting against the Black Hand extortion racket in New York City in the first decade of the 20th century.

It's a Big Country: It's a Big Country: An American Anthology is a 1951 anthology film consisting of eight segments directed by seven directors: Clarence Brown, Don Hartman, John Sturges, Richard Thorpe, Charles Vidor, Don Weis, and William A. Wellman.

Burning an Illusion: Burning an Illusion is a 1981 British film written and directed by Menelik Shabazz, about a young British-born black woman's love life, mostly shot in London's Notting Hill and Ladbroke Grove communities.  It was only the second British feature to have been made by a black director, following Horace Ové’s 1975 "Pressure", and is described by Stephen Bourne as "the first British film to give a black woman a voice of any kind."  Imruh Bakari worked with Shabazz and co-founded Kumba productions with him.

Question: Are both Horace Ové and Richard Thorpe American film directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "directors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          },
          "is_american": {
            "type": "boolean"
          }
        },
        "required": [
          "name",
          "nationality",
          "is_american"
        ],
        "additionalProperties": false
      }
    },
    "all_directors_are_american": {
      "type": "boolean",
      "description": "Indicates if all listed directors are American."
    },
    "final_answer": {
      "type": "boolean",
      "description": "The final answer to the question: Are both Horace Ov\u00e9 and Richard Thorpe American film directors?"
    }
  },
  "required": [
    "directors",
    "all_directors_are_american",
    "final_answer"
  ],
  "additionalProperties": false
}
