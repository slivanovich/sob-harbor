{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nChuck Berry: Charles Edward Anderson Berry (October 18, 1926 – March 18, 2017) was an American singer, songwriter, musician, and one of the pioneers of rock and roll music.  With songs such as \"Maybellene\" (1955), \"Roll Over Beethoven\" (1956), \"Rock and Roll Music\" (1957) and \"Johnny B. Goode\" (1958), Berry refined and developed rhythm and blues into the major elements that made rock and roll distinctive.  Writing lyrics that focused on teen life and consumerism, and developing a music style that included guitar solos and showmanship, Berry was a major influence on subsequent rock music.\n\nWilliam McDowell (musician): William David McDowell (born August 31, 1976) is an American gospel musician.  He started his music career, in 2009, with the release of, \"As We Worship\", by Entertainment One Music.  This album would chart on three \"Billboard\" charts Gospel Albums, Independent Albums and Heatseekers Albums.  His second album, \"Arise\", was released in 2011 with Entertainment One.  The album charted three \"Billboard\" charts again, this time The \"Billboard\" 200, Gospel Albums and Independent Albums.  His third album, \"Withholding Nothing\", was released in 2013, with Entertainment One.  This album would chart on three charts The \"Billboard\" 200, Gospel Albums, and Independent Albums.  He was nominated for Grammy Award for Best Gospel Album, for his third album.\n\nJimmy Hicks: Jimmy Hicks is an American gospel musician.  He started his music career, in 2001, with the release of, \"Turn It Around\", by Amen Records, and this was his breakthrough release upon the \"Billboard\" Gospel Albums chart.  His subsequent album, \"Crossroads\", was released in 2003 by Worldwide Gospel Records, but this failed to chart.  The third album, \"Born Blessed\", was released by World Wide Gospel in 2006, and this would place upon the aforementioned chart.  He released, \"The Jimmy Hicks Project\" in 2007, yet this did not chart.  He received a Stellar Awards nomination at the 23rd edition.\n\nMarcus Cole (musician): Marcus Randell Cole (born November 9, 1971) is an American gospel musician and worship leader, Christian R&B, urban gospel and black gospel recording artist and singer.  He started his music career, in 1996, with the gospel music group, Commissioned until 2002.  He has released two studio albums, \"Chillin' Up In Heaven\", in 1999, with Godson Records, and, \"Write My Song\", in 2006, from PureSprings Gospel.  The second album was his breakthrough release, entering the \"Billboard\" magazine charts.\n\nDebbie McClendon: Debbie McClendon (born June 15, 1960) is an American gospel musician and Christian R&B singer, who is a traditional black gospel, urban contemporary gospel, and contemporary Christian music recording artist.  She started her music career, in 1985, and released four studio albums until 1990, \"I Can Hardly Wait\", \"Count It All Joy\", \"Morning Rises\", and \"Get a Grip\".  McClendon was nominated for two GMA Dove Awards in 1987 and 1988, in the Contemporary Black Gospel Album category.  She was nominated for a Grammy Award, in 1988, for Best Gospel Vocal Performance, Female.\n\nSara Jordan Powell: Sara Jordan Powell (born October 6, 1938) is an American gospel musician.  Her first works, \"Touch Somebody's Life\" and \"When Jesus Comes,\" were released in 1972, and got significant radio airtime.  She has released an album that was produced by James Cleveland, \"Touch Somebody's Life,\" which came out in 1975 on Savoy Records.  Powell released four more albums on that label, 1980's \"I Must Tell Jesus\", 1990's \"Sara Jordan Powell\" and \"When Jesus Comes to Stay,\" and 1995's \"The Soul of Sara Jordan Powell.\"  Subsequently, she released one album with Compendia Music Group that same year, \"Live in Houston.\"  Her music even has been performed at the White House.  She performed in 1979 for President Jimmy Carter, and she was joined by Chuck Berry, Billy Eckstine, Evelyn \"Champagne\" King, and Andraé Crouch.  President Ronald Reagan appointed her to serve on the Year of the Bible Committee.  She got the opportunity to minister to President Bill Clinton in Memphis, Tennessee, at the request of Bishop Louis Henry Ford, along with Dr. Vernard Johnson.\n\nThe Clark Sisters: The Clark Sisters are an American gospel vocal group consisting of five sisters: Jacky Clark Chisholm (b. 1948), Denise Clark Bradford (b. 1953), Elbernita \"Twinkie\" Clark-Terrell (b. 1954), Dorinda Clark-Cole (b. 1957), and Karen Clark Sheard (b. 1960).  The Clark Sisters are the daughters of gospel musician and choral director Mattie Moss Clark.  They are credited for helping to bring gospel music to the mainstream and are considered as pioneers of contemporary gospel.  Their biggest crossover hits include: \"Is My Living in Vain?\" , \"Hallelujah\", \"He Gave Me Nothing to Lose\", \"Endow Me\", their hit song \"Jesus Is A Love Song\", \"Pure Gold\", \"Expect a Miracle\", and their largest mainstream crossover gold certified, \"You Brought the Sunshine\".  The Clark Sisters have won three Grammy Awards.  With 16 albums to their credit and millions in sales, the Clark Sisters are the highest-selling female gospel group in history.\n\nJimmy &amp; Rosalynn Carter Work Project: The Jimmy & Rosalynn Carter Work Project - formerly the Jimmy Carter Work Project (JCWP) - is an annual home building blitz organized by Habitat for Humanity International and its affiliates.  It generally takes place in the United States one year, and an international location the next.  President Jimmy Carter and Rosalynn Carter helped Habitat volunteers renovate the 19-unit building, and media coverage brought attention to Habitat, which had been founded in 1976 in Americus, Georgia, a short distance from Carter’s hometown of Plains, Georgia.  Even though President Carter has said repeatedly he never intended to start an annual project, the following year the Carters returned to the same site to finish the renovation work.  On Oct. 10, 2013, as part of the 30th annual project, the Carters returned to the building and met with families living there.\n\nAntonio Neal: Antonio Neal Phelon (born June 7, 1973) is an American gospel musician and music producer, Christian R&B, Christian hip hop, urban gospel and black gospel recording artist and singer.  He started his music career, in 1999, with an independently-made album.  His first studio album, \"Days of My Life\", that was released by EMI Gospel.  His only hip hop music album, \"Bible Megamix\", was released Anshar Forever Records, in 2009.  The only extended play, \"Welcome Home\", a contemporary R&B work, was released by Madison Line, in 2014.  He has won two GMA Dove Awards, one for his songwriting and another for his music production work.\n\nDarrel Petties: Darrel Darnell Petties (born December 17, 1983) is an American gospel musician, worship leader and pastor, while he is an urban contemporary gospel and a traditional black gospel recording artist and singer, with his choir, Strength In Praise.  He started his music career, in 2005, with the studio album, \"Count It All Joy\", that released in 2006, from EMI Gospel.  The album got two songs, \"Yes Lord\" and \"Thank Ya Jesus\", to chart on the \"Billboard\" magazine Gospel Songs chart, and for them to appear on two songs to appear on the WOW Gospel Albums, in 2005, being \"Glory Hallelujah\", and, in 2007, with \"Thank Ya Jesus\".\n\nQuestion: Sara Jordan Powell, is an American gospel musician, she performed in 1979 for President Jimmy Carter, and she was joined by who, which was an American singer, songwriter, musician, and one of the pioneers of rock and roll music?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"main_performer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the primary musician who performed.\"\n    },\n    \"event_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the event where the performance took place.\"\n    },\n    \"event_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the performance occurred.\"\n    },\n    \"co_performer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the co-performer.\"\n        },\n        \"musical_roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of musical roles held by the co-performer.\"\n        },\n        \"pioneering_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The music genre the co-performer was a pioneer of.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"musical_roles\",\n        \"pioneering_genre\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"main_performer_name\",\n    \"event_description\",\n    \"event_year\",\n    \"co_performer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "main_performer_name": {
        "type": "string",
        "description": "The name of the primary musician who performed."
      },
      "event_description": {
        "type": "string",
        "description": "A description of the event where the performance took place."
      },
      "event_year": {
        "type": "integer",
        "description": "The year the performance occurred."
      },
      "co_performer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the co-performer."
          },
          "musical_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of musical roles held by the co-performer."
          },
          "pioneering_genre": {
            "type": "string",
            "description": "The music genre the co-performer was a pioneer of."
          }
        },
        "required": [
          "name",
          "musical_roles",
          "pioneering_genre"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "main_performer_name",
      "event_description",
      "event_year",
      "co_performer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
