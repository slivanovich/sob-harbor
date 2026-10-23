{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSyrian-Qatari Holding Company: The Syrian-Qatari Holding Company (SQHC) is a holding company founded in 2008 and based in Damascus that is equally owned by the governments of Syria and Qatar.  With a declared capital of USD 5 billion it is Syria's largest holding company.  The company has invested or plans to invest, among others, in power generation, agriculture, dairy and juice manufacturing, phosphate fertilizers, health care, real estate, financial services and fuel distribution.  In October 2009 it signed a Memorandum of Understanding with the Syrian Ministry of Housing and Construction to invest in wastewater treatment.  Qatar’s shares are held by Qatar Investment Authority.\n\nEric Copeland: Eric Copeland is an experimental musician based in New York City.  He is a core member of Black Dice and forms half of the duo Terrestrial Tones with Animal Collective's Avey Tare.\n\nHolding company: A holding company is a company that owns other companies' outstanding stock.  The term usually refers to a company that does not produce goods or services itself; rather, its purpose is to own shares of other companies to form a corporate group.  Holding companies allow the reduction of risk for the owners and can allow the ownership and control of a number of different companies.\n\nHongkong Chinese Limited: The HKCB Bank Holding Company Limited was incorporated in 1992 (and registered as a foreign company in Hong Kong on 20 October 1992).  In 2001, the subsidiary Hongkong Chinese Bank was sold to CITIC Ka Wah Bank for HK$4.2 billion.  The holding company itself was renamed to Hongkong Chinese Limited on 8 February 2002.  In the same year 85% shares of Macau Chinese Bank and 85% stake of ImPac Asset Management were acquired, for MOP$190 million (from and Alvaro Pinho da Costa Leite) and US$2.125 million (from ImPac Partners) respectively.  An additional 15% shares of the bank were acquired from Wong Kon Kei in September 2007, for MOP$47.2 million.  In the same year Hongkong Chinese Limited proposed to sell 60% shares of the intermediate holding company of the bank, Winwise Holdings Limited.  However, the deal collapsed.\n\nTerrestrial Tones: Terrestrial Tones are Dave Portner of Animal Collective and Eric Copeland of Black Dice.  The two were roommates who got together to record when both of their respective main bands went on temporary hiatus in November 2004.\n\nPost Present Medium: Post Present Medium (or PPM) is a record label started and run by Dean Allen Spunt, also from the band No Age.  Since he started the label in 2001 with the release of a 7\" by Portland/Olympia natives The Intima, PPM has released over 50 records.  Some of those artists include Mika Miko, Abe Vigoda, Barr, Best Coast, No Age, Gun Outfit, Silk Flowers, John Wiese, Eric Copeland, Infinite Body, and SFV Acid.\n\nCommercial National Financial: Commercial National Financial Corporation is a registered financial holding company under the Bank Holding Company Act of 1956 as amended.  The company wholly owns Commercial Bank & Trust of PA under the Bank Holding Company Act.  The company’s principal business is the operation of Commercial Bank & Trust of PA, which offers various commercial banking and trust services including offering deposit services, providing financial counseling, investing and extending credit.  Commercial National Financial Corporation uses CNAF as the trading symbol on the OTCQB tier of the OTC Markets.\n\nKingdom Holding Company: The Kingdom Holding Company (Arabic: شركة المملكة القابضة‎ ‎ ) is a Saudi conglomerate holding company based in Riyadh.  The Kingdom Holding Company (KHC) is a publicly listed company on the Tadawul (Saudi Stock Exchange).  The KHC consists of a select team of experienced investment specialists directed by its founder and chairman, HRH Prince Alwaleed bin Talal and Chief Executive Officer, Eng.  Talal Ibrahim Al Maiman.  The company describes itself as a diversified investment company, whose main interests are financial services, real estate, tourism and hospitality, media, entertainment, petrochemicals, aviation and technology.\n\nCTBC Financial Holding: CTBC Financial Holding Co., Ltd. (Former: Chinatrust Financial Holding Company Ltd.) is a holding company principally engaged in the finance industry through its eight major subsidiaries.  Assets — $115.7 billion (2015).  The holding company is based in CTBC Financial Park, Taipei, Taiwan.\n\nJohn Eric Copeland: John Eric Copeland (known professionally as Eric Copeland) is a Christian and jazz music producer, arranger, songwriter, author, and keyboardist.  His production company Creative Soul works with Christian and jazz artists both nationally and internationally, and is the parent company to Creative Soul Records, Creative Soul Jazz, and Masterscore Music, all based near Nashville, Tennessee.  As an artist, he is noted for his unique arrangements and songwriting fusing gospel and jazz styles together.\n\nQuestion: What is the name of John Eric Copeland's holding company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the person.\"\n    },\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the holding company.\"\n    },\n    \"company_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of company, e.g., 'holding company' or 'production company'.\"\n    },\n    \"company_purpose\": {\n      \"type\": \"string\",\n      \"description\": \"The primary business or purpose of the company.\"\n    },\n    \"subsidiaries\": {\n      \"type\": \"array\",\n      \"description\": \"A list of companies that are parented by the holding company.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"company_name\",\n    \"company_type\",\n    \"company_purpose\",\n    \"subsidiaries\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the person."
      },
      "company_name": {
        "type": "string",
        "description": "The name of the holding company."
      },
      "company_type": {
        "type": "string",
        "description": "The type of company, e.g., 'holding company' or 'production company'."
      },
      "company_purpose": {
        "type": "string",
        "description": "The primary business or purpose of the company."
      },
      "subsidiaries": {
        "type": "array",
        "description": "A list of companies that are parented by the holding company.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "person_name",
      "company_name",
      "company_type",
      "company_purpose",
      "subsidiaries"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
