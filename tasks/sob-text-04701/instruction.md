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
The Dance Goes On: The Dance Goes On (German: Der Tanz geht weiter) is a 1930 American crime film directed by William Dieterle and starring Dieterle, Lissy Arna and Anton Pointner.  It was made by Warner Brothers as the German-language version of their film "Those Who Dance".

Man by the Wayside: Man by the Wayside (German: Der Mensch am Wege) is a 1923 German silent drama film directed by William Dieterle and starring Alexander Granach, Emilia Unda and Dieterle.

Behind the Altar: Behind the Altar or The Secret of Abbe X (German: Das Geheimnis des Abbe X) is a 1927 German silent drama film directed by Julius Brandt and William Dieterle and starring Dieterle, Marcella Albani and Alfred Gerasch.

The Saint and Her Fool: The Saint and Her Fool (German:Die Heilige und ihr Narr) is a 1928 German silent drama film directed by William Dieterle and starring Dieterle, Lien Deyers and Gina Manès.  It was based on a novel by and premiered at the Capital am Zoo in Berlin.  Art direction was by Andrej Andrejew.  For a long time, the movie was considered lost.  Although never released in the US, a nitrate copy was discovered in Jack Warner's personal vault.  In 2008 it was given to the UCLA in Los Angeles and restored.

Coleman Francis: Coleman C. Francis (January 24, 1919 – January 15, 1973) was an American actor, writer, producer, and director.  He was best known for his film trilogy consisting of "The Beast of Yucca Flats" (1961), "The Skydivers" (1963), "Red Zone Cuba" (1966), all three of which were filmed in the general Santa Clarita, California area and used preoccupation with light aircraft and parachuting, coffee or cigarettes serving as a prop or a center of conversation, and a vigilante-style gunning down of suspects without a trial to conclude the film as frequent motifs.

Mistress of the World: Mistress of the World (German: "Die Herrin der Welt" , French: "Les mystères d'Angkor" , Italian: "Il mistero dei tre continenti" ) is a 1960 German-French-Italian science fiction-spy film directed by William Dieterle and starring Martha Hyer and Carlos Thompson.  It marked the comeback in his native country of the director William Dieterle after several decades spent in Hollywood.  In West Germany it was released in a longer version split in two parts ("Die Herrin der Welt - Teil I" and "Die Herrin der Welt - Teil II").

Kismet (1944 film): Kismet is a 1944 Metro-Goldwyn-Mayer film in Technicolor starring Ronald Colman, Marlene Dietrich, Joy Page, and Florence Bates.  James Craig played the young Caliph of Baghdad, and Edward Arnold was the treacherous Grand Vizier.  It was directed by William Dieterle, but was not a success at the box office.  Dieterle had directed Marlene two decades prior in the German silent film "Man by the Wayside", which was both the first role in which Dietrich was cast competitively and Dieterle's directorial debut.

Rustle of Spring (film): Rustle of Spring (German: Frühlingsrauschen) is a 1929 German silent romance film directed by William Dieterle and starring Dieterle, Lien Deyers and Julius Brandt.

Quick, Let's Get Married: Quick, Let's Get Married (also known as The Confession) is a 1964 American comedy film directed by William Dieterle and starring Ginger Rogers, Ray Milland and Barbara Eden.  It was produced by Rogers' husband William Marshall in an attempt to revive her screen career.  The film had a troubled production, with original director Victor Stoloff being replaced by Dieterle.  It sat on the shelf for several years and did not get a full release until 1971.

William Dieterle: William Dieterle (July 15, 1893 – December 9, 1972) was a German actor and film director, who worked in Hollywood for much of his career.  His best known films include "The Devil and Daniel Webster", "The Story of Louis Pasteur" and "The Hunchback of Notre Dame".  His 1937 film "The Life of Emile Zola" won the Academy Award for Best Picture.

Question: Coleman Francis and William Dieterle, have which occupations in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the individuals being compared."
    },
    "common_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of occupations shared by both individuals."
    },
    "number_of_common_occupations": {
      "type": "integer",
      "description": "The count of occupations shared by both individuals."
    }
  },
  "required": [
    "person_names",
    "common_occupations",
    "number_of_common_occupations"
  ],
  "additionalProperties": false
}
