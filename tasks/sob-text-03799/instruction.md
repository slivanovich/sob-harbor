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
Lytton Strachey: A Critical Biography: Lytton Strachey: A Critical Biography is a book-length biography of Lytton Strachey by Michael Holroyd, the author's magnum opus.  He published a revised version in 1994 under the revised subtitle, The New Biography.

Eminent Victorians: Eminent Victorians is a book by Lytton Strachey (one of the older members of the Bloomsbury Group), first published in 1918 and consisting of biographies of four leading figures from the Victorian era.  Its fame rests on the irreverence and wit Strachey brought to bear on three men and a woman who had till then been regarded as heroes and heroine.  They were:

Giuseppe Levi: Giuseppe Levi (October 14, 1872 – February 3, 1965) was an Italian anatomist and histologist, professor of human anatomy (since 1916) at the universities of Sassari, Palermo and Turin.  He was born on October 14, 1872 in Trieste to Jewish parents, Michele Levi and Emma Perugia.  He was married to Lidia Tanzi and had five children: Gino, Mario, Alberto, Paola (who became the wife of Adriano Olivetti), and writer Natalia Ginzburg (wife of Leone Ginzburg and mother of Carlo Ginzburg), who described her father's personality in the successful Italian book "Lessico famigliare" (1963).

Monk's House: Monk's House is an 18th-century weatherboarded cottage in the village of Rodmell, three miles (4.8km) south-east of Lewes, East Sussex, England.  The writer Virginia Woolf and her husband, the political activist, journalist and editor Leonard Woolf, bought the house in 1919, and received there many important visitors connected to the Bloomsbury Group, including T. S. Eliot, E. M. Forster, Roger Fry and Lytton Strachey.

Carrington (film): Carrington is a 1995 British biographical film written and directed by Christopher Hampton about the life of the English painter Dora Carrington (1893–1932), who was known simply as "Carrington".  The screenplay is based on biographies of writer and critic Lytton Strachey (1880–1932) by Michael Holroyd.

Natalia Ginzburg: Natalia Ginzburg, (] ; ] ; 14 July 1916 – 7 October 1991), was an Italian author whose work explored family relationships, politics during and after the Fascist years and World War II, and philosophy.  She wrote novels, short stories and essays, for which she received the Strega Prize and Bagutta Prize.  Most of her works were also translated into English and published in the United Kingdom and United States.

Lytton Strachey: Giles Lytton Strachey ( ; 1 March 1880 – 21 January 1932) was a British writer and critic.

Leone Ginzburg: Leone Ginzburg (] ; ] ; ] ; 4 April 1909 – 5 February 1944) was an Italian editor, writer, journalist and teacher, as well as an important anti-fascist political activist and a hero of the resistance movement.  He was the husband of the renowned author Natalia Ginzburg and the father of the historian Carlo Ginzburg.

Julia Strachey: Julia Strachey (August 14, 1901 – 1979) was an English writer, born in Allahabad, India, where her father, Oliver Strachey, the elder brother of Lytton Strachey, was a civil servant.  Her mother, Ruby, was of Swiss-German origin.  For most of Julia's life she lived in England, where she worked as a model at Poiret, as a photographer and as a publisher's reader, before she embarked upon a career in novel-writing.  She is perhaps best remembered for her work "Cheerful Weather for the Wedding", a book originally published by the Hogarth Press and recently reprinted by Persephone Books.

Roger Senhouse: Roger Henry Pocklington Senhouse (1899 – 1970) was an English publisher and translator, and a member of the Bloomsbury Group of writers, intellectuals, and artists.  The private letters of openly gay writer Lytton Strachey reveal that Roger Senhouse was his last lover, with whom he had a secretly sado-masochistic relationship in the early 1930s.

Question: Natalia Ginzburg and Lytton Strachey, have which occupation in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person mentioned in the question."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person mentioned in the question."
    },
    "common_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "person_1_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of all occupations identified for the first person."
    },
    "person_2_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of all occupations identified for the second person."
    }
  },
  "required": [
    "person_1_name",
    "person_2_name",
    "common_occupation",
    "person_1_occupations",
    "person_2_occupations"
  ],
  "additionalProperties": false
}
