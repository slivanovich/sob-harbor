{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBig Band Bossa Nova: Big Band Bossa Nova is a 1962 bossa nova album by American impresario, jazz composer, trumpeter, arranger and record producer Quincy Jones and his band.  It features the popular number \"Soul Bossa Nova.\"  The title \"Big Band Bossa Nova\" was also used for three other 1962 albums, by Stan Getz, Oscar Castro-Neves and Enoch Light.\n\nPensativa: \"Pensativa\" is a bossa nova jazz standard by American pianist/composer/arranger Clare Fischer, first recorded in 1962 by a quintet under the joint leadership of Fischer and saxophonist Bud Shank, and released that year as part of an album entitled \"Bossa Nova Jazz Samba\", comprising music in this style, as per its title, all of it arranged by Fischer, and, with the exception of Erroll Garner's \"Misty\", composed by him as well.  In retrospect, this would prove to be just the first of countless forays by Fischer into various areas of Latin music (with \"area\" denoting both genre \"and\" geographic region).  This particular song was one of the first, and almost certainly the most famous, of all the foreign-born - i.e. non-Brazilian - bossa novas. Its form, though extended (64 mm.) , is standard A-A-B-A, with each section consisting of 16 measures instead of eight.\n\nLuiz Eça: Luiz Mainzi da Cunha Eça (April 3, 1936 – May 24, 1992) was a Brazilian jazz samba and bossa nova pianist from Rio de Janeiro, probably best known for his 1960s work with the bossa nova Tamba Trio/Tamba 4 (with Helcio Milito and Bebeto Castilho).  Trained as a classical pianist, Eça created a formal, but stunning approach to bossa nova classics such as \"The Hill\" by Antonio Carlos Jobim and works by Edu Lobo.  His own composition, the Dolphin, is considered a jazz standard, being recorded by artists as diverse as Stan Getz, Bill Evans and Denny Zeitlin.  The Tamba 4 group also featured Otávio Bailly, who eventually replaced Bebeto.\n\nBossa nova: Bossa nova is a genre of Brazilian music, which developed and was popularized in the 1950s and 1960s and is today one of the best-known Brazilian music genres abroad.  The phrase \"bossa nova\" means literally \"new trend\" (] ).  A lyrical fusion of samba and jazz, bossa nova acquired a large following in the 1960s, initially among young musicians and college students.\n\nThe Girl from Ipanema: \"Garota de Ipanema\" (\"The Girl from Ipanema\") is a Brazilian bossa nova jazz song.  It was a worldwide hit in the mid-1960s and won a Grammy for Record of the Year in 1965.  It was written in 1962, with music by Antônio Carlos Jobim and Portuguese lyrics by Vinicius de Moraes.  English lyrics were written later by Norman Gimbel.\n\nJazz Samba: Jazz Samba is a bossa nova album by Stan Getz and Charlie Byrd released by Verve Records in 1962.  \"Jazz Samba\" signaled the beginning of the bossa nova craze in America.  Stan Getz was the featured soloist and the tracks were arranged by Charlie Byrd, who had first heard bossa nova during a tour of Brazil in 1961.\n\nBrazil (Rosemary Clooney album): Brazil is a 2000 album by Rosemary Clooney.  John Pizzarelli accompanies Clooney on vocals on five of the tracks, and sings Antonio Carlos Jobim's \"Wave\".  Diana Krall duets with Clooney on \"The Boy from Ipanema\".\n\nSylvia Telles: Sylvia Telles (August 27, 1934 – December 17, 1966) was a Brazilian jazz samba and bossa nova singer of the 1950s and 1960s.  Perhaps one of the most highly spoken of singers of the time, Telles preceded the advent of bossa nova, and then began covering songs by such influential composers as Antonio Carlos Jobim, and worked with others such as Luiz Bonfá.  She also did several tribute albums to Antonio Carlos Jobim.  One of the most famous classic bossa nova songs was written for her by Jobim, its namesake her nickname - \"Dindi\".\n\n1960s in jazz: In the late 1960s, Latin jazz, combining rhythms from African and Latin American countries, often played on instruments such as conga, timbale, güiro, and claves, with jazz and classical harmonies played on typical jazz instruments (piano, double bass, etc.) broke through.  There are two main varieties: Afro-Cuban jazz was played in the US right after the bebop period, while Brazilian jazz became more popular in the 1960s.  Afro-Cuban jazz began as a movement in the mid-1950s as bebop musicians such as Dizzy Gillespie and Billy Taylor started Afro-Cuban bands influenced by such Cuban and Puerto Rican musicians as Xavier Cugat, Tito Puente, and Arturo Sandoval.  Brazilian jazz such as bossa nova is derived from samba, with influences from jazz and other 20th-century classical and popular music styles.  Bossa is generally moderately paced, with melodies sung in Portuguese or English.  The style was pioneered by Brazilians João Gilberto and Antônio Carlos Jobim.  The related term jazz-samba describes an adaptation of bossa nova compositions to the jazz idiom by American performers such as Stan Getz and Charlie Byrd.\n\nIpanema: Ipanema (] ) is a neighborhood located in the South Zone of the city of Rio de Janeiro (Brazil), between Leblon and Arpoador.  The beach at Ipanema became known internationally with the popularity of the bossa nova jazz song, \"The Girl from Ipanema\" (\"\"Garota de Ipanema\"\"), written by Antônio Carlos Jobim and Vinícius de Moraes.\n\nQuestion: What year was this song written, which is a Brazilian bossa nova jazz song and was a duet between Diana Krall and Rosemary Clooney on Brazil?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_name\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"original_writing_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the song was originally written.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the song.\"\n    },\n    \"album_appearance\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album on which the song appears.\"\n        },\n        \"album_artist\": {\n          \"type\": \"string\",\n          \"description\": \"The main artist of the album.\"\n        },\n        \"featured_duet_artists\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of artists who performed the duet on this album.\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"album_artist\",\n        \"featured_duet_artists\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_name\",\n    \"original_writing_year\",\n    \"genre\",\n    \"album_appearance\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_name": {
        "type": "string",
        "description": "The title of the song."
      },
      "original_writing_year": {
        "type": "integer",
        "description": "The year the song was originally written."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the song."
      },
      "album_appearance": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album on which the song appears."
          },
          "album_artist": {
            "type": "string",
            "description": "The main artist of the album."
          },
          "featured_duet_artists": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of artists who performed the duet on this album."
          }
        },
        "required": [
          "album_title",
          "album_artist",
          "featured_duet_artists"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_name",
      "original_writing_year",
      "genre",
      "album_appearance"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
