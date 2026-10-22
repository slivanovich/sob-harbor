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
Four Mohawk Kings: The Four Indian Kings or Four Kings of the New World were three Mohawk chiefs of the Iroquois Confederacy and a Mahican of the Algonquian peoples, whose portraits were painted by Jan Verelst in London to commemorate their travel from New York to meet the Queen of Great Britain in 1710.  The three Mohawk were: "Sa Ga Yeath Qua Pieth Tow" of the Bear Clan, called King of Maguas, with the Christian name Peter Brant (grandfather of Mohawk leader Joseph Brant); "Ho Nee Yeath Taw No Row" of the Wolf Clan, called King of "Canajoharie" ("Great Boiling Pot"), or John of Canajoharie; and "Tee Yee Ho Ga Row", meaning "Double Life", of the Wolf Clan, also called "Hendrick Tejonihokarawa" or King Hendrick.  The Mohican chief was "Etow Oh Koam" of the Turtle Clan, mistakenly identified in his portrait as "Emperor of the Six Nations".  The Algonquian-speaking Mohican people were not part of the Iroquois Confederacy.  Five chiefs set out on the journey, but one died in mid-Atlantic.

Paul Edwards (athlete): Paul Michael Edwards (born 16 February 1959 in Chiswick, Greater London) is a retired professional athlete who competed in the men's shot put event during his career.  He competed for both Wales and England during his career and twice represented Great Britain at the Summer Olympics: 1988 and 1992.  Edwards was affiliated with the Walton Athletic Club and Belgrave Harriers in London.  He represented Great Britain 43 times and won 11 AAA titles and 5 UK titles.  In addition, he also represented Great Britain in decathlon and held Welsh national records at shot put, discus and decathlon and won 9 Welsh titles.

Great Britain at the 1952 Summer Olympics: The United Kingdom of Great Britain and Northern Ireland competed as Great Britain at the 1952 Summer Olympics in Helsinki, Finland.  257 competitors, 213 men and 44 women, took part in 127 events in 18 sports.  British athletes have competed in every Summer Olympic Games.  Indeed, it is the only country to have won at least one gold medal at every Summer Olympic Games: in 1952, they achieved their only gold medal during the last event of the last day of competition in Helsinki.  This was Great Britain's lowest ever medal count.

Great Britain at the 1924 Summer Olympics: The United Kingdom of Great Britain and Ireland competed as Great Britain at the 1924 Summer Olympics in Paris, France.  Despite the name, athletes from the newly independent Irish Free State competed separately.  Following the Royal and Parliamentary Titles Act 1927, the name changed (officially) to 'United Kingdom of Great Britain and Northern Ireland' but the Olympic team competed as Great Britain from the 1928 games onwards.  267 competitors, 239 men and 28 women, took part in 115 events in 18 sports.

Great Britain at the 2014 Winter Olympics: Great Britain, represented by the British Olympic Association (BOA), competed at the 2014 Winter Olympics in Sochi, Russia, from 7 to 23 February 2014.  The British team was made up of athletes from the whole United Kingdom including Northern Ireland, whose athletes may have elected to hold Irish citizenship, allowing them to represent either Great Britain or Ireland.  Additionally some British overseas territories competed separately from Britain in Olympic competition.  A total of 56 athletes competed in 11 sports making it the biggest contingent that Great Britain had sent to a Winter Olympic Games for twenty-six years.

