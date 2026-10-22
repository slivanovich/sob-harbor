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
Filmworks X: In the Mirror of Maya Deren: Filmworks X: In the Mirror of Maya Deren features a score for film by John Zorn.  The album was released on Zorn's own label, Tzadik Records, in 2001 and contains music that Zorn wrote and recorded for the documentary film "In the Mirror of Maya Deren" on the life and work of Maya Deren directed by Martina Kudlácek.

Teiji Ito: Teiji Ito (伊藤貞司 , Itō Teiji , January 22, 1935 – August 16, 1982) was a Japanese composer and performer.  He is best known for his scores for the avant-garde films by Maya Deren.  The independent filmmaker, Barbara Hammer, continues to promote and educate the world about both Teiji and his wife, Maya Deren.

Vase de Noces: Vase de Noces (1974) is a Belgian film directed by Thierry Zéno and starring Dominique Garny.

Lynne Sachs: Lynne Sachs (born August 10, 1961 in Memphis, Tennessee) is an American experimental filmmaker who makes films, videos, installations and web projects exploring the relationship between personal observations and broader historical experiences.  She is known for weaving together poetry, collage, painting, politics and layered sound design.  After graduating from Brown University and majoring in history, she developed an interest in experimental documentary filmmaking while attending the 1985 Robert Flaherty Documentary Film Seminar through a scholarship.  There, she was particularly inspired by the works of Bruce Conner, who would later become her mentor, and Maya Deren.  That same year, Sachs moved to San Francisco to attend San Francisco State University and later the San Francisco Art Institute.  It was during this time that she studied and collaborated with Trinh T. Minh-ha, George Kuchar and Gunvor Nelson.

In the Mirror of Maya Deren: The documentary In the Mirror of Maya Deren ("Im Spiegel der Maya Deren", 2002) is a film about avant garde filmmaker Maya Deren (1917-1961) by Austrian film maker Martina Kudlacek.  It is based on the biography "The Legend of Maya Deren".

Thierry Zéno: Thierry Zéno (born Thierry Jonard; 22 April 1950 – 7 June 2017) was a Belgian author-filmmaker.

Maya Deren Award: The American Film Institute Award for Independent Film and Video Artists, subtitled and generally known as the Maya Deren Award, was an award presented to filmmakers and video artists by the American Film Institute to honor independent filmmaking.  Named for the avant-garde experimental film artist Maya Deren, it was given from 1986 through 1996.

Maya Deren: Maya Deren (April 29, 1917 – October 13, 1961), born Eleanora Derenkowskaia (Russian: Элеоно́ра Деренко́вская ), was a Russian-American filmmaker and one of the most important American experimental filmmakers and entrepreneurial promoters of the avant-garde in the 1940s and 1950s.  Deren was also a choreographer, dancer, film theorist, poet, lecturer, writer and photographer.

At Land: At Land (1944) is a 15-minute silent experimental film written, directed by, and starring Maya Deren.  It has a dream-like narrative in which a woman, played by Deren, is washed up on a beach and goes on a strange journey encountering other people and other versions of herself.  Deren once said that the film is about the struggle to maintain one's personal identity.

Illusions &amp; Mirrors: Illusions & Mirrors is a 2013 short film directed by Iranian-born American artist and filmmaker Shirin Neshat.  The film, shot in black-and-white, stars Tarek Aylouch, Michael Markiewicz, and the Israeli-born American actress Natalie Portman.  The film was commissioned by Dior, for which Portman is a spokesmodel, for the Miss Dior Expo at the Grand Palais, Paris.  Shirin Neshat said that the film is a tribute to the black-and-white silent films made by such surrealist filmmakers as Man Ray, Jean Cocteau, Luis Buñuel, and Maya Deren.

Question: Were Thierry Zéno and Maya Deren Filmmakers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "is_filmmaker": {
          "type": "boolean"
        },
        "nationality": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "is_filmmaker",
        "nationality"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "is_filmmaker": {
          "type": "boolean"
        },
        "nationality": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "is_filmmaker",
        "nationality"
      ],
      "additionalProperties": false
    },
    "both_are_filmmakers": {
      "type": "boolean"
    }
  },
  "required": [
    "person_1",
    "person_2",
    "both_are_filmmakers"
  ],
  "additionalProperties": false
}
