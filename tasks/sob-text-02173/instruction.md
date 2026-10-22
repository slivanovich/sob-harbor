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
Gustaf Dalén: Nils Gustaf Dalén (30 November 1869 – 9 December 1937) was a Swedish Nobel Laureate and industrialist, the founder of the AGA company and inventor of the AGA cooker and the Dalén light.  In 1912 he was awarded the Nobel Prize in Physics for his "invention of automatic regulators for use in conjunction with gas accumulators for illuminating lighthouses and buoys".

AGA AB: AGA AB, previously "AB Gasaccumulator" and "AB Svenska Gasaccumulator", was a Swedish industrial gas company founded in 1904.  Nobel Prize laureate Gustaf Dalén was instrumental in the success of the company.  Important inventions included the AGA cooker and the Dalén light.  In the 1990s AGA conceived and developed HiQ for specialty gases.  In 2000, AGA was integrated into Linde AG.

Benjamin Aga: Benjamin Aga (Karaim: Беньямин Агъа), who died in 1824, was the leader of the Crimean Karaites.  He was the royal treasurer of Şahin Giray, the last Crimean Khan, and therefore is called in Karaite literature "ha-Neeman" ("the Trusted")—an appellation bestowed also upon his father Samuel, who died in 1770, and who probably held the same office under former khans.  When Şahin Giray fled for his life from his rebellious subjects, and sought succor from his protectress Catherine II in St. Petersburg, Benjamin Aga followed him, hoping to collect the large sums of money that he had advanced to the fugitive.  Following the last partition of Poland in 1795, after Crimea had been under Russian rule for over a decade, Vilnius, Lutsk and Trakai came under Russian Rule.  Benjamin Aga, Solomon ben Nahamu Bobowitz, and the astronomer Isaac of Kalea, the son-in-law of Jacob Aga, who was the elder brother of Benjamin, went to St. Petersburg as a delegation from the Crimean Karaites, to petition the empress to release their sect from the double rate of taxation which all the Jews then had to pay.  Through the intervention of Count Nikolay Zubov, the delegation obtained from the empress the exemption from the "Jewish" taxes, some land grants, and other privileges which had not been asked for.  This established an important precedent for exempting the Karaites from subsequent anti-Jewish legislation.  The extraordinary success of the mission served to arouse great enthusiasm among the Karaites, and Aga and his fellow delegates were received with great honor on their return.  A large monolith, fashioned out of marble, with fitting inscription, was erected in the court of the kenesa at Eupatoria, to commemorate an event so important in the history of the Karaites of Russia.

Community Cooker: The Community Cooker (Kiswahili translation on "Jiko ya Jamii") is a stove designed to produce safe, clean and cheap energy for cooking from rubbish.  The Community Cooker was invented by Jim Archer, the Chairman of Planning Systems Services Ltd. (PLANNING) to address the accumulation of rubbish throughout Kibera, while providing relief to the deforestation and ground water pollution.

AGA cooker: The AGA cooker is a heat storage stove and cooker, which works on the principle that a heavy frame made of cast iron can absorb heat from a relatively low-intensity but continuously burning source, and the accumulated heat can then be used for cooking.  Originally heated by slow-burning coal, the Aga cooker was invented in 1922 by the Nobel Prize–winning Swedish physicist Gustaf Dalén (1869–1937), who was employed first as the chief engineer of the Swedish AGA company (Swedish "Aktiebolaget Svenska Gasaccumulator", English "Swedish Gas Accumulator, Limited").  The cookers were first imported to Britain in 1929, and were first manufactured there under licence in the early 1930s.  The cast-iron parts were first cast at the Coalbrookdale foundry in the 1940s, where they are still made by the Aga Rangemaster Group.

Amy Willcock: Amy Willcock is an American-born British-based cookery book writer, who having specialised in cooking on the AGA cooker, is popularly known as the "Queen of AGA cooking."

Natroun: Natroun (20 April 1984 – 2005) was a French Thoroughbred racehorse and sire.  Owned and bred by the Aga Khan IV and trained by Alain de Royer-Dupre he won three of five races as a three-year-old in 1987.  Unraced as a two-year-old he won two minor races in the spring before recording his most important success in the Prix du Jockey Club.  In his two remaining races he ran well when fourth under top weight in the Prix Niel and finished unplaced in the Prix de l'Arc de Triomphe.  He was retired from racing at the end of the year to stand as a breeding stallion but had very little success as a sire of winners in either Europe or Japan.

Karl Drais: Karl Drais (29 April 1785 – 10 December 1851) was a German inventor, who invented the Laufmaschine ("running machine"), also later called the velocipede, "draisine" (English) or "draisienne" (French), also nicknamed the dandy horse.  This incorporated the two-wheeler principle that is basic to the bicycle and motorcycle and was the beginning of mechanized personal transport.  Drais also invented the earliest typewriter with a keyboard in 1821, later developed into an early stenograph machine, a meat grinder, and a wood-saving cooker using a hay chest.

Aga saga: The Aga saga is a subgenre of the family saga genre of literature.  The genre is named for the AGA cooker, a type of stored-heat oven that came to be popular in medium to large country houses in the UK after its introduction in 1929.  It refers primarily to fictional family sagas dealing with British "middle-class country or village life".  The nickname "Aga saga" is sometimes used condescendingly about this type of fiction.  The term was incorporated into the "Oxford Companion to English Literature" in 2000.

Steam digester: The steam digester (or bone digester, and also known as Papin’s digester) is a high-pressure cooker invented by French physicist Denis Papin in 1679.  It is a device for extracting fats from bones in a high-pressure steam environment, which also renders them brittle enough to be easily ground into bone meal.  It is the forerunner of the autoclave and the domestic pressure cooker.

Question: Who invented the AGA cooker and was instrumental to the success of AGA AB?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the person."
    },
    "birth_year": {
      "type": "integer",
      "description": "The year the person was born."
    },
    "death_year": {
      "type": "integer",
      "description": "The year the person died."
    },
    "nobel_prize_winner": {
      "type": "boolean",
      "description": "Indicates if the person was a Nobel Prize laureate."
    },
    "invented_products": {
      "type": "array",
      "description": "A list of products invented by the person.",
      "items": {
        "type": "object",
        "properties": {
          "product_name": {
            "type": "string",
            "description": "The name of the invented product."
          },
          "invention_year": {
            "type": "integer",
            "description": "The year the product was invented, if specified."
          }
        },
        "required": [
          "product_name"
        ],
        "additionalProperties": false
      }
    },
    "company_affiliations": {
      "type": "array",
      "description": "A list of companies the person was affiliated with and their role.",
      "items": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string",
            "description": "The name of the company."
          },
          "role": {
            "type": "string",
            "description": "The role or contribution of the person to the company."
          }
        },
        "required": [
          "company_name",
          "role"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "person_name",
    "nationality",
    "birth_year",
    "death_year",
    "nobel_prize_winner",
    "invented_products",
    "company_affiliations"
  ],
  "additionalProperties": false
}
