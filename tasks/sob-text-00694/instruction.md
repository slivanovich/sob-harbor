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
Max Boot: Max Boot (born September 12, 1969) is a Russian-American author, consultant, editorialist, lecturer, and military historian.  He has been an advocate of American values in foreign policy.  He once described his ideas as "American might to promote American ideals."  Boot worked as a writer and editor for "Christian Science Monitor" and then for "The Wall Street Journal" in the 1990s.  He is now Jeane J. Kirkpatrick Senior Fellow in National Security Studies at the Council on Foreign Relations.  He has written for numerous publications such as "The Weekly Standard", "The Los Angeles Times", and "The New York Times", and he has also authored books of military history.  Boot's most recent book, titled "Invisible Armies" which came out in 2013, is about the history of guerrilla warfare.

Girilal Jain: Girilal Jain (1924 – 19 July 1993), was an Indian journalist.  He served as the editor of The Times of India from 1978 till 1988.  He was sympathetic to Hindu nationalism and authored books on the subject, the best known of which, "The Hindu Phenomenon", was published posthumously.  The Government of India awarded him the civilian honour of the Padma Bhushan in 1989.

Charlotte Zolotow Award: The Charlotte Zolotow Award is an American literary award presented annually for outstanding writing in a picture book published in the United States during the preceding year.  By contrast, the Caldecott Medal is for outstanding illustration in a picture book.  The Zolotow award was established in 1998 by the Cooperative Children's Book Center (CCBC) at the University of Wisconsin–Madison School of Education and named to honor the work of Charlotte Zolotow, an American children's book editor and author.  Ms. Zolotow worked with Harper Junior Books for 38 years during which time she wrote more than 70 picture books.  Zolotow attended the University of Wisconsin in Madison on a writing scholarship from 1933-36.  The Cooperative Children's Book Center is a children's literature library of the School of Education, University of Wisconsin–Madison.

Jennifer Westwood: Jennifer Westwood (5 January 1940 – 12 May 2008) was a British author, broadcaster and folklorist.  She was a Doctor of Philosophy with special interests in English Language, Anglo-Saxon and Old Norse.  Her first book, "Mediaeval Tales", was published in 1968.  An active committee member of The Folklore Society from 1987 until 2003, she undertook a variety of duties including editing its publications and helping other authors.  As a broadcaster, she worked on programmes produced for BBC Radio 4 and the corporation's Radio Norfolk.  Commonly known as "Jen", after her second marriage she also authored books in the name of Jennifer Chandler.

Clinton Bennett: Clinton Bennett (born 7 October 1955) is a British American scholar of religions and participant in interfaith dialogue specialising in the study of Islam and Muslim-non-Muslim encounter.  An ordained Baptist minister, he was a missionary in Bangladesh before serving as the second director of interfaith relations at the British Council of Churches in succession to Kenneth Cracknell.  Bennett has also taken part in the dialogue activities of the World Council of Churches.  A graduate of Manchester, Birmingham and Oxford Universities he has held several academic appointments in the United Kingdom and in the United States, where he now lives.  He currently writes for various publications and teaches part-time at the State University of New York at New Paltz and at Marist College.  He is a Fellow of the Royal Asiatic Society, of the Royal Anthropological Institute and of the Committee for the Scientific Examination of Religion.  He has authored books, chapters in books, journal articles and Encyclopedia entries.  He can be considered to have made a significant contribution toward developing a Christian appreciation of Islam and of Muhammad.  Ahmad Shafaat writes, 'Bennett's approach allows him to treat Islamic traditions and their Muslim interpretations with sensitivity and respect, not often found among Christian writings on Islam.'  Bennett became a US citizen during 2012.

