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
PowerHUB: PowerHUB refers to the name of a series of Integrated Circuits (ICs) developed by ST-Ericsson, a 50/50 joint venture of Ericsson and STMicroelectronics established on February 3, 2009.

STMicroelectronics: STMicroelectronics is a French-Italian multinational electronics and semiconductor manufacturer headquartered in Geneva, Switzerland.  It is commonly called ST, and it is Europe's largest semiconductor chip maker based on revenue.  While STMicroelectronics corporate headquarters and the headquarters for EMEA region are based in Geneva, the holding company, STMicroelectronics N.V. is registered in Amsterdam, Netherlands.

NovaThor: NovaThor was a platform consisting of integrated System on Chips (SoC) and modems for smartphones and tablets developed by ST-Ericsson, a 50/50 joint venture of Ericsson and STMicroelectronics established on February 3, 2009.  ST-Ericsson also sold the SoCs (Nova) and the modems (Thor) separately.  The application processor portion of the system was the successor of the previous Nomadik line from STMicroelectronics.

Renesas Electronics: Renesas Electronics Corporation (ルネサス エレクトロニクス株式会社 , Runesasu Erekutoronikusu Kabushiki Gaisha ) is a Japanese semiconductor manufacturer headquartered in Tokyo.  It has manufacturing, design and sales operations in around 20 countries.  It was the world's largest auto semiconductor maker in 2014, and the world's largest maker of microcontrollers.  It also makes mixed-signal integrated circuits and system on a chip semiconductors.

AKM Semiconductor, Inc.: AKM Semiconductor, Inc. (AKMS) is a semiconductor manufacturer headquartered in San Jose, California.  It is subsidiary of Asahi Kasei Microdevices (AKM) based in Tokyo, Japan.

Sony Mobile: Sony Mobile Communications Inc. is a multinational telecommunications company founded on October 1, 2001 as a joint venture between Sony and Ericsson, headquartered in Tokyo, Japan and wholly owned by Sony.  It was originally incorporated as Sony Ericsson, until Sony acquired Ericsson's share in the venture on February 16, 2012.

NXP Semiconductors: NXP Semiconductors N.V. is a Dutch global semiconductor manufacturer headquartered in Eindhoven, Netherlands.  The company employs approximately 45,000 people in more than 35 countries, including 11,200 engineers in 23 countries.  NXP reported revenue of $6.1 billion in 2015, including one month of revenue contribution from recently merged Freescale Semiconductor.

RIFA (manufacturer): RIFA (Radioindustrins Fabrik Aktiebolag) is a Swedish electronics manufacturer which was established in 1942 and originally manufactured resistors and capacitors. RIFA manufactured parts for the Swedish radio industry during World War II.  In 1947, it became incorporated into Telefonaktiebolaget LM Ericsson and became Ericsson Components in 1988 and then Ericsson Microelectronics in 2000.  The company made hybrid components for telephone exchanges for the joint venture company Ellemtel between Ericsson and Televerket.

ST-Ericsson: ST-Ericsson was a multinational manufacturer of wireless products and semiconductors, supplying to mobile device manufacturers.  ST-Ericsson was a 50/50 joint venture of Ericsson and STMicroelectronics established on 3 February 2009 and dissolved 2 August 2013.  Headquartered in Geneva, Switzerland, it was a fabless company, outsourcing semiconductor manufacturing to foundry companies.

Kyocera: Kyocera Corporation (京セラ株式会社 , Kyōsera Kabushiki-gaisha ) (   ) is a Japanese multinational electronics and ceramics manufacturer headquartered in Kyoto, Japan.  It was founded as Kyoto Ceramic Company, Limited (京都セラミック株式会社 , Kyōto Seramikku Kabushiki-gaisha ) in 1959 by Kazuo Inamori and renamed in 1982.  The company has diversified its founding technology in ceramic materials through internal development as well as strategic mergers and acquisitions.  It manufactures industrial ceramics, solar power generating systems, telecommunications equipment, office document imaging equipment, electronic components, semiconductor packages, cutting tools, and components for medical and dental implant systems.

Question: What is the name of this French-Italian multinational electronics and semiconductor manufacturer headquartered in Geneva, Switzerland, and part of a joint venture with Ericsson called ST-Ericsson?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "manufacturer_name": {
      "type": "string",
      "description": "The name of the French-Italian multinational electronics and semiconductor manufacturer."
    },
    "manufacturer_details": {
      "type": "object",
      "properties": {
        "nationality": {
          "type": "string",
          "description": "The nationality of the manufacturer."
        },
        "headquarters_city": {
          "type": "string",
          "description": "The city where the manufacturer is headquartered."
        },
        "headquarters_country": {
          "type": "string",
          "description": "The country where the manufacturer is headquartered."
        },
        "industry_type": {
          "type": "string",
          "description": "The primary industry of the manufacturer."
        }
      },
      "required": [
        "nationality",
        "headquarters_city",
        "headquarters_country",
        "industry_type"
      ],
      "additionalProperties": false
    },
    "joint_venture_participation": {
      "type": "object",
      "properties": {
        "joint_venture_name": {
          "type": "string",
          "description": "The name of the joint venture the manufacturer is part of."
        },
        "partner_company_name": {
          "type": "string",
          "description": "The name of the other main partner in the joint venture."
        },
        "joint_venture_role": {
          "type": "string",
          "description": "The role of the manufacturer in the joint venture (e.g., 'partner')."
        }
      },
      "required": [
        "joint_venture_name",
        "partner_company_name",
        "joint_venture_role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "manufacturer_name",
    "manufacturer_details",
    "joint_venture_participation"
  ],
  "additionalProperties": false
}
