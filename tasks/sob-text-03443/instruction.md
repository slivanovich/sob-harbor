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
Bahia de Todos-os-santos (book): Bahia de Todos-os-santos: guia de ruas e mistérios de Salvador (Bahia of all-saints: a guide to the streets and mysteries of Salvador) is a book by the Brazilian writer, Jorge Amado, first published in Portuguese in 1945.  It has not yet been published in English.

Jorge Amado: Jorge Leal Amado de Faria (] , 10 August 1912 – 6 August 2001) was a Brazilian writer of the modernist school.  He remains the best known of modern Brazilian writers, with his work having been translated into some 49 languages and popularized in film, notably "Dona Flor and Her Two Husbands" in 1978.  His work reflects the image of a Mestiço Brazil and is marked by religious syncretism.  He depicted a cheerful and optimistic country that was beset, at the same time, with deep social and economic differences.

Coasting (memoir): Coasting, subtitled Notes for a Memoir that I will never write, (Portuguese: Navegação de cabotagem: Apontamentos para um livro de memórias que jamais escreverei) is a memoir by the Brazilian writer Jorge Amado.

Zélia Gattai: Zélia Gattai Amado de Faria (July 2, 1916 – May 17, 2008) was a Brazilian photographer, memoirist, novelist and author of children's literature, as well as a member of the Brazilian Academy of Letters.  She was married to internationally famous writer Jorge Amado from 1945 until his death in 2001.

Mangue Seco: Mangue Seco is a beach village in Jandaíra, Bahia, Brazil.  It is very famous in Brazil because of a soap-opera (telenovela) adaptation of the novel "Tieta do Agreste", by the Brazilian writer Jorge Amado, which was shot on its white beaches in 1996.

Luís Fernando Veríssimo: Luís Fernando Veríssimo (born September 26, 1936 in Porto Alegre, Rio Grande do Sul, Brazil) is a Brazilian writer.  Verissimo is the son of Brazilian writer Erico Verissimo and lived with his father in the United States during his childhood.  Best known for his "crônicas" and texts of humor, more precisely satire of manners, published daily in several Brazilian newspapers, Verissimo is also a cartoonist, translator, and television writer, playwright and novelist.  He has also been advertising and newspaper copy desk.  He is also a musician, having played saxophone in a few sets.  With over 60 published titles, is one of the most popular contemporary Brazilian writers.

Tent of Miracles (novel): Tent of Miracles (Portuguese: "Tenda dos Milagres" ) is a Brazilian Modernist novel.  It was written by Jorge Amado in 1967 and published the following year.  It was later adapted to a 1977 Cinema Novo (Nouvelle Vague) film by director/screenplay writer Nelson Pereira dos Santos.

Leopoldo Serran: Leopoldo Augusto Bhering Serran (May 6, 1942 – 20 August 2008) was a Brazilian screenwriter best known for the 1976 film "Dona Flor and Her Two Husbands", based on the novel by Jorge Amado.

Sarah Caudwell: Sarah Caudwell was the pseudonym of Sarah Cockburn (27 May 1939 – 28 January 2000), a British barrister and writer of detective stories.

José Lins do Rego: José Lins do Rego Cavalcanti (July 3, 1901 in Pilar Paraíba – September 12, 1957 in Rio de Janeiro) was a Brazilian novelist most known for his semi-autobiographical "sugarcane cycle."  These novels were the basis of films that had distribution in the English speaking world.  Along with Graciliano Ramos and Jorge Amado he stands as one of the greatest regionalist writers of Brazil According to Otto Maria Carpeaux, José Lins was "the last of the story tellers".  His first novel, Menino de Engenho ("Boy from the plantation"), was published with difficulty, but soon it got praised by the critics.

Question: Which writer, Jorge Amado or Sarah Caudwell, remains the best known of modern Brazilian writers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "best_known_writer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the writer identified as the best known."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the best known writer."
        },
        "is_modern_brazilian": {
          "type": "boolean",
          "description": "True if the writer is a modern Brazilian writer."
        },
        "reason_for_fame": {
          "type": "string",
          "description": "The reason provided in the context for the writer's fame."
        }
      },
      "required": [
        "name",
        "nationality",
        "is_modern_brazilian",
        "reason_for_fame"
      ],
      "additionalProperties": false
    },
    "candidate_writers_evaluated": {
      "type": "array",
      "description": "A list of writers considered in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the candidate writer."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the candidate writer."
          },
          "is_modern_brazilian": {
            "type": "boolean",
            "description": "True if the candidate writer is a modern Brazilian writer."
          }
        },
        "required": [
          "name",
          "nationality",
          "is_modern_brazilian"
        ],
        "additionalProperties": false
      }
    },
    "comparison_result_accurate": {
      "type": "boolean",
      "description": "Indicates if the comparison was successfully made based on the context."
    }
  },
  "required": [
    "best_known_writer",
    "candidate_writers_evaluated",
    "comparison_result_accurate"
  ],
  "additionalProperties": false
}
