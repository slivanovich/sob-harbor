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
Abigail Child: Abigail Child is a filmmaker, poet, and writer who has been active in experimental writing and media since the 1970s.  She has completed more than thirty film and video works and installations, and six books.  An acknowledged pioneer in montage, Child’s early film work addressed the interplay between sound and image through reshaping narrative tropes, prefiguring many concerns of contemporary film and media.

Nabil Ayouch: Nabil Ayouch (born 1 April 1969) is a French-Moroccan television and film director, producer and writer of Moroccan origin.

Much Loved: Much Loved (also known as Zin Li Fik) is a 2015 French-Moroccan drama film directed by Nabil Ayouch about the prostitution scene in Marrakesh.  It was screened in the Directors' Fortnight section at the 2015 Cannes Film Festival.  The film has been banned in Morocco for its "contempt for moral values and the Moroccan woman".  It was screened in the Contemporary World Cinema section of the 2015 Toronto International Film Festival.

Horses of God: Horses of God (French: Les chevaux de Dieu , Arabic: يا خيل الله‎ ‎ , translit.   Ya khayl Allah) is 2012 Moroccan drama film about the 2003 Casablanca bombings.  It was directed by Nabil Ayouch, and based on the novel "The Stars of Sidi Moumen" by Moroccan writer Mahi Binebine.  The film won several awards, and was Morocco's submission for the 85th Academy Awards (held in February 2013).

Nabil Kassel: Nabil Kassel (born March 10, 1984) is an Algerian boxer best known to win the middleweight gold at the 2007 All-Africa Games.  The family name is Kassel, Algerians generally write this first (Kassel Nabil).

Whatever Lola Wants (film): Whatever Lola Wants is a 2007 French-Canadian romantic drama film directed by Nabil Ayouch.  The film had its world premiere on December 11, 2007 at the Dubai International Film Festival and stars Laura Ramsey as an American postal worker who travels to Egypt to seek out a legendary belly dancer.

Ana María Simo: Ana Maria Simo is a New York playwright, essayist and novelist.  Born in Cuba, educated in France, and writing in English, she has collaborated with such experimental artists as composer Zeena Parkins, choreographer Stephanie Skura and filmmakers Ela Troyano and Abigail Child.

Mektoub: Mektoub is a 1997 French-Moroccan drama film directed by Nabil Ayouch.  The film was selected as the Moroccan entry for the Best Foreign Language Film at the 71st Academy Awards, but was not accepted as a nominee.

Razzia (2017 film): Razzia is a 2017 Moroccan drama film directed by Nabil Ayouch.  It was selected as the Moroccan entry for the Best Foreign Language Film at the 90th Academy Awards.  "Razzia" is mostly set in Casablanca and characters frequently discuss the 1942 film "Casablanca".

Assaad Bouab: Assaad Bouab (born 1980, Aurillac, France) is a French-Moroccan actor whose first co-starring role is "Whatever Lola Wants", directed by Nabil Ayouch and co-starring Laura Ramsey as Lola.  The film premiered 11 December 2007 at the Dubai International Film Festival.  Bouab attended Cours Florent from 1999 to 2002, and graduated from CNSAD in Paris in 2006.

Question: Do Abigail Child and Nabil Ayouch both write media?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "answer": {
      "type": "boolean",
      "description": "True if both individuals write media, false otherwise."
    },
    "individuals": {
      "type": "array",
      "description": "Details about each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_writer": {
            "type": "boolean",
            "description": "Indicates if the individual is identified as a writer in the context."
          },
          "writing_context": {
            "type": "string",
            "description": "The specific phrase from the context confirming their writing activity."
          }
        },
        "required": [
          "name",
          "is_writer",
          "writing_context"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_asked",
    "answer",
    "individuals"
  ],
  "additionalProperties": false
}
