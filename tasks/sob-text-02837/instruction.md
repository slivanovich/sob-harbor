{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHalford (band): Halford is an American heavy metal band formed in 1999 by British singer Rob Halford, who is best known as the lead vocalist for Judas Priest.  Halford formed the band to return to his heavy metal roots.  His two previous projects were a \"street metal\"-style band called Fight and the industrial metal band 2wo.\n\nMetal Health: Metal Health is the third studio album by American heavy metal band Quiet Riot.  It was released on March 11, 1983, bolstered by the No. 5 hit \"Cum On Feel the Noize\" and the No. 31 hit \"Metal Health\".  \"Metal Health\" is notable for being the first heavy metal album to reach the top spot on the \"Billboard\" 200, replacing the Police's \"Synchronicity\" at number one in November 1983.  The album went on to sell more than six million copies and is considered a classic among heavy metal fans.  Some critics, such as AllMusic, describe it as a one-hit wonder, owing to Quiet Riot's relative lack of critical and commercial success with following albums (and subsequent disintegration) towards the end of the 1980s.  The title track was ranked No. 35 on VH1's 40 Greatest Metal Songs.\n\nMarch of the Saint: March of the Saint is the first album by American heavy metal band Armored Saint.  It was released in 1984 on Chrysalis Records and recorded with producer Michael James Jackson who previously worked for Kiss.  The debut album yielded a minor MTV hit with \"Can U Deliver\", but Joey Vera and John Bush later recalled the album's recording as a frustrating and disappointing experience, explaining that Jackson's approach was much more commercial than the heavy metal sound the band had wanted.  As Vera recalled in 2006: \"At the end of the record we were very unhappy with the production, the mix, the way we worked and who we worked with.  And the producer and our manager let us spend over ($)300,000 on our first record.  To this day we are still in debt for that one.\"\n\nJoey Jordison: Nathan Jonas \"Joey\" Jordison (born April 26, 1975), is an American musician, songwriter, record producer and multi-instrumentalist, best known for his work as the former drummer and co-songwriter for the American heavy metal band Slipknot as well as guitarist in the American horror punk band Murderdolls.  Jordison played in Slipknot since their formation in 1995 until his departure from the band in December 2013.  He was the drummer and founder of the American heavy metal band Scar the Martyr which formed in 2013 and disbanded in 2016.  He grew up in Waukee, Iowa with his parents and two sisters, and was given his first drum kit at the age of 8.  He performed in several bands until joining in the summer of 1995 with the group The Pale Ones, which would later change their name to Slipknot.  Of Slipknot's nine-member lineup which lasted from 1999–2010, Joey was the third to join the band.\n\nKurdt Vanderhoof: Kurdt Vanderhoof (born June 28, 1961) is an American guitarist, best known as the lead guitarist and founding member of the American heavy metal band Metal Church.  As early as 1976, in Aberdeen, Vanderhoof was ardently networking with local musicians and had formed a band called Tyr, which included Kirk Arrington on drums and Vanderhoof on rhythm guitar.  In 1978 Vanderhoof joined Seattle hardcore punk band The Lewd adopting the stage name \"Blobbo\" on bass guitar, switching instruments to guitar the following year.  The Lewd relocated from Seattle to San Francisco in 1980.  Following Vanderhoof's departure from The Lewd he formed Metal Church, named after a nickname given to his San Francisco apartment.  Vanderhoof moved back to his hometown, Aberdeen, Washington, with a vinyl single of Trash Can Baby as proof of his interlude with the Lewd.  In the summer of 1982, he formed a heavy metal cover band named Shrapnel.  It consisted of Tom Weber on drums, Duke Erickson on bass (both from Hoquiam), Mike Murphey (\"muff\", from Montesano) and a guitar player Vanderhoof had jammed with in high school(Aberdeen).  Shrapnel played four events to warm up, including a frat party at Pacific Lutheran University, after which the other guitar player quit, having had a religious experience, unwilling to cover The Number of The Beast by Iron Maiden.  His part was replaced by Craig Wells of Aberdeen, and Tom was eventually replaced by Kirk Arrington (also from Hoquiam) on drums.  When Mike Murphy left the band, they recruited David Wayne for vocal duties.  By 1983, Shrapnel had renamed itself to Vanderhoof's original band name, Metal Church.\n\nChimaira: Chimaira is an American heavy metal band from Cleveland, Ohio.  Formed in 1998, the group was a notable member of the New Wave of American Heavy Metal scene.  The band's name is derived from the word Chimera, a monstrous creature in Greek mythology.  Throughout its history, the band endured numerous line-up changes, leaving vocalist Mark Hunter as the only constant member.  The band dissolved in 2014, but announced a one-off reunion in late 2017.\n\nAbsolutely (Story of a Girl): \"Absolutely (Story of a Girl)\" is a song recorded by American rock band Nine Days for the group's fourth studio album, \"The Madding Crowd\" (2000).  The song was released as the lead single from \"The Madding Crowd\" in April 2000 through 550 Music and Epic Records.  The song is an upbeat power pop anthem written by guitarist/vocalist John Hampson for his wife, who was his girlfriend at the time it was composed.  Brian Desveaux, the group's other guitarist, also receives songwriting credit.  The song represented a breakthrough for the band after years of attempting to interest major record labels.  It was recorded in Atlanta, Georgia at Tree Sound Studios with producer Nick DiDia.\n\nRage Against the Machine: Rage Against the Machine is an American heavy metal band from Los Angeles, California.  Formed in 1991, the group consists of rapper and vocalist Zack de la Rocha, bassist and backing vocalist Tim Commerford, guitarist Tom Morello, and drummer Brad Wilk.  They draw inspiration from early heavy metal instrumentation, hip hop acts such as Afrika Bambaataa, Public Enemy, and the Beastie Boys, punk rock such as the Sex Pistols and Fugazi, and Dutch crossover band Urban Dance Squad.  Rage Against the Machine is well known for the members' revolutionary political views, which are expressed in many of the band's songs.  As of 2010, they had sold over 16 million records worldwide.\n\nNick DiDia: Nick DiDia is an American record producer, engineer and mixer currently residing in Australia.  He has lived and worked in Los Angeles and later Atlanta before moving to Byron Bay, Australia.  Since the early 1990s, he has amassed over 40 million in sales with a variety of artists including Bruce Springsteen and Rage Against the Machine.\n\nWolverine Blues: Wolverine Blues is the third studio album by Swedish death metal band Entombed, released on October 4, 1993 by Earache Records.  The album displays a completely different sound from previous releases, combining elements of hard rock, heavy metal, and hardcore while still retaining much of their traditional, death metal roots, in a style that would later be known as death 'n' roll.  The band also adopted a mid-tempo groove metal style for this release, similar to that of American heavy metal band Pantera.\n\nQuestion: What state is the American heavy metal band, who worked with Nick DiDia, from?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American heavy metal band.\"\n    },\n    \"band_origin_state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the band is from.\"\n    },\n    \"band_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The primary genre of the band.\"\n    },\n    \"producer_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"producer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the producer who worked with the band.\"\n        },\n        \"producer_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the producer (e.g., record producer, engineer, mixer).\"\n        },\n        \"sales_contribution_millions\": {\n          \"type\": \"integer\",\n          \"description\": \"The total sales in millions attributed to the producer's work with various artists, including this band.\"\n        }\n      },\n      \"required\": [\n        \"producer_name\",\n        \"producer_role\",\n        \"sales_contribution_millions\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"band_origin_state\",\n    \"band_genre\",\n    \"producer_info\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the American heavy metal band."
      },
      "band_origin_state": {
        "type": "string",
        "description": "The state where the band is from."
      },
      "band_genre": {
        "type": "string",
        "description": "The primary genre of the band."
      },
      "producer_info": {
        "type": "object",
        "properties": {
          "producer_name": {
            "type": "string",
            "description": "The name of the producer who worked with the band."
          },
          "producer_role": {
            "type": "string",
            "description": "The role of the producer (e.g., record producer, engineer, mixer)."
          },
          "sales_contribution_millions": {
            "type": "integer",
            "description": "The total sales in millions attributed to the producer's work with various artists, including this band."
          }
        },
        "required": [
          "producer_name",
          "producer_role",
          "sales_contribution_millions"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "band_name",
      "band_origin_state",
      "band_genre",
      "producer_info"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
