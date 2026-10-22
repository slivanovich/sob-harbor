Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Israeli presidential election, 2014: Indirect presidential elections were held in Israel on 10 June 2014.  The result was a victory for Reuven Rivlin of Likud.  Rivlin was sworn in on 24 July.

Presidency of Shimon Peres: The Presidency of Shimon Peres, the ninth President of Israel, began after the Israeli presidential election, 2007 on 13 June 2007 in which Peres defeated Reuven Rivlin and Colette Avital.  Peres was sworn in as President on 15 July 2007.

Rivka Ravitz: Rivka Ravitz (Hebrew: רבקה רביץ‎ , born 1976) is an Israeli Haredi political administrator.  Since 1999, she has worked for Israeli politician Reuven Rivlin, first as his bureau chief and campaign adviser, and, since his election as President of Israel in 2014, as his chief of staff.  She has received extensive media coverage for being a Haredi mother of 11 in a high-profile political position.

President of Israel: The President of the State of Israel (Hebrew: נָשִׂיא מְדִינַת יִשְׂרָאֵל‎ , "Nasi Medinat Yisra'el", or Hebrew: נָשִׂיא הַמְדִינָה‎ , "Nasi HaMedina", lit.  "President of the State") is the head of state of Israel.  The position is largely a ceremonial figurehead role, with executive power effectively being exercised by the prime minister.  The current president is Reuven Rivlin, who took office on 24 July 2014.  Presidents are elected by the Knesset for a seven-year term and are limited to a single term.

Israeli presidential election, 2007: Indirect presidential elections were held in Israel on 13 June 2007.  The Knesset elected Shimon Peres, a former Prime Minister and a member of the Kadima party.  His opponents were Reuven Rivlin, a former Knesset speaker, of the Likud Party, and Colette Avital, of the Labor party.  After the first round of voting put Peres in a commanding lead, but just short of the absolute majority required for election, Rivlin and Avital bowed out and Peres was elected easily in the second round.

Israeli presidential election, 1957: An election for President of Israel was held in the Knesset on 28 October 1957 following the end of Yitzhak Ben-Zvi's five-year term in office.  Ben-Zvi stood again, and it was suggested that Yosef-Yoel Rivlin (father of Reuven Rivlin) would run against him as a representative of Herut.  However, in the end Rivlin did not participate in the election.

David Saranga: David Saranga (Hebrew: דוד סרנגה‎ ‎ ) (born February 18, 1964) is an Israeli diplomat who serves as the Senior Foreign Affairs Advisor to the President of the State of Israel, Reuven (Ruvi) Rivlin, and former Head of European Parliament Liaison Department at the Israeli embassy in Brussels.  Prior to that he served as Consul for Media and Public Affairs of Israel in the United States.  Saranga was responsible for Israel’s image in the United States and was the liaison person of Israel to the American media. " The Jewish Chronicle" described him as “The man whose campaigns are rebranding Israel."  Saranga’s initiative to invite "Maxim" magazine to Israel generated debate about the definition of public diplomacy.  Prof. John H. Brown of Georgetown University described this initiative as the first event in a new branch of Public Diplomacy.  Saranga was the first diplomat who implemented Web 2.0 governmental initiatives, including the first official blog of a country, a MySpace page, YouTube channel, Facebook page and a political blog.

Nechama Rivlin: Nechama Rivlin (Hebrew: נחמה ריבלין‎ ‎ ; born 5 June 1945) is the First Lady of Israel.  She is married to the current President of Israel, Reuven Rivlin.

Lehava: Lehava (Hebrew: למניעת התבוללות בארץ הקודש‎ ‎ "LeMeniat Hitbolelut B'eretz HaKodesh"; "Prevention of Assimilation in the Holy Land") is a Jewish far-right organization based in Israel that strictly opposes Jewish assimilation, objecting to personal relationships between Jews and non-Jews.  It is opposed to the Christian presence in Israel.  It has an anti-miscegenation focus, denouncing marriages between Jewish women and non-Jewish, particularly Arab, men.  Its actions have been denounced by President of Israel Reuven Rivlin as being like "rodents gnawing under the shared democratic and Jewish foundation of Israel".

Reuven Rivlin: Reuven "Ruvi" Rivlin (Hebrew: רְאוּבֵן "רוּבִי" רִיבְלִין‎ , ] ; born 9 September 1939) is an Israeli politician and lawyer who has been the tenth and current President of Israel since 2014.  He is a member of the Likud party.  Rivlin was Minister of Communications from 2001 to 2003, and subsequently served as Speaker of the Knesset from 2003 to 2006, and again from 2009 to 2013.  On 10 June 2014, he was elected President of Israel.

Question: Lehava, is a Jewish far-right organization based in Israel that strictly opposes Jewish assimilation, objecting to personal relationships between Jews and non-Jews, its actions have been denounced by Reuven Rivlin, current President of Israel since which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "organization_name": {
      "type": "string",
      "description": "The name of the organization being discussed."
    },
    "denouncer_name": {
      "type": "string",
      "description": "The name of the person who denounced the organization."
    },
    "denouncer_role": {
      "type": "string",
      "description": "The political role of the denouncer at the time of denouncement."
    },
    "denouncer_political_party": {
      "type": "string",
      "description": "The political party of the denouncer."
    },
    "presidency_start_year": {
      "type": "integer",
      "description": "The year Reuven Rivlin began his term as President of Israel."
    },
    "denouncement_quote": {
      "type": "string",
      "description": "The specific quote used by Reuven Rivlin to denounce the organization."
    }
  },
  "required": [
    "organization_name",
    "denouncer_name",
    "denouncer_role",
    "denouncer_political_party",
    "presidency_start_year",
    "denouncement_quote"
  ],
  "additionalProperties": false
}
