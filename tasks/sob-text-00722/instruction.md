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
See How They Fall: See How They Fall (French: "Regarde les hommes tomber") is a 1994 film directed by Jacques Audiard.  It stars Jean-Louis Trintignant, Jean Yanne and Matthieu Kassovitz.  It won three César Awards for Best First Work, Best Editing and Most Promising Actor in 1995.

Michel Audiard: Paul Michel Audiard (] ; 15 May 1920 – 27 July 1985) was a French screenwriter and film director.  He was the father of French film director Jacques Audiard.

Lee Grant (New Zealand actress): Leonara Elizabeth Grant {'1': ", '2': ", '3': ", '4': "} (3 August 1931 – 22 July 2016), known professionally as Lee Grant or Miss Lee Grant, was an English-born New Zealand actress and singer.

Lee Grant: Lee Grant (born Lyova Haskell Rosenthal; October 31, during the mid 1920s) is an American actress and film director.

The Sunshine: "The Sunshine" (Tamil title: "சூரியரேகை") is written by writer-actor Shobasakthi (aka Antonythasan Jesuthasan, who acted in Jacques Audiard’s Palm d’ Or winning "Dheepan)" and writer, poet, actor Leena Manimekalai, which is directed by Leena Manimekalai and produced by S.R. Prakashbabu and S.R. Prabhu of Dream Warrior Pictures.

Tahar Rahim: Tahar Rahim (born 4 July 1981) is a French actor of Algerian descent.  He is known for his starring role as Malik El Djebena in the 2009 award-winning French movie "A Prophet" by Jacques Audiard.

Dheepan: Dheepan is a 2015 French crime drama film directed by Jacques Audiard and co-written by Audiard, Thomas Bidegain, and Noé Debré.  The film was partly inspired by Montesquieu's "Persian Letters", as well as the 1971 film "Straw Dogs", with guidance from Antonythasan Jesuthasan, who stars as the title character.

Jacques Audiard: Jacques Audiard (] ; born 30 April 1952) is a French film director and screenwriter.  He is the son of Michel Audiard, also a screenwriter and film director.

A Prophet: A Prophet (French: Un prophète ) is a 2009 French prison drama-crime film directed by Jacques Audiard from a screenplay he co-wrote with Thomas Bidegain, Abdel Raouf Dafri and Nicolas Peufaillit.  The film stars Tahar Rahim in the title role as an imprisoned petty criminal of Algerian origins who rises in the inmate hierarchy, becoming an assassin and drug trafficker as he initiates himself into the Corsican and then Muslim subcultures.

Thomas Bidegain: Thomas Bidegain is a French screenwriter, producer and film director.  He is noted for his collaborations with the director Jacques Audiard.  He received the César Award for Best Original Screenplay in 2010 for "A Prophet" and Best Adaptation in 2013 for "Rust and Bone"; both awards were shared with Audiard.  Bidegain's directorial debut "The Cowboys" premiered in the Directors' Fortnight section at the 2015 Cannes Film Festival.

Question: What do Lee Grant and Jacques Audiard: have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person."
    },
    "person_1_nationality": {
      "type": "string",
      "description": "The nationality of the first person."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person."
    },
    "person_2_nationality": {
      "type": "string",
      "description": "The nationality of the second person who is a film director."
    },
    "common_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions shared by both individuals."
    }
  },
  "required": [
    "person_1_name",
    "person_1_nationality",
    "person_2_name",
    "person_2_nationality",
    "common_professions"
  ],
  "additionalProperties": false
}
