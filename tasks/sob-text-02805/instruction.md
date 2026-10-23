{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJimmy McCulloch: James McCulloch (4 June 1953 – 27 September 1979) was a Scottish musician and songwriter best known for playing lead guitar and bass, as a member of Paul McCartney's band Wings from 1974 to 1977.  McCulloch was a member of the Glasgow psychedelic band One in a Million (formerly known as the Jaygars), Thunderclap Newman, and Stone the Crows.  He also made appearances on many albums, including John Entwistle's \"Whistle Rymes\" in 1972, as lead guitarist playing alongside Peter Frampton on \"Apron Strings\" and \"I Feel Better\"; and on Roy Harper's album, \"Bullinamingvase\", and Ricci Martin's album, \"Bleached\", both in 1977.  McCulloch also played guitar on Roger Daltrey's album \"One of the Boys\" which was released in 1977.  McCulloch was a friend of the Who and a member of the band Thunderclap Newman, which was created and produced by his mentor Pete Townshend.  At age 11, he was also a protégé of the Shadows' Hank Marvin.  His brother is drummer Jack McCulloch.\n\nAndrew Stockdale: Andrew James Stockdale (born 20 July 1976) is an Australian rock musician, singer and songwriter best known as the lead vocalist, lead guitarist and only mainstay member of the rock band Wolfmother, which formed in 2000.  In 2007, alongside his Wolfmother bandmates, he won 'Songwriter of the Year' at the APRA Awards.  Aside from his work with Wolfmother, Stockdale was featured on the 2010 single \"By the Sword\" by Slash.\n\nRyan Ross: George Ryan Ross III (born August 30, 1986) is an American musician, singer, and songwriter best known for his work as the lead guitarist and primary songwriter of the band Panic!  at the Disco before his departure in 2009.  Ross and former Panic bassist Jon Walker are the founding members of the band The Young Veins, in which Ross is the lead vocalist.\n\nEric Friedman: Eric Charles \"Erock\" Friedman (born June 28, 1984) is an American musician and songwriter, best known as the current touring guitarist and backing vocalist for Creed, as well as Tremonti, which is fronted by Alter Bridge and Creed lead guitarist Mark Tremonti.  He played with the band on their 2009 United States reunion tour with Staind and their 2010 Tour with Skillet.  He is the former lead guitarist for the band Submersed and also the former lead guitarist for Daughters of Mara.  Submersed and Daughters of Mara both disbanded in 2008.  He also currently plays lead guitar and co writes for the rock band Hemme.  At the age of thirteen Friedman was the youngest guitarist at the time to be fully endorsed by Fender.  His first introduction to Mark Tremonti was at a NAMM show where his then manager introduced them both.  They subsequently jammed at one of the Rivera amp booths and noticed, that although they had different styles, (Tremonti being heavily influenced by metal and Friedman Blues), they both complemented each other.\n\nHank Marvin: Hank Brian Marvin (born Brian Robson Rankin, 28 October 1941) is an English multi-instrumentalist, vocalist and songwriter.  He is best known as the lead guitarist for the Shadows, a group which primarily performed instrumentals and was the backing band for Cliff Richard and subsequently for Marvin, Welch & Farrar.  Many leading British and Canadian rock guitarists cite Marvin as an influence.\n\nLeigh Stephens: Leigh Stephens is an American guitarist and songwriter best known for being former lead guitarist of the San Francisco psychedelic rock group Blue Cheer.\n\nJosh Farro: Joshua Neil \"Josh\" Farro (born September 29, 1987) is an American guitarist, Singer, and songwriter best known as the former lead guitarist and backing vocalist of the rock band Paramore.  He is currently pursuing his solo career, as the lead vocalist and guitarist of his self-named band, Farro.  His debut solo album, \"Walkways\", was released on 5 February 2016 via iTunes.\n\nThe Day I Met Marie: \"The Day I Met Marie\" is a song by Cliff Richard with B-side as \"Our Story Book\".  It was released as a non-album single in 1967 reaching #10 on the UK singles chart and #10 in Ireland.  It also reached #5 in Australia and #4 in New Zealand and #7 in the Netherlands.  The song was written by Hank Marvin and produced by Norrie Paramor.\n\nMick Jones (The Clash guitarist): Michael Geoffrey \"Mick\" Jones (born 26 June 1955) is a British musician, singer and songwriter best known as the lead guitarist, co-lead vocalist, cofounder and songwriter for The Clash until his dismissal in 1983.  Afterwards, he formed the band Big Audio Dynamite with Don Letts.  Jones has recently played with the group Carbon/Silicon along with Tony James and has toured the world as part of the Gorillaz live band.  In late 2011, Jones collaborated with Pete Wylie and members of The Farm to form The Justice Tonight Band.\n\nThe Edge: David Howell Evans (born 8 August 1961), better known by his stage name The Edge (or just Edge), is an English-born Irish musician and songwriter best known as the lead guitarist, keyboardist and backing vocalist of the rock band U2.  A member of the group since its inception, he has recorded 13 studio albums with the band as well as one solo record.  As a guitarist, the Edge has crafted a minimalistic and textural style of playing.  His use of a rhythmic delay effect yields a distinctive ambient, chiming sound that has become a signature of U2's music.\n\nQuestion: \"The Day I Met Marie\" is a song written by an English songwriter best known as the lead guitarist for what band?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song mentioned in the question.\"\n    },\n    \"songwriter_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the songwriter for the specified song.\"\n    },\n    \"songwriter_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the songwriter.\"\n    },\n    \"songwriter_primary_role\": {\n      \"type\": \"string\",\n      \"description\": \"The primary role the songwriter is best known for.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band the songwriter is best known for as lead guitarist.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"songwriter_name\",\n    \"songwriter_nationality\",\n    \"songwriter_primary_role\",\n    \"band_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song mentioned in the question."
      },
      "songwriter_name": {
        "type": "string",
        "description": "The name of the songwriter for the specified song."
      },
      "songwriter_nationality": {
        "type": "string",
        "description": "The nationality of the songwriter."
      },
      "songwriter_primary_role": {
        "type": "string",
        "description": "The primary role the songwriter is best known for."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band the songwriter is best known for as lead guitarist."
      }
    },
    "required": [
      "song_title",
      "songwriter_name",
      "songwriter_nationality",
      "songwriter_primary_role",
      "band_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
