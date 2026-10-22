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
Marguerite Yourcenar: Marguerite Yourcenar (] ; 8 June 1903 – 17 December 1987) was a French novelist and essayist born in Brussels, Belgium, who became a US citizen in 1947.  Winner of the "Prix Femina" and the Erasmus Prize, she was the first woman elected to the Académie française, in 1980, and the seventeenth person to occupy seat 3.

The Abyss (Yourcenar novel): The Abyss (French: L'Œuvre au noir ) is a 1968 novel by the Belgian-French writer Marguerite Yourcenar.  Its narrative centers on the life and death of Zeno, a physician, philosopher, scientist and alchemist born in Bruges during the Renaissance era.  The book was published in France in 1968 and was met with immediate popular interest as well as critical acclaim, obtaining the Prix Femina with unanimous votes the year of its publication.  The English translation by Grace Frick has been published under the title "The Abyss" or alternatively Zeno of Bruges.  Belgian filmmaker André Delvaux adapted it into a film in 1988.

Fernande de Cartier de Marchienne: Ferdinande Louise Marie Ghislaine (Fernande) de Cartier de Marchienne (Suarlée, 23 February 1872-Bruxelles 19 June 1903) was the Belgian mother of Marguerite Yourcenar.  She was a daughter of Arthur de Cartier de Marchienne

Grace Frick: Grace Marion Frick (January 12, 1903 – November 18, 1979) was a translator and researcher for her lifelong partner French author Marguerite Yourcenar.  Grace Frick taught languages at US colleges and was the second academic dean to be appointed to Hartford Junior College.

A Coin in Nine Hands: A Coin in Nine Hands (French: Denier du rêve ) is a 1934 novel by the French writer Marguerite Yourcenar.  A reworked edition was published in 1959.

Memoirs of Hadrian: Memoirs of Hadrian (French: Mémoires d'Hadrien ) is a novel by the Belgian-born French writer Marguerite Yourcenar about the life and death of Roman Emperor Hadrian.  First published in France in French in 1951 as "Mémoires d'Hadrien", the book was an immediate success, meeting with enormous critical acclaim.  Although the historical Hadrian wrote an autobiography, it has been lost.

Oriental Tales: Oriental Tales (French: Nouvelles orientales ) is a 1938 short story collection by the French writer Marguerite Yourcenar.  The stories share a self-consciously mythological form; some are based on pre-existing myths and legends, while some are new.  The story "How Wang-Fo Was Saved" was adapted into an animated short film by René Laloux in the 1980s.

Wyndham Lewis: Percy Wyndham Lewis (18 November 1882 – 7 March 1957) was an English writer, painter and critic (he dropped the name 'Percy', which he disliked).  He was a co-founder of the Vorticist movement in art, and edited the literary magazine of the Vorticists, "BLAST".  His novels include his pre-World War I-era novel "Tarr" (set in Paris), and "The Human Age", a trilogy comprising "The Childermass" (1928), "Monstre Gai" and "Malign Fiesta" (both 1955), set in the afterworld.  A fourth volume of "The Human Age", "The Trial of Man," was begun by Lewis but left in a fragmentary state at the time of his death.  He also wrote two autobiographical volumes, "Blasting and Bombardiering" (1937) and "Rude Assignment: A Narrative of my Career Up-to-Date" (1950).

Fires (book): Fires (French: Feux ) is a 1936 prose book by the French writer Marguerite Yourcenar.  It consists of aphorisms, prose poetry and fragmentary diary entries alluding to a love story.

Coup de Grâce (novel): Coup de Grâce (French: Le Coup de grâce ) is a 1939 novel in French by Marguerite Yourcenar.  The narrative is a triangle drama set in the Baltics during the Russian Civil War (1917-1922).

Question: Were Marguerite Yourcenar and Wyndham Lewis from the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_answer": {
      "type": "boolean",
      "description": "True if Marguerite Yourcenar and Wyndham Lewis are from the same country, false otherwise."
    },
    "person_one_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person."
        },
        "nationalities_mentioned": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of nationalities or citizenships mentioned for the first person."
        },
        "birth_country": {
          "type": "string",
          "description": "The country where the first person was born."
        }
      },
      "required": [
        "name",
        "nationalities_mentioned",
        "birth_country"
      ],
      "additionalProperties": false
    },
    "person_two_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the second person."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the answer based on the nationalities found in the text."
    }
  },
  "required": [
    "question_answer",
    "person_one_details",
    "person_two_details",
    "reasoning"
  ],
  "additionalProperties": false
}
