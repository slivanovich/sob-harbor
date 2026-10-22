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
Deals on Wheels: Deals on Wheels was a British television series originally shown by United Kingdom TV channel Channel 4, but now shown on the Discovery Channel, fronted by Mike Brewer and Richard Sutton.  The original run of the series was between 1997 and 2001.  there were 5 seasons.  For season 1 the show was set in a fictional garage.  Season 2 was set in a different garage.  but for seasons 3 and 4, the show was set in an ally garage.  but on a fictional street.  Richard Sutton left the show in 2000 leaving Mike Brewer to continue the show.  It was cancelled in 2001 to make way for Wheeler Dealers.

Carzone: Carzone is an Irish website for motor dealers and consumers located in Dublin, Ireland, and is owned by the Auto Trader Group.

List of Wheeler Dealers episodes: Wheeler Dealers is a British television series produced by Attaboy TV for the Discovery Channel, fronted by Mike Brewer, with mechanic Edd China in Series 1-13 and Ant Anstead in Series 14.  The premise of the show is that Brewer and China are on a mission to save repairable enthusiast vehicles, by repairing or otherwise improving an example of a particular make and model to a budget, then selling it to a new owner.

Phnom Penh Cable Television: Phnom Penh Cable Television, also known as PPCTV, is a direct-to-home cable TV and subscription service included MMDS TV, Fiber Optic and Internet Service, established by Phnom Penh Municipal Cable Television (PPCTV).  It is one of the major cable TV services in Cambodia with the largest number of viewers, especially in Phnom Penh.  PPCTV is also the first to offer true 1080P HD experiences via the Digital TV service.  Some of the HD channels include Fox Movie Premium HD, AXN HD, SOne HD, National Geographic Channel HD, History HD, Starworld HD, KBS World HD, etc.  TV viewers would be able to watch super clear full HD resolution on modern televisions that support 1080P high definition.

Wheeler Dealers: Wheeler Dealers is a British television series originally produced by Attaboy TV for the Discovery Channel in the UK and Velocity Channel HD in the U.S.  The programme is fronted by car enthusiast Mike Brewer.  Edd China served as the programme's mechanic for series 1 to 13; he will be replaced by Ant Anstead in series 14.  The premise of the show has the presenters on a mission to save old and repairable enthusiast vehicles, by repairing or otherwise improving an example of a particular make and model to a budget, then selling it to a new owner.

Edd China: Edward John "Edd" China (born May 9, 1971 in London) is an English television presenter, mechanic, motor specialist and inventor, best known as being presenter and mechanic on Discovery Channel's television show "Wheeler Dealers", but has also appeared on "Top Gear", "Scrapheap Challenge" and "Fifth Gear".

AutoTrader.co.za: According to SimilarWeb, autotrader.co.za is South Africa's largest website in their "Autos and Vehicles" category.  Autotrader.co.za is an online automotive classifieds advertising website, which is part of Auto Trader South Africa.  The company publishes an automotive classifieds magazine Auto Trader as well.  Auto Trader South Africa was previously a subsidiary of the Auto Trader Group.  In 2013, the Auto Trader Group sold their South African business, Auto Trader South Africa, which then became a wholly South African-owned business.  The autotrader.co.za website is South Africa’s largest automotive marketplace website for buyers and sellers of both new and used cars and other types of vehicles.

Pinoy Auto Trader: Pinoy Auto Trader is an online automotive marketplace that primarily caters for the Philippine market.  It is owned and operated by Netrepreneur Connections Enterprises and is a sister-company of the Philippine buy and sell website Sulit.com.ph.  Pinoy Auto Trader is primarily a business-to-consumer (B2C) website.

Auto Trader (TV series): Auto Trader was a British television series, first shown on the Discovery Channel.  It was presented by Mike Brewer and Edd China, who have worked together on other TV series, including "Wheeler Dealers".

RMC Découverte: RMC Découverte is a French television channel broadcast on channel 24 and owned by NextRadioTV.  Created in 2012, it mainly broadcast documentaries such as "Wheeler Dealers", "Ancient Aliens", Swamp Loggers.  RMC Découverte broadcasts the French version of the British show "Top Gear".

Question: Which show played on Velocity Channel HD, Auto Trader or Wheeler Dealers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_name": {
      "type": "string",
      "description": "The name of the television series that played on the specified channel."
    },
    "channel_name": {
      "type": "string",
      "description": "The name of the channel where the show was broadcast."
    },
    "channel_location": {
      "type": "string",
      "description": "The geographical region where the channel broadcasted the show."
    },
    "other_channels_for_show": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other channels where the identified show was broadcast."
    }
  },
  "required": [
    "show_name",
    "channel_name",
    "channel_location",
    "other_channels_for_show"
  ],
  "additionalProperties": false
}
