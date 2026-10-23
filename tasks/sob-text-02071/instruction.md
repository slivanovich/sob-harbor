{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBalwant Singh Sagwal: Balwant Singh Sagwal (died 14 November 2010), popularly known as Ballu, was an Indian volleyball player, considered a star of the India men's national volleyball team.  His Son Narender is a professional Volleyball player .  Narender play for Indian volleyball Team .  Kaul Village also organised Balwant Singh Ballu Memoriel tournament ( after his death & orgained by Kaul Village & also by his son Narender ) in his born place ( his village ) Kaul ( Kaithal ) Participate all India top 8 Teams .\n\nG. R. Vaishnav: Govindarajan Ramakrishnan Vaishnav (born 11 February 1991) alies Vaishnav Ramakrishnan is a member of the India men's national volleyball team.  He wears the Number 1 Jersey for the Team.  He also plays for Indian overseas bank volleyball team.  He hails from Coimbatore.\n\nSahara India Pariwar: Sahara India Pariwar is an Indian conglomerate headquartered in Lucknow, India with business interests in finance, infrastructure & housing, media & entertainment, consumer merchandise retail venture, manufacturing and information technology.  The company has an estimated market capitalisation of 25.94 billion as of March 2011.  The group is a major promoter of sports in India and was the main sponsor of the India national cricket team.  The company owns a 42.5% stake in Formula One's Force India Formula 1 Team and also sponsors the India national field hockey team.  In more recent times, the company has faced criticism due to allegations regarding questionable financial practices, crony capitalism and its close nexus with and favoritism from political parties.\n\nGeorgios Lykoudis: Georgios Lykoudis (Greek: Γιώργος Λυκούδης , born (1964--)04 1964 ) is a retired Greek male volleyball player and volleyball coach currently coaching Panachaiki.  He has 154 appearances with Greece men's national volleyball team.  He played for Olympiacos for 6 years (1988-1996), winning 6 consecutive Greek Championships, 4 Greek Cups and the .  In 1993 (while still an active player) he became head coach of Olympiacos Women's Volleyball Team and coached the team for 3 years.  In 2002 he became assistant coach of Olympiacos.  In 2006-07 he was appointed head coach Olympiacos Women's Volleyball Team for the second time and in 2009 he became head coach of Greece women's national volleyball team.\n\nClaudio Cuello: Claudio César Cuello (born March 4, 1958) is a former Argentine volleyball player and current coach.  He was head coach of Argentina women's national volleyball team from 1997 to 2002 and in 2003 he became head coach of Argentina men's national volleyball team.  In 2004–2005 he was appointed head coach of the Greek powerhouse Olympiacos and coached the club to the triumph.  In 2005–06 season he worked in CS Petrolul Ploiesti, and led the team to the 2006 Romanian Championship.  From 2006 to 2009 he was head coach of HotVolleys Vienna and coached them to 2 consecutive (2006–07, 2007–08) and 1 (2008–09).  In 2007, after his first season with HotVolleys Vienna, he was appointed head coach of Austria men's national volleyball team as well, coaching the team until 2009.  He then moved to Italy, where he became head coach of Sirio Perugia (2010–2012) and (2012–2013) women's teams in .  In 2013–2014 he coached Lokomotiv Baku women's team in Azerbaijan.\n\nIndia men's national volleyball team: The India men's national volleyball team represents India in international volleyball competitions which is managed by Volleyball Federation of India.  It is currently sponsored by Sahara India Pariwar and Asics.\n\nAustralia men's national volleyball team: The Australia Men's national volleyball team, also known as Volleyball Team Australia Men (VTAM) or the Volleyroos, is the national volleyball team of the volleyball-playing nation of Australia.  As of August 2015, they are ranked 13th in the world.  They are a member of the Asian Volleyball Confederation (AVC).  Their best result came in 2007, when they won the Asian Men's Volleyball Championship.\n\nG. E. Sridharan: G E Sridharan is a former India men's national volleyball team player from Tamil Nadu, India who played during the late 1970s to late 1980s.  He was the second player from Tamil Nadu to receive Arjuna Award in 1982.  He is the current coach for India men's national volleyball team and former coach for Tamil Nadu Volleball team.  He's one of the efficient coach who took Indian youth volleyball to a new height winning gold in Asian volleyball Championship.  He was awarded Dronacharya Award in 2008, which many people feel its given too late in his life, seeing his achievements list lying before.\n\nBrazilian Volleyball Confederation: The Brazilian Volleyball Confederation (Portuguese: \"Confederação Brasileira de Voleibol, CBV\" ) is the governing body of volleyball and beach volleyball in Brazil.  Formed in 1954, its headquarters are in Barra da Tijuca, Rio de Janeiro.  The CBV is a member of the International Volleyball Federation (FIVB) and the South American Volleyball Confederation (CSV) and it is affiliated to the Brazilian Olympic Committee.  It organizes both the men's and women's Brazilian Volleyball Superleague, which are the top level's volleyball competition in Brazil, and also organizes the Salonpas Cup, which is an international women's club cup competition played annually in Brazil.  The organization also administrates the Brazil men's national volleyball team and the Brazil women's national volleyball team.\n\nK. Udayakumar: Karunakarakurup Udayakumar was an India men's national volleyball team player known for his allround skills at offence and defence and a member of the Indian volleyball team during what many consider as the golden era of Indian volleyball.  A former captain of the Indian national volleyball team, Udayakumar was a member of the team, which included Jimmy George and Cyril C. Valloor, that won the Bronze medal in the 1986 Asian Games held in Seoul.  Udayakumar played for the Kerala police Volleyball team.  The Government of India, in 1991, honoured his services to Indian volleyball by bestowing on him, the second highest Indian sports award, the Arjuna Award.\n\nQuestion: What is the estimated market capitalisation of the Indian conglomerate that sponsored the India men's national volleyball team along with Asics?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"conglomerate_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Indian conglomerate.\"\n    },\n    \"sponsorship_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"sponsored_team\": {\n          \"type\": \"string\",\n          \"description\": \"The national team sponsored by the conglomerate.\"\n        },\n        \"other_sponsors\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Other entities that sponsored the team along with the conglomerate.\"\n        }\n      },\n      \"required\": [\n        \"sponsored_team\",\n        \"other_sponsors\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"market_capitalization\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"value\": {\n          \"type\": \"number\",\n          \"description\": \"The estimated market capitalization value.\"\n        },\n        \"unit\": {\n          \"type\": \"string\",\n          \"description\": \"The unit of the market capitalization (e.g., 'billion').\"\n        },\n        \"as_of_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date as of which the market capitalization was estimated.\"\n        }\n      },\n      \"required\": [\n        \"value\",\n        \"unit\",\n        \"as_of_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"conglomerate_name\",\n    \"sponsorship_details\",\n    \"market_capitalization\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "conglomerate_name": {
        "type": "string",
        "description": "The name of the Indian conglomerate."
      },
      "sponsorship_details": {
        "type": "object",
        "properties": {
          "sponsored_team": {
            "type": "string",
            "description": "The national team sponsored by the conglomerate."
          },
          "other_sponsors": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other entities that sponsored the team along with the conglomerate."
          }
        },
        "required": [
          "sponsored_team",
          "other_sponsors"
        ],
        "additionalProperties": false
      },
      "market_capitalization": {
        "type": "object",
        "properties": {
          "value": {
            "type": "number",
            "description": "The estimated market capitalization value."
          },
          "unit": {
            "type": "string",
            "description": "The unit of the market capitalization (e.g., 'billion')."
          },
          "as_of_date": {
            "type": "string",
            "description": "The date as of which the market capitalization was estimated."
          }
        },
        "required": [
          "value",
          "unit",
          "as_of_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "conglomerate_name",
      "sponsorship_details",
      "market_capitalization"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
