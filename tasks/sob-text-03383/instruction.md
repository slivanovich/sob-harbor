{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nVirgin Mobile France: Virgin Mobile France was a cellular telephone operator in France.  It launched in 2006 as a joint venture between Virgin Group and Carphone Warehouse.  The company operated as a mobile virtual network operator (MVNO), whereby it did not own or operate its own mobile network but instead used the network of Orange S.A. As of June 2014, the company was the largest MVNO in France, with 1.5 million customers, and had a market share of 1.3% at the beginning of 2014.\n\nCoop (Italy): Coop is a system of Italian consumers' cooperatives which operates the largest supermarket chain in Italy.  Its headquarters are located in Casalecchio di Reno, Province of Bologna.\n\nMobile country code: The ITU-T Recommendation E.212 defines mobile country codes as well as mobile network codes.  The mobile country code consists of 3 decimal digits and the mobile network code consists of 2 or 3 decimal digits (for example: MNC of 001 is not the same as MNC of 01).  The first digit of the mobile country code identifies the geographic region as follows (the digits 1 and 8 are not used):\n\nCoopVoce: CoopVoce is an Italy-based Mobile virtual network operator launched on June 1, 2007 by the owner Coop and based on Telecom Italia Mobile GSM/GPRS network.\n\nOrange Slovensko: Orange Slovensko, a.s. is a Slovak mobile network operator, also offering fibre connections, since 15 January 1997 (previously named Globtel), when it became the first mobile operator in Slovakia to operate the GSM digital mobile network at the 900 MHz frequency.  On 15 November 1999, the company launched the commercial operation of the mobile network in the 1800 MHz frequency band.  It is also the first company to cover more than 66% of the country with 3G HSDPA high-speed internet with the maximum speed of 42 Mbit/s, launched the HSPA+ upgrade to the maximum of 21.2-42.2 Mbit/s in 2011.  The operator plans to commercially operate LTE network by the end of 2012.\n\nZong Pakistan: Zong (Urdu: ‎ ) or China Mobile Pakistan is a pan Pakistan mobile network operator headquartered in Islamabad, which offers voice and data services ranging from postpaid and prepaid plans, 2G, 3G and 4G services, mobile banking to fixed telephony.  It is the first oversea setup of China Mobile through acquisition of a license from Millicom to operate a GSM network in Pakistan in 2008.\n\nVodafone Hungary: Vodafone Hungary, member of the Vodafone Group is a mobile telephone company in Hungary.  It started to operate in 1999 after securing the third GSM 900/1800 MHz license of the country and it was the first provider operating in the DCS-1800 band in Hungary.  Vodafone is the third largest mobile network operator of the country, and controlling 22,84% of the market as of June 2012.\n\nVodafone Czech Republic: Vodafone Czech Republic a.s. is a Czech telecommunications company.  It is among the largest Czech companies by revenue.  It was established as Český Mobil (Czech Mobile) in 1999, when the government of Miloš Zeman granted it a free license to operate the third mobile GSM network.  Its mobile network was called Oskar; the company itself was renamed in September 2004 to Oskar Mobil.  In 2005 the international company Vodafone became the sole shareholder, which in November 2005, approved the most recent change in the company name.  Czech Vodafone currently has over 3 million customers.  The director is Balesh Sharma since the end of 2013.\n\nLocation area identity: Each location area of a public land mobile network (PLMN) has its own unique identifier which is known as its location area identity (LAI).  This internationally unique identifier is used for location updating of mobile subscribers.  It is composed of a three decimal digit mobile country code (MCC), a two to three digit mobile network code (MNC) that identifies a Subscriber Module Public Land Mobile Network (SM PLMN) in that country, and a location area code (LAC) which is a 16 bit number with two special values, thereby allowing 65534 location areas within one GSM PLMN.as briefed to Mr Deepji on 25 Sep 17.\n\nIrish Continental Group: Irish Continental Group is an Irish shipping and transport group.  Operating roll on/roll off passenger, freight and container freight services on routes between Ireland, the United Kingdom and Continental Europe.  Irish Continental Group also operate container terminals in the ports of Dublin and Belfast.\n\nQuestion: In which country does the Coop supermarket group also operate a mobile network, called CoopVoce?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"country_name\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the Coop supermarket group and CoopVoce operate.\"\n    },\n    \"supermarket_group\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the supermarket group.\"\n        },\n        \"headquarters_location\": {\n          \"type\": \"string\",\n          \"description\": \"The location of the supermarket group's headquarters.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"headquarters_location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"mobile_network_operator\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the mobile virtual network operator.\"\n        },\n        \"launch_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the mobile network operator was launched.\"\n        },\n        \"owner\": {\n          \"type\": \"string\",\n          \"description\": \"The owner of the mobile network operator.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of mobile network operator (e.g., MVNO).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"launch_date\",\n        \"owner\",\n        \"type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"country_name\",\n    \"supermarket_group\",\n    \"mobile_network_operator\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "country_name": {
        "type": "string",
        "description": "The country where the Coop supermarket group and CoopVoce operate."
      },
      "supermarket_group": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the supermarket group."
          },
          "headquarters_location": {
            "type": "string",
            "description": "The location of the supermarket group's headquarters."
          }
        },
        "required": [
          "name",
          "headquarters_location"
        ],
        "additionalProperties": false
      },
      "mobile_network_operator": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the mobile virtual network operator."
          },
          "launch_date": {
            "type": "string",
            "description": "The date the mobile network operator was launched."
          },
          "owner": {
            "type": "string",
            "description": "The owner of the mobile network operator."
          },
          "type": {
            "type": "string",
            "description": "The type of mobile network operator (e.g., MVNO)."
          }
        },
        "required": [
          "name",
          "launch_date",
          "owner",
          "type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "country_name",
      "supermarket_group",
      "mobile_network_operator"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
