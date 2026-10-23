{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPodesta Group: The Podesta Group is a lobbying and public affairs firm based in Washington, D.C..  It was founded in 1988 by brothers John Podesta and Tony Podesta and has previously been known as Podesta Associates, podesta.com and PodestaMattoon.  The firm most recently reorganized in January 2007 after current Chairman Tony Podesta split with former business partner Dan Mattoon.\n\nAtef Yassien El Sherif: Atef Yassien ElSherif was the former chairman of the Egyptian Exchange (July 2013 – August 2013) , the former chairman counselors of the Egyptian Exchange and the founder and principal partner of ElSherif Law Firm & Consultants.ElSherif represents the Egyptian Exchange in many stock exchange conferences and International, African & Arabian stock market unions and contributes in preparation of many of legislations and Egyptian stock market rules since joining the Egyptian Exchange in 1994 to 2015.  and also he contributes in establishing the Damascus Securities Exchange and the Libyan Stock Market.  He also is the founder and board member of Egyptian investor relations association (EIRA).\n\nPolitiquera: A politiquera in the United States is an individual who is paid for by an election campaign to knock on doors to issue fliers and encourage people to get out and vote in favour of the candidate.  Candidates who generally lack the grass root volunteers who normally do this job, resort to politiqueras to achieve the goal.  Use of politiqueras in southern regions of Texas during the democratic primary on March 4, 2008 by Hillary Clinton campaign is one such example.\n\nStephanie Hannon: Stephanie Hannon (born October 31, 1974) was the chief technology officer (CTO) of Hillary Clinton's 2016 presidential campaign.  She was the first woman to hold the title of CTO on a major presidential campaign.  Prior to working for the Clinton campaign, Hannon was Google's director of product management for civic innovation and social impact.  Her focus was on building tools to help communities respond to natural disasters as well as producing and sharing transparent election results.  She worked previously as a product manager on Google Maps and Google Wave.\n\nJohn Podesta: John David Podesta (born January 8, 1949) is a columnist and former chairman of the 2016 Hillary Clinton presidential campaign.  He previously served as chief of staff to President Bill Clinton and Counselor to President Barack Obama.\n\n2016 United States presidential election recounts: Following Republican nominee Donald Trump's presumed electoral college victory in the United States presidential election of 2016, a group of computer scientists, cyber security experts, and election monitors raised concerns about the integrity of the election results.  They urged the campaign staff of Democratic nominee Hillary Clinton, who had conceded the campaign on November 9, to petition for a recount in three key states: Michigan, Pennsylvania, and Wisconsin.  When the Clinton campaign declined to file for recounts, Green Party presidential nominee Jill Stein agreed to spearhead the recount effort on November 23, on the grounds that unspecified \"anomalies\" may have affected the election's outcome.  The Clinton team subsequently pledged to support the recount efforts \"in order to ensure the process proceeds in a manner that is fair to all sides.\"  President-elect Trump and his supporters filed legal motions in all three states to prevent the recounts.  Two other states were the subject of recount bids that were separate from Stein's efforts in the Rust Belt states: American Delta Party/Reform Party presidential candidate Rocky De La Fuente filed for a partial recount in Nevada on November 30, and three Florida citizens filed for a complete hand recount in their state on December 6.\n\nKarl Friedrich von Lindenau: Karl Friedrich von Lindenau (1746 – 21 February 1817), served in the Prussian army before an incident compelled him to switch allegiance to Habsburg Austria in 1789.  A staff officer at the beginning of the French Revolutionary Wars, he was asked to mentor the young Archduke Charles, Duke of Teschen.  The association with Charles lasted for the rest of his military career.  After being promoted to general officer in 1797, he led a brigade during the 1799 campaign and was elevated in rank to division commander.  In 1803 he was appointed Proprietor (Inhaber) of an infantry regiment.  In 1805 he fought with distinction while leading a grenadier division in Italy.  The 1809 campaign found him leading an infantry division in Germany, after which he retired from active service.\n\nPantsuit Nation: Pantsuit Nation is a private Facebook group and Twitter hashtag used to rally camaraderie among Hillary Clinton supporters during her 2016 presidential campaign.  Though the group is not affiliated with a political party, its symbol—the pantsuit—was used as a metonym for Hillary Clinton's 2016 presidential campaign similar to how the color red was used for the campaign of her opponent, Donald Trump.  At the time of the November 2016 election, the group had 2.9 million members and had raised US $170,000 for the Clinton campaign.\n\nVanni Treves: Vanni Emanuele Treves CBE (born 1940 in Florence, Italy) is a former Chairman of Channel 4, former Senior Partner of City law firm Macfarlanes and former Chairman (2001-2009) of Equitable Life.\n\nIan Lang Livingstone: Ian Lang Livingstone, CBE, DL (born 23 February 1938) is a Scottish businessman; former Chairman of the board of Motherwell College; former Chairman of Motherwell Football Club; former Chairman of Lanarkshire Health Board; and former Chairman of the Lanarkshire Development Agency.\n\nQuestion: In what year did the former chairman of the 2016 Clinton campaign found a firm in D.C.?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the individual who founded the firm.\"\n    },\n    \"role_in_campaign\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the individual in the 2016 Clinton campaign.\"\n    },\n    \"firm_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the firm founded by the individual.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the firm was founded.\"\n    },\n    \"firm_location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the firm is based.\"\n    },\n    \"co_founder_present\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if there was a co-founder for the firm.\"\n    },\n    \"co_founder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-founder, if any.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"role_in_campaign\",\n    \"firm_name\",\n    \"founding_year\",\n    \"firm_location\",\n    \"co_founder_present\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the individual who founded the firm."
      },
      "role_in_campaign": {
        "type": "string",
        "description": "The role of the individual in the 2016 Clinton campaign."
      },
      "firm_name": {
        "type": "string",
        "description": "The name of the firm founded by the individual."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the firm was founded."
      },
      "firm_location": {
        "type": "string",
        "description": "The city and state where the firm is based."
      },
      "co_founder_present": {
        "type": "boolean",
        "description": "Indicates if there was a co-founder for the firm."
      },
      "co_founder_name": {
        "type": "string",
        "description": "The name of the co-founder, if any."
      }
    },
    "required": [
      "person_name",
      "role_in_campaign",
      "firm_name",
      "founding_year",
      "firm_location",
      "co_founder_present"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
