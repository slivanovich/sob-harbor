{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGeorge Thomas, 1st Viscount Tonypandy: Thomas George Thomas, 1st Viscount Tonypandy, PC (29 January 1909 – 22 September 1997) was a British Labour Party politician and Speaker of the House of Commons.  Born in Port Talbot, Wales, he initially worked as a teacher in both London and Cardiff.  An MP from 1945 to 1983, he held office in Harold Wilson's 1964–1970 Labour administration, notably as Secretary of State for Wales from 1968 to 1970.  As a junior minister at the Wales Office, he was one of the first on the scene of the Aberfan disaster 21 October 1966, although later involved in the controversial government decision to use money from the Aberfan Charity Fund to clear remaining National Coal Board waste tips from around the village.  In 1976 Thomas was elected Speaker of the House of Commons, in which role the first broadcasting of parliamentary proceedings brought him unprecedented public attention.  He retired from parliament in 1983 and was elevated to the peerage as Viscount Tonypandy, of Rhondda in the County of Mid Glamorgan.\n\nSylvia Heal: Sylvia Lloyd Heal (born 20 July 1942) is a British Labour Party politician who was the Member of Parliament (MP) for Halesowen and Rowley Regis from 1997 to 2010, having previously been the MP for Mid Staffordshire from 1990 to 1992.  She served as the First Deputy Chairman of Ways and Means and a Deputy Speaker of the House of Commons.\n\nRosie Winterton: Dame Rosalie Winterton, {'1': \", '2': \", '3': \", '4': \"} (born 10 August 1958) is a British Labour Party politician who has been the Member of Parliament (MP) for Doncaster Central since 1997.  Since June 2017 Winteron has served as Second Deputy Chairman of Ways and Means.  She served under Prime Minister Gordon Brown as the Minister for Work and Pensions from 2008 to 2009, and the Minister for Local Government from 2009 to 2010.  She later entered the Shadow Cabinet in May 2010 as the Shadow Leader of the House of Commons.  In September 2010, she was nominated and elected unopposed as Labour Chief Whip and served until October 2016.  She was elected as one of three deputy speakers of the House of Commons on 28 June 2017.\n\nMont Follick: Montefiore Follick (31 December 1887 – 10 December 1958) was a British Labour Party politician, a campaigner for spelling reform, polyglot and advocate of decimal currency.  He was Member of Parliament (MP) for Loughborough from 1945 to 1955, having previously held the post of Professor of English at the University of Madrid in Spain.  He had been adopted by the Loughborough Labour Party in 1936 as prospective parliamentary candidate but had a long wait because of the war years before being elected.  In 1949 and again in 1952 he introduced private member's bills in the UK parliament for the reform of English spelling.  He also bought the Loughborough Labour Party's current Building Unity House in 1947.\n\nIan Murray (British politician): Ian Murray (born 10 August 1976) is a British Labour Party politician who has represented Edinburgh South as Member of Parliament (MP) since the 2010 general election.  He served as an Edinburgh City Councillor for Liberton & Gilmerton Ward from 2003 to 2010, before his Westminster election as an Edinburgh MP.  From 2015 to 2017, Murray was the only Labour Party MP representing a Scottish constituency in the House of Commons.\n\nAlan Campbell (politician): Alan Campbell (born 8 July 1957) is a British Labour Party politician who has been the Member of Parliament (MP) for Tynemouth since 1997.  He served as Parliamentary Under-Secretary of State at the Home Office from 2008 until 2010, and is currently the Deputy Chief Whip of the Labour Party.\n\nBarbara Follett (politician): Daphne Barbara Follett ( Hubbard; born 25 December 1942) is a British Labour Party politician who served as the Member of Parliament (MP) for Stevenage from 1997 until 2010.  During this time she held several parliamentary and ministerial positions.  In the decade before entering Parliament she played a major part in transformation of the Labour Party, firstly by making members more aware of their visual impact on voters and secondly by co-founding and running two organisations, Labour Women's Network and Emily's List UK, which spearheaded reforms that helped Labour to return a record 101 women to Parliament in 1997.  Following the United Kingdom Parliamentary expenses scandal, she repaid more than £32,000 which she had claimed in expenses.  She stood down in 2010 in order to take over the running of her husband, bestselling author Ken Follett's, growing business.\n\nHarriet Harman: Harriet Ruth Harman, {'1': \", '2': \", '3': \", '4': \"} (born 30 July 1950) is a British solicitor and Labour Party politician who has been a Member of Parliament (MP) since 1982, first for Peckham, and then for its successor constituency of Camberwell and Peckham since 1997.  She has served in various Cabinet and Shadow Cabinet positions and, in her role as Deputy Leader of the Labour Party, she was twice the Acting Leader of the Labour Party and Leader of the Opposition: from May to September 2010 and from May to September 2015.  She remains the only politician to have held this position on two separate occasions.\n\nChairman of Ways and Means: In the United Kingdom, the Chairman of Ways and Means is a senior member of the House of Commons who acts as one of the Speaker's three deputies.  The position is currently held by Lindsay Hoyle, member of parliament for Chorley, who was elected by secret ballot on 8 June 2010.\n\nLindsay Hoyle: Lindsay Harvey Hoyle (born 10 June 1957) is a British Labour Party politician who has been the member of parliament (MP) for Chorley since 1997.  He is the son of Doug Hoyle, a former Labour MP for Warrington North.\n\nQuestion: In the United Kingdom, the Chairman of Ways and Means is a senior member of the House of Commons who acts as one of the Speaker's three deputies, the position is currently held by which British Labour Party politician, who has been the member of parliament (MP) for Chorley since 1997?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"chairman_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the current Chairman of Ways and Means.\"\n    },\n    \"political_party\": {\n      \"type\": \"string\",\n      \"description\": \"The political party the chairman belongs to.\"\n    },\n    \"constituency\": {\n      \"type\": \"string\",\n      \"description\": \"The parliamentary constituency the chairman represents.\"\n    },\n    \"mp_since_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the chairman became a Member of Parliament for their current constituency.\"\n    },\n    \"role_start_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date when the individual was elected as Chairman of Ways and Means.\"\n    }\n  },\n  \"required\": [\n    \"chairman_name\",\n    \"political_party\",\n    \"constituency\",\n    \"mp_since_year\",\n    \"role_start_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "chairman_name": {
        "type": "string",
        "description": "The full name of the current Chairman of Ways and Means."
      },
      "political_party": {
        "type": "string",
        "description": "The political party the chairman belongs to."
      },
      "constituency": {
        "type": "string",
        "description": "The parliamentary constituency the chairman represents."
      },
      "mp_since_year": {
        "type": "integer",
        "description": "The year the chairman became a Member of Parliament for their current constituency."
      },
      "role_start_date": {
        "type": "string",
        "description": "The date when the individual was elected as Chairman of Ways and Means."
      }
    },
    "required": [
      "chairman_name",
      "political_party",
      "constituency",
      "mp_since_year",
      "role_start_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
