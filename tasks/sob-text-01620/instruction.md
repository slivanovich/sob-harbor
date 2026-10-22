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
Electoral district of Murray (South Australia): Murray is a defunct electoral district that elected members to the House of Assembly, the lower house of the bicameral legislature of the Australian state of South Australia.  The electorate, incorporating part of the River Murray, was rural in nature, with Mannum the only large town within its boundaries.  From its establishment to the 1938 state election, Murray was a three-member electorate, but was made a single-member electorate afterwards, as part of a system of electoral malapportionment known as the "Playmander".  In both incarnations it elected candidates from both major parties as marginal and safe seat holders at various times.  If just 21 LCL votes were Labor votes in Murray at the 1968 election, Labor would have formed majority government.  Murray was one of two gains in 1968 that put the LCL in office.  The electorate was abolished prior to the 1985 election, with its territory now forming part of the districts of Hammond, Kavel, and Schubert.  In total, 24 people represented Murray between 1902 and 1985, with its most notable member being Thomas Playford IV, who later served as Premier of South Australia.

Electoral district of Queanbeyan: Queanbeyan was an electoral district of the Legislative Assembly in the Australian state of New South Wales from 1859 to 1913, in the Queanbeyan area.  It replaced parts of the electoral district of United Counties of Murray and St Vincent and the electoral district of Southern Boroughs.  It was merged with the electoral district of Monaro in 1913, when much of its former territory had been absorbed in the Australian Capital Territory.

Electoral district of Kaurna: Kaurna is an electoral district of the House of Assembly in the Australian state of South Australia.  Named after the Kaurna aboriginal tribe which originally inhabited the Adelaide plains, it is a 52.7 km² semi-urban electorate on Adelaide's far-southern beaches, taking in the suburbs of Aldinga Beach, Maslin Beach, Moana, Port Noarlunga, Port Noarlunga South, Port Willunga, Seaford, Seaford Meadows and Seaford Rise as well as parts of Aldinga and Christies Beach.  It is one of only two state districts named after South Australia's indigenous people (the other being the Electoral district of Narungga).

Electoral district of Broken Hill: Broken Hill was an electoral district of the Legislative Assembly in the Australian state of New South Wales.  From 1894 to 1913, the Broken Hill district was covered by the electoral districts of "Broken Hill", Willyama and Sturt.  In the 1912 redistribution, the electoral district of "Broken Hill" was abolished and absorbed into "Willyama" and "Sturt".  In 1920, "Willyama", "Sturt" and the electoral district of Cobar were combined to create a three-member "Sturt".  In 1927, single-member electorates were recreated and the city of Broken Hill was split between "Sturt" and Murray.  From 1932, the city of Broken Hill was split between "Sturt" and Cobar.  In 1968 "Sturt" was renamed Broken Hill and included all of the city of Broken Hill.  In 1999, it was merged with part of "Murray" and renamed the electoral district of Murray-Darling.

Isobel Redmond: Isobel Mary Redmond (born 8 April 1953) has been the member for the electoral district of Heysen in the House of Assembly since 2002.  She was the parliamentary leader of the South Australian Division of the Liberal Party of Australia and the Leader of the Opposition in the Parliament of South Australia between 2009 and 2013, and was the first female leader of a South Australian state major party.  Under Redmond, the Liberals won 18 of 47 seats in the South Australian House of Assembly at the 2010 election, a gain of three from the 2006 election.  She resigned as leader of the Liberal Party on 31 January 2013.

Electoral district of Heysen: Heysen is an electoral district of the House of Assembly in the Australian state of South Australia.  It is named after Sir Hans Heysen, a prominent South Australian landscape artist.  It is a 1,102 km² electoral district that takes in some of the outer southern suburbs of Adelaide before fanning south-east to include most of the Adelaide Hills, as well as farming areas some distance from the capital.  It includes the areas of Aldgate, Bridgewater, Echunga, Hahndorf, Macclesfield, Meadows, Stirling and Strathalbyn, as well as part of Mount Barker.  Although geographically it is a hybrid urban-rural seat, it is counted as a metropolitan seat.

Electoral district of Barossa: Barossa was an electoral district of the House of Assembly in the colony (Australian state from 1901) of South Australia from 1857 to 1938 and again from 1956 to 1970.  Barossa was also the name of an electoral district of the unicameral South Australian Legislative Council from 1851 until its abolition in 1857, George Fife Angas being the member.

Electoral district of Braidwood: Braidwood was an electoral district of the Legislative Assembly in the Australian state of New South Wales between 1859 and 1904, which included the town of Braidwood.  It replaced parts of the electoral district of United Counties of Murray and St Vincent and the electoral district of Southern Boroughs.  In 1904 it was largely absorbed into the electoral district of Queanbeyan.

Electoral district of Bragg: Bragg is an electoral district of the House of Assembly in the Australian state of South Australia.  The seat of Bragg is named after the eminent physicists Bragg – William Henry and his son, William Lawrence.  The electorate is largely urban and encompasses a significant portion of the City of Burnside, stretching from the east parklands of Adelaide into the Adelaide Hills.  After a redistribution following the 2006 election, the boundary moved eastwards to include suburbs that had formerly been in the seat of Heysen and now borders Kavel.  Bragg currently includes the metropolitan suburbs of Beaumont, Burnside, Dulwich, Erindale, Hazelwood Park, Heathpool, Kensington Park, Leabrook, Linden Park, Rose Park, Marryatville, Skye, St Georges, Stonyfell, Toorak Gardens, Tusmore, Wattle Park and parts of Glen Osmond, and in the hills it includes Crafers, Cleland, Greenhill, Mount Osmond, Piccadilly, Summertown and parts of Ashton, Basket Range, Carey Gully, Horsnell Gully, Leawood Gardens and Uraidla.

Hans Heysen: Sir Hans Heysen {'1': ", '2': ", '3': ", '4': "} (8 October 18772 July 1968) was a German-born Australian artist.  He became a household name for his watercolours of monumental Australian gum trees. Heysen also produced images of men and animals toiling in the Australian bush, as well as groundbreaking depictions of arid landscapes in the Flinders Ranges.  He won the Wynne Prize for landscape painting a record nine times.

Question: Hans Heysen, whose name was given to an electoral district of the House of Assembly in the Australian state of South Australia, won what for landscape painting a record nine times?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person mentioned in the question."
    },
    "award_name": {
      "type": "string",
      "description": "The name of the award won by the person."
    },
    "award_category": {
      "type": "string",
      "description": "The category for which the award was given."
    },
    "times_won": {
      "type": "integer",
      "description": "The number of times the person won the award."
    },
    "electoral_district_named_after_person": {
      "type": "string",
      "description": "The name of the electoral district named after the person."
    },
    "electoral_district_state": {
      "type": "string",
      "description": "The Australian state where the electoral district is located."
    }
  },
  "required": [
    "person_name",
    "award_name",
    "award_category",
    "times_won",
    "electoral_district_named_after_person",
    "electoral_district_state"
  ],
  "additionalProperties": false
}
