{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoe R. Lansdale: Joe Richard Lansdale (born October 28, 1951) is an American writer, author, martial arts expert, and martial arts instructor.\n\nBleeding Shadows: Bleeding Shadows is a short story collection by American author Joe R. Lansdale.  It was published by Subterranean Press on 28 November 2013.  This volume contains 30 short stories that span Mr. Lansdale's extensive career.  This book is the largest collection of Mr. Lansdale's short stories available to date.\n\nAtomic Chili: \"Atomic Chili: The Illustrated Joe R. Lansdale\" by Lansdale et al., (Klaw, ed.)  (Mojo Press, 1998) is a collection of previously written stories by Joe R. Lansdale, adapted into comic book form by assorted artists and writers.  The book was designed by John Picacio, and featured a cover by Dave Dorman.\n\nLost Lansdale Series: The Lost Lansdale Series is a series of four books by Joe R. Lansdale.  None of the books in the Lost Lansdale series will ever be re-issued in any form including paperback.  All have long since sold out.\n\nVeil's Visit: a Taste of Hap and Leonard: Veil's Visit: a Taste of Hap and Leonard is a collection of stories and excerpts by American author Joe R. Lansdale featuring his longtime protagonists Hap Collins and Leonard Pine.  The eponymous first story was co-written by longtime Lansdale friend Andrew Vachss and ends with Lansdale \"interviewing\" his two heroes.  This book was published by Subterranean Press as a limited edition hardcover and trade paperback and is long out of print.\n\nHigh Cotton: Selected Stories of Joe R. Lansdale: High Cotton is a collection of short fiction by Joe R. Lansdale, initially published in 2000.  In his introduction, Lansdale cites it as the \"Best of Lansdale\", and has called this work a companion piece to the 2004 collection \"Bumper Crop\".  Initially issued as a hardcover, it has been reissued as a trade paperback.\n\nMiracles Ain't What They Used To Be: Miracles Ain't What They Used To Be Plus... is a 2016 collection of memoirs and essays by American author Joe R. Lansdale.  It includes Lansdale's essays on how he came to be an author, and on his inspirations, personal beliefs, ideas for the vast amount of published work he has done over his 40 years of writing novels, short stories, novellas, and comic books.  This book shows a never before insight into his long career.  This is the first book in which Lansdale discusses his ideas and personal beliefs that influence his storytelling which has spanned 40 years and has included over 40 novels and almost as many short story collections.  It is a rare glimpse into the mind that has entertained so many readers over the years.  His work has been adapted to several films and most recently into a series on The Sundance Channel with his first bringing of longtime protagonist Hap and Leonard to television.  Season 2 is now filming.\n\nHell's Bounty: Hell's Bounty is a horror novel written by American brothers Joe R. Lansdale and John L. Lansdale.  It takes place in the old western town of Falling Rock.  Bounty hunter Smith(no first name given) sets off a chain of events as he searches for one bad hombre Quill.  He is blown to hell, literally, where he makes a deal with a bartender Snappy, who is really Satan.  He will save Smith from the bowels of hell if he returns to Falling Rock and stops Quill who has made a deal with the \"Old Ones\" who are so evil even Satan can't abide.  Smith teams up with a whip snapping redhead whore named Payday, a legless man called Undertaker, and a whisky drinking doctor to stop Quill who has turned into a winged demon and has turned the people of the town into ghouls to try to stop Smith and his band from ruining his plans.\n\nH. L. Mencken: Henry Louis Mencken (September 12, 1880 – January 29, 1956) was an American journalist, satirist, cultural critic and scholar of American English.  Known as the \"Sage of Baltimore\", he is regarded as one of the most influential American writers and prose stylists of the first half of the twentieth century.  He commented widely on the social scene, literature, music, prominent politicians and contemporary movements.  His satirical reporting on the Scopes trial, which he dubbed the \"Monkey Trial\", also gained him attention.\n\nBy Bizarre Hands: By Bizarre Hands is the first collection of short stories by American writer Joe R. Lansdale, published in 1989.  The collection was nominated for a Bram Stoker Award for best fiction collection, and contains two stories which won Stokers.  It has an introduction by Lewis Shiner.  This book was re-issued as By Bizarre Hands Rides Again in 2010.  The re-issue contains a new introduction by Joe R. Lansdale and new artwork by Alex McVey.  This book is limited to 300 copies and is signed by both writer and artist.  It also contains two stories not in the original issue.\n\nQuestion: H. L. Mencken shares what profession with Joe R. Lansdale?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_a_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person mentioned in the question.\"\n    },\n    \"person_b_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person mentioned in the question.\"\n    },\n    \"shared_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession that both individuals share.\"\n    },\n    \"person_a_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions for the first person.\"\n    },\n    \"person_b_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions for the second person.\"\n    }\n  },\n  \"required\": [\n    \"person_a_name\",\n    \"person_b_name\",\n    \"shared_profession\",\n    \"person_a_professions\",\n    \"person_b_professions\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_a_name": {
        "type": "string",
        "description": "The name of the first person mentioned in the question."
      },
      "person_b_name": {
        "type": "string",
        "description": "The name of the second person mentioned in the question."
      },
      "shared_profession": {
        "type": "string",
        "description": "The profession that both individuals share."
      },
      "person_a_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions for the first person."
      },
      "person_b_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions for the second person."
      }
    },
    "required": [
      "person_a_name",
      "person_b_name",
      "shared_profession",
      "person_a_professions",
      "person_b_professions"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
