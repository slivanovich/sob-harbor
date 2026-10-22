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
Fauve (collective): Fauve collective, sometimes stylized as FAUVE, is a French arts collective of music and videography established in 2010 in Paris.  The band also uses the not equal to sign ≠.  The act depends mostly on story telling through acting, through spoken word and musical accompaniment.  The collective has its own record label called FAUVE CORP.

Writer: A writer is a person who uses written words in various styles and techniques to communicate their ideas.  Writers produce various forms of literary art and creative writing such as novels, short stories, poetry, plays, screenplays, and essays as well as various reports and news articles that may be of interest to the public.  Writers' texts are published across a range of media.  Skilled writers who are able to use language to express ideas well often contribute significantly to the cultural content of a society.  The word is also used elsewhere in the arts – such as songwriter – but as a standalone term, "writer" normally refers to the creation of written language.  Some writers work from an oral tradition.

Dibby Dibby Sound: "Dibby Dibby Sound" is a song by British record producer DJ Fresh and American record producer Jay Fay (whose track it is heavily based on), featuring vocals from British singer Ms. Dynamite.  It was released on 2 February 2014 as the second single from his forthcoming fourth studio album.  The song was written by Dan Stein, The Invisible Men, Niomi McLean-Daley and Joshua Fagin.  It premiered on Zane Lowe's BBC Radio 1 show, who made it the week's "Hottest Record in the World" on 29 October 2013.

Archaeoastronomy: Archaeoastronomy (also spelled archeoastronomy) is the study of how people in the past "have understood the phenomena in the sky, how they used these phenomena and what role the sky played in their cultures." Clive Ruggles argues it is misleading to consider archaeoastronomy to be the study of ancient astronomy, as modern astronomy is a scientific discipline, while archaeoastronomy considers symbolically rich cultural interpretations of phenomena in the sky by other cultures.  It is often twinned with "ethnoastronomy", the anthropological study of skywatching in contemporary societies.  Archaeoastronomy is also closely associated with historical astronomy, the use of historical records of heavenly events to answer astronomical problems and the history of astronomy, which uses written records to evaluate past astronomical practice.

Narration: Narration is the use of a written or spoken commentary to convey a story to an audience.  Narration encompasses a set of techniques through which the creator of the story presents their story, including:

Audio tour: An audio tour or audio guide provides a recorded spoken commentary, normally through a handheld device, to a visitor attraction such as a museum.  They are also available for self-guided tours of outdoor locations, or as a part of an organised tour.  It provides background, context, and information on the things being viewed.  Audio guides are often in multilingual versions and can be made available in different ways.  Some of the more elaborate tours may include original music and interviews.  Traditionally rented on the spot, more recently downloaded from the Internet or available via the mobile phone network.  Some audio guides are free or included in the entrance fee, others have to be purchased separately.

Sign language: Sign language (also signed language) is a language which chiefly uses manual communication to convey meaning, as opposed to spoken language.  This can involve simultaneously combining hand shapes, orientation and movement of the hands, arms or body, and facial expressions to express a speaker's thoughts.  Sign languages share many similarities with spoken languages (sometimes called "oral languages"), which depend primarily on sound, and linguists consider both to be types of natural language.  Although there are some significant differences between signed and spoken languages, such as how they use space grammatically, sign languages show the same linguistic properties and use the same language faculty as do spoken languages.  They should not be confused with body language, which is a kind of non-linguistic communication.

Farewell Aunty Jack: "Farewell Aunty Jack" was the closing theme to The Aunty Jack Show, played at the end of each episode.  It was re-recorded and released as a hit single in late 1973 and spent 3 weeks at number one in the charts in Australia in March 1974.  The music was written by Rory O'Donoghue, who also did the singing as the character "Thin Arthur", whereas "Aunty Jack" (Grahame Bond) provided wise-cracks and other spoken commentary to the lyrics, addressed to the listener and the singer.

Françoise Prévost: Françoise Prévost (c. 1680 – 1741) was a French ballerina who helped establish dramatic dance in the early world of classical ballet.  She was expressive, light and dramatic in style.  Prevost debuted at the Académie d'Opera in the ballet, "Atys", later replacing Marie-Thérèse de Subligny as the female lead.  In 1708, she performed with Jean Balon in the final scene of Corneille's "Les Horaces".  The performance, though only of the final scene of the play and entirely in pantomime, is said to have caused the audience to weep.  The "pantomime" came from the popular theaters of the time and freely used bold gestures and body language to communicate the narrative to the audience.  The goal was to convey a story of meaning using purely movement, without spoken word.  Maintaining her interest in the dramatic potential of dance, Prevost created a famous solo in 1714 called "Les Caracteres de la Danse."  Choreographed to a suite of dances by composer Jean Ferry Rebel, the "characters" depicted a series of lovers of varying ages and sexes, and Prevost enacted each one to a different piece of music: the bourree, the menuet, the passepied.  She taught this solo to her two most accomplished female students: Marie Camargo and Marie Sallé.  Camargo was the first to learn the solo for her debut at the Paris Opera.  Her growing success incited jealousy in Prevost, and she relegated Camargo to the corps de ballet.  One day however, Camargo made an spectacular impromptu improvisation solo for a missing male dancer.  The arrival of Marie Salle, and her dramatic recreation of the famous solo into a pas de deux of rich emotional interaction, highlighted the different approaches to dance of the period: technical flash verses dramatic depth.

Chris Porter (producer): Chris Porter is a British record producer, engineer, narrator.  He has worked with Sir Elton John, Take that, George Michael and Chris de Burgh.

Question: Which British record producer also uses written or spoken commentary to convey a story to an audience?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "producer_name": {
      "type": "string",
      "description": "The name of the record producer."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the record producer."
    },
    "is_narrator": {
      "type": "boolean",
      "description": "Indicates if the record producer also works as a narrator."
    },
    "other_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other professions held by the individual besides record producer and narrator."
    }
  },
  "required": [
    "producer_name",
    "nationality",
    "is_narrator",
    "other_professions"
  ],
  "additionalProperties": false
}
