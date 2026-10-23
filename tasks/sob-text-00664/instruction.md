{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRhonda Vincent: Rhonda Lea Vincent (born July 13, 1962) is an American bluegrass singer, songwriter, and multi-instrumentalist.  In 2000, \"The Wall Street Journal\" proclaimed Vincent \"the new Queen of Bluegrass\".\n\nDavid Bach (author): David L. Bach is an American financial author, television personality, motivational speaker, entrepreneur and founder of FinishRich.com.  Bach, is best known for his \"Finish Rich Book Series\" and \"Automatic Millionaire Series\" of motivational financial books under the Finish Rich® Brand.  He has written 12 books since 1998 with over seven million copies in print.  Eleven of Bach’s books have been national bestsellers, including nine consecutive New York Times bestsellers, two of which were consecutive #1 \"New York Times\" bestsellers (\"The Automatic Millionaire\" and \"Start Late, Finish Rich\").  Bach has had four of his books \"Smart Women Finish Rich, Smart Couples Finish Rich, The Automatic Millionaire and The Finish Rich Workbook\" appear simultaneously on the \"Wall Street Journal, BusinessWeek, and USA Today\" bestseller lists.  Eleven of Bach’s books have been published from Random House (Broadway Books).  Bach's first book \"Smart Women Finish Rich\" was published in 1998, and appeared on the bestseller lists for a decade.  His most recent book \"Debt Free For Life\" (2011) was published by Crown Business Books, and appeared simultaneously on the \"New York Times, \"Wall Street Journal\" and \"USA Today\" bestseller lists.\n\nWall Street Journal Economic Survey: The Wall Street Journal Economic Survey, also known as the Wall Street Journal Economic Forecasting Survey, could refer to either the monthly or the semi-annual survey conducted by the \"Wall Street Journal\" of over 50 economists on important indicators of the economy of the United States.\n\nMike Vranos: Michael W. \"Mike\" Vranos is an American hedge fund manager and philanthropist who in the 1990s was referred to by some as the \"most powerful man on Wall Street.\"  In 1993, he reportedly earned $15 million from trading mortgage bonds. \"Fortune Magazine\" once called him \"one of the best bond traders on Wall Street.\"  According to a 2007 \"Wall Street Journal\" article, he has continued to be regarded as \"the best-known mortgage-bond trader on Wall Street.\"\n\nThe Wall Street Journal Asia: The Wall Street Journal Asia, a version of \"The Wall Street Journal\", provides news and analysis of global business developments for an Asian audience.  Formerly known as \"The Asian Wall Street Journal\", it was founded in 1976 and is printed in nine Asian cities: Bangkok, Hong Kong, Jakarta, Kuala Lumpur, Manila, Seoul, Singapore, Taipei, and Tokyo.  Average circulation for 2011 was 83,421.  Its largest markets in order of importance are: Hong Kong, Singapore, the Philippines, Japan, Thailand, South Korea, Indonesia, Taiwan, Malaysia, China, India and Vietnam.\n\nL. Gordon Crovitz: Louis Gordon Crovitz is an American media executive and advisor to media and technology companies.  He is a former publisher of \"The Wall Street Journal\" who also served as executive vice-president of Dow Jones and launched the company's Consumer Media Group, which under his leadership integrated the global print, online, digital, TV and other editions of \"The Wall Street Journal\", MarketWatch.com and Barron's across news, advertising, marketing and other functions.  He stepped down from those positions in December 2007, when News Corp. completed its acquisition of Dow Jones.  He writes a weekly column in The Wall Street Journal, titled \"Information Age.\"\n\nThe Wall Street Journal Europe: The Wall Street Journal Europe is a daily English-language newspaper that covers global and regional business news for Europe, the Middle East and Africa (EMEA).  Published by Dow Jones & Company (a News Corp company), it forms part of the business publication franchise which includes \"The Wall Street Journal\", \"The Wall Street Journal Asia\", and The Wall Street Journal Online (WSJ.com).  Together, these publications have a total circulation of 3.8 million.\n\nThat's Why I Sing This Way: That's Why I Sing This Way is the fourth studio album by American country music singer Daryle Singletary.  It was released on April 23, 2002 via Koch Records.  Except for its title track, the album is composed of cover songs. Two singles were released from it: the title track and a cover of Conway Twitty's 1980 Number One single \"I'd Love to Lay You Down\", which respectively reached #47 and #43 on the U.S. \"Billboard\" country singles charts.  The version of \"I Never Go Around Mirrors\" on this album was first recorded by Keith Whitley, Whitley had Shafer write the second verse heard here.  The album includes guest appearances from George Jones, Dwight Yoakam, Rhonda Vincent, John Wesley Ryles, Merle Haggard and Johnny Paycheck.\n\nThe Wall Street Journal Special Editions: The Wall Street Journal Special Editions is a venture launched in 1994 by \"The Wall Street Journal\" to expand its readership abroad, especially in the Americas.  It publishes pages, bearing the \"Journal's\" banner, within major daily and weekly newspapers around the world featuring selected content from \"The Wall Street Journal\".  Its Special Editions are carried in 37 newspapers in 35 countries, translated into 10 languages, with a total combined circulation of 5.2 million.\n\nYaroslav Trofimov: Yaroslav Trofimov is an award-winning author and journalist who writes a weekly column on the Greater Middle East, Middle East Crossroads, in The Wall Street Journal.  He has been a foreign correspondent for \"The Wall Street Journal\" since 1999, covering the Middle East, Africa and Asia.  Prior to 2015 he was The Wall Street Journal's bureau chief in Afghanistan and Pakistan.\n\nQuestion: Rhonda Vincent, who appeared on the album \"That's why I Sing this Way\" has been called the \"new queen of\" what, by the Wall Street Journal\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person being described.\"\n    },\n    \"proclaiming_publication\": {\n      \"type\": \"string\",\n      \"description\": \"The publication that bestowed the title.\"\n    },\n    \"title_given\": {\n      \"type\": \"string\",\n      \"description\": \"The full title given to the person.\"\n    },\n    \"title_category\": {\n      \"type\": \"string\",\n      \"description\": \"The specific category or genre associated with the title.\"\n    },\n    \"proclamation_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the title was proclaimed.\"\n    },\n    \"album_name_appeared_on\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album the person appeared on.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"proclaiming_publication\",\n    \"title_given\",\n    \"title_category\",\n    \"proclamation_year\",\n    \"album_name_appeared_on\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person being described."
      },
      "proclaiming_publication": {
        "type": "string",
        "description": "The publication that bestowed the title."
      },
      "title_given": {
        "type": "string",
        "description": "The full title given to the person."
      },
      "title_category": {
        "type": "string",
        "description": "The specific category or genre associated with the title."
      },
      "proclamation_year": {
        "type": "integer",
        "description": "The year the title was proclaimed."
      },
      "album_name_appeared_on": {
        "type": "string",
        "description": "The name of the album the person appeared on."
      }
    },
    "required": [
      "person_name",
      "proclaiming_publication",
      "title_given",
      "title_category",
      "proclamation_year",
      "album_name_appeared_on"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
