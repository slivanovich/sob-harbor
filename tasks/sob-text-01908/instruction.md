{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPirates in Oz: Pirates in Oz (1931) is the twenty-fifth in the series of Oz books created by L. Frank Baum and his successors, and the eleventh written by Ruth Plumly Thompson.  It was illustrated by John R. Neill.\n\nThey Only Come Out at Night (Peter Brown song): They Only Come Out at Night is 1984 dance single by Peter Brown.  The single was his first number one on the dance chart, where it stayed for one week.  \"They Only Come Out at Night\", also peaked at number fifty on the soul singles chart, but unlike previous Peter Brown entries, it did not make the Hot 100.  It did, however, reach No. 102 on the \"Billboard\" Bubbling Under the Hot 100 chart.\n\nPeter M. Brown: Peter MacLachlan Brown was born in Vancouver, like his father, Ralph, and grandfather before him.  Peter Brown’s grandfather Brenton was a well-connected businessman and power broker of his time, head of the Crown Life Insurance Co., onetime president of the Vancouver Board of Trade, and a founder of the right-of-centre municipal NPA party.  His grandson would one day follow in his footsteps.\n\nCory Wade (music producer): Cory Wade is a former American record producer and songwriter, known for producing some of the biggest hits in disco in the 1970s.  A producer for TK Records, Wade co-produced the 1977 single \"Do Ya Wanna Get Funky With Me\" by Peter Brown, which became the first 12-inch single to sell a million copies.  Wade also produced hit recordings for KC and the Sunshine Band, T-Connection, Foxy and made a comeback in the 1990s with a remake of Peter Brown's \"Crank It Up\" by Lawrence Leritz, released on Spectrum Records.  Residing in Horn Lake, Mississippi, Cory Wade is currently working on a 3D feature films\n\nPeter Brown (Oz): Peter Brown is a major character in the Oz novels of Ruth Plumly Thompson, who continued the series of Oz books after the death of their creator, L. Frank Baum.  Thompson used Peter as the protagonist in three of her books: \"The Gnome King of Oz\" (1927), \"Jack Pumpkinhead of Oz\" (1929), and \"Pirates in Oz\" (1931).\n\nPeter Hoyt Brown: Peter Hoyt Brown (born October 16, 1936) is a politician who held office as an at-large Council Member in the city of Houston, Texas.  Known locally as \"Peter Brown,\" he was a candidate for the 2009 Houston Mayoral race, to succeed then Mayor Bill White who vacated the position due to term limits.  Although an independent poll conducted by 11 News/KUHF Houston Public Radio poll in late October 2009, showed Brown holding the lead in the Mayor's race with a nine-point lead over his nearest opponent, he was eliminated in the November 3, 2009 election.\n\nGordon Brown (rugby union): Gordon Lamont Brown (1 November 1947 - 19 March 2001) was a Scottish international rugby union footballer.  He was inducted into the International Rugby Hall of Fame in 2001.  He was also an inductee to the Scottish Rugby Union Hall of Fame in 2010.  And, The World Rugby Hall of Fame at a ceremony at Wembley during the Rugby World Cup 2015.  His nickname was Broon frae Troon (i.e. Brown from Troon) after his home town in west central Scotland.  Brown played second row for West of Scotland, Scotland and the British Lions.  He is often considered \"Scotland's greatest second row\".  He was the younger brother of Peter Brown, the son of footballer John Brown, and the nephew of footballers Tom and Jim Brown.\n\nBrendan B. Brown: Brendan B. Brown (born October 11, 1973) is an American musician from Northport, New York.  Commonly known as BBB to fans, Brown is the lead vocalist, guitarist, and the only remaining founding member of pop rock band Wheatus, which he formed in 1995 with his brother, Peter Brown (drums) and Rich Liegey (bass).\n\nPeter Brown (lecturer): Peter Brown is Head of Education at the Institute of Investing and Financial Trading (IIFT) and also financial advisor at Baggot Asset Management.  He is recognisable as a financial commentator on radio and television in Ireland, appearing on shows such as \"Tonight with Vincent Browne\", \"Today with Pat Kenny\", \"RTÉ News at One\" and Newstalk.  Brown has worked in Barclays Bank, Citi Bank, Banque National de Paris and Ulster Bank.\n\nThe Woman You Love: \"The Woman You Love\" is a song recorded by American recording artist Ashanti and Brooklyn native rapper Busta Rhymes.  It was written by Arden \"Keys\" Altino, Eric Bellinger, Peter Brown, John Bruce, Ashanti, \"Jerry Wonder\" Duplessis, Shama \"Sak Pase\" Joseph, Rhymes and Alozono Stevenson while Sak Pase, Jerry Wonder and Arden \"Keys\" Altino produced the song.  \"The Woman You Love\" samples elements of Cream's 1968 single \"White Room\", written by Bruce and Brown.\n\nQuestion: Who created the series who has Peter Brown as the protagonist ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the book series.\"\n    },\n    \"series_creator\": {\n      \"type\": \"string\",\n      \"description\": \"The original creator of the book series.\"\n    },\n    \"protagonist_character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character who is the protagonist.\"\n    },\n    \"author_who_used_protagonist\": {\n      \"type\": \"string\",\n      \"description\": \"The author who used the character as a protagonist in books within the series.\"\n    },\n    \"protagonist_books_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of books in which the character was a protagonist by the specified author.\"\n    },\n    \"protagonist_books_titles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of titles of the books where the character was a protagonist.\"\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"series_creator\",\n    \"protagonist_character_name\",\n    \"author_who_used_protagonist\",\n    \"protagonist_books_count\",\n    \"protagonist_books_titles\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the book series."
      },
      "series_creator": {
        "type": "string",
        "description": "The original creator of the book series."
      },
      "protagonist_character_name": {
        "type": "string",
        "description": "The name of the character who is the protagonist."
      },
      "author_who_used_protagonist": {
        "type": "string",
        "description": "The author who used the character as a protagonist in books within the series."
      },
      "protagonist_books_count": {
        "type": "integer",
        "description": "The number of books in which the character was a protagonist by the specified author."
      },
      "protagonist_books_titles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of titles of the books where the character was a protagonist."
      }
    },
    "required": [
      "series_name",
      "series_creator",
      "protagonist_character_name",
      "author_who_used_protagonist",
      "protagonist_books_count",
      "protagonist_books_titles"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
