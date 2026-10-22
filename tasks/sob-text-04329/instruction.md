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
Silk (novel): Silk (Italian: Seta ) is a 1996 novel by the Italian writer Alessandro Baricco.  It was translated into English in 1997 by Guido Waldman.  A new English translation by Ann Goldstein was published in 2006.

Patrick White: Patrick Victor Martindale White (28 May 191230 September 1990) was an Australian writer who is widely regarded as one of the most important English-language novelists of the 20th century.  From 1935 to 1987, he published twelve novels, three short-story collections and eight plays.

Patrick White Award: The Patrick White Award is an annual literary prize established by Patrick White.  White used his 1973 Nobel Prize in Literature award to establish a trust for this prize.

La Conquista (opera): La Conquista (also known as Montezuma) is an opera in two acts by Lorenzo Ferrero set to a trilingual libretto by the composer and Frances Karttunen, based on a concept by Alessandro Baricco.  It depicts the major episodes of the Spanish conquest of the Aztec Empire in 1521 and the subsequent destruction of the Aztec civilization.  The libretto (English-Spanish-Nahuatl) is a blend of historical and literary sources drawn from transcriptions of indigenous and European literature, both kept, with some exceptions, in their original languages.  The texts are taken from "The Truthful History of the Conquest of New Spain" by Bernal Díaz del Castillo, the Book XII of the "Florentine Codex", the works of Juan Boscán Almogáver, Bernardino de Sahagún, Lope de Vega, Heinrich Heine, and from Aztec prayers, songs and poems as collected in "Cantares Mexicanos" and "Romances de los señores de Nueva España".

The Legend of 1900: The Legend of 1900 (Italian: La leggenda del pianista sull'oceano , The Legend of the Pianist on the Ocean) is a 1998 Italian drama film directed by Giuseppe Tornatore and starring Tim Roth, Pruitt Taylor Vince and Mélanie Thierry.  It was Tornatore's first English-language film.  The film is inspired by "Novecento", a monologue by Alessandro Baricco.  The film was nominated for a variety of awards worldwide, winning several for its soundtrack.

Ocean Sea (novel): Ocean Sea (Italian: Oceano mare ) is a 1993 novel by the Italian writer Alessandro Baricco.  Its narrative revolves around the lives of a group of people gathered at a remote seaside hotel.  The novel won the Viareggio Prize.

Patrick White Playwrights' Award: The Patrick White Playwrights' Award is an annual Australian literary award established jointly by the Sydney Theatre Company and "The Sydney Morning Herald" in honour of Patrick White's contribution to Australian theatre.  The award was launched in 2000 and in 2011, was amended to include the Patrick White Fellowship.

City Reading (Tre Storie Western): City Reading (Tre Storie Western) is a 2003 album by the French duo Air in collaboration with the Italian writer Alessandro Baricco.  In this album, Baricco narrates some passages from his novel "City" with Air's music in the background.  The impetus for the album was in 2001, when Air performed background music to a live theater reading of "City" at the request of Baricco.  The following month, they recorded three excerpts from his book: Bird (track 1), La Puttana Di Closingtown (tracks 2–10) and Caccia All'Uomo (tracks 11–19).  The album was mixed by Radiohead producer Nigel Godrich.

Silk (2007 film): Silk is a film adaptation of Italian author Alessandro Baricco's novel of the same name.  It was released in September 2007 through New Line Cinema and directed by "The Red Violin" director, François Girard.

Alessandro Baricco: Alessandro Baricco (] ; born January 25, 1958 in Turin, Piedmont) is a popular Italian writer, director and performer.  His novels have been translated into a wide number of languages.  He currently lives in Rome with his wife and two sons.

Question: Which writer is older, Alessandro Baricco or Patrick White?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "older_writer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "younger_writer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "age_difference_years": {
      "type": "integer",
      "description": "The difference in birth years between the two writers."
    },
    "question_answer": {
      "type": "string",
      "description": "The name of the writer who is older."
    }
  },
  "required": [
    "older_writer",
    "younger_writer",
    "age_difference_years",
    "question_answer"
  ],
  "additionalProperties": false
}
