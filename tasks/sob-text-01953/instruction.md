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
6PR: 6PR, known as 882 6PR, is a commercial radio station based in Perth, Australia.  Its focus is on news, talk and sport, and is Perth's only commercial talkback radio station.  6PR is owned by Fairfax Media, an Australian media company that owns television and radio businesses throughout Australia and New Zealand.  It commenced broadcasting on 14 October 1931.

Gary Roberts (radio broadcaster): Gary Roberts is managing director of Perth radio station Nova 93.7 having started his radio career in the late 60's at 3AW in Melbourne.  He spent nine years on air with a number of stations including 5AD (radio station) Adelaide, 2UW Sydney and 6KY Perth before moving into Programming.  As a Programme Director, he programmed four stations to No 1 in their respective markets including a record run of 34 consecutive No 1 surveys with 96fm (Perth radio station), which he launched in 1980.  He was General Manager of 96fm from 1984 to 1992 when he left to take over the same role at 94.5FM in Perth.

3YB: 3YB is a radio station based in Warrnambool, Victoria, Australia.  It broadcasts on the medium wave radio band, at a frequency of 882 kHz.  The station is part of the Ace Radio AM network.  The station has a classic hits music format mixed with talk such as Mornings with Neil Mitchell syndicated from 3AW.

Steve Price (broadcaster): Steve Price (born 13 January 1955) is an Australian journalist and radio broadcaster.  Price is currently working at Macquarie Media broadcasting on 2GB and 3AW, he was previously the program director and breakfast presenter at MTR 1377.

Southern Cross Media Group: Southern Cross Media Group (formerly Macquarie Media Group) is one of Australia's major media companies.  On 3 July 2007 Southern Cross Broadcasting recommended Macquarie Media Group's offer of A$1.35 billion, for a takeover of the corporation.  Under the deal, Macquarie Media Group would then onsell the metropolitan radio stations to Fairfax Media.  On 5 November 2007, the company officially acquired Southern Cross Broadcasting's assets.  On 17 December 2009 shareholders approved a restructuring plan.  The company was then renamed from Macquarie Media Group to its current name on 17 December 2009.

Talking Lifestyle 882: Talking Lifestyle (ACMA callsign: 4BH) is a radio station in Brisbane, the state capital of Queensland, Australia.  Its analog broadcast frequency is 882 KHz AM, simulcasted on digital radio channel 9B, and markets itself for the baby boomer market.  It is owned by Macquarie Media.

KURE: KURE (88.5 FM) is a radio station licensed to Community Media Broadcasting in Ames, Iowa, United States.  The station serves the Iowa State community, Ames, and surrounding areas.  The broadcast license is currently owned by Community Media Broadcasting.  The station has been led by its general manager Miranda Cheers since spring 2017.

KRRQ: KRRQ (branded as Q-95-5) is a radio station serving the Lafayette metropolitan area with an Urban Contemporary format.  It operates on FM frequency 95.5 and is under ownership of Cumulus Media.  They are very well known for their 48-hour live Christmas special, donated to Africa.  For the majority of the 1990s it was owned by Cavendish Media Broadcasting, LLC.  as a Rock station, branded as ""Rock 95 and a Half - Acadiana's Rock"" and later sold to the now defunct Citadel Broadcasting.  (Now Cumulus Media) On March 1, 1996 the station flipped from the Modern Rock format to its now current Contemporary Hip Hop and R&B.

Justin Smith (radio): Justin Smith (born 16 December 1968) is an Australian journalist, radio presenter, producer, and writer.  He currently works with the Fairfax Radio Network, and was the drive-time presenter on Sydney metropolitan station, 2UE.  He is an experienced presenter on prime time metropolitan AM radio, firstly on Melbourne radio station 3AW as senior producer/fill-in presenter on "Mornings with Neil Mitchell" was with 2UE until December 2015, and has since returned to 3AW Melbourne.  His articles appear regularly in mainstream Australian newspapers including The Age and Sydney Morning Herald, and on the Fairfax websites.

3AW: 3AW is a talkback radio station based in Melbourne.  It is broadcast on 693 kHz AM.  It began transmission on 22 February 1932 as Melbourne's fifth commercial radio station.

Question: In what city is Macquarie Media broadcasting's 3AW talkback radio station located?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "radio_station_name": {
      "type": "string",
      "description": "The name of the radio station."
    },
    "station_type": {
      "type": "string",
      "description": "The type or format of the radio station."
    },
    "owner_company": {
      "type": "string",
      "description": "The company that owns the radio station."
    },
    "location_city": {
      "type": "string",
      "description": "The city where the radio station is located."
    }
  },
  "required": [
    "radio_station_name",
    "station_type",
    "owner_company",
    "location_city"
  ],
  "additionalProperties": false
}
