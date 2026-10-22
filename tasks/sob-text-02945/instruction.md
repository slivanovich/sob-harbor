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
Zorobabel Rodríguez (writer): Zorobabel Rodríguez (1849–1901) was a Chilean lawyer, politician, writer and journalist.  He was born in Quillota on October 4, 1849 and died in Valparaiso on September 29, 1901.  He founded the "El Independiente" and "La Union" newspapers.  He was the son of José Martín Rodríguez Osorio and Francisca Benavides Carrera.

Oaxaca International Literary Competition: The Oaxaca International Literature Competition also known as El Concurso Internacional De Literatura Oaxaca is an "event within an event", where the main event is the Oaxaca International Independent Film and Video Festival also known as Festival Internacional De Cine Independiente y Video Oaxaca.  The two events are held each November in the Mexican city of Oaxaca.  The festival is an official cultural event of the city of Oaxaca de Juarez.

National Anti-Communist Front: The National Anti-Communist Front (Frente Anti-Communista Nacional) was a coalition of the anti-communist parties and groups (of ten or more) that supported Carlos Castillo Armas.  Its program envisioned economic and social reforms for the development of Guatemala and the elimination of communist infiltration.  Its members included the Anti-Communist Unification Party (PUA), Independent Anti-Communist Party of the West (PIACO), Anti-Communist University Students Committee (CEUA), Comités como el Cívico Independiente, Obrero Anticomunista, Femenino Anticomunista, de Locatarias, Asociación Juvenil Anticomunista, among others.  In 1955, most member organizations were involved in the establishment of the National Democratic Movement (MDN).

Albert Jennings Fountain: Colonel Albert Jennings Fountain (October 23, 1838 – disappeared February 1, 1896) was born on Staten Island, New York, on October 23, 1838, to Solomon Jennings and Catherine de la Fontaine.  He was trained as an attorney and elected to the Texas Senate and the New Mexico Legislature.  In 1873, Fountain moved from El Paso to Mesilla with his wife Mariana Pérez Fountain and their five children.  He served the Union Army in California and Arizona during the American Civil War and later as a militia officer defending against raiding Apaches.  Later, however, he developed a long and supportive history with several tribes, many Mescaleros calling him a friend.  In Mesilla, he worked as assistant district attorney and probate judge as well as a newspaper editor, founding, in 1877, the Mesilla Valley Independent and the Spanish edition El Independiente del Valle de la Mesilla.  He also founded the Mesilla Dramatic Society and the Mesilla Valley Opera House, now The Fountain Theater, both originally operated by his family.  Following a purge of corruption among cattle rustlers, Fountain and his 8-year-old son Henry disappeared near White Sands, New Mexico, where his wagon, stains of blood, and evidence of an ambush were left.  Suspicion centered on two rival landowners, Oliver M. Lee and Albert B. Fall.  The bodies were never discovered.

Videoscandals: The Videoscandals were political scandals in Mexico in 2004 when videos of prominent politicians taken with hidden cameras were made public.  The majority of them involved politicians in corrupt dealings with former business man Carlos Ahumada, and another showed a politician spending money in Las Vegas.

El Hijo del crack: El Hijo del crack (meaning "Son of the Star") is a 1953 Argentine football drama film co-directed by Leopoldo Torre Nilsson and Leopoldo Torres Ríos and starring Armando Bo and Oscar Rovito.  The film, a tale of a dwindling professional football star and his son was released on December 15, 1953 in Normandie cinema in Buenos Aires.  The cast involved major professional football players of the time as Mario Boyé, Tucho Méndez and Ángel Labruna and journalists such as Fioravanti.  It is the last film in which Leopoldo Torres Ríos and Leopoldo Torre Nilsson (father and son) worked together.  The 77 minute film was produced by Sociedad Independiente Filmadora Argentina  (SIFA).

National Accountability Bureau: The National Accountability Bureau (Urdu: ‎ ; abbreviated NAB), is an autonomous and constitutionally established federal institution responsible to build efforts against corruption and prepare critical national economic intelligence assessments against economic terrorism to the Government of Pakistan.  It has come under criticism for inhumane treatment of its detainees and the sweeping powers bestowed upon it under the National Accountability Ordinance 1999 promulgated by a military junta.  Pakistan's parliamentary committee that monitors corruption cases has criticized The National Accountability Bureau for its unwillingness to prosecute former Army officers involved in corruption scandals.

El Independiente (Colombian newspaper): El Independiente (English: The Independent ) was a Colombian newspaper that replaced El Espectador, when this newspaper suspended its publication due to a series of illegal actions committed against it by the military regime of Gustavo Rojas Pinilla in 1956.

Televisión Independiente de México: Televisión Independiente de México ("Independent Mexican Television", known on air as TIM or Cadena TIM) was a Mexican national television network founded in 1965 by Eugenio Garza Sada.  It operated until 1973, when it merged with its primary competitor, Telesistema Mexicano, owned by Emilio Azcárraga Vidaurreta, to form the Televisa conglomerate.  Televisa absorbed all of TIM's assets, including its television transmitters and its series, including pioneering programs such as El Chavo del Ocho.

Carlos Ahumada: Carlos Agustín Ahumada Kurtz (born 1964) is an entrepreneur of dual Argentine-Mexican nationality.  His main areas of business are mining, construction and football.  He founded the "El Independiente" newspaper in Mexico and was a partner and founding member of Colegio de Imagen Pública A.C.

Question: What year did the Video Scandals come out that involved the entrepreneur who founded the El Independiente? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The name of the political scandals."
    },
    "year_of_occurrence": {
      "type": "integer",
      "description": "The year the scandals occurred."
    },
    "involved_entrepreneur": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the entrepreneur involved in the scandals."
        },
        "role_in_scandals": {
          "type": "string",
          "description": "Description of the entrepreneur's involvement in the scandals."
        },
        "founded_newspaper": {
          "type": "string",
          "description": "The name of the newspaper founded by the entrepreneur."
        }
      },
      "required": [
        "name",
        "role_in_scandals",
        "founded_newspaper"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "event_name",
    "year_of_occurrence",
    "involved_entrepreneur"
  ],
  "additionalProperties": false
}
