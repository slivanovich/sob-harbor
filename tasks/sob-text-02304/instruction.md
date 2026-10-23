{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2018 Campeonato Carioca: The 2018 Campeonato Carioca de Futebol will be the 115th edition of the main division of football in Rio de Janeiro.  The contest is organized by FERJ.  The top four teams will compete in 2018 Copa do Brasil.  was maintained the format of the edition of 2017, with the initial phase with the four worst of worse campaign over two teams promoted the Série B1, with the two best placed along the main phase, divided into two groups of six teams and two shifts (Taça Guanabara and Taça Rio) and the four finalists for the championship, coming from the teams best placed in the general classification.\n\nBentley compounds: The Bentley compounds are a class of semi-synthetic opioids that were first synthesized by K. W. Bentley by Diels-Alder reaction of thebaine with various dienophiles.  The compounds are also known as thevinols, orvinols, or bridged oripavine derivatives, due to the characteristic 6,14-\"endo\"-etheno- bridge and substitution at the 7α position.  Buprenorphine and etorphine are perhaps the best known of the family, which was the first series of extremely potent μ-opioid agonists, with some compounds in the series having over many thousands of times the analgesic potency of morphine.\n\n2008 Twenty20 Cup knockout stage: The knockout stage of the 2008 Twenty20 Cup comprises the quarter-finals, semi-finals and final of the 2008 Twenty20 Cup.  The top two teams from each of the three groups progressed to the quarter finals along with the two best placed third teams.  The teams were redrawn and played one knockout match to decide the semi-finalists.  Finals day was held on 26 July 2008.\n\nStuart Turnbull: Stuart McLean Turnbull (born 1947) is a finance academic and practitioner, best known for the Jarrow–Turnbull model for pricing credit derivatives. His research has focused on credit- and market risk models, counterparty risk modeling, pricing CDS tranches, and forward default premiums.  He has authored over fifty academic papers and has published two books on derivatives.\n\nWilliam Toy: William W. Toy (\"Bill\") is a leading finance practitioner in the area of equity derivatives, and a pioneering modeller in the area of interest rate derivatives.  He is best known as a co-developer of the Black–Derman–Toy short rate model, widely used for interest rate and bond options.  His roles have included managing director and head of US Equity Derivatives at CDC Capital, Inc. in New York City, a subsidiary of Caisse des dépôts et consignations, and Vice President in Goldman Sachs' equity derivatives department.  He earned his S.B., S.M. and Ph.D. (1978; experimental elementary particle physics) at MIT.\n\nKalle Reichelt: Karl Ludvig \"Kalle\" Reichelt (28 November 1933 – 29 October 2016) was a Norwegian medical researcher.  He was best known for his research on the opioid peptides in casein and gluten.  He also did important work on cancer.\n\nKazuhiro Sano: Kazuhiro Sano (佐野和宏 , \"Sano Kazuhiro\" , born in 1956) is a Japanese film director, screenwriter and actor best known for his \"pink films\" of the 1990s.  Along with fellow directors, Takahisa Zeze, Toshiki Satō and Hisayasu Sato, he is known as one of the \"Four Heavenly Kings of Pink\" (ピンク四天王 , pinku shitenno ) .  Sano's films differ from those of other \"Pink film\" directors of the time in that, while not necessarily optimistic or upbeat, they are more concerned with relationships and romance than violence and sadism.  He has the distinction of winning the Best Director prize three consecutive years at the Pink Grand Prix.  He has also been given two Best Actor awards, two Best Actor second place awards, and a Best Screenplay award at this ceremony.\n\nBuprenorphine: Buprenorphine, sold under the brand name Subutex, among others, is an opioid used to treat opioid addiction, moderate acute pain and moderate chronic pain.  The combination buprenorphine/naloxone is also used for opioid addiction.\n\nChronics: Chronics are an Italian power pop and punk band, known for playing power pop with a garage rock attitude, and often drawing comparisons to The Saints (band) and The Real Kids.  In 1999 they released their debut single on Rip Off Records (a cult record label in the 90′s along with In the Red Records and Sympathy For The Record Industry), along with two full-length albums and two best of records.  After several years idle, Chronics returned in 2014 by releasing a split single on Asian Man Records with Mike Watt and the Secondmen.  In 2015 they release two more split 7\", another split single with Mike Watt (Minutemen (band), The Stooges) and a split single with Barrence Whitfield & the Savages.\n\nPilot (Faking It): Pilot is the first episode of MTV's comedy series \"Faking It\".  The episode aired on the MTV in the United States on April 22, 2014.  The episode primarily focuses on introducing the series, two best friends, Karma (Katie Stevens) and Amy (Rita Volk) after numerous failed attempts to become popular, they are mistakenly outed as lesbians, which instantly makes them popular and the centre of attention.  Karma is aroused with their sudden popularity, as the most handsome guy Liam (Gregg Sulkin) notices her and becomes attracted to her.  On the contrary, Amy is annoyed with having to carry on.\n\nQuestion: Which opioid along with Subutex makes up the two best known of the thevinol, orvinol, or bridged oripavine derivatives?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"opioid_class_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the class of semi-synthetic opioids.\"\n    },\n    \"primary_opioid_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the opioid mentioned in the question.\"\n    },\n    \"primary_opioid_brand_name\": {\n      \"type\": \"string\",\n      \"description\": \"The brand name of the primary opioid.\"\n    },\n    \"other_known_opioid\": {\n      \"type\": \"string\",\n      \"description\": \"The other best-known opioid derivative from the same class.\"\n    },\n    \"derivatives_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the characteristic structure of these derivatives.\"\n    }\n  },\n  \"required\": [\n    \"opioid_class_name\",\n    \"primary_opioid_name\",\n    \"primary_opioid_brand_name\",\n    \"other_known_opioid\",\n    \"derivatives_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "opioid_class_name": {
        "type": "string",
        "description": "The name of the class of semi-synthetic opioids."
      },
      "primary_opioid_name": {
        "type": "string",
        "description": "The name of the opioid mentioned in the question."
      },
      "primary_opioid_brand_name": {
        "type": "string",
        "description": "The brand name of the primary opioid."
      },
      "other_known_opioid": {
        "type": "string",
        "description": "The other best-known opioid derivative from the same class."
      },
      "derivatives_description": {
        "type": "string",
        "description": "A description of the characteristic structure of these derivatives."
      }
    },
    "required": [
      "opioid_class_name",
      "primary_opioid_name",
      "primary_opioid_brand_name",
      "other_known_opioid",
      "derivatives_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
