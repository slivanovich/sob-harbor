{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCaterham F1: The Caterham F1 Team was a Malaysian, later British, owned Formula One team based in the United Kingdom which raced under a Malaysian licence.  The Caterham brand had competed in the Formula One World Championship from 2012 to 2014, following the acquisition of British sportscar manufacturer Caterham Cars by former owner and team principal Tony Fernandes, forming the Caterham Group.\n\nChristijan Albers: Christijan Albers (   ) (born 16 April 1979 in Eindhoven) is a Dutch professional racing driver.  After success in the DTM he drove in Formula One from until the 2007 British Grand Prix, shortly after which he was dropped by the Spyker F1 team.  In 2008, he returned to the DTM series as a driver for the Audi Futurecom TME team.  Albers acted as Team Principal and CEO of the Caterham F1 Team from July to September 2014 after it was acquired by new team owners.\n\nTony Fernandes: Tan Sri Anthony Francis \"Tony\" Fernandes, CBE (born 30 April 1964) is a Malaysian entrepreneur.  He is the founder of Tune Air Sdn.  Bhd., who introduced the first budget no-frills airline, AirAsia, to Malaysians with the tagline \"Now everyone can fly\".  Fernandes managed to turn AirAsia, a failing government-linked commercial airline, into a highly successful budget airline public-listed company.  He has since founded the Tune Group of companies.\n\nCaterham CT03: The Caterham CT03 is a Formula One racing car designed by Mark Smith for the Caterham F1 team.  It was used during the 2013 Formula One season, where it was driven by Charles Pic and Giedo van der Garde.  The car was unveiled on the eve of testing for the 2013 season at the Circuito de Jerez.\n\nCaterham CT01: The Caterham CT01 is a Formula One racing car produced by the British-based Caterham F1 Team which competed in the 2012 Formula One season.  The car, designed under the leadership of the team's technical director Mike Gascoyne, is the third car to be produced by the team and the first to carry the team's new name, following their renaming from Team Lotus at the end of 2011.  The CT01 was the first car launched for the 2012 season, when an online launch initially planned for 26 January, was cancelled and the car was released a day earlier instead.  The car was driven by Heikki Kovalainen and Vitaly Petrov, who replaced Jarno Trulli after the first test at Jerez.\n\nVitaly Petrov: Vitaly Aleksandrovich Petrov (Russian: Вита́лий Алекса́ндрович Петро́в ; ] , born 8 September 1984) is a Russian racing driver who drove in Formula One for Renault F1 Team in 2010, Lotus Renault GP in 2011 and Caterham F1 Team in 2012.  Born in Vyborg, he is known as the \"Vyborg Rocket\" (Russian: Вы́боргская Раке́та ; ] ) in Russia.  He was the first Russian to compete in the Formula One World Championship.\n\nWill Stevens: William \"Will\" Stevens (born 28 June 1991 in Rochford, Essex) is a British racing driver, who formerly competed in the Formula One, Eurocup Formula Renault 2.0, Toyota Racing Series and the British Formula Renault Championships.  In Formula One, he made his debut at the 2014 Abu Dhabi Grand Prix with Caterham F1, replacing Marcus Ericsson for the double points race.  During the 2015 season he competed with the Manor Marussia F1 Team.  s of October 2016 , he races in the FIA World Endurance Championship, with G-Drive Racing in the LMP2 category.\n\nColin Kolles: Colin Kolles (born Călin Colesnic 13 December 1967 in Timişoara, Romania) is the former team principal and managing director of the Hispania Racing F1 Team, previously holding a similar position at the team known under the names Jordan, Midland, Spyker and Force India from 2005 to 2008.  He was an advisor to Caterham F1 and had a part in the unsuccessful Forza Rossa Racing project.\n\nTune Group: Tune Group Sdn Bhd (or Tune Group \"Sendirian Berhad\", meaning 'private limited') is a leisure and entertainment corporation founded by the Malaysian entrepreneurs Tony Fernandes and Kamarudin Meranun.  Tune Group's mission is to provide affordability and accessibility to leisure activities and entertainment, primarily in Asian markets.  It does this via its airline, hotel, telecommunication, financial services, sports, media and creative industries subsidiaries.  Its subsidiaries include: budget airline Air Asia; Caterham Group a motor engine-based technology company, though which it formerly owned the Caterham F1 Team; and Queens Park Rangers, an English football club.  Tune Group was the official shirt sponsor of FA match officials until 2013.\n\nRiad Asmat: Riad Asmat (born 17 November 1971 in Petaling Jaya, Selangor, Malaysia) is the CEO of Caterham F1 Team and Team Principal of the Caterham Racing GP2 team.  He is the son of Perodua Chairman Tan Sri Datuk Asmat Kamaludin.  Tony Fernandes and fellow shareholders Kamarudin Meranun and SM Nasarudin have confirmed that with immediate effect Riad Asmat has been promoted Group CEO of Caterham Group for Caterham F1 Team, Caterham Cars, Caterham Racing, merchandising, engineering and all related interests.\n\nQuestion: The former owner and principal of the Caterham F1 Team founded what company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"founder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the individual who founded the company.\"\n    },\n    \"founder_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the founder in relation to the Caterham F1 Team.\"\n    },\n    \"founded_company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company founded by the individual.\"\n    },\n    \"company_description\": {\n      \"type\": \"string\",\n      \"description\": \"A brief description of the founded company, if available.\"\n    }\n  },\n  \"required\": [\n    \"founder_name\",\n    \"founder_role\",\n    \"founded_company_name\",\n    \"company_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "founder_name": {
        "type": "string",
        "description": "The name of the individual who founded the company."
      },
      "founder_role": {
        "type": "string",
        "description": "The role of the founder in relation to the Caterham F1 Team."
      },
      "founded_company_name": {
        "type": "string",
        "description": "The name of the company founded by the individual."
      },
      "company_description": {
        "type": "string",
        "description": "A brief description of the founded company, if available."
      }
    },
    "required": [
      "founder_name",
      "founder_role",
      "founded_company_name",
      "company_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
