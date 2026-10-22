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
J. Paul Getty: Jean Paul Getty (December 15, 1892 – June 6, 1976) was an American industrialist.  He founded the Getty Oil Company, and in 1957 "Fortune" magazine named him the richest living American, while the 1966 Guinness Book of Records named him as the world's richest private citizen, worth an estimated $1.2 billion (approximately $ billion in 2016).  At his death, he was worth more than $2 billion (approximately $ billion in 2016).  A book published in 1996 ranked him as the 67th richest American who ever lived, based on his wealth as a percentage of the gross national product.

Trust (U.S. TV series): Trust is an upcoming American television anthology series.  The series was ordered by and will premiere on FX in January 2018.  "Trust"'s 10-episode first season is set in 1973 and centers on John Paul Getty III, then-heir to Getty Oil.  The first season will be written by Simon Beaufoy and directed by Danny Boyle.

John Paul Getty Jr.: Sir John Paul Getty, KBE (born Eugene Paul Getty; 7 September 1932 – 17 April 2003), was a wealthy American-born British philanthropist and book collector.  He was the elder son of Jean Paul Getty Sr. (1892–1976), one of the richest men in the world at the time, and his wife Ann Rork.  The Getty family's wealth was the result of the oil business founded by George Franklin Getty.  At birth he was given the name Eugene Paul Getty, but in later life he adopted other names, including Paul Getty, John Paul Getty, Jean Paul Getty Jr., and John Paul Getty II.  A long-time Anglophile, he became a British citizen in 1997.  In 1986, he was awarded an honorary knighthood for services to causes ranging from cricket, to art and to the Conservative Party.  His honorary knighthood became substantive when he became a British citizen.  In 1998 he changed his name by deed poll when he renounced the first name Eugene and wished to be known as Sir Paul Getty, KBE.

Damien Hirst: Damien Steven Hirst ( ; born 7 June 1965) is an English artist, entrepreneur, and art collector.  He is the most prominent member of the group known as the Young British Artists (or YBAs), who dominated the art scene in the UK during the 1990s.  He is internationally renowned, and is reportedly the United Kingdom's richest living artist, with his wealth valued at £215M in the 2010 "Sunday Times" Rich List.  During the 1990s his career was closely linked with the collector Charles Saatchi, but increasing frictions came to a head in 2003 and the relationship ended.

Skelly Oil: Skelly Oil Company was a medium-sized oil company founded in 1919 by William Grove (Bill) Skelly, Chesley Coleman Herndon and Frederick A. Pielsticker in Tulsa, Oklahoma.  J. Paul Getty acquired control of the company during the 1930s.  Skelly Oil became part of Getty Oil Company, Mission Oil Company, Tidewater Oil Company.  It became defunct when absorbed by Getty Oil Company in 1974, and the abandoned Skelly brand logo was revived by Nimmons-Joliet Development Corp. in 2012.

Mohammed Hussein Al Amoudi: Mohammed Hussein Ali Al-'Amoudi (Amharic: , Arabic: محمد حسين علي العمودي‎ ‎ ) is a Saudi Arabian and Ethiopian billionaire businessman.  In 2016, his net worth was estimated by "Forbes" at approximately $10.9 billion and a relative fall in net value was linked to the global fall in oil and gold prices at the time of estimation.  He was also listed as Ethiopia's richest man, the second richest Saudi Arabian citizen in the world and the second richest black person in the world.  Al Amoudi made his fortune in construction and real estate before branching out to buy oil refineries in Sweden and Morocco.  He is the largest individual foreign investor in Ethiopia and a major investor in Sweden.

Getty Oil: Getty Oil is an American oil marketing company with its origins as part of the large integrated oil company founded by the father of J. Paul Getty.

Ludvig Nobel: Ludvig Immanuel Nobel ( ; Russian: Лю́двиг Эммануи́лович Нобе́ль; Swedish: "Ludvig Emmanuel Nobel" ] ; 27 July 1831, Stockholm – 12 April 1888, Cannes) was a Swedish-Russian engineer, a noted businessman and a humanitarian.  One of the most prominent members of the Nobel family, he was the son of Immanuel Nobel (also an engineering pioneer) and the older brother of Alfred Nobel (founder of the Nobel Prize).  With his brother Robert, he operated Branobel, an oil company in Baku, Azerbaijan which at one point produced 50% of the world's oil.  He is credited with creating the Russian oil industry.  Ludvig Nobel built the largest fortune of any of the Nobel brothers and was one of the world's richest men.  Following the Bolshevik revolution, the communists confiscated the Nobel family's vast fortune in Russia.

Gordon Getty: Gordon Peter Getty (born December 20, 1933) is an American businessman, investor, philanthropist and classical music composer, the fourth child of oil tycoon J. Paul Getty.  His mother, Ann Rork, was his father's fourth wife.  When his father died in 1976, Gordon assumed control of Getty's US$2 billion trust.  According to the Forbes 400, as of September 2011 his net worth is $2 billion, making him number 212 on the list of the richest Americans.

Andrew Vicari: Andrew Vicari (born Andrea Antonio Giovanni Vaccari, 20 April 1932 – 3 October 2016) was a Welsh painter working in France, who established a career painting portraits of prominent people.  Despite being largely unknown in his own country, as of 2004 Vicari was Britain's richest living painter, and at one time Britain 18th richest person.

Question: In what year did the founder of Getty Oil get coined the "Fortune" magazine's richest living American?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who was named the richest American."
    },
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine that awarded the title."
    },
    "title_awarded": {
      "type": "string",
      "description": "The specific title or recognition given by the magazine."
    },
    "year_awarded": {
      "type": "integer",
      "description": "The year the person was named the richest living American by the magazine."
    }
  },
  "required": [
    "person_name",
    "magazine_name",
    "title_awarded",
    "year_awarded"
  ],
  "additionalProperties": false
}
