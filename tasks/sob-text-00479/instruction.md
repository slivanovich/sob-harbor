{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nToi, la musique et moi: \"Toi, la musique et moi\" (English translation: \"You, the Music and I\") was the Monegasque entry in the Eurovision Song Contest 1976, performed in French by French singer Mary Christy.  Christy recorded the song in five languages; French, Italian (as \"La musica e noi due\"), Spanish (\"La música, tú y yo\"), German (\"Die Musik und ich\") and English (\"Thank You for Rushing into My Life\").\n\nRichard Stone (musician): Richard Stone is an American lutenist, music director, educator and music editor.  He performs on lute and theorbo as a soloist and accompanist; he co-founded and co-directs Tempesta di Mare, The Philadelphia Baroque Orchestra; his musical editions are published by AR Editions and Prima la Musica; and he lectures and teaches lute, theorbo, continuo and performance practice for singers and instrumentalists at the Peabody Conservatory of The Johns Hopkins University.\n\nMusica e dischi: Musica e dischi is the oldest music industry publication in Italy.  It was founded in October 1945 in Milan, Italy on the initiative of the journalist and musicologist Aldo Mario De Luigi, a former senior record of VCM (now EMI Italy).  In the beginning, the magazine was published with the name \"Musica\" (\"Dischi\" was added on the second edition) on a monthly basis.  \"Musica e dischi\" later issued a list of best-seller music recordings nationally.  On its 735th edition on December 2009, \"Musica e dischi\" director Mario De Luigi announced that they would publish an online magazine since March 2010 and stop the publication of physical magazine after 65 years.\n\nLa bella Antonia, prima monica e poi dimonia: La bella Antonia, prima monica e poi dimonia, also known as \"Naughty Nun\", is a 1972 Italian commedia sexy all'italiana directed by Mariano Laurenti.\n\nViva La Musica: Viva La Musica is a popular band from Zaire (now DR Congo) founded by singer Papa Wemba in 1977.  While Viva La Musica started out as a soukous band (essentially a spin-off of Zaiko Langa Langa), it eventually grew into a world music act, reaching some popularity and success in the European, American, and even Asian markets, as well as in most of Africa.  The band is still active today, although it is just one of a number of musical ensembles used by Papa Wemba as a backup for his essentially soloist production.\n\nLa Musica deuxième: La Musica Deuxième is a play written by Marguerite Duras, published in 1985 by Éditions Gallimard.  It is an extension of the work \"La Musica\".\n\nPrima la musica e poi le parole: Prima la musica e poi le parole (\"First the music and then the words\"), also called \"Prima la musica, poi le parole \" is an opera in one act by Antonio Salieri to a libretto by Giovanni Battista Casti.  The work was first performed on 7 February 1786 in Vienna, following a commission by the Emperor Joseph II.  The opera (more specifically, a \"divertimento teatrale \") was first performed at one end of the orangery of the Schönbrunn Palace in Vienna by an Italian troupe: simultaneously, Mozart's \"Der Schauspieldirektor\" was staged at the other end.\n\nAntonio Salieri: Antonio Salieri (] ; 18 August 17507 May 1825) was an Italian classical composer, conductor, and teacher.  He was born in Legnago, south of Verona, in the Republic of Venice, and spent his adult life and career as a subject of the Habsburg Monarchy.\n\nLa Musica Lirica: La Musica Lirica is a five-week training program structured for performance artists looking to gain hands-on training and experience, immersed in its environment, as a way to help bridge the gap between college and career.  Founded in 1999, this music festival now produces three to four operas each season with over seventy performers.  Soprano Brygida Bziukiewicz-Kulig is the General Director of La Musica Lirica, and baritone Brian Leeper is the Artistic Director.\n\nGiulio Sabino: The opera, staged in six or seven European countries at the end of the 18th century, was the subject of a parody in Antonio Salieri's 1786 work \"Prima la musica e poi le parole\".\n\nQuestion: In which city was the composer of \"Prima la musica e poi le parole\" born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"composer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the composer.\"\n    },\n    \"work_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the musical work.\"\n    },\n    \"birth_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the composer was born.\"\n    },\n    \"birth_region\": {\n      \"type\": \"string\",\n      \"description\": \"The historical region or state where the composer was born.\"\n    }\n  },\n  \"required\": [\n    \"composer_name\",\n    \"work_title\",\n    \"birth_city\",\n    \"birth_region\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "composer_name": {
        "type": "string",
        "description": "The name of the composer."
      },
      "work_title": {
        "type": "string",
        "description": "The title of the musical work."
      },
      "birth_city": {
        "type": "string",
        "description": "The city where the composer was born."
      },
      "birth_region": {
        "type": "string",
        "description": "The historical region or state where the composer was born."
      }
    },
    "required": [
      "composer_name",
      "work_title",
      "birth_city",
      "birth_region"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
