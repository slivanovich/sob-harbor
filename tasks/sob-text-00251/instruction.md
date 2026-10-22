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
Swedish Parasports Federation: The Swedish Parasports Federation (Swedish: "Svenska parasportförbundet" ), earlier the Swedish Sports Organization for the Disabled ((Swedish: "Svenska handikappidrottsförbundet" )) (SHIF) and later the Swedish Sports Organization for the Disabled and Swedish Paralympic Committee ((Swedish: "Svenska handikappidrottsförbundet och Sveriges paralympiska kommitté" )) (SHIF/SPK) is the umbrella organization for disability sports in Sweden.  The current name was adopted during a meeting in Malmö on 9 May 2015.

Yiddisher Arbeter Sport Klub (Antwerp): Yiddisher Arbeter Sport Klub (Yiddish for 'Jewish Workers Sports Club', abbreviated YASK; Dutch: "Joodse Arbeiders Sportklub" , abbreviated JASK) was a Jewish sports organization in Antwerp, Belgium.  It was founded in 1936.  YASK was linked to the Communist Party of Belgium.  A product of the Popular Front era, YASK was set up as an open sports organization for the Jewish population at large.  The club emphasized anti-fascism, whilst maintaining a neutral stand on Zionism.

Jennifer A. Hillman: Jennifer Anne Hillman is a law professor at the Georgetown University Law Center, teaching courses in international economic law, including international trade, investment and international business transactions.  Hillman’s career focuses on international trade and investment, financial services and the adjudication of international economic disputes.  She recently served as one of seven judges from around the world on the World Trade Organization’s (WTO) highest court, its Appellate Body, where she helped adjudicate 20 disputes involving a wide variety of legal obligations, ranging from claims arising from subsidies to Airbus, Boeing and US cotton producers, to regulations over trade in agriculture products, to antidumping disputes, to claims regarding the nature and extent of China’s WTO accession commitments.  Hillman also has in-depth experience adjudicating antidumping, countervailing duty, patent and safeguards cases as a result of her nine-year service as a Commissioner at the United States International Trade Commission.  Through her work as the General Counsel at the Office of the United States Trade Representative, Hillman was integrally involved in all litigation matters in which the United States was a party or third party in disputes before panels of the NAFTA or the WTO.  She demonstrated great success at negotiating trade agreements, having reached mutually acceptable agreements with over 45 countries while serving as USTR’s Ambassador and Chief Textiles Negotiator.  Hillman also has extensive policy-making experience, having worked in the United States Senate on numerous pieces of legislation relating to banking, securities, financial services, investment, housing and international trade.

ORDECA: The Central American Sports Organization (acronym: ORDECA; Spanish: Organización Deportiva Centroamericana) is an international organization which represents the current 7 National Olympic Committees of the Central American region.  It is affiliated with the Pan American Sports Organization.

Sim Bhullar: Gursimran "Sim" Bhullar (born December 2, 1992) is a Canadian professional basketball player for Dacin Tigers of the Taiwanese Super Basketball League (SBL).  He played college basketball for New Mexico State University and is the first player of Indian descent to play in the NBA.  At 7'5", he also became the sixth tallest player in NBA history, being tied with Chuck Nevitt and Pavel Podkolzin for that record.

Bolivian Olympic Committee: The Bolivian Olympic Committee (Spanish: Comité Olímpico Boliviaano - COB) is the National Olympic Committee representing Bolivia in the International Olympic Committee (IOC), the Pan American Sports Organization(PASO), the Association of National Olympic Committees(ANOC) and the South American Sports Organization (ODESUR).  It was created 1932 and recognized by the IOC in 1936.

DGI-Huset: DGI-Huset or DGI Huset Aarhus is a sports center located in Aarhus, Denmark.  Parts of the buildings are historic, built in 1910 as part of the Aarhus Central Workshops for the Danish national railway company DSB.  In 1990, DSB closed and sold their repair facilities to Aarhus Municipality and in 1997 the sports organization of DGI bought the building.  An extensive renovation and construction project was completed on 11 October 2003, including new extensions.  The buildings now serves as the primary facility for the sports organization Danske Gymnastik- & Idrætsforeninger in Aarhus, featuring a number of sports facilities, conference rooms.  It is also home to some local sports clubs.  The organization "DGI-Århusegnen", the local chapter of the national organization DGI, took initiative to establish the sports center in the building.

Jon Rauch: Jon Erich Rauch (born September 27, 1978) is an American former professional baseball pitcher.  At 6 ft , he is the tallest player in Major League Baseball history.  He is also an Olympic Gold Medalist.

Bids for the 2015 Pan and Parapan American Games: Three cities submitted bids to host the 2015 Pan American Games and Parapan games that were recognized by the Pan American Sports Organization (PASO), all three of which made the PASO Executive Committee's shortlist.  The games were awarded to Toronto, Ontario, Canada on November 6, 2009.  The other shortlisted cities were Lima, Peru and Bogota, Colombia.  Toronto won an absolute majority of votes after just one round of voting, eliminating the need for subsequent rounds of voting.  PASO delegates and the media identified a number of factors in its favor, including the size of the country, safety, experience in staging multi sporting events, government guarantees, security and cleanliness.  Moreover, the other two nations are not as developed, and with the troubles faced with the 2011 Pan American Games, Toronto was seen as the favourite.  Mario Vazquez Rana, the president of the Pan American Sports Organization was also known to be favouring Toronto.  Moreover, the head of Lima's bid Ricardo Mungi even admitted Toronto was the best choice as they had the facilities and budget to stage the games.

Eric Hillman: John Eric Hillman (born April 27, 1966 in Gary, Indiana) is a former Major League Baseball and Nippon Professional Baseball pitcher.  He pitched his entire 3-year MLB career with the New York Mets (1992–1994).  After his MLB career, he pitched in NPB from 1995-1998 for the Chiba Lotte Marines and the Yomiuri Giants.  Hillman was tied with fellow former pitcher Randy Johnson and current pitchers Andrew Sisco of the New York Yankees organization and Chris Young of the New York Mets, for the tallest player in the league, at 6 ft , before later being passed by 6 ft Jon Rauch of the Toronto Blue Jays.  Hillman worked as an analyst for FSN Rocky Mountain's coverage of the Colorado Rockies between 2005-2008.

Question: Both Eric Hillman and Jon Rauch are tied for being the tallest player in what sports organization?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sports_organization": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the sports organization where the players are noted for their height."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "players_noted_for_height": {
      "type": "array",
      "description": "Details about the players mentioned in the context regarding their height records within the organization.",
      "items": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string",
            "description": "The full name of the player."
          },
          "height_achievement_description": {
            "type": "string",
            "description": "A description of the player's height-related achievement or status as stated in the context."
          }
        },
        "required": [
          "player_name",
          "height_achievement_description"
        ],
        "additionalProperties": false
      }
    },
    "note_on_question_premise": {
      "type": "string",
      "description": "A clarification addressing the 'tied' aspect of the question based on the information provided in the context."
    }
  },
  "required": [
    "sports_organization",
    "players_noted_for_height",
    "note_on_question_premise"
  ],
  "additionalProperties": false
}
