{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGary Turner (musician): Gary Albert Turner is a musician, writer, composer, publisher, record company owner, and film & television developer and producer.  He was born in Adelaide, South Australia, and grew up in the working class suburb of Klemzig.  He is the co-founder and owner of one of the world's leading music education publishers, Koala Music Publications / LearnToPlayMusic.com, and has written over ninety music education books, that have been translated into many languages, with total sales of over twenty million copies.  He is the owner and co-founder of the film, television and new media production company, Angel Phoenix Media.\n\nEiji Tsuburaya: Eiji Tsuburaya (円谷 英二 , Tsuburaya Eiji ) (Eiichi Tsumuraya (圓谷 英一 , Tsumuraya Eiichi ) ; July 10, 1901 – January 25, 1970, in Sukagawa, Fukushima) was a Japanese special effects director responsible for many Japanese science-fiction films and television series, being one of the co-creators of the \"Godzilla\" series, as well as the main creator of the \"Ultra Series\".  During his rise to post-war fame in the wake of \"Godzilla\" (1954), many press accounts gave Tsuburaya's birthdate as July 7, which falls on the high day of the star festival, \"Tanabata\", a sign of good fortune.  This is akin to an American saying that they were born on the Fourth of July.  Tsuburaya's actual birthdate of July 10 has been verified by his last surviving son, Akira, and the company Eiji founded, Tsuburaya Productions, as the official entry in the Tsuburaya Family Register, in researching the official English-language biography on this important figure of cinema, \"Eiji Tsuburaya: Master of Monsters\", Chronicle Books, 2007.\n\nDigital credential: Digital credentials are the digital equivalent of paper-based credentials.  Just as a paper-based credential could be a passport, a driver's license, a membership certificate or some kind of ticket to obtain some service, such as a cinema ticket or a public transport ticket, a digital credential is a proof of qualification, competence, or clearance that is attached to a person.  Also, digital credentials prove something about their owner.  Both types of credentials may contain personal information such as the person's name, birthplace, birthdate, and/or biometric information such as a picture or a finger print.\n\nTrademark dilution: Trademark dilution is a trademark law concept giving the owner of a famous trademark standing to forbid others from using that mark in a way that would lessen its uniqueness.  In most cases, trademark dilution involves an unauthorized use of another's trademark on products that do not compete with, and have little connection with, those of the trademark owner.  For example, a famous trademark used by one company to refer to hair care products might be \"diluted\" if another company began using a similar mark to refer to breakfast cereals or spark plugs. Dilution is a basis of trademark infringement that only applies to famous marks.  With non-famous marks, the owner of the mark must show that the allegedly infringing use creates a likelihood of confusion as to the source of the product or service being identified by the allegedly infringing use.  With non-famous marks, it is highly unlikely a likelihood of confusion will be found if the products or services are in unrelated markets.  However, with famous marks, any use by another person of the mark has the potential for confusion, since a famous mark is so well known among the consuming public that people will assume affiliation with the owner of the mark regardless of the product or service being sold under the infringing use.\n\nAlexander Volchek: Alexander Volchek (Russian: Александр Волчек ; born 15 March 1983 Minsk Belarus) is a Russian entrepreneur, CEO and Owner of AGRO24 / АГРО24 marketplace, information and analytics platform for grocery.  In the past he has been the CEO and Owner of training company Business Molodost, CEO of the leading Russian SaaS provider Megaplan, Owner of software development company iTecGroup.\n\nStreet name securities: The phrase street name securities or \"nominee name securities\" is used in the United States to refer to securities of companies which are held electronically in the account of a stockbroker or bank or custodian, similar to a bank account.  The entity whose name is recorded as the legal owner of the securities is known as the \"nominee owner,\" and that entity has ownership rights in the security.  The nominee owner holds those ownership rights on behalf of the true economic owner who is referred to as the beneficial owner.  In the US, Cede & Co., a nominee of Depository Trust Company, is typically the largest stockholder of a company.  In the US where Cede & Co. is the street name holder, therefore, all beneficial rights such as voting rights and dividends flow first to the nominee holder Cede, and then are passed onward, and ultimately to the beneficial owners.  In the United Kingdom this is known as holding shares in a nominee account.\n\nSeb Bishop: Sebastian Luke (Seb) Bishop (born 1974) was the CEO of GOOP, Gwyneth Paltrow's lifestyle company, from 2011 to 2014.  Prior to joining GOOP, Bishop was the International CEO of (RED), the organisation created by Bono and Bobby Shriver to raise money for The Global Fund to Fight AIDS, Tuberculosis and Malaria.  He had previously started the firm Espotting at the age of 26.\n\nGwyneth Paltrow: Gwyneth Kate Paltrow (born September 27, 1972) is an American actress, singer, and food writer.  Following early notice for her work in films such as \"Seven\" (1995), \"Emma\" (1996), \"Sliding Doors\" (1998) and \"A Perfect Murder\" (1998), Paltrow rose to worldwide recognition for her performance in \"Shakespeare in Love\" (1998), winning the Academy Award and the Golden Globe Award for Best Actress.\n\nJerry Moyes: Jerry Moyes is the founder, chairman and CEO of Phoenix-based Swift Transportation, one of the largest trucking companies in the United States.  Moyes is also owner of charter airline Swift Air.  Moyes is also controlling owner of SME Steel Contractors Inc., a steel erector company based in Utah.  He was a majority owner of the Phoenix Coyotes of the National Hockey League before the Coyotes filed bankruptcy and were sold to the NHL in 2009, and the Arizona Sting of the National Lacrosse League.  Moyes is also a limited partner in the Arizona Diamondbacks, and was once a minority owner of the Phoenix Suns.\n\nGoop (company): Goop (often stylized as goop) is a company owned by actress Gwyneth Paltrow.  It was launched as a \"lifestyle brand\" by Paltrow in September 2008, beginning as a weekly e-mail newsletter providing new age advice, such as \"police your thoughts\" and \"eliminate white foods\", and the slogan \"Nourish the Inner Aspect\".  A lifestyle website was later added, and then Goop expanded into e-commerce, collaborating with fashion brands, launching pop-up shops, and holding a \"wellness summit\".\n\nQuestion: What is the birthdate of the owner of the company Goop?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person.\"\n    },\n    \"person_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the person in relation to the company.\"\n    },\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company.\"\n    },\n    \"birthdate_full\": {\n      \"type\": \"string\",\n      \"description\": \"The full birthdate of the person.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the person.\"\n    },\n    \"birth_month\": {\n      \"type\": \"string\",\n      \"description\": \"The birth month of the person.\"\n    },\n    \"birth_day\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth day of the month for the person.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"person_role\",\n    \"company_name\",\n    \"birthdate_full\",\n    \"birth_year\",\n    \"birth_month\",\n    \"birth_day\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person."
      },
      "person_role": {
        "type": "string",
        "description": "The role of the person in relation to the company."
      },
      "company_name": {
        "type": "string",
        "description": "The name of the company."
      },
      "birthdate_full": {
        "type": "string",
        "description": "The full birthdate of the person."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the person."
      },
      "birth_month": {
        "type": "string",
        "description": "The birth month of the person."
      },
      "birth_day": {
        "type": "integer",
        "description": "The birth day of the month for the person."
      }
    },
    "required": [
      "person_name",
      "person_role",
      "company_name",
      "birthdate_full",
      "birth_year",
      "birth_month",
      "birth_day"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
