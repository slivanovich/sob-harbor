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
Vertic: Vertic (Vertic A/S) is a Danish digital marketing and advertising agency founded in Copenhagen, Denmark in 2002.  The company has offices in Copenhagen, New York City, Seattle and Singapore.  Its clients include GE, Microsoft, Novo Nordisk, SAP, AARP and Vestas.  Vertic is a development partner for LinkedIn and twice (2011, 2013) received The Internationalist's Award for Innovative Digital Marketing Solutions for its marketing of the LinkedIn platform.

Luna\TBWA: Luna\TBWA is a Slovenian advertising agency based in Ljubljana.  Its clients include Si.mobil, NLB, Krka, Beiersdorf, Mars, Nissan, BMW and Henkel.  In March 2012, Luna\TBWA was proclaimed the best Slovenian advertising agency of 2011 at the Slovenian Advertising Festival.

Lupin Limited: Lupin Limited is a transnational pharmaceutical company based in Mumbai.  It is the seventh-largest company by market capitalization; and the 10th-largest generic pharmaceutical company by revenue globally.  Lupin is the fifth-largest generic pharmaceutical company in the US by prescription-led market share and 3rd largest Indian pharmaceutical company by revenue.  It has the distinction of being the fastest growing generic pharmaceutical player in the US and Japan;, and is the 4th largest and the fastest growing generic pharmaceutical player in South Africa.

Social Beat: Social Beat, is a Digital Marketing services and product company based in Chennai, Bangalore and Mumbai, India.  Its services include search engine marketing, social media marketing, web design and integrated digital marketing.  Their clients include Dr. Mohan's Diabetes Centre , Dr. Smilez Chain of Dental Clinics, India Home Healthcare, PlanetSuperheroes.com and Magickart.in.

Fast Web Media: Fast Web Media is a digital marketing agency with offices in MediaCityUK and London.  The company provides clients with digital marketing services, specialising in search marketing, search engine optimisation, technical development, social media and mobile, and was named Best Agency at the UK Search Awards 2011.

Sun Pharmaceutical: Sun Pharmaceutical Industries Limited (, ) is an Indian multinational pharmaceutical company headquartered in Mumbai, Maharashtra that manufactures and sells pharmaceutical formulations and active pharmaceutical ingredients (APIs) primarily in India and the United States.  The company offers formulations in various therapeutic areas, such as cardiology, psychiatry, neurology, gastroenterology and diabetology.  It also provides APIs such as warfarin, carbamazepine, etodolac, and clorazepate, as well as anticancers, steroids, peptides, sex hormones, and controlled substances.

Digital Marketing Institute: The Digital Marketing Institute is a higher education body in the Republic of Ireland offering further education in the field of digital marketing.  The Digital Marketing Institute is the world’s leading digital marketing and selling professional certification body.  Through its growing network of over 80 education partners in 100 countries, the digital specialist offers industry validated professional certifications from associate to master level.

Teva Pharmaceutical Industries: Teva Pharmaceutical Industries Ltd. (Hebrew: טבע תעשיות פרמצבטיות בע"מ‎ ) is an Israeli multinational pharmaceutical company headquartered in Petah Tikva, Israel.  It specializes primarily in generic drugs, but other business interests include active pharmaceutical ingredients and, to a lesser extent, proprietary pharmaceuticals.  It is the largest generic drug manufacturer in the world and one of the 15 largest pharmaceutical companies worldwide.  Teva's facilities are located in Israel, North America, Europe, and South America.  Teva shares trade on both the New York Stock Exchange (via ADRs) and the Tel Aviv Stock Exchange.  The company is a member of the Pharmaceutical Research and Manufacturers of America (PhRMA).

Ranbaxy Laboratories: Ranbaxy Laboratories Limited () is an Indian multinational pharmaceutical company that was incorporated in India in 1961.  The company went public in 1973 and Japanese pharmaceutical company Daiichi Sankyo acquired a controlling share in 2008.  In 2014, Sun Pharma acquired the entire 63.4% share of Ranbaxy making the conglomerate the world’s fifth largest specialty generic pharma company.

Novo Nordisk: Novo Nordisk is a Danish multinational pharmaceutical company headquartered in Bagsværd, Denmark, with production facilities in eight countries, and affiliates or offices in 75 countries.  Novo Nordisk is controlled by majority shareholder Novo Holdings A/S which holds approximately 25% of its shares and a supermajority (75%) of its voting shares.

Question: Vertic A/S is a Danish digital marketing and advertising agency, clients include which Danish multinational pharmaceutical company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "agency_name": {
      "type": "string",
      "description": "The name of the digital marketing and advertising agency."
    },
    "agency_country": {
      "type": "string",
      "description": "The country where the agency was founded."
    },
    "client_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the client company."
        },
        "type": {
          "type": "string",
          "description": "The industry type of the client company."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the client company is headquartered."
        },
        "is_multinational": {
          "type": "boolean",
          "description": "Indicates if the client company is multinational."
        }
      },
      "required": [
        "name",
        "type",
        "country_of_origin",
        "is_multinational"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "agency_name",
    "agency_country",
    "client_company"
  ],
  "additionalProperties": false
}
