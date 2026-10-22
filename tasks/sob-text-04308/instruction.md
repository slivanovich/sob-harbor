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
Armani: Giorgio Armani S.P.A. (] ) is an Italian fashion house founded by Giorgio Armani which designs, manufactures, distributes and retails haute couture, ready-to-wear, leather goods, shoes, watches, jewelry, accessories, eyewear, cosmetics and home interiors.  The brand markets these products under several labels: "Giorgio Armani Privé", "Giorgio Armani", "Armani Collezioni", "Emporio Armani" (including "EA7"), "AJ | Armani Jeans", "Armani Junior", "AX | Armani Exchange".  The brand utilizes the association of the Armani name with high-fashion, benefiting from its prestige in the fashion industry.  In 2016, estimated sales of the company were around $2.65 billion.

Nathalie Colin: Nathalie Colin is a French Creative Director born in 1966 in the East of France.  In 2006, she was appointed by Swarovski as Creative Director for the Consumer Goods Business division (CGB), in charge of modernizing the brand.  She is still currently leading all creative studios, in charge of the international collections of jewelry, watches, accessories, and crystal living.  Nowadays, Swarovski Crystal Business has a global reach with approximately 2,680 stores in around 170 countries, more than 26,000 employees, and revenue of about 2.6 billion euros (in 2016).

Swarovski crystal mesh Armani Privé gown: A Swarovski crystal mesh Armani Privé gown was worn by Cate Blanchett at the 79th Academy Awards on 25 February 2007.  It is a one shoulder long grey mesh gown studded with Swarovski crystals, described as a "stunning" dress by "The Hollywood Reporter".

Swarovski Kristallwelten (Crystal Worlds): The Swarovski Crystal Worlds (Swarovski Kristallwelten) is a museum, located in Wattens, Austria.  The museum was built in 1995 in celebration of the 100th anniversary of the Austria based crystal company Swarovski.

Daniel Swarovski: Daniel Swarovski (24 October 1862 – 23 January 1956) was a Czech-Austrian glass cutter, jeweler, and founder of the Swarovski crystal dynasty.

Swarovski: Swarovski ( , ] ) is an Austrian producer of crystal headquartered in Wattens, Austria.  The company is split into three major industry areas: the Swarovski Crystal Business, that primarily produces crystal jewelry and accessories; Swarovski Optik, which produces optical instruments such as telescopes and binoculars; Tyrolit, a leading manufacturer of grinding, sawing, drilling, and dressing tools, as well as a supplier of tools and machines.

Cate Blanchett: Catherine Elise Blanchett, {'1': ", '2': ", '3': ", '4': "} ( ; born 14 May 1969) is an Australian actress and theatre director.  She has received international acclaim and many accolades, including two Academy Awards, three Golden Globe Awards, three BAFTA Awards, six AACTA Awards, and three Screen Actors Guild Awards. Blanchett came to international attention for her role as Elizabeth I of England in Shekhar Kapur's 1998 film "Elizabeth", for which she won the BAFTA Award for Best Actress, the Golden Globe Award, and earned her first Academy Award for Best Actress nomination.  Her portrayal of Katharine Hepburn in Martin Scorsese's 2004 film "The Aviator" brought her critical acclaim and many accolades, including the Academy Award for Best Actress in a Supporting Role, making her the only actor to win an Oscar for portraying another Oscar-winning actor.  In 2013, she starred as Jasmine Francis in Woody Allen's "Blue Jasmine", for which she won numerous accolades including the Academy Award for Best Actress.

Gown: A gown, from medieval Latin "gunna", is a usually loose outer garment from knee- to full-length worn by men and women in Europe from the early Middle Ages to the 17th century, and continuing today in certain professions; later, "gown" was applied to any full-length woman's garment consisting of a bodice and attached skirt.  A long, loosely fitted gown called a Banyan was worn by men in the 18th century as an informal coat.

Karl-Heinz Grasser: Karl-Heinz Grasser (born 2 January 1969) is a former Austrian politician (FPÖ at first and later associated with but never officially a member of the ÖVP), who held the office of Austrian Minister of Finance from February 2000 to January 2007 as a member of the two subsequent governments of Wolfgang Schüssel.  While at the time praised by many for consolidating Austria's budget, he has since then been known for his alleged involvement in major corruption scandals.  For some time, he was also some kind of a jet set person after marrying Fiona Swarovski, the heir of the Swarovski crystal manufacturers in Tyrol, Austria.

Khrui: The khrui (Thai: ครุย ,  ] ) is a light outer garment worn as a gown or robe in certain ceremonial settings in Thailand.  It is long-sleeved and open at the front, and is made of a sheer or mesh fabric, lined with a band of satin, felt or other material, and may be exquisitely embroidered.  Dating from at least the 17th century, it was originally worn only in the royal court, but nowadays is most recognisable as the form of academic dress employed by many universities, especially Chulalongkorn University.

Question: A Swarovski crystal mesh Armani Privé gown was worn by an Australian actress who has what middle name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The full name of the actress who wore the gown."
    },
    "actress_nationality": {
      "type": "string",
      "description": "The nationality of the actress."
    },
    "middle_name": {
      "type": "string",
      "description": "The middle name of the actress."
    },
    "gown_details": {
      "type": "object",
      "properties": {
        "brand": {
          "type": "string",
          "description": "The brand of the gown."
        },
        "material": {
          "type": "string",
          "description": "The primary material of the gown."
        },
        "adornment": {
          "type": "string",
          "description": "The type of adornment on the gown."
        }
      },
      "required": [
        "brand",
        "material",
        "adornment"
      ],
      "additionalProperties": false
    },
    "event_worn_at": {
      "type": "string",
      "description": "The event where the gown was worn."
    }
  },
  "required": [
    "actress_name",
    "actress_nationality",
    "middle_name",
    "gown_details",
    "event_worn_at"
  ],
  "additionalProperties": false
}