Flora Harris: Flora Harris (born 21 March 1988 in London, later moving to live near Taunton, before setting up her own yard near Banbury in Oxfordshire, Flora is now based in Bramley, Hampshire.  is an eventrider who became a full senior in 2010.  In 2007, she competed for Great Britain at the Young Rider European Eventing Championships at Blair Castle, Scotland.

Great Britain at the 2016 Summer Olympics: The United Kingdom of Great Britain and Northern Ireland competed as Great Britain at the 2016 Summer Olympics in Rio de Janeiro, Brazil, from 5 to 21 August 2016.  The United Kingdom was represented by the British Olympic Association (BOA), and the team of selected athletes was also known as Team GB.  British athletes have appeared in every Summer Olympic Games of the modern era, alongside Australia, France, Greece, and Switzerland, though Great Britain is the only country to have won at least one gold medal at all of them.  Although the British Olympic Association is the National Olympic Committee (NOC) for Great Britain and Northern Ireland, Northern Irish athletes can choose whether to compete for Great Britain or for the Republic of Ireland, as they are entitled to citizenship of either nation under the Good Friday Agreement.  In 2016 Northern Ireland born representatives in Team GB included returning rowers Alan Campbell, Peter Chambers and Richard Chambers, archer Patrick Huston and four members of the men's field hockey team: David Ames, Mark Gleghorne, Iain Lewers and Ian Sloan.  The team also represents, and included representation from, the Crown dependencies, among which were Guernsey's Heather Watson and Carl Hester, and from the ten of the thirteen British Overseas Territories represented by the BOA rather than their own NOC, whose representatives include Turks and Caicos-born sprinter Delano Williams and Anguillan-born long jumper Shara Proctor

Blair Castle: Blair Castle stands in its grounds near the village of Blair Atholl in Perthshire in Scotland.  It is the ancestral home of the Clan Murray, and was historically the seat of their chief, the Duke of Atholl, though the current (12th) Duke, Bruce Murray, lives in South Africa.  The castle stands in Glen Garry, and commands a strategic position on the main route (now the A9 road) through the central Scottish Highlands.

Great Britain at the 2008 Summer Olympics: The United Kingdom of Great Britain and Northern Ireland competed as Great Britain at the 2008 Summer Olympics in Beijing, China.  The United Kingdom was represented by the British Olympic Association (BOA), and the team of selected athletes was officially known as Team GB.  Britain is one of only five NOCs to have competed in every modern Summer Olympic Games since 1896.  The delegation of 547 people included 311 competitors – 168 men, 143 women – and 236 officials.  The team was made up of athletes from the whole United Kingdom including Northern Ireland (whose people may elect to hold Irish citizenship and are able to be selected to represent either Great Britain or Ireland at the Olympics).  Additionally some British overseas territories compete separately from Britain in Olympic competition.

Great Britain women's national rugby league team: The Great Britain women's national rugby league team, also known as the Great Britain Lionesses, represents Great Britain in Women's rugby league.  They are administered by the Rugby Football League.  The Great Britain Lionesses have placed third in every Women's Rugby League World Cup in which they have competed.  In 2006, the RFL announced that after the 2007 All Golds Tour the Great Britain team would no longer compete on a regular basis, and that players would be able to represent England, Wales and Scotland at Test level.  It is planned that the Great Britain team will come together in future only for occasional tours, same as the Great Britain Lions.

Question: What was the home of Clan Murrary and where Flora Harris competed for Great Britain in 2007?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "location_name": {
      "type": "string",
      "description": "The name of the location."
    },
    "historical_significance": {
      "type": "object",
      "description": "Details about the historical significance of the location.",
      "properties": {
        "clan_name": {
          "type": "string",
          "description": "The name of the clan associated with the location."
        },
        "relationship": {
          "type": "string",
          "description": "The relationship of the location to the clan (e.g., ancestral home)."
        }
      },
      "required": [
        "clan_name",
        "relationship"
      ],
      "additionalProperties": false
    },
    "event_hosted": {
      "type": "object",
      "description": "Details about an event hosted at this location.",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the event took place."
        },
        "competitor_name": {
          "type": "string",
          "description": "The name of the athlete who competed."
        },
        "competition_name": {
          "type": "string",
          "description": "The name of the competition."
        },
        "country_represented": {
          "type": "string",
          "description": "The country the athlete represented."
        }
      },
      "required": [
        "year",
        "competitor_name",
        "competition_name",
        "country_represented"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "location_name",
    "historical_significance",
    "event_hosted"
  ],
  "additionalProperties": false
}
