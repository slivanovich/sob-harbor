{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n'Til Tuesday: 'Til Tuesday (often written as ’til tuesday) was an American new wave band formed in Boston.  The band, consisting of Aimee Mann (vocals, bass), Robert Holmes (guitar, vocals), Joey Pesce (keyboard), and Michael Hausman (drums), was active from 1982 to 1989.  They are best known for their 1985 hit single \"Voices Carry\".\n\nOne More Drifter in the Snow: One More Drifter in the Snow is the sixth album and first Christmas album by Aimee Mann, released by SuperEgo Records in the United States on October 31, 2006 (see 2006 in music).  It was produced by Paul Bryan and comprises covers of \"standard great Christmas classics\" and two original compositions: \"Christmastime\", written by Mann's husband Michael Penn, and \"Calling on Mary\".  Grant-Lee Phillips sings with her on the track \"You're a Mean One, Mr. Grinch\".\n\nMorgan Murphy (comedian): Morgan Murphy (born October 23, 1981) is an American stand-up comic, comedy writer, and actress.  She has performed in the Comedians of Comedy tour and appeared in the \"Comedians of Comedy: Live at the Troubador\" DVD.  Bobcat Goldthwait cast her in the films \"Sleeping Dogs Lie\" and \"World's Greatest Dad\".  She has also been a featured performer for all three years of Aimee Mann's \"Christmas Spectacular\" tours and appeared in the video for Mann's song \"31 Today\".  Morgan has made numerous appearances on \"Jimmy Kimmel Live! \", for which she also worked as a writer.\n\nMichael Penn: Michael Penn (born August 1, 1958) is an American singer, songwriter, and composer.  He is noted for the 1989 single \"No Myth\", a top 20 hit in the US and successful in several other countries.\n\nUnited Musicians: United Musicians is an independent music collective founded by Aimee Mann, Michael Penn and Michael Hausman.  According to UM's Web site, it is \"founded on the principle that every artist should be able to retain copyright ownership of the work he or she has created and that this ownership is the basis for artistic strength and true independence.\"\n\nBachelor No. 2 or, the Last Remains of the Dodo: Bachelor No. 2 or, the Last Remains of the Dodo (also shortened to Bachelor No. 2) is the third studio album by American singer-songwriter Aimee Mann, released on May 2, 2000.  The album is notable for the fact that Mann was initially without a record company and sold the album through her website, but the album went on to gain a worldwide release and achieve respectable sales.  This was aided by the success of the \"Magnolia\" soundtrack, for the film of the same name by Paul Thomas Anderson, with which the album shares material.\n\nMental Illness (album): Mental Illness is the ninth studio album by singer-songwriter Aimee Mann.  It was released on March 31, 2017, by SuperEgo Records.  Mann has described it as her \"saddest, slowest and most acoustic\" album to date.\n\nSuperEgo Records: SuperEgo Records is a record label co-founded by Aimee Mann and her manager Michael Hausman in 1999, after Mann negotiated a release from her contract with Geffen Records.  Mann has released all of her solo albums since 1999 on SuperEgo.  The first of these albums was \"Bachelor No. 2 or, the Last Remains of the Dodo\", which she released in 2000 after buying back the rights to its music from Interscope Records.\n\nVoices Carry: \"Voices Carry\" is a song by the American rock band 'Til Tuesday.  It was produced by Mike Thorne for the band's debut studio album, \"Voices Carry\" (1985).  The song's lyrics, written by the band's frontwoman Aimee Mann, portray a lover in an affair, and were originally written and sung as if to a woman, but changed due to Epic Records' pressure.  The song was inspired by Mann's breakup with 'Til Tuesday drummer, Michael Hausman.\n\nJonathan Norton: Jonathan Hayes \"Butch\" Norton (born March 21, 1958) is an American drummer, percussionist and vocalist, best known for his work with the Los Angeles-based indie rock band Eels between 1996 and 2003.  Since his departure from the group, he has gone on to work with notable musicians like Fiona Apple, Tracy Chapman, Lisa Germano, Aimee Mann, Michael Miller, Michael Penn, Rufus Wainwright, and Lucinda Williams.\n\nQuestion: What is the nationality of the singer who cofounded United Musicians with Aimee Mann and Michael Hausman?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"cofounder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-founder in question.\"\n    },\n    \"cofounder_role\": {\n      \"type\": \"string\",\n      \"description\": \"The primary role of the co-founder mentioned in the context.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the co-founder.\"\n    },\n    \"organization_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the organization co-founded.\"\n    }\n  },\n  \"required\": [\n    \"cofounder_name\",\n    \"cofounder_role\",\n    \"nationality\",\n    \"organization_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "cofounder_name": {
        "type": "string",
        "description": "The name of the co-founder in question."
      },
      "cofounder_role": {
        "type": "string",
        "description": "The primary role of the co-founder mentioned in the context."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the co-founder."
      },
      "organization_name": {
        "type": "string",
        "description": "The name of the organization co-founded."
      }
    },
    "required": [
      "cofounder_name",
      "cofounder_role",
      "nationality",
      "organization_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
