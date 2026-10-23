{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nL.V. (singer): Larry Sanders (born November 21, 1960 ), better known by his stage name L.V. (which stands for \"Large Variety\"), is an American award-winning R&B singer.  He is best known for his collaboration with rapper Coolio on the Grammy Award-winning single, \"Gangsta's Paradise\", and has been featured on multiple soundtracks since then.  Having released two solo albums to date, he was also a member of the gangsta rap group South Central Cartel since their beginning, usually singing the vocals and chorus.\n\nRather Be: \"Rather Be\" is a song by the English electronic music group Clean Bandit.  It features vocals by Jess Glynne.  The track was released on 17 January 2014 as the fourth single from the group's debut studio album, \"New Eyes\" (2014).  It was co-written by band members Jack Patterson and Grace Chatto, along with Jimmy Napes and Nicole Marshall, and produced by Patterson and Chatto.  Warner Music Group released a number of official remixes for download, with DJs such as All About She, Cash Cash, and OVERWERK.\n\nTears (Clean Bandit song): \"Tears\" is a song by English electronic group Clean Bandit, featuring English singer Louisa Johnson.  It was released on 27 May 2016.  It is the last single to feature Neil Amin-Smith as violinist after his departure.  Clean Bandit and Johnson performed the song with 5 After Midnight during the finals of \"The X Factor\" on 10 December 2016.\n\nAaron A. Brooks: Aaron A. Brooks, also known as, Aaron Kinsley-Brooks (born January 24, 1964, San Francisco, California) is an American rock musician, drummer, producer and composer.  He co-founded The Little Death with Moby, Laura Dawn and Daron Murphy.  He is a founding member of the American alternative rock band, The Mars Bonfire.  Aaron also plays or has played drums for the electronic pop band Leisure Cruise; Grammy nominated electro-pop chanteuse Angela McCluskey (of Télépopmusik and Wild Colonials); Grammy award-winning producer/songwriter Mark Hudson; Emmy award-winning actress and singer Jackie Cruz; Grammy award-winning artist Moby; Singer/songwriter and progressive political activist Laura Dawn; Grammy award-winning bassist/songwriter and rock musician Duff McKagen of Guns N' Roses; Circle of Soul; Erin Evermore; Grammy award-winning pianist and songwriter A.J. Croce; Grammy winning singer/songwriter Lana Del Ray; Writer, radio host, progressive political comic and guitarist/singer Jamie Kilstein and his band The Agenda; Model/actress/singer/songwriter Heidi Merrill; And NY based rock singer Carleigh Jade.\n\nClean Bandit discography: English electronic music group Clean Bandit have released one studio album, three extended plays, seven singles (including one as a featured artist) and eleven music videos.  In December 2012, the group released their debut single \"A+E\", which peaked at number 100 on the UK Singles Chart.  The song is the lead single from their debut album, \"New Eyes\", which was released in May 2014.  The album's second single, \"Mozart's House\", charted at number seventeen on the UK Singles Chart, becoming Clean Bandit's first top twenty single on the chart. \" Dust Clears\" was released as the third single from the album, reaching number forty-three on the UK chart.  The album's fourth single, \"Rather Be\", features Jess Glynne and topped the UK Singles Chart, the group's first number one on the chart.  Their 2016 single \"Rockabye\", which features rapper Sean Paul and singer Anne-Marie, became their second number-one hit in the UK, becoming the Christmas number one single for 2016 in its seventh consecutive week at number-one.  The follow-up to \"Rockabye\", \"Symphony\", featured Zara Larsson and became their third UK number one single.\n\nStronger (Clean Bandit song): \"Stronger\" is a song by English electronic group Clean Bandit featuring uncredited vocals by Alex Newell and Sean Bass, brother of Sharna Bass (who sings the vocals of Clean Bandit's hit \"Extraordinary\").  It was originally released on 22 November 2014, featuring uncredited vocals from Olly Alexander, the lead singer of Years & Years.  The song has since been re-recorded and was released as a single on 19 April 2015.  It was also remixed by American electronic duo Vindata.\n\nSymphony (Clean Bandit song): \"Symphony\" is a song by British classical crossover band Clean Bandit featuring Swedish singer Zara Larsson.  It is taken as the third single from their upcoming second album.  The song was also released as the sixth single from Larsson's second studio album, \"So Good\" (2017).  The song is the final track on the album.  The song peaked at number one on the Swedish singles chart, becoming Larsson's fifth number one in her home country.  It has also reached number one in Norway and the United Kingdom, becoming Larsson's first number one single in the latter country, as well as Clean Bandit's third number one in the UK.\n\nSharna Bass: Sharna Bass (born 21 May 1997) is a singer from North West London.  She is featured on the Clean Bandit single \"Extraordinary\".  Bass also has a twin brother, Sean Bass, in the industry who was also spotted by Clean Bandit and sings the vocals in their song Stronger.\n\nForgot About Dre: \"Forgot About Dre\" is a Grammy Award-winning single from rapper Dr. Dre's \"2001\", featuring vocals from rapper Eminem.  The track reached No. 25 on the \"Billboard\" Hot 100, No. 14 on the U.S. R&B chart, No. 32 on the U.S. Pop chart, and No. 7 on the UK Singles Chart.  Released as the album's second single on January 29, 2000, like \"Still D.R.E.\", the song addresses Dre's critics in a defiant manner, as Dre announces his return to the hip-hop scene and reminds listeners of his significant influence on the genre.  \"Forgot About Dre\" won Best Rap Performance by a Duo or Group at the 2001 Grammy Awards.\n\nJess Glynne: Jessica Hannah \"Jess\" Glynne (born 20 October 1989) is an English singer and songwriter, signed to Atlantic Records.  She rose to prominence as a featured artist on Clean Bandit's Grammy Award-winning single \"Rather Be\" and Route 94's \"My Love\", both of which reached number one on the UK Singles Chart in 2014.  Her debut solo single, \"Right Here\", reached the top ten the same year.\n\nQuestion: Who produced Clean Bandit's Grammy Award-winning single ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the Grammy Award-winning single by Clean Bandit.\"\n    },\n    \"award_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the award won by the single.\"\n    },\n    \"producers\": {\n      \"type\": \"array\",\n      \"description\": \"A list of individuals who produced the song.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"producer_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the producer.\"\n          }\n        },\n        \"required\": [\n          \"producer_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"award_name\",\n    \"producers\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the Grammy Award-winning single by Clean Bandit."
      },
      "award_name": {
        "type": "string",
        "description": "The name of the award won by the single."
      },
      "producers": {
        "type": "array",
        "description": "A list of individuals who produced the song.",
        "items": {
          "type": "object",
          "properties": {
            "producer_name": {
              "type": "string",
              "description": "The name of the producer."
            }
          },
          "required": [
            "producer_name"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "song_title",
      "award_name",
      "producers"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
