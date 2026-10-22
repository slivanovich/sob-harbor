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
Gerd Neggo: Gerd Neggo (9 November 1891 – 1 September 1974) was an Estonian dancer, dance teacher and choreographer.  She studied the musical response methods of É.  Jaques-Dalcroze, trained under Rudolf von Laban in Hamburg, Germany, and in 1924 established her own dance studio at Tallinn, Estonia, and promoted modern dance and mime based on classical ballet.  During the Soviet occupation of Estonia, she and her husband Paul Olak migrated to Sweden.  Her contributions to the cultural heritage of Estonia, as the founder of modern dance and mime in her country, is recognised via a scholarship, awarded annually since 2011.

Loie Fuller: Loie Fuller (also Loïe Fuller; January 15, 1862 – January 1, 1928) was an American dancer who was a pioneer of both modern dance and theatrical lighting techniques.

Stuart Hodes: Stuart Hodes (born 1924) is an American dancer, choreographer, dance teacher, dance administrator and author.  He was Martha Graham’s partner, danced on Broadway, in TV, film, in recitals, and with his own troupe.  His choreography has appeared on the Boston Ballet, Dallas Ballet, Harkness Ballet, Joffrey Ballet, San Francisco Ballet and other troupes.  He taught at the Martha Graham School, Neighborhood Playhouse, NYC High School of Performing Arts, headed dance at NYU School of the Arts and Borough of Manhattan Community College.  He was Dance Associate for the NY State Council on the Arts, dance panelist for the National Endowment for the Arts, president of the National Association of Schools of Dance, and a member of the First American Dance Study Team to China in 1980, returning in 1992 to teach the Guangzhou modern dance troupe.

Graham technique: Graham technique is a modern dance movement style and pedagogy created by American dancer and choreographer Martha Graham (1894–1991).  Graham technique has been called the "cornerstone" of American modern dance, and has been taught worldwide.  It is widely regarded as the first codified modern dance technique, and strongly influenced the later techniques of Merce Cunningham, Lester Horton, and Paul Taylor.

Dance in California: California is rich in dance history.  In classical ballet, California is home to the oldest professional ballet company in the United States.  The San Francisco Ballet, founded as the San Francisco Opera Ballet in 1933, predates both American Ballet Theater and New York City ballet.  Barbara Crockett founded the Sacramento Ballet in 1954 and hosted the first festival for the Pacific Western Region of Regional Dance America in 1966.  In modern dance, Ruth St. Denis established her second school in the Hollywood area of Los Angeles in 1940 while Lester Horton created the Horton Dance Group in 1934, also in Los Angeles.  Ann Halprin founded the San Francisco Dancers’ Workshop in 1950 and continues to live and work in the San Francisco Bay Area.  The Bay Area in also home to Alonzo King's Lines Ballet and Oberlin Dance Collective.

Lila York: Lila York (born 29 November 1948) is an American dancer and choreographer based in New York City.  She studied English Literature at Skidmore College before studying ballet and modern dance at the Martha Graham Center of Contemporary Dance and with Paul Sanasardo.  York joined the Paul Taylor Dance Company in 1973 where she danced for more than a decade.  After leaving the company, she left the "very heart of American modern dance" to become one of "ballet's most sought-after choreographers", working with many of the world's foremost ballet companies.

Contemporary ballet: Contemporary ballet is a genre of dance that incorporates elements of classical ballet and modern dance.  It employs classical ballet technique and in many cases classical pointe technique as well, but allows greater range of movement of the upper body and is not constrained to the rigorously defined body lines and forms found in traditional, classical ballet.  Many of its attributes come from the ideas and innovations of 20th century modern dance, including floor work and turn-in of the legs.

Ballet Philippines: Ballet Philippines (BP) is a ballet company in the Philippines founded in 1969 by Alice Reyes with the support of Eddie Elejar and the Cultural Center of the Philippines.  Proficient in both ballet and modern dance, the company synthesizes diverse dance and movement forms, from classical ballet to avant-garde choreography, from traditional dance to modern dance, from martial arts to aerial movements, into distinctively Filipino contemporary expressions.

Contemporary dance in Japan: Western schools covered classical ballet, jazz-dance, and modern dance and influenced the butoh avant-garde dance movement.  Ballet was said to have replaced traditional Japanese arts, such as flower arrangement and the tea ceremony, in the hearts of young girls.  Prima ballerina Morishita Yoko sat on the jury for the Prix de Lausanne Ballet Competition in 1989, held for the first time in Tokyo, marking the arrival of Japanese classical ballet in the international community.  Horiuchi Gen, a 1980 Prix de Lausanne winner, became a major soloist with the New York City Ballet, and Japanese performers noted for their superb technique were members of many major international companies.  Modern dance was performed early after World War II and was later taught by such famous dancers as Eguchi Takaya.  The Tokyo Modern Dance School and the Ozawa Hisako Modern Dance Company also promoted avant-garde modern dance.  A wide experimental range within modern dance occurred from which choreographer Teshigawara Saburo skillfully drew to create multifaceted works for his KARAS Company.

Free dance: Free dance is a 20th-century dance form that preceded modern dance.  Rebelling against the rigid constraints of classical ballet, Loie Fuller, Isadora Duncan and Ruth St. Denis (with her work in theater) developed their own styles of free dance and laid the foundations of American modern dance with their choreography and teaching.  In Europe Rudolf Laban, Emile Jaques-Dalcroze and François Delsarte developed their own theories of human movement and methods of instruction that led to the development of European modern and Expressionist dance.

Question: Free dance is a 20th-century dance form, that preceded modern dance, rebelling against the rigid constraints of classical ballet, assisting was Loie Fuller, was an American dancer who was a pioneer of both modern dance and theatrical lighting techniques, she passed away on which date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the dancer."
    },
    "death_date": {
      "type": "string",
      "description": "The specific date of the person's death."
    },
    "pioneering_contributions": {
      "type": "array",
      "description": "A list of areas where the person was a pioneer.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "person_name",
    "death_date",
    "pioneering_contributions"
  ],
  "additionalProperties": false
}
