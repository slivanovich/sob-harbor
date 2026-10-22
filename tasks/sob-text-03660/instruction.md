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
Anni (film): Anni is a 1948 Austrian-German romance film directed by Max Neufeld and starring Elfie Mayerhofer, Siegfried Breuer and Josef Meinrad.  It is part of the genre of Vienna films.

Princess (2006 film): Princess is a 2006 adult-themed Danish animated film directed by Anders Morgenthaler and co-written by Morgenthaler and Mette Heeno.  The film tells the harsh story of a 32-year old missionary named August whose sister, a former porn star nicknamed "The Princess," has died of drug abuse and left behind her 5-year old daughter.  August adopts the child and they embark on a violent mission of vengeance to destroy all existing pornographic material featuring Princess.  "Princess", rated for mature audiences, won awards at three European film festivals and was nominated for the 2007 Robert Award for Best Danish Film.

Anders Morgenthaler: Anders Morgenthaler (born 5 December 1972) is a Danish comics artist, children's book author, animator and film director.

Max Neufeld: Max Neufeld (13 February 1887 – 2 December 1967) was an Austrian film director, actor and screenwriter.  He directed 70 films between 1919 and 1957.  He directed the 1934 film "The Song of the Sun", which starred Vittorio De Sica.

A Waltz by Strauss (1925 film): A Waltz by Strauss (German:Ein Walzer von Strauß) is a 1925 Austrian silent film directed by  Max Neufeld and starring  Eugen Neufeld, Tessy Harrison and Svet Petrovich.

The 11th Hour (2014 film): The 11th Hour is a 2014 drama film directed and written by Anders Morgenthaler.  The film stars Kim Basinger and Jordan Prentice.

Mikael Wulff: Mikael Wulff (born 2 September 1972) is a Danish comedian, who appeared in television shows such as Dolph og Wulff, and is co-illustrator of the Wulffmorgenthaler comic strips, which he produces together with Anders Morgenthaler.

The Arsonists of Europe: The Arsonists of Europe (German: Die Brandstifter Europas) is a 1926 Austrian silent drama film directed by Max Neufeld and starring Charlotte Ander, Eugen Neufeld and Robert Valberg.

Wumo: WUMO, formerly Wulffmorgenthaler, is a webcomic and newspaper comic strip created by Danish writer/artist duo Mikael Wulff and Anders Morgenthaler.  The name of the strip was a portmanteau created from the pair's surnames.  The name was also given to a comedy TV series, broadcast on the Danish channel DR2 in 2005.  In June 2012, the strip changed its name to 'WUMO'.

The Song of the Sun: The Song of the Sun (Italian: La canzone del sole ) is a 1933 Italian-German comedy film directed by Max Neufeld and starring Vittorio De Sica.

Question: Anders Morgenthaler and Max Neufeld are both what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the individuals being compared."
    },
    "common_profession": {
      "type": "string",
      "description": "The profession that both individuals share."
    },
    "individuals_professions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of all professions attributed to the individual in the context."
          }
        },
        "required": [
          "name",
          "professions"
        ],
        "additionalProperties": false
      },
      "description": "Details of each individual and their listed professions."
    }
  },
  "required": [
    "person_names",
    "common_profession",
    "individuals_professions"
  ],
  "additionalProperties": false
}
