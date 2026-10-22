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
L'Olimpiade (Pergolesi): L'Olimpiade is an opera in the form of a dramma per musica in three acts by the Italian composer Giovanni Battista Pergolesi.  Pergolesi took the text, with a few modifications, from the libretto of the same name by Pietro Metastasio.  The opera first appeared during the Carnival season of 1735 at the in Rome and "came to be probably the most admired" of the more than 50 musical settings of Metastasio’s drama.

Il Flaminio: Il Flaminio is a 1735 opera buffa by Giovanni Battista Pergolesi to a libretto by Gennaro Antonio Federico, first performed at the Teatro Nuovo, Naples.  Untypically in Pergolesi's difficult and short career the opera was an immediate success and continued to be staged up to 1750.

Adriano in Siria (Pergolesi): Adriano in Siria is an opera by Giovanni Battista Pergolesi setting Metastasio's libretto of the same name.  It was the third of his four opere serie, premiered at Teatro San Bartolomeo in Naples on 25 October 1734.  Pergolesi also provided a comic intermezzo "La contadina astuta", later better known as "Livietta e Tracollo", to a libretto by Tomasso Mariani.

Giovanni Battista Pergolesi: Giovanni Battista Draghi (] ; 4 January 1710 – 16 March 1736), best known as Pergolesi (] ) or Giovanni Battista Pergolesi, was an Italian composer, violinist and organist.

Pergolesi (film): Pergolesi is a 1932 Italian historical musical film directed by Guido Brignone and starring Elio Steiner, Dria Paola and Tina Lattanzi.  It portrays the brief life of the eighteenth century Italian composer Giovanni Battista Pergolesi.

La Salustia: La Salustia is a 1732 opera in three acts by Giovanni Battista Pergolesi to a revised text, possibly by Sebastiano Morelli, after Apostolo Zeno's famous 1716 libretto "Alessandro Severo", which was also later adapted by Handel.  The production was marred when the leading man Nicolo Grimaldi "Nicolini" fell fatally ill before the performance and an inexperienced substitute Gioacchino Conti "Gizziello" had to be called in at the last minute.  "La Salustia" was Pergolesi's first opera seria.  The story is based on the life of the Roman emperor Alexander Severus and his wife Sallustia Orbiana.

Pietro Mascagni: Pietro Antonio Stefano Mascagni (] ; 7 December 1863 – 2 August 1945) was an Italian composer most noted for his operas. His 1890 masterpiece "Cavalleria Rusticana" caused one of the greatest sensations in opera history and single-handedly ushered in the "Verismo" movement in Italian dramatic music.  While it was often held that Mascagni, like Leoncavallo, was a "one-opera man" who could never repeat his first success, "L'amico Fritz" and "Iris" have remained in the repertoire in Europe (especially Italy) since their premieres.  Mascagni said that at one point, "Iris" was performed in Italy more often than "Cavalleria" (cf. Stivender).

Stabat Mater (Pergolesi): Stabat Mater is a musical setting of the "Stabat Mater " sequence, composed by Giovanni Battista Pergolesi in 1736.  Composed in the final weeks of Pergolesi's life, it is scored for soprano and alto soloists, violin I and II, viola and basso continuo (cello and organ).

Il prigionier superbo: Il prigionier superbo ("The Proud Prisoner") is an "opera seria" in three acts composed by Giovanni Battista Pergolesi to a libretto attributed to Gennaro Antonio Federico and based on an earlier libretto by Francesco Silvani for Gasparini's opera, "La fede tradita e vendicata".  It was premiered at the Teatro San Bartolomeo in Naples on 5 September 1733 and received further performances in October.  The opera, with its labyrinthine plot involving the rivalry of Metalce (King of the Goths) and Viridate (Prince of Denmark) for the hand of Rosmene (a Norwegian princess whose father is Metalce's prisoner), soon sank into oblivion, but its comic intermezzo, "La serva padrona" (also by Pergolesi) was to achieve considerable success when performed on its own.

La conversione e morte di San Guglielmo: La conversione e morte di San Guglielmo ("The Conversion and Death of Saint William") is a sacred musical drama ("dramma sacro") in three parts by the Italian composer Giovanni Battista Pergolesi.  The libretto, by Ignazio Mancini, is based on the life of Saint William of Aquitaine as recounted by Laurentius Surius.  It was Pergolesi's first operatic work, possibly written as a study exercise for his conservatory.  The work was premiered at the Monastery of Sant'Agnello Maggiore, Naples in the summer of 1731.

Question: Who was born first, Pietro Mascagni or Giovanni Battista Pergolesi?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first composer."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the first composer in YYYY-MM-DD format."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "composer_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second composer."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the second composer in YYYY-MM-DD format."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "first_born_composer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the composer who was born first."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the composer who was born first."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "composer_1",
    "composer_2",
    "first_born_composer"
  ],
  "additionalProperties": false
}
