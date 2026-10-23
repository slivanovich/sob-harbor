{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMonna Vanna: Monna Vanna (Russian: Монна Ванна ) is an unfinished opera by Sergei Rachmaninoff after a play by Maurice Maeterlinck.  Rachmaninoff had completed Act I in short vocal score, with piano accompaniment, and then he went to ask for permission to set the text in a full three-act treatment.  However, another composer, Henry Février, had by then received the rights to an operatic setting of the text.  Had Rachmaninoff proceeded to a complete operatic setting, such a work could not have been produced in European countries that were signatories to copyright laws that covered the work of Maeterlinck.  This opera could only have been produced in countries that at the time were not signatories to European copyright law, such as Russia.  Ultimately, Rachmaninoff abandoned further work on this opera and never wrote a complete setting.\n\nThe Letters of Kingsley Amis: The Letters of Kingsley Amis (2001) was assembled and edited by the American literary critic Zachary Leader.  It is a collection of more than 800 letters from Amis to many different friends and professional acquaintances from 1941 until shortly before his death in 1995.  About one quarter of the letters selected were addressed to Amis's close friend, the poet Philip Larkin.\n\nKingsley Amis: Sir Kingsley William Amis, CBE (16 April 1922 – 22 October 1995) was an English novelist, poet, critic, and teacher.  He wrote more than 20 novels, six volumes of poetry, a memoir, various short stories, radio and television scripts, along with works of social and literary criticism.  According to his biographer, Zachary Leader, Amis was \"the finest English comic novelist of the second half of the twentieth century.\"  He is the father of British novelist Martin Amis.\n\nMaurice Maeterlinck: Maurice Polydore Marie Bernard Maeterlinck (also called \"Comte (Count) Maeterlinck\" from 1932; ] in Belgium, ] in France; 29 August 1862 – 6 May 1949) was a Belgian playwright, poet, and essayist who was Flemish but wrote in French.  He was awarded the Nobel Prize in Literature in 1911 \"in appreciation of his many-sided literary activities, and especially of his dramatic works, which are distinguished by a wealth of imagination and by a poetic fancy, which reveals, sometimes in the guise of a fairy tale, a deep inspiration, while in a mysterious way they appeal to the readers' own feelings and stimulate their imaginations\".  The main themes in his work are death and the meaning of life.  His plays form an important part of the Symbolist movement.  In later life, Maeterlinck committed plagiarism.\n\nPelleas und Melisande (Schoenberg): Pelleas und Melisande, Op. 5, is a symphonic poem written by Arnold Schoenberg and completed in February 1903.  It was premiered on 25 January 1905 at the Musikverein in Vienna under the composer's direction in a concert that also included the first performance of Alexander von Zemlinsky's \"Die Seejungfrau\".  The work is based on Maurice Maeterlinck's play \"Pelléas and Mélisande\", a subject suggested by Richard Strauss.  When he began composing the work in 1902, Schoenberg was unaware that Claude Debussy's opera, also based on Maeterlinck's play, was about to premiere in Paris.\n\nPelléas et Mélisande (Fauré): Pelléas et Mélisande, Op. 80 is a suite derived from incidental music by Gabriel Fauré for Maurice Maeterlinck's play of the same name.  He was the first of four leading composers to write music inspired by Maeterlinck's drama.  Debussy, Schoenberg and Sibelius followed in the first decade of the 20th century.\n\nGeorgette Leblanc: Georgette Leblanc (8 February 1869 Rouen, – 27 October 1941 Le Cannet, near Cannes) was a French operatic soprano, actress, author, and the sister of novelist Maurice Leblanc.  She became particularly associated with the works of Jules Massenet and was an admired interpreter of the title role in Bizet's \"Carmen\".  For many years Leblanc was the lover of Belgian playwright and writer Maurice Maeterlinck, and he wrote several parts for her within his stage plays.  She portrayed the role of Ariane in \"Ariane et Barbe-bleue\", both in the original 1899 stage play by Maeterlinck and in the 1907 opera adaptation by Paul Dukas.  Leblanc also appeared in a couple of French films, most notably \"L'Inhumaine\" in 1924.  In the last few decades of her life she turned to writing, producing two commercially successful autobiographies and several children's books and travelogues.\n\nTeikoku Bungaku: Teikoku Bungaku (帝国文学, \"teikoku\" empire + \"bungaku\" literature) was a literature magazine from 1895 to 1920 contributed by Japanese writers, Inoue Tetsujiro, Ueda Kazutoshi, Takayama Chogyu and Ueda Bin.  With a focus on asserting the individuality of Japanese literature, the magazine often contrasted Japanese and global literature by covering writers such as Maurice Maeterlinck, George Bernard Shaw and Friedrich Nietzsche.  The magazine was published by Tokyo Imperial University.\n\nThe James Bond Dossier: The James Bond Dossier (1965), by Kingsley Amis, is a critical analysis of the James Bond novels.  Amis dedicated the book to friend and background collaborator, the poet and historian Robert Conquest.  Later, after Ian Fleming's death, Amis was commissioned as the first continuation novelist for the James Bond novel series, writing \"Colonel Sun\" (1968) under the pseudonym Robert Markham.  \"The James Bond Dossier\" was the first, formal, literary study of the James Bond character.  More recent studies of Fleming's secret agent and his world include \"The Politics of James Bond: From Fleming’s Novels to the Big Screen\" (2001), by the historian Jeremy Black.\n\nZachary Leader: Zachary Leader (born 1946) is a professor of English Literature at the University of Roehampton.  He was an undergraduate at Northwestern University, and later pursued graduate study at Trinity College, Cambridge and at Harvard University.  Though born in the U.S. and remaining an American citizen, Leader has lived and worked for over forty years in the UK.  His best-known works are probably \"The Letters of Kingsley Amis\", which he edited and published in 2001, and \"The Life of Kingsley Amis\" (2006, UK; 2007, US), a finalist for the 2008 Pulitzer Prize in Biography.  The first volume of his two-volume biography of Saul Bellow, \"The Life of Saul Bellow: To Fame and Fortune, 1915-1964\", was published in May 2015 by Alfred Knopf in the US and Jonathan Cape in the UK.  \"On Life-Writing\", an edited collection, will be published in September by OUP.  He is General Editor of the Oxford History of Life-Writing, a seven-volume series published by OUP.  A recipient of Guggenheim, Leverhulme and British Academy Fellowships, he is also a Fellow of the Royal Society of Literature.\n\nQuestion: Are Maurice Maeterlinck and Kingsley Amis both English writers?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed.\"\n    },\n    \"answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both writers are English, false otherwise.\"\n    },\n    \"writers\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each writer mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the writer.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the writer as stated in the context.\"\n          },\n          \"is_english\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the writer is English, false otherwise.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"nationality\",\n          \"is_english\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for the given answer based on the writers' nationalities.\"\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"answer\",\n    \"writers\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed."
      },
      "answer": {
        "type": "boolean",
        "description": "True if both writers are English, false otherwise."
      },
      "writers": {
        "type": "array",
        "description": "Details about each writer mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the writer."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the writer as stated in the context."
            },
            "is_english": {
              "type": "boolean",
              "description": "True if the writer is English, false otherwise."
            }
          },
          "required": [
            "name",
            "nationality",
            "is_english"
          ],
          "additionalProperties": false
        }
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for the given answer based on the writers' nationalities."
      }
    },
    "required": [
      "question_asked",
      "answer",
      "writers",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
