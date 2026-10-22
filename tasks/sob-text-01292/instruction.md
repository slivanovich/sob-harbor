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
Herero Mall: Herero Mall is an informal business area in the Katutura suburb of Windhoek, the capital of Namibia.  It is situated in Clemens Kapuuo Street and was established in 2003.  The area was initially used by the Paramount chief of the Herero as a meeting venue.  Over the years small businesses started trading there, ranging from shebeens to car wash businesses.  The City of Windhoek wants to revamp this place and turn it into shopping complex, but the local people are opposing this move.

Mitsubishi Aircraft Company: Mitsubishi Aircraft Company ("Mitsubishi Kokuki") was the new name given by the Mitsubishi Company ("Mitsubishi Shokai"), in 1928, to its subsidiary, Mitsubishi Internal Combustion ("Mitsubishi Nainenki"), to reflect its changing role as an aircraft manufacturer catering to the growing demand for military aircraft in Japan.

Mitsubishi: The Mitsubishi Group (三菱グループ , Mitsubishi Gurūpu , also known as the Mitsubishi Group of Companies or Mitsubishi Companies, and informally as the Mitsubishi "Keiretsu") is a group of autonomous Japanese multinational companies in a variety of industries.  Its total revenue is about 1.4% of Japan's GDP.

Hyundai Cement: Hyundai Cement Co, Ltd. is a cement and concrete company headquartered in Seoul, South Korea, established in 1964.  It is a manufacturer of portland cement.  Manufacturing is based in Danyang, Chungcheongbuk-do and Yeongwol, Gangwon-do.  Hyundai Cement Co., Ltd. was originally a member of the Hyundai Business Group and split off into the Sungwoo Group.  The founder of the Sungwoo Group, Chung Soon-Young, is the younger brother of Chung Ju-yung, founder of the Hyundai Business Group.  The Sungwoo Group is headed by Chung Mong-Sun, the eldest son of Chung Soon-Young and is also involved in resorts.  Former and current affiliates of this group include Hyundai Welding Co., Ltd., Sungwoo Automotive Co., Ltd., Sungwoo Finance Co., Ltd., Sungwoo Precision Co., Ltd., and Hyundai Automotive Co., Ltd. disposal in 2016 Sungwoo Construction Co., Ltd. takeover in 2017 Hanil Cement Group.

Primal Pictures: Primal Pictures, an informal business, established in 1991, is a 3D graphic rendering of human anatomy, built using real scan data from the visible human project, for use by healthcare medical professionals.

Mitsubishi PX33: The Mitsubishi PX33 is a prototype passenger car built by Mitsubishi Heavy Industries, the company which would eventually sire Mitsubishi Motors.  Commissioned for military use by the Japanese government in 1934, it was the first Japanese-built sedan to have full-time four-wheel drive, a technology the company would return to fifty years later in pursuit of motorsport success.  Four working prototypes were built, and a version was in development using Mitsubishi's 6.7 litre, 70 PS "445AD" powerplant, Japan's first direct injection diesel engine.  However, the entire PX33 project was cancelled in 1937 after the government decided to prioritize Mitsubishi's manufacturing capabilities on commercial development of trucks and buses.  In 1937, another Japanese company Tokyu Kurogane Kogyo began production of a smaller four-wheel drive car called the Kurogane Type 95.

Keiretsu: A keiretsu ( , literally "system", "series", "grouping of enterprises", "order of succession") is a set of companies with interlocking business relationships and shareholdings.  It is a type of informal business group.  The "keiretsu" maintained dominance over the Japanese economy for the second half of the 20th century.

Human trafficking in Tanzania: Tanzania is a source, transit, and destination country for men, women, and children trafficked for the purposes of forced labor and sexual exploitation.  Boys are trafficked within the country for forced labor on farms, in mines, and in the informal business sector.  Tanzanian girls from rural areas are trafficked to urban centers and the island of Zanzibar for domestic servitude and commercial sexual exploitation; some domestic workers fleeing abusive employers fall prey to forced prostitution.  In some regions, unregistered employment agencies are involved in recruiting minors from rural areas to work as domestic helpers in the capital, where they are subject to exploitation.  Tanzanian children and adults are reportedly trafficked to other countries including Mozambique, Uganda, Kenya, South Africa, Ethiopia, Yemen, Oman, the United Arab Emirates, Saudi Arabia, Pakistan, the

Uni-ball: Uni-ball and Uni are brands of pens and pencils, made by the Mitsubishi Pencil Company Limited (三菱鉛筆株式会社 , Mitsubishi Enpitsu Kabushiki Gaisha ) of Japan.  Mitsubishi Pencil Company distributes products in over 100 countries through subsidiaries, such as Mitsubishi Pencil Company UK.  Sanford (a division of Newell Brands) distributes uni-ball in the United States and Canada, Faber-Castell does so for Germany, and Linc Pen and Plastics Limited (LPPL) in India.  Despite its naming and the near identical logomarks, Mitsubishi Pencil Company is unrelated to the Mitsubishi Group, and has never been a part of their zaibatsu.

Mitsubishi A5M: The Mitsubishi A5M, formal Japanese Navy designation Mitsubishi Navy Type 96 Carrier-based Fighter (九六式艦上戦闘機), experimental Navy designation Mitsubishi Navy Experimental 9-Shi Carrier Fighter, company designation Mitsubishi Ka-14, was a Japanese carrier-based fighter aircraft.  It was the world's first monoplane shipboard fighter to enter service and the direct predecessor of the famous Mitsubishi A6M "Zero".  The Allied reporting name was Claude.

Question: What type of "informal business group" is the Mitsubishi company considered to be an example of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "business_group_type": {
      "type": "string",
      "description": "The specific type of informal business group."
    },
    "group_example": {
      "type": "string",
      "description": "The name of the company or group that is an example of this type."
    },
    "type_definition": {
      "type": "string",
      "description": "A definition or description of the business group type."
    },
    "is_informal_business_group": {
      "type": "boolean",
      "description": "Indicates if the identified type is an informal business group."
    }
  },
  "required": [
    "business_group_type",
    "group_example",
    "type_definition",
    "is_informal_business_group"
  ],
  "additionalProperties": false
}