João Almino: João Almino is a Brazilian novelist.  He is the author of "The Brasília Quintet", which consists of the novels "Ideas on Where to Spend the End of the World", "Samba-Enredo", "The Five Seasons of Love" (first published in Portuguese by Editora Record; published in Spanish by Alfaguara, México, and by Corregidor, in Argentina; in Italian by Editrice Il Sirente; Casa de las Americas 2003 Literary Award; in English by Host Publications, 2008); "The Book of Emotions" (shortlisted for the Zaffari & Bourbon Literary Award and the Portugal-Telecom Literary Award; Editora Record, 2008; Dalkey Archive Press, 2012) and "Cidade Livre" ("Free City", Editora Record, 2010; Passo Fundo Zaffari & Bourbon Literary Award for best novel published in Portuguese from May 2009 to May 2011; shortlisted for the Jabuti Award 2011 and for the Portugal-Telecom Literary Award 2011; translated as "Free City", it was published by Dalkey Archive Press in 2013).  His most recent novel was published in Brazil in 2015: "Enigmas da Primavera" ("Enigmas of Spring"), which was published in English in 2016 by Dalkey Archive Press.  He has also authored books of philosophical and literary essays.  He taught at the National Autonomous University of Mexico (UNAM), at the University of Brasília (UnB), the Instituto Rio Branco, Berkeley, Stanford and The University of Chicago.

Bruce Jackson (scholar): Bruce Jackson (born May 21, 1936) is an American folklorist, documentary filmmaker, writer, photographer.  He is SUNY Distinguished Professor and the James Agee Professor of American Culture at the University at Buffalo.  Jackson has edited or authored books published by major university presses.  He has also directed and produced five documentary films.

Philip Pullman: Philip Pullman CBE, FRSL (born 19 October 1946) is an English novelist.  He is the author of several best-selling books, most notably the fantasy trilogy "His Dark Materials" and the fictionalised biography of Jesus, "The Good Man Jesus and the Scoundrel Christ".  In 2008, "The Times" named Pullman one of the "50 greatest British writers since 1945".  In a 2004 poll for the BBC, Pullman was named the eleventh most influential person in British culture.

Jonathan Marcantoni: Jonathan Marcantoni was born on June 6, 1984 in Collegeville, PA.  He is of Puerto Rican and Corsican descent and spent much of his childhood in Puerto Rico.  He is a novelist, screenwriter and editor based out of San Antonio, Texas.  He is a co-founder and Managing Editor in Chief of Aignos, an independent, royalty publisher that seeks out experimental and innovative fiction and nonfiction.  He has two novels published, both with Savant Books and Publications, Communion (with Jean Blasiar), and Traveler's Rest.  His work is a mix of stream of consciousness, existentialism, surrealism, and ellipsism.  He blends film and theatrical techniques with his narratives, making the environmental and intellectual musings of his characters as essential to the story as the action and dialogue.

David Fickling: David Fickling is an English children's book editor and publisher based in Oxford.  Fickling runs David Fickling Books, which became an independent publishing house in July 2013.  He has published books by authors including Philip Pullman, Mark Haddon, John Boyne and Linda Newbery.

Question: Which English novelist authored books published by a children's book editor based in Oxford?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "novelist_name": {
      "type": "string",
      "description": "The name of the English novelist."
    },
    "novelist_nationality": {
      "type": "string",
      "description": "The nationality of the novelist."
    },
    "editor_details": {
      "type": "object",
      "properties": {
        "editor_name": {
          "type": "string",
          "description": "The name of the children's book editor."
        },
        "editor_location": {
          "type": "string",
          "description": "The city where the editor is based."
        },
        "editor_specialty": {
          "type": "string",
          "description": "The type of books the editor works with."
        }
      },
      "required": [
        "editor_name",
        "editor_location",
        "editor_specialty"
      ],
      "additionalProperties": false
    },
    "published_by_editor": {
      "type": "boolean",
      "description": "Indicates if the novelist's books were published by the specified editor."
    }
  },
  "required": [
    "novelist_name",
    "novelist_nationality",
    "editor_details",
    "published_by_editor"
  ],
  "additionalProperties": false
}
