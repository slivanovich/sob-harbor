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
Robert W. Gore: Robert W. "Bob" Gore (born April 15, 1937) is an American engineer and scientist, inventor and businessman.  Gore has led his family's company, W. L. Gore & Associates, in developing applications of polytetrafluoroethylene (PTFE) ranging from computer cables to medical equipment to the outer layer of space suits.  His most significant breakthrough is likely the invention of Gore-Tex, a waterproof/breathable fabric popularly known for its use in sporting and outdoor gear.

Boot socks: Boot socks are a type of sock suitable for wearing with boots.  Typically made from a knitted material, popular styles of knit currently are the cable and fairisle knit.  Boot socks provide additional comfort and warmth in colder weather.  Boots are often worn by both genders, with military boots, brogue boots and hiking boots all being popular styles to pair with boot socks.  Boot socks vary in lengths, ranging from normal sized socks to knee high length socks.

Gore-Tex: Gore-Tex is a waterproof, breathable fabric membrane and registered trademark of W. L. Gore and Associates.  Invented in 1969, Gore-Tex is able to repel liquid water while allowing water vapor to pass through, and is designed to be a lightweight, waterproof fabric for all-weather use.  It is composed of stretched polytetrafluoroethylene (PTFE), which is more commonly known as the generic trademark Teflon.

Eyes Wide Open (exhibit): Eyes Wide Open is an exhibit created by the American Friends Service Committee observing the American soldiers and marines that have died in the Iraq War.  It contains a pair of combat boots to represent every American soldier and marine that has died in the war, as well as shoes representing Iraqi civilians who have lost their lives during the invasion and occupation.  The exhibit was first shown in Chicago's Federal Plaza in January 2004.  At that time, the exhibit contained 504 pairs of boots.

Hiking boot: Hiking (walking) boots are footwear specifically designed for protecting the feet and ankles during outdoor walking activities such as hiking.  They are one of the most important items of hiking gear, since their quality and durability can determine a hiker's ability to walk long distances without injury.  Hiking boots are constructed to provide comfort for walking considerable distance over rough terrain.  Boots that protect the hiker's feet and heel are recommended.  Hiking boots give ankle support and are fairly stiff.  A less popular alternative is to use light trainers with thin soles.  Footwear should be neither too loose nor too tight, to help prevent blisters and sore feet.  Hiking socks that wick sweat from the feet, provide warmth, and cushion the feet are recommended and a thin, inner sock may also help.  Most hiking boots are also designed for other outdoor activities such as backpacking, climbing, mountaineering, and hunting.

Tanker boot: Tanker boots are military boots closely associated with soldiers who serve on tanks and tracked vehicles in general.  It is said the idea was borrowed from the French crewmen encountered during World War I when then-Captain George S. Patton, Jr. established the United States Tank Corps.  Whereas regular combat boots are laced through metal eyelets in the leather upper, the tanker boots are fastened with leather straps which wrap around the upper and buckle near the top.  This benefits the wearer in several ways:

Fashion boot: A fashion boot is a boot worn for reasons of style or fashion (rather than for utilitarian purposes – e.g. not hiking boots, riding boots, rain boots, etc.).  The term is usually applied to women’s boots.  Fashion boots come in a wide variety of styles, from ankle to thigh-length, and are used for casual, formal, and business attire.  Although boots were a popular style of women’s footwear in the Nineteenth Century, they were not recognized as a high fashion item until the 1960s.  They became widely popular in the 1970s and have remained a staple of women’s winter wardrobes since then.

Desert Combat Boot: Desert Combat Boots are type of combat boot designed specifically for use in humid or arid regions for desert warfare, where a traditional or standard issued black leather combat boot might be deemed uncomfortable or unnecessary.  Like jungle boots, desert boots may implement similar designs; such as nylon canvas sides, speed lacing, and drainage vents on the instep.  Boots made for desert warfare may commonly come in colors such as tan or beige, and range from dark to lighter versions of the two.

Hiking apparel: Hiking apparel is clothing suitable for hiking, including trousers, sweaters, underwear, and hiking boots. Today's hiking apparel is more advanced than previous years, having material that can be wind resistant, [Waterproofing#In clothing|water-repellent]] and yet breathable, and lightweight.  Some hiking apparel is designed to be "breathable", drawing moisture away from the body while protecting from the weather.  Today's hiking boots have been designed to give maximum ankle support, and to be durable but light in weight.  Many have a long-lasting hardened rubber sole.  Hiking apparel is usually selected to suit predicted weather conditions, taking into account UPF rating (Ultraviolet Protection Factor), weight, water and wind resistance.

Combat boot: Combat boots are military boots designed to be worn by soldiers during combat or combat training, as opposed to during parades and other ceremonial duties.  Modern combat boots are designed to provide a combination of grip, ankle stability, and foot protection suitable for a rugged environment.  They are traditionally made of hardened and sometimes waterproofed leather.  Today, many combat boots incorporate technologies originating in civilian hiking boots, such as Gore-Tex nylon side panels, which improve ventilation and comfort.  They are also often specialized for certain climates and conditions, such as jungle boots, desert boots, and cold weather boots as well as specific uses, such as tanker boots and jump boots.

Question: Combat boots are military boots designed to be worn by soldiers during combat or combat training, as opposed to during parades and other ceremonial duties, today, many combat boots incorporate technologies originating in civilian hiking boots, such as what, which  is a waterproof, breathable fabric membrane and registered trademark of W. L. Gore and Associates?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "technology_name": {
      "type": "string",
      "description": "The name of the technology."
    },
    "is_waterproof": {
      "type": "boolean",
      "description": "Indicates if the technology is waterproof."
    },
    "is_breathable": {
      "type": "boolean",
      "description": "Indicates if the technology is breathable."
    },
    "trademark_owner": {
      "type": "string",
      "description": "The company that owns the registered trademark for the technology."
    },
    "incorporated_into_product_type": {
      "type": "string",
      "description": "The type of product that incorporates this technology."
    },
    "origin_product_category": {
      "type": "string",
      "description": "The category of product from which this technology originated."
    }
  },
  "required": [
    "technology_name",
    "is_waterproof",
    "is_breathable",
    "trademark_owner",
    "incorporated_into_product_type",
    "origin_product_category"
  ],
  "additionalProperties": false
}
