{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMaps (Yeah Yeah Yeahs song): \"Maps\" is a single by Yeah Yeah Yeahs from their debut full-length album, \"Fever to Tell\" (2003).  The song is about the relationship between Liars frontman Angus Andrew and Yeah Yeah Yeahs lead singer Karen O.  It was released on February 10, 2004, and the band performed the song at that year's MTV Movie Awards.  The music video received much play on MTV.  It reached #9 on \"Billboard\"' s Alternative Songs chart and was included in the popular video game \"Rock Band\".\n\nGold Lion: \"Gold Lion\" is the first single by the Yeah Yeah Yeahs from their second album, \"Show Your Bones\".  Distinct in the Yeah Yeah Yeahs' discography, it features acoustic guitar and a more slowed-down pace in contrast to former works like \"Bang! \" and \"Date with the Night.\"  It was released on March 21, 2006, and became the band's second major hit after 2004's \"Maps.\"\n\nAlan Moulder: Alan Moulder is an English record producer, mixing engineer and audio engineer.  He has worked with such artists as Nine Inch Nails, Foo Fighters, The Killers, Gary Numan, Foals, Arctic Monkeys, Editors, Interpol, Two Door Cinema Club, Twin Atlantic, Bear Hands, The Joy Formidable, Slaves, Royal Blood, The Naked And Famous, The Jesus and Mary Chain, Curve, Ride, White Lies, My Bloody Valentine, , The Vaccines, Placebo, A Perfect Circle, Lush, The Smashing Pumpkins, Them Crooked Vultures, Death Cab for Cutie, Yeah Yeah Yeahs, Puscifer, Marilyn Manson, Saul Williams, Blonde Redhead, The Morning After Girls, How to Destroy Angels, .\n\nYeah Yeah Yeahs (EP): Yeah Yeah Yeahs is the debut EP by American indie rock band Yeah Yeah Yeahs, released in 2001 by the band's own label, \"Shifty\".  It is sometimes incorrectly called \"Master\" due to the prominence of a necklace bearing that word on the album's cover.  It reached number 1 on the UK Indie Chart.  As of 2009, sales in the United States have exceeded 71,000 copies, according to Nielsen SoundScan .  The EP was named \"NME\"' s second best single of 2002.\n\nLook to the Sky: Look to the Sky is the second solo album of James Iha, former member of The Smashing Pumpkins.  It was released on 14 March 2012 in Japan, with a worldwide release in September 2012.  The album has many collaborations, including Karen O and Nick Zinner (Yeah Yeah Yeahs), Sara Quin (Tegan and Sara), Nathan Larson (Shudder To Think), Nina Persson (The Cardigans), Tom Verlaine (Television) and Mike Garson.\n\nDate with the Night: \"Date with the Night\" is the first single from \"Fever to Tell\" by the Yeah Yeah Yeahs.  This single also includes the B-side \"Yeah!  New York\" which can also be found as a bonus track on the UK release of \"Fever to Tell\", and an exclusive remix of \"Bang\" from their debut EP, \"Yeah Yeah Yeahs\" (2001).  The single peaked at number sixteen on the UK's official charts.  The video, directed by Patrick Daughters, was, supposedly, shot at Bristol University Union's Anson Rooms on Saturday 1 March 2003 but also contains scenes shot at other venues during the same tour, including The Zodiac in Oxford.  The song is also available as a downloadable track for the music video game series \"Rock Band\".  The song was also featured on the soundtrack for the British teen soap opera Skins.\n\nYeah Yeah Yeahs: Yeah Yeah Yeahs is an American indie rock band formed in New York City in 2000.  The group is composed of vocalist and pianist Karen O, guitarist and keyboardist Nick Zinner, and drummer Brian Chase.  They are complemented in live performances by second guitarist David Pajo, who joined as a touring member in 2009 and replaced Imaad Wasif who had previously held this role.  According to an interview that aired during the ABC network's \"Live from Central Park SummerStage\" series, the band's name was taken from modern New York City vernacular.\n\nWichita Recordings: Wichita Recordings is an independent record label located in London, founded in 2000 by Mark Bowen and Dick Green.  Its most notable signees include Bloc Party, The Cribs, Clap Your Hands Say Yeah, Bright Eyes, My Morning Jacket, Yeah Yeah Yeahs, Best Coast, Los Campesinos!  and Peter Bjorn and John.  The label signed Clap Your Hands Say Yeah for a UK distribution deal for the group's debut album.  They also signed the UK producers Simian Mobile Disco for the UK.\n\nITunes Originals – Yeah Yeah Yeahs: iTunes Originals – Yeah Yeah Yeahs is a compilation album by American indie rock band Yeah Yeah Yeahs, released exclusively through the iTunes Store on October 20, 2009 as part of the iTunes Originals series.  The album consists of both acoustic versions and original studio recordings of the band's songs, as well as interview tracks.\n\nThe Smashing Pumpkins: The Smashing Pumpkins are an American alternative rock band from Chicago, Illinois, formed in 1988.  Formed by frontman Billy Corgan (lead vocals, guitar) and James Iha (guitar), the band included D'arcy Wretzky (bass guitar) and Jimmy Chamberlin (drums) in its original incarnation.  It has undergone many line-up changes over the course of its existence, with the current lineup being Corgan and rhythm guitarist Jeff Schroeder.\n\nQuestion: Which band, The Smashing Pumpkins or Yeah Yeah Yeahs, is from Chicago?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_from_chicago\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that is from Chicago.\"\n    },\n    \"chicago_band_origin_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city of origin for the band from Chicago.\"\n    },\n    \"other_band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other band mentioned in the question.\"\n    },\n    \"other_band_origin_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city of origin for the other band.\"\n    },\n    \"question_context\": {\n      \"type\": \"string\",\n      \"description\": \"The original question asked.\"\n    }\n  },\n  \"required\": [\n    \"band_from_chicago\",\n    \"chicago_band_origin_city\",\n    \"other_band_name\",\n    \"other_band_origin_city\",\n    \"question_context\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_from_chicago": {
        "type": "string",
        "description": "The name of the band that is from Chicago."
      },
      "chicago_band_origin_city": {
        "type": "string",
        "description": "The city of origin for the band from Chicago."
      },
      "other_band_name": {
        "type": "string",
        "description": "The name of the other band mentioned in the question."
      },
      "other_band_origin_city": {
        "type": "string",
        "description": "The city of origin for the other band."
      },
      "question_context": {
        "type": "string",
        "description": "The original question asked."
      }
    },
    "required": [
      "band_from_chicago",
      "chicago_band_origin_city",
      "other_band_name",
      "other_band_origin_city",
      "question_context"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
