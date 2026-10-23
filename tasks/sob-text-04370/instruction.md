{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBlacksmith (song): \"Blacksmith\" (Roud 816) is a traditional English folk song, also known as \"A Blacksmith Courted Me\".  The song was noted down by Ralph Vaughan Williams in 1909 from a Mrs Ellen Powell of Westhope near Weobley, Herefordshire.  On that occasion it was sung to the tune \"Monk's Gate\", better known as the tune of \"To be a pilgrim\", the hymn by John Bunyan.  The same tune is sometimes used for the song \"Our Captain Cried\".  There is a setting by George Butterworth (a friend of Vaughan Williams and Cecil Sharp) in his 1912 collection \"Folk Songs from Sussex\" (recorded by Roderick Williams and Iain Burnside in the Naxos English Song Series 8.572426).\n\nPossessed by Paul James: Konrad Wert, known as Possessed by Paul James since 2005, (born July 26, 1976), is an American folk singer, songwriter and musician from Lee County, Florida.  His music is composed of string instruments including banjo, guitar and fiddle with written roots within folk, blues and punk.  Raised within a small Mennonite Community among pacifists, service workers and transplants.  He graduated from Eastern Mennonite University in 2001 with a degree in liberal arts with various minors.  He is currently living in Boerne, Texas with his wife and sons meeting the music demand by touring, sales on line etc.  He is also a special education teacher at Curington Elementary School in Boerne, Texas.  Possessed by Paul James has starred in \"The Folk Singer\", a film by Slowboat Films in 2008 while in circulation internationally.\n\nOld Brown's Daughter: Old Brown's Daughter (Roud 1426) was an English music hall song, sung by Alfred Vance, and became a Newfoundland folk song.  It was written by G. W. Hunt (1839–1904), circa 1878, although it is often wrongly credited to Johnny Burke (1851–1930).  It was in the repertoire of English folk singer Walter Pardon on his 1975 album, A Proper Sort.  Peter Bellamy also sang a version of Old Brown's Daughter  on his 1975 self-titled album.  In 1991, Damien Barber recorded the song for Fellside Records and it was released on the compilation Voices in 1992.  The melody was rewritten by Newfoundland singer/songwriter Ron Hynes and Hynes' version was covered by Great Big Sea on their 1999 album, \"Turn\".\n\nThe Manchester Rambler: \"The Manchester Rambler\", also known as \"I'm a Rambler\" and \"The Rambler's Song\", is a song written by the English folk singer Ewan MacColl.  It was inspired by his participation in the Kinder trespass, a protest by the urban Young Communist League of Manchester, and was the work that began MacColl's career as a singer-songwriter.\n\nThe World of Carl Sandburg: The World of Carl Sandburg was a stage presentation of selections from the poetry and prose of Carl Sandburg, chosen and arranged by Norman Corwin, starring Bette Davis.  There was a 21-week national tour 1959–1960, co-starring Davis's husband Gary Merrill, towards the end, he was replaced by Barry Sullivan.  Afterwards, there was a one-month run at the Henry Miller Theatre in the fall of 1960, co-starring Leif Erickson.  Guitar accompaniment and singing was provided by the folk singer Clark Allen.\n\nThe Maid Freed from the Gallows: \"The Maid Freed from the Gallows\" is one of many titles of a centuries-old folk song about a condemned maiden pleading for someone to buy her freedom from the executioner.  In the collection of ballads compiled by Francis James Child in the late 19th century, it is indexed as Child Ballad number 95; 11 variants, some fragmentary, are indexed as 95A to 95K.  In the Roud Folk Song Index it is number 144.  The ballad exists in a number of folkloric variants, from many different countries, and has been remade in a variety of formats.  For example, it was recorded in 1939 as \"The Gallis Pole\" by folk singer Huddie \"Lead Belly\" Ledbetter, and - the most famous version - in 1970 as \"Gallows Pole\", an arrangement of the Fred Gerlach version by English rock band Led Zeppelin, on the album \"Led Zeppelin III\".\n\nRapperiya Baalam: Ashok Manda Bishnoi, better known by his stage name Rapperiya Baalam, is a Jaipur, Rajasthan based Rapper, Song writer, Music Composer and Producer.  He Rose to fame in 2014 with his song “Mharo Rajasthan”, a Folk hip hop fusion song which become one of the most popular song in Rajasthan and gained amazing popularity among the youth, the Song co-written by Kunaal Vermaa Featuring Indian Idol Fame Folk Singer Swaroop Khan.  His other hits are “Hariyala Banna”, “Jaipur Anthem”,“Des Padharo Sa”, “Dil Mere”.  He along with lyrics writer kunaal Vermaa has worked with bollywood playback singer Ravindra Upadhyay for song “Des Padharo Sa”,and with musician Mohit Gaur for Song “phir mujhe dil se pukaar tu”.  Better known for his experiments in rajasthani folk music Rapperiya Baalam and his team came up with Hariyala Banna in 2016, the song earned 3 million hits in three months and become one of the most popular folk fusion song in regional category.  Hariyala Banna sung by Bollywood playback Singer Ravindra Upadhyay and Kamal Choudhary.\n\nEwan MacColl: James Henry Miller (25 January 1915 – 22 October 1989), better known by his stage name Ewan MacColl, was an English folk singer, songwriter, communist, labour activist, actor, poet, playwright and record producer.\n\nJim Moray: Jim Moray (born 1981) is an English folk singer, multi-instrumentalist and record producer.\n\nThe Shoals of Herring: The Shoals of Herring (Roud 13642) is a ballad, written by Ewan MacColl for the third of the original eight BBC \"Radio ballads\" \"Singing the Fishing,\" which was first broadcast on August 16, 1960.\n\nQuestion: The Shoals of Herring (Roud 13642) is a ballad, written by James Henry Miller, was an English folk singer, songwriter, communist, labour activist, actor, poet, playwright and record producer, and better known by which stage name ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_real_name\": {\n      \"type\": \"string\",\n      \"description\": \"The real name of the individual.\"\n    },\n    \"person_stage_name\": {\n      \"type\": \"string\",\n      \"description\": \"The stage name by which the individual is better known.\"\n    },\n    \"person_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the person.\"\n    },\n    \"person_primary_roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of primary roles or professions of the person.\"\n    },\n    \"song_written\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song written by the person.\"\n    }\n  },\n  \"required\": [\n    \"person_real_name\",\n    \"person_stage_name\",\n    \"person_nationality\",\n    \"person_primary_roles\",\n    \"song_written\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_real_name": {
        "type": "string",
        "description": "The real name of the individual."
      },
      "person_stage_name": {
        "type": "string",
        "description": "The stage name by which the individual is better known."
      },
      "person_nationality": {
        "type": "string",
        "description": "The nationality of the person."
      },
      "person_primary_roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of primary roles or professions of the person."
      },
      "song_written": {
        "type": "string",
        "description": "The title of the song written by the person."
      }
    },
    "required": [
      "person_real_name",
      "person_stage_name",
      "person_nationality",
      "person_primary_roles",
      "song_written"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
