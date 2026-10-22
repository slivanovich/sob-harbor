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
Astrotech Corporation: Astrotech Corporation, formerly Spacehab Inc., is a technology incubator headquartered in Austin, Texas.  Astrotech uses technology sourced internally and from research institutions, government laboratories, and universities to fund, manage and sell start-up companies.

Qulliq Energy: Qulliq Energy Corporation (QEC) is a Canadian Crown corporation owned by the Government of Nunavut.  It draws its name from the qulliq (kudlik), an Inuit oil lamp.  The company uses name Nunavut Power as a trading name for power generation.  It is headquartered in Baker Lake, Nunavut.

J &amp; J Snack Foods: J&J Snack Foods Corporation (JJSF) is an American manufacturer, marketer, and distributor of branded niche snack foods and frozen beverages for the food service and retail supermarket industries.  Headquartered in Pennsauken, NJ JJSF uses over 175 facilities for manufacturing, warehousing, and distributing located in 44 states, Mexico and Canada.  The company is listed on the NASDAQ Global Select Market as “JJSF”, and serves both nation and international markets.

Sony: Sony Corporation (ソニー株式会社 , Sonī Kabushiki Kaisha ) (often referred to simply as Sony) is a Japanese multinational conglomerate corporation headquartered in Kōnan, Minato, Tokyo.  Its diversified business includes consumer and professional electronics, gaming, entertainment and financial services.  The company is one of the leading manufacturers of electronic products for the consumer and professional markets.  Sony was ranked 113th on the 2016 list of Fortune Global 500.

BNY Mellon Center (Pittsburgh): BNY Mellon Center is a 55-story, 220.98 m , skyscraper located at 500 Grant Street in downtown Pittsburgh, Pennsylvania.  Announced on March 27, 1980, the tower was completed in June 1984.  It is the second-tallest building in the city and was initially planned to be the world headquarters of the Dravo Corporation (now Carmeuse Corporation) by its majority owner at the time and current neighbor U.S. Steel.  From its inception until 2007, the building housed the global headquarters of the Mellon Financial Corporation, until the company merged with Bank of New York.  The resulting corporation, The Bank of New York Mellon, uses the building as one of its major offices.  The building was named One Mellon Center until 2008, when it was renamed as part of a branding initiative by The Bank of New York Mellon.

Bristol Bay Native Corporation: Bristol Bay Native Corporation, or BBNC, is one of thirteen Alaska Native Regional Corporations created under the Alaska Native Claims Settlement Act of 1971 (ANCSA) in settlement of aboriginal land claims.  Bristol Bay Native Corporation was incorporated in Alaska on June 13, 1972.  Headquartered in Anchorage, Alaska, Bristol Bay Native Corporation is a for-profit corporation with approximately 9,900 Alaska Native shareholders primarily of Eskimo, Aleut, and Indian descent.  BBNC states its mission as “Enriching Our Native Way Of Life" as a corporation "that protects the past, present and future of the Natives from Bristol Bay.”

Yadkin Financial: Yadkin Financial Corporation was a bank holding company and the parent of Yadkin Bank, a defunct regional bank with $7.3 billion in assets and 110 branches in North and South Carolina before the 2017 purchase by FNB Corporation of Pittsburgh.  The bank was headquartered in Elkin, North Carolina.  On July 4, 2014, Yadkin Financial and VantageSouth Bancshares Inc. completed a merger which resulted in the largest community bank based in North Carolina, and the fourth-largest bank headquartered in the state, with $4 billion in assets and $3.2 billion in deposits.  The company was headquartered in Raleigh, North Carolina with banking operations based in Statesville, North Carolina.

COFINA: The Puerto Rico Urgent Interest Fund Corporation (also known as the Puerto Rico Sales Tax Financing Corporation) —Spanish: "Corporación del Fondo de Interés Apremiante" (COFINA)— is a government-owned corporation of Puerto Rico that issues government bonds and uses other financing mechanisms to pay and refinance the public debt of Puerto Rico.  The Corporation is a subsidiary of the Government Development Bank and was created by Law No. 291 of 2006.  Bonds issued by COFINA are called Puerto Rico Sales Tax Revenue Bonds.

Panasonic Avionics Corporation: Panasonic Avionics Corporation (PAC) designs, engineers, manufactures, sells and installs customized in-flight entertainment and communications solutions to airlines worldwide.  Panasonic Avionics Corporation is a subsidiary of Panasonic Corporation of North America, the principal North American subsidiary of Panasonic Corporation.  Panasonic Avionics Corporation is headquartered in Lake Forest, California and has major business functions in Bothell, WA.  Panasonic Avionics Corporation traces its roots to Matsushita Avionics Systems Corporation, founded in 1979.

WirelessHD: WirelessHD, also known as UltraGig, is a proprietary standard owned by Silicon Image (originally SiBeam) for wireless transmission of high-definition video content for consumer electronics products.  The consortium currently has over 40 adopters; key members behind the specification include Broadcom, Intel, LG, Panasonic, NEC, Samsung, SiBEAM, Sony, Philips and Toshiba.  The founders intend the technology to be used for Consumer Electronic devices, PCs, and portable devices.

Question: Where is the Japenese corporation that uses WirelessHD headquartered?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "corporation_name": {
      "type": "string",
      "description": "The name of the Japanese corporation."
    },
    "headquarters_location": {
      "type": "string",
      "description": "The city and country where the corporation is headquartered."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the corporation is based."
    },
    "is_wirelesshd_member": {
      "type": "boolean",
      "description": "Indicates if the corporation is a key member of the WirelessHD consortium."
    }
  },
  "required": [
    "corporation_name",
    "headquarters_location",
    "country_of_origin",
    "is_wirelesshd_member"
  ],
  "additionalProperties": false
}
