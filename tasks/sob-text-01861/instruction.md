{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe European (newspaper): The European, billed as \"Europe's first national newspaper\", was a British weekly newspaper founded by Robert Maxwell.  It was published from 11 May 1990 until December 1998.\n\nFalkirk Herald: The Falkirk Herald is a weekly newspaper and daily news website published by Johnston Press.  It provides reportage, opinion and analysis of current affairs in the towns of Falkirk, Grangemouth, Larbert and Denny as well as the neighbouring villages of Polmont, Redding, Brightons, Banknock and Bonnybridge.  The paper's circulation area has a total population of 151,600, the fifth largest urban area in Scotland.  \"The Falkirk Herald\" had an audited circulation of 21,937 in the six months from July-December 2012, making it the biggest selling local weekly newspaper in Scotland.  It was named Weekly Newspaper of the Year at the 2013 Scottish Press Awards.\n\nDumfries &amp; Galloway Standard: The Dumfries & Galloway Standard is a tabloid newspaper primarily serves Dumfries and the surrounding towns and villages such as Thornhill, Sanquhar, Lockerbie and Annan.  But it also covers Castle Douglas, Kirkcudbright, Gretna and news in Wigtownshire such as in the town of Stranraer.  Its sister paper is the \"Galloway News\" which covers the Galloway area more in depth with Castle Douglas, Kirkcudbright and Dalbeattie the three main towns in its patch.  Both are owned by Scottish & Universal Newspapers Limited, also known as the Trinity Mirror.  \"The Standard\", as it is colloquially known, was established in 1853 and prints twice weekly on a Wednesday and a Friday.  It was the 2003 regional newspaper of the year.  It was named Weekly Newspaper of the Year in Scotland by the Newspaper Society in 2007 and also won Scottish Weekly Newspaper of the Year at the Scottish Press Awards in May 2010.\n\nThe Caribbean Times: The Caribbean Times was a British weekly newspaper that was first published in 1981 by Hansib Publications, a publishing house for Caribbean, African and Asian writers and their communities, founded in London by Guyanese-born businessman Arif Ali in 1970.  The newspaper covered news, sport and social developments in the Caribbean, targeting the UK's West Indian and African-Caribbean population.  It was \"an important anti-racist campaigning organ\" and the UK's oldest Black weekly newspaper.  Hansib brought out other publications, including the weekly \"Asian Times\" in 1983 and the \"African Times\" in 1984, but in 1997 sold off the newspapers in order to concentrate on producing books.\n\nThe Lana Sisters: The Lana Sisters were formed by Iris Long in 1958, along with Lynne Abrams.  They put an advert in \"The Stage\" for a third member and got a reply from Mary O'Brien, who would go on to solo success a few years later as Dusty Springfield.  After Iris left the Lana Sisters she formed the Chantelles with two friends.\n\nBronx Press-Review: The Bronx Press-Review is a weekly newspaper published in the Bronx, New York.  The newspaper was established in 1940, and it remains the longest-publishing weekly newspaper in the Bronx.  The \"Bronx Press-Review\" is a borough-wide newspaper that covers local news, politics, and community events.  It publishes editorials and letters to the editor from readers.  It used to be sold on newsstands and available through paid subscription.  In the late 1990s, it became a free newspaper that is available through vending machines and distributed in public places such as banks and libraries.  Since the newspaper is free, it relies on exclusively on advertising and classified ads for revenue.\n\nLake County Examiner: The Lake County Examiner is a weekly newspaper published in Lakeview, Oregon, United States.  The newspaper was founded in 1880 by Stephen P. Moss and Charles A. Cogswell.  Over the years, the paper has had a number of publishers.  Today, it is owned by the Pioneer News Group.  In addition to the weekly newspaper, the \"Examiner\" staff publishes a number of special editions each year along with a local real estate guide and a twice-weekly news flyer.\n\nThe Stage: The Stage is a British weekly newspaper and website covering the entertainment industry, and particularly theatre.  It was founded in 1880.  It contains news, reviews, opinion, features, and recruitment advertising, mainly directed at those who work in theatre and the performing arts.\n\nKhasokhas Weekly: (Nepali: खसोखास साप्ताहिक) is a Nepali weekly magazine, published in New York City.  It started as a weekly newspaper in 2012 in the United States, before becoming a weekly magazine.  It has been published every Friday since its launch on 15 January 2012.  \"Khasokhas Weekly\" was also the first Nepali weekly newspaper to have been published in the United States and \"Khasokhas Weekly Magazine\" is the first Nepali weekly magazine in Nepali diaspora.  \"Khasokhas\" is a Nepalese word whose dictionary meaning translates to \"verified truth\".  Kishor Panthi is the editor-in-chief of the newspaper since 2012.\n\nCleave's Weekly Police Gazette: Cleave's Weekly Police Gazette (also known by contemporaries simply as the Weekly Police Gazette) was a British weekly newspaper published by John Cleave between 1834 and 1836.  It was \"one of the first and most popular unstamped newspapers to mix political news with coverage of non-political events like sensational crimes, strange occurrences, and excerpts from popular fiction\".\n\nQuestion: The Lana Sisters put an advert for a third member in this British weekly newspaper that was founded in which year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"newspaper_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the newspaper where the advert was placed.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the newspaper was founded.\"\n    },\n    \"newspaper_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of newspaper, e.g., 'British weekly newspaper'.\"\n    },\n    \"advert_purpose\": {\n      \"type\": \"string\",\n      \"description\": \"The purpose of the advert placed by The Lana Sisters.\"\n    }\n  },\n  \"required\": [\n    \"newspaper_name\",\n    \"founding_year\",\n    \"newspaper_type\",\n    \"advert_purpose\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "newspaper_name": {
        "type": "string",
        "description": "The name of the newspaper where the advert was placed."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the newspaper was founded."
      },
      "newspaper_type": {
        "type": "string",
        "description": "The type of newspaper, e.g., 'British weekly newspaper'."
      },
      "advert_purpose": {
        "type": "string",
        "description": "The purpose of the advert placed by The Lana Sisters."
      }
    },
    "required": [
      "newspaper_name",
      "founding_year",
      "newspaper_type",
      "advert_purpose"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
