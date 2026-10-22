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
Pierre Savorgnan de Brazza: Pietro Paolo Savorgnan di Brazzà, then known as Pierre Paul François Camille Savorgnan de Brazza (26 January 1852 – 14 September 1905), was an Italian-born French explorer.  With the backing of the Société de Géographie de Paris, he opened up for France entry along the right bank of the Congo that eventually led to French colonies in Central Africa.  His easy manner and great physical charm, as well as his pacific approach among Africans, were his trademarks.  Under French colonial rule, the capital of the Republic of the Congo was named Brazzaville after him and the name was retained by the post-colonial rulers.

Jean-Baptiste Lully: Jean-Baptiste Lully (] ; born Giovanni Battista Lulli ] ; 28 November 1632 – 22 March 1687) was an Italian-born French composer, instrumentalist, and dancer who spent most of his life working in the court of Louis XIV of France.  He is considered a master of the French baroque style.  Lully disavowed any Italian influence in French music of the period.  He became a French subject in 1661.

Gaspard de la Nuit (poetry collection): Gaspard de la Nuit — Fantaisies à la manière de Rembrandt et de Callot (English: Gaspard of the Night — Fantasies in the Manner of Rembrandt and Callot ) is a compilation of prose poems by Italian-born French poet Aloysius Bertrand.  Considered one of the first examples of modern prose poetry, it was published in 1842, one year after Bertrand's death from tuberculosis, from a manuscript dated 1836, by his friend David d'Angers.  The text includes a short address to Victor Hugo and another to Charles Nodier, and a Memoir of Bertrand written by Sainte-Beuve was included in the original 1842 edition.

Acis et Galatée: Acis et Galatée ("Acis and Galatea") is an opera by Jean-Baptiste Lully.  Unlike most of his operas, which are designated "tragédies en musique", Lully called this work a "pastorale-héroïque", because it was on a pastoral theme and had only three acts (plus a prologue) compared to the usual five.  Otherwise, there is little musically or dramatically to distinguish it from Lully's "tragédies".

Pastorale héroïque: Pastorale héroïque was a type of ballet héroïque, a form of the opéra-ballet genre of French Baroque opera.  The first work to bear the name was Jean-Baptiste Lully's final completed opera "Acis et Galatée" (1686), although musical works on pastoral themes had already appeared on the French stage.  The pastorale héroique usually drew on Classical subject matter associated with pastoral poetry.  Like the tragédie en musique, it had an allegorical prologue; however, its structure consisted of three acts, rather than the five of the tragédie en musique.  Later examples were written by Jean-Philippe Rameau; these include "Zaïs" (1748) and "Naïs" (1749), and "Acante et Céphise" (1751).

Pygmalion and Galatea (Gérôme painting): Pygmalion and Galatea (French: Pygmalion et Galatée ) is an 1890 painting by the French artist Jean-Léon Gérôme.  The motif is taken from Ovid's "Metamorphoses", and depicts how the sculptor Pygmalion kisses his ivory statue Galatea, after the goddess Venus has brought her to life.

Alfred Rode: Alfred Rode (4 June 1905 – 22 July 1979) was an Italian-born French composer, musician, actor and film director.  He was born in Torre del Greco as Alfred Spedaliere.  In 1936 Rode appeared in the British film "Gypsy Melody" alongside Lupe Velez, which was a remake of his own 1935 film "Juanita".  Rode was married to the French actress Claudine Dupuis from 1951.

Nino Frank: Nino Frank (born 27 June 1904 in Barletta, Italy − Paris, 17 August 1988) was an Italian-born French film critic and writer who was most active in the 1930s and 1940s.  Frank is best known for being the first film critic to use the term "film noir" to refer to 1940s US crime drama films such as "The Maltese Falcon," although research indicates that the term was used in French film reviews and newspaper articles in 1938 and 1939.

Jules Danilo: Jules Danilo (born 18 May 1995 in Milan, Italy) is an Italian-born French Grand Prix motorcycle racer.  He has also previously competed in the French 125cc/Moto3 championship – twice finishing as runner-up in the series – and the CEV Moto3 series.

Urbain Caffi: Urbain Caffi (10 January 1917 – 16 March 1991) was an Italian-born French racing cyclist.  He won the French national road race title in 1944.  He also rode in the 1947 and 1948 Tour de France.

Question: Acis et Galatée is an operat by which Italian-born French composer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "opera_title": {
      "type": "string",
      "description": "The title of the opera."
    },
    "composer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the composer."
        },
        "nationality_origin": {
          "type": "string",
          "description": "The country where the composer was born."
        },
        "nationality_adopted": {
          "type": "string",
          "description": "The country where the composer spent most of their life or became a subject."
        }
      },
      "required": [
        "name",
        "nationality_origin",
        "nationality_adopted"
      ],
      "additionalProperties": false
    },
    "opera_type": {
      "type": "string",
      "description": "The specific designation or type of the opera."
    },
    "number_of_acts": {
      "type": "integer",
      "description": "The number of acts in the opera, excluding the prologue."
    }
  },
  "required": [
    "opera_title",
    "composer",
    "opera_type",
    "number_of_acts"
  ],
  "additionalProperties": false
}
