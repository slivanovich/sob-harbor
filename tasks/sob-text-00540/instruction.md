{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShady Lady (Ani Lorak song): \"Shady Lady\" was the Ukrainian entry for the 2008 Eurovision Song Contest.  It was sung by Ani Lorak, composed by Philipp Kirkorov and written by Karen Kavaleryan.  However, in Greece, around the time of the Contest, there were many rumors stating that popular composer Dimitris Kontopoulos had actually composed the song.  Although his name was not credited during the Eurovision Song Contest performances, it was later confirmed that Kontopoulos was indeed a producer of the song.\n\nPhilipp Kirkorov: Philipp Bedrosovich Kirkorov PAR (Russian: Фили́пп Бедро́сович Кирко́ров ; Bulgarian: Филип Бедросов Киркоров , born 30 April 1967) is a Russian pop singer of Bulgarian origin, five-time received the World Music Awards award as the \"World's Best Selling Russian Artist\".\n\nKids Jury in the Junior Eurovision Song Contest: The use of a Kids' Jury in the Junior Eurovision Song Contest was first introduced at the Junior Eurovision Song Contest 2012, in Amsterdam, Netherlands, as part of a new voting system for the Junior Eurovision Song Contest following discussions between the European Broadcasting Union (EBU), KidsRights Foundation, and the Junior Eurovision Song Contest 2012 host broadcaster Algemene Vereniging Radio Omroep (AVRO).  Three of the four spokespersons who announced the jury points at each annual contest were former winners of the Junior Eurovision Song Contest.  As of 2016, the results of each country's Kids' Jury have been integrated with the adult jury to give out two sets of 1-8, 10, and 12 points per country.\n\nUkraine in the Eurovision Song Contest 2017: Ukraine participated in the Eurovision Song Contest 2017.  In addition to participating in the contest, the Ukrainian broadcaster National Television Company of Ukraine (NTU) also hosted the Eurovision Song Contest at the International Exhibition Centre in Kiev after winning the competition in 2016 with the song \"1944\" performed by Jamala.  The Ukrainian entry for the 2017 contest was selected through a national final, which NTU organised in collaboration with the commercial broadcaster STB.\n\nPortugal in the Junior Eurovision Song Contest: The participation of Portugal in the Junior Eurovision Song Contest first began at the Junior Eurovision Song Contest in 2006 which took place in Bucharest, Romania.  Rádio e Televisão de Portugal (RTP), a member of the European Broadcasting Union (EBU), were responsible for the selection process of their participation.  Portugal used a national selection format, broadcasting a show entitled \"\"Festival da Canção Junior\"\", for their participation at the contests.  This was a junior version of Festival da Canção, the national music competition organised by broadcaster RTP to choose the Portuguese entry for the Eurovision Song Contest.  The first representative to participate for the nation at the 2006 contest was Pedro Madeira with the song \"Deixa-me sentir\", which finished in second-last place out of fifteen participating entries, achieving a score of twenty-two points.  Portugal withdrew from competing in the Junior Eurovision Song Contest in 2008, and will return for the Junior Eurovision Song Contest 2017 in Tbilisi, Georgia.\n\nAnri Jokhadze: Anri Jokhadze (Georgian: ანრი ჯოხაძე ; born 6 November 1980) is a Georgian pop singer from Tbilisi who represented Georgia in the Eurovision Song Contest 2012 with the song \"I'm a Joker\".  The singer is a winner and laureate of 13 international contests.  Prior to his appearance at the Eurovision Song Contest 2012, Anri Jokhadze has also represented Georgia in the Eurovision Song Contest 2008 as a backing vocalist for Diana Gurtskaya and her song \"Peace Will Come.\"  Besides, he is the composer of the Georgian entry at the Eurovision Song Contest 2017, \"Keep the Faith\" sung by Tamara Gachechiladze.\n\nUkraine in the Eurovision Song Contest 2014: Ukraine participated in the Eurovision Song Contest 2014 in Copenhagen, Denmark.  The Ukrainian entry was selected through a national final, organised by Ukrainian broadcaster National Television Company of Ukraine (NTU).  Mariya Yaremchuk performed the Ukrainian entry \"Tick-Tock\", which she co-wrote with Sandra Bjurman.  The song qualified from the first semi-final and placed 6th in the final, scoring 113 points.\n\nSweet People: \"Sweet People\" is a song by Ukrainian singer Alyosha.  It was the Ukrainian entry for the Eurovision Song Contest 2010 in Oslo, Norway.  At first, a song performed by Vasyl Lazarovich was intended to represent Ukraine at Eurovision, but a new national final was held due to the broadcasting network's internal selection of Lazarovich.  Alyosha won the new final with \"To Be Free\", but it was disqualified since it had previously been released.  \"Sweet People\"was then chosen to represent Ukraine.  The song finished tenth in the Eurovision final, receiving 108 points.\n\nBelieve (Dima Bilan song): \"Believe\" is the winning Russian entry for the 2008 Eurovision Song Contest sung by Dima Bilan.  The song was composed and written by Jim Beanz (a.k.a. James Washington) & Dima Bilan.  On 20 May 2008 Bilan sang in the first semi-final of the Eurovision Song Contest, and the song was voted into the final by public vote.  It was performed 24th out of 25 songs in the final on 24 May 2008.\n\nJunior Eurovision Song Contest 2013: The Junior Eurovision Song Contest 2013 was the 11th annual Junior Eurovision Song Contest.  It took place in Kiev, Ukraine on 30 November 2013.  The venue for the contest was announced on 10 April 2013, as the Palace \"Ukraine\".  Ukrainian broadcaster National Television Company of Ukraine (NTU) was the host broadcaster for the event.  It was the second time the contest was held in Kiev, the first being the 2009 contest .  It was also the second time in the history of the Junior Eurovision Song Contest that the event took place in last year's winning country, as well as the first time that the event was held in the same city twice.  A total of twelve countries participated, with Macedonia and Malta making a return, and Albania , Belgium and Israel choosing to withdraw.  San Marino made their debut in the contest.  Cyprus was originally the thirteenth country to take part but pulled out the last minute.\n\nQuestion: What is the nationality of the composer of the Ukrainian entry for the 2008 Eurovision Song Contest?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song that was the Ukrainian entry.\"\n    },\n    \"contest_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year of the Eurovision Song Contest.\"\n    },\n    \"country_entry\": {\n      \"type\": \"string\",\n      \"description\": \"The country that entered the song.\"\n    },\n    \"composer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the composer.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the composer.\"\n        },\n        \"origin\": {\n          \"type\": \"string\",\n          \"description\": \"The origin of the composer, if different from nationality.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"contest_year\",\n    \"country_entry\",\n    \"composer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song that was the Ukrainian entry."
      },
      "contest_year": {
        "type": "integer",
        "description": "The year of the Eurovision Song Contest."
      },
      "country_entry": {
        "type": "string",
        "description": "The country that entered the song."
      },
      "composer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the composer."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the composer."
          },
          "origin": {
            "type": "string",
            "description": "The origin of the composer, if different from nationality."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_title",
      "contest_year",
      "country_entry",
      "composer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
