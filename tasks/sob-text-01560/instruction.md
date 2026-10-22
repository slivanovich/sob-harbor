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
Kingu (magazine): Kingu (キング , meaning "King" in English) was a Japanese monthly general interest and entertainment magazine published in Tokyo, Japan.  The magazine existed between 1925 and 1957.  It was the first popular best-selling Japanese magazine.  It was also one of two most significant magazines in mid-twentieth century Japan, the other one being "Ie no Hikari".

Kalima (magazine): Kalima (meaning both "Word" and "the act of Speaking" in English) was a French language monthly women's magazine and news magazine published in Morocco between 1986 and 1989.  The magazine was a feminist publication.

Jane (magazine): Jane was an American magazine created to appeal to the women who grew up reading "Sassy Magazine"; Jane Pratt was the founding editor of each.  Its original target audience (pitched to advertisers) was aged 18–34, and was designed to appeal to women who did not like the typical women's magazine format.  Pratt originally intended the magazine to be named "Betty", but she was voted down by everyone else involved in the making of the magazine.

Investir: Investir was a French language monthly business magazine published in Paris, France, between 1974 and 2011.

Mieux Vivre Votre Argent: Mieux Vivre Votre Argent (also known as "MVVA") is a French language monthly business magazine published in Paris, France.

Gael (magazine): Gael is a French language monthly women's and lifestyle magazine published monthly in Mechelen, Belgium.

Pleine Vie: Pleine Vie (meaning "Full Life" in English) is a French language monthly general interest and women's magazine published in Paris, France.

Modes &amp; Travaux: Modes & Travaux is a French language monthly general interest women's magazine based in Paris, France.  Founded in 1919 it is one of the oldest magazines in the country.

Le Monde mensuel: Le Monde mensuel was a French language monthly news magazine published in Paris, France, from 2010 to 2014.  It mostly covered selected articles from "Le Monde" published in the preceding month.

Contenido: Contenido is a Mexican monthly general interest magazine covering articles on the experience of people.  The magazine was founded in 1963.  The headquarters of the magazine, which is published by Editorial Contenido S.A. DE C.V., is in Mexico City.  The magazine is similar to "Reader's Digest".

Question: What is is a French language monthly general interest and women's magazine published in Paris, France, Jane or Pleine Vie?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine."
    },
    "language": {
      "type": "string",
      "description": "The primary language of the magazine."
    },
    "frequency": {
      "type": "string",
      "description": "How often the magazine is published (e.g., monthly, weekly)."
    },
    "categories": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of categories or interests the magazine covers."
    },
    "publication_city": {
      "type": "string",
      "description": "The city where the magazine is published."
    },
    "publication_country": {
      "type": "string",
      "description": "The country where the magazine is published."
    },
    "is_correct_answer": {
      "type": "boolean",
      "description": "True if this magazine is the correct answer to the question, false otherwise."
    }
  },
  "required": [
    "magazine_name",
    "language",
    "frequency",
    "categories",
    "publication_city",
    "publication_country",
    "is_correct_answer"
  ],
  "additionalProperties": false
}
