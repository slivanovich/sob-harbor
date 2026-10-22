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
Impulse Airlines: Impulse Airlines was an independent airline in Australia which operated regional and low cost trunk services between 1992 and 2004.  It was acquired by Qantas in 2001 and later formed the basis of Qantas' low-cost airline Jetstar.  The airline had its head offices on the grounds of Sydney Airport in Mascot.

1935–36 Iraqi Shia revolts: 1935 Rumaytha and Diwaniyya revolt or the 1935–1936 Iraqi Shia revolts consisted of a series of Shia tribal uprisings in the mid-Euphrates region against the Sunni dominated authority of the Kingdom of Iraq.  In each revolt, the response of the Iraqi government was to use military force to crush the rebellions with little mercy.  The administrative task of this forceful disciplining of the Shi'a tribes fell to General Bakr Sidqi – the same man responsible for the brutal massacre of Assyrians in 1933.  Parallel revolts, opposing conscription, also broke out that year in northern Iraq (Kurdish populated) and Jabal Sinjar (mostly Yazidi populated) regions.

C. W. McCall &amp; Co.: C. W. McCall & Co. is country musician C. W. McCall's sixth and last album of original songs, released on Polydor Records in 1979 (see 1979 in music), before McCall (or, more accurately, Bill Fries, the man playing his role) announced his retirement from the music industry.  Out of the ten tracks, only one ("The Little Things in Life") was written as a collaboration between McCall and Chip Davis, the man responsible for popularizing the distinctive McCall persona, while one other, "Silver Cloud Breakdown", was composed by Davis several years earlier and was featured in the movie "Convoy", though it was not present on its soundtrack.

Trans Australia Airlines: Trans Australia Airlines or TAA (renamed Australian Airlines in 1986) was one of the two major Australian domestic airlines between its inception in 1946 and its merger with Qantas in September 1992.  As a result of the "COBRA" (or Common Branding) project, the entire airline was rebranded Qantas about a year later with tickets stating in small print "Australian Airlines Limited trading as Qantas Airways Limited" until the adoption of a single Air Operator Certificate a few years later.  At that point, the entire airline was officially renamed "Qantas Airways Limited" continuing the name and livery of the parent company with the only change being the change of by-line from "The Spirit of Australia" to "The Australian Airline" under the window line with the existing "Qantas" title appearing above.

Saeed Mortazavi: Saeed Mortazavi (Persian: سعید مرتضوی‎ ‎ , born 1967) is an Iranian politician, former judge and former prosecutor.  He was prosecutor of the Islamic Revolutionary Court, and Prosecutor General of Tehran, a position he held from 2003 to 2009.  He has been called as "butcher of the press" and "torturer of Tehran" by some observers.  Mortazavi has been accused of the torture and death in custody of Iranian-Canadian photographer Zahra Kazemi by the Canadian government and was named by 2010 Iranian parliamentary report as the man responsible for abuse of dozens and death of three political prisoners at Kahrizak detention center in 2009.  He was put on trial in February 2013 after a parliamentary committee blamed him for the torture and deaths of at least three detainees who participated in the protests against President Mahmud Ahmadinejad's reelection.  On 15 November 2014, he was banned from all political and legal positions for life.

Jetconnect: Jetconnect is a wholly owned subsidiary airline of Qantas that is based in Auckland, New Zealand.  It was established in July 2002, commencing operations in October the same year.  It operates trans-Tasman services between New Zealand and Australia under the Qantas brand.  It employs crew based in New Zealand and operates aircraft registered in New Zealand.  It also operated domestic services within New Zealand until these services were taken over by Jetstar Airways, another Qantas subsidiary, on 10 June 2009.  Its main base is Auckland Airport.

Qantas Freight: Qantas Freight is a subsidiary company of Qantas, responsible for the air cargo operations of the Qantas group.  It is the owner of freight airline Express Freighters Australia, freight forwarder Qantas Courier and trucking company Jets Transport Express.  Qantas Freight was also a partner in two joint ventures with Australia Post: Australian air Express, specialising in door-to-door package delivery, and Star Track Express, a road freight company.  In November 2012 Qantas Freight fully acquired Australia air Express and divested its shareholding in Star Track to Australia Post.  Qantas Freight was also the owner of Asian-based freight forwarder DPEX Worldwide until that company was acquired by its competitor Toll Holdings in 2010.

Arthur Drakeford: Arthur Samuel Drakeford (26 April 1878 – 9 June 1957) was an Australian politician and was the minister responsible for the Royal Australian Air Force during World War II.  He was also responsible for the establishment of the former domestic carrier Trans Australia Airlines and for the nationalisation of Qantas.

Søren Solkær: Søren Solkær (born 3 September 1969 and formerly known as Søren Solkær Starbird), is a Danish photographer best known for his portraits of musicians.  He is most recognised as the man responsible for various iconic images of Björk, The White Stripes, Franz Ferdinand, David Lynch, Arctic Monkeys, R.E.M. and U2.

Lester Brain: Lester Joseph Brain, AO, AFC (27 February 1903 – 30 June 1980) was a pioneer Australian aviator and airline executive.  Born in New South Wales, he trained with the Royal Australian Air Force (RAAF) before joining Queensland and Northern Territory Aerial Services (Qantas) as a pilot in 1924.  He was awarded the Air Force Cross in 1929, after locating the lost aircraft "Kookaburra" in northern Australia.  Having risen to Chief Pilot at Qantas by 1930, he was appointed Flying Operations Manager in 1938.  As a member of the RAAF reserve, Brain coordinated his airline's support for the Australian military during World War II.  He earned a King's Commendation for his rescue efforts during an air raid on Broome, Western Australia, in 1942, and was promoted to wing commander in 1944.

Question: The man responsible for the establishment of the airline that merged with Qantas in 1992 was born in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person identified."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the person."
        },
        "role_in_airline_establishment": {
          "type": "string",
          "description": "The role of the person in establishing the airline."
        }
      },
      "required": [
        "name",
        "birth_year",
        "role_in_airline_establishment"
      ],
      "additionalProperties": false
    },
    "established_airline_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the airline established by the person."
        },
        "merger_partner": {
          "type": "string",
          "description": "The name of the airline it merged with."
        },
        "merger_year": {
          "type": "integer",
          "description": "The year the airline merged with its partner."
        }
      },
      "required": [
        "name",
        "merger_partner",
        "merger_year"
      ],
      "additionalProperties": false
    },
    "answer_birth_year": {
      "type": "integer",
      "description": "The birth year of the man responsible for the establishment of the airline."
    }
  },
  "required": [
    "person_of_interest",
    "established_airline_details",
    "answer_birth_year"
  ],
  "additionalProperties": false
}
