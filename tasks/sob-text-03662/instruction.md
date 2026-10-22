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
Riverina: is an agricultural region of South-Western New South Wales (NSW), Australia.  The Riverina is distinguished from other Australian regions by the combination of flat plains, warm to hot climate and an ample supply of water for irrigation.  This combination has allowed the Riverina to develop into one of the most productive and agriculturally diverse areas of Australia.  Bordered on the south by the state of Victoria and on the east by the Great Dividing Range, the Riverina covers those areas of New South Wales in the Murray and Murrumbidgee drainage zones to their confluence in the west.

Michael McCormack (Australian politician): Michael Francis McCormack (born 2 August 1964), an Australian federal politician, is a member of the Australian House of Representatives representing the seat of Riverina, New South Wales for the National Party of Australia, elected at the 2010 federal election.

John Barilaro: Giovanni Domenic "John" Barilaro, an Australian politician, is the 18th Deputy Premier of New South Wales, the Minister for Regional Development (later renamed as the Minister for Regional New South Wales), Minister for Small Business, and Minister for Skills since October 2014, and the New South Wales Leader of The Nationals since November 2016.

New South Wales wine: New South Wales wine is Australian wine produced in New South Wales, Australia.  New South Wales is Australia's most populous state and its wine consumption far outpaces the region's wine production.  The Hunter Valley, located 130 km north of Sydney, is the most well-known wine region but the majority of the state's production takes place in the Big Rivers zone-Perricoota, Riverina and along the Darling and Murray Rivers.  The wines produced from the Big Rivers zone are largely used in box wine and mass-produced wine brands such as Yellow Tail.  A large variety of grapes are grown in New South Wales, including Cabernet Sauvignon, Chardonnay, Shiraz and Sémillon.

Triple M Riverina MIA 963: Triple M Riverina MIA 963 (call sign 2RG) is an Australian radio station in New South Wales.  Owned and operated as part of Southern Cross Austereo's LocalWorks network, it broadcasts a classic hits format to Griffith, New South Wales and surrounding areas.  The station launched on 15 September 1936, and marked only the second commercial radio station to launch in the Riverina.  The station was formerly operated by DMG Regional Radio, Macquarie Regional RadioWorks, and Southern Cross Media Group - and broadcasts from studios in Griffith alongside sister station hit99.7 Riverina MIA.

Minister for Small Business (Australia): The Australian Minister for Small Business is the Hon. Michael McCormack {'1': ", '2': ", '3': ", '4': "} .

Steve Whan: Steven James Robert "Steve" Whan ( ) (born 11 February 1964), an Australian politician, was a member of the New South Wales Legislative Council from 2011 to 2015.  Whan represented the electoral district of Monaro in the New South Wales Legislative Assembly for the Australian Labor Party from 2003 until his defeat at the 2011 state election.  Whan served as Minister of Emergency Services, Minister for Small Business and Minister for Rural Affairs in the Rees and Keneally ministries from 2009 to 2011.

Division of Barrier: The Division of Barrier was an Australian Electoral Division in New South Wales.  The division was created in 1900 and was one of the original 75 divisions contested at the first federal election.  It was named for the Barrier Range near the city of Broken Hill in western New South Wales.  In 1901 it included Broken Hill, Wilcannia, White Cliffs and Tibooburra and the surrounding pastoral areas.  In 1906 it gained Menindee, Wentworth from Riverina and in 1913 it gained Balranald and Deniliquin from Riverina.  It was abolished in 1922 with Broken Hill, Wentworth and Balranald being transferred to Darling and Deniliquin transferred to Riverina.  It was a very safe seat for the Australian Labor Party, although both its members left the ALP at the end their terms: Josiah Thomas to join the Nationalists, and Michael Considine (a radical socialist) to sit as an independent.

Jodi McKay: Jodi Leyanne McKay (born 16 August 1969) is an Australian politician.  She is a member of the New South Wales Legislative Assembly, having represented Strathfield for the Australian Labor Party since 2015.  She previously represented Newcastle from 2007 until her defeat at the 2011 election.  Between 2008 and 2011, McKay held a number of junior ministerial responsibilities in the Rees and Keneally governments, including serving as the Minister for the Hunter, Tourism, Small Business, Science and Medical Research, Commerce, and Women, and Minister Assisting the Minister for Health (Cancer).

Division of Riverina-Darling: The Division of Riverina-Darling was an Australian Electoral Division in the state of New South Wales.  It was located in south-west rural New South Wales, and included the towns of Broken Hill, Griffith, Hay and Narrandera.  The Division was created in 1984, largely replacing the abolished division of Riverina.  Its name indicated its relationship with Riverina and the seat of Darling, abolished in 1969.

Question: Which Minister for Small business was also represented the seat of Riverina, New South Wales?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician_name": {
      "type": "string",
      "description": "The full name of the politician who meets the criteria."
    },
    "electoral_division_represented": {
      "type": "string",
      "description": "The electoral division represented by the politician."
    },
    "ministerial_position_held": {
      "type": "string",
      "description": "The specific ministerial role held by the politician."
    },
    "ministerial_level": {
      "type": "string",
      "description": "The level of government for the ministerial position (e.g., Federal, State)."
    },
    "political_party": {
      "type": "string",
      "description": "The political party the politician belongs to."
    }
  },
  "required": [
    "politician_name",
    "electoral_division_represented",
    "ministerial_position_held",
    "ministerial_level",
    "political_party"
  ],
  "additionalProperties": false
}
