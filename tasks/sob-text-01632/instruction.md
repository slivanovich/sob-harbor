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
Operation Moshtarak: Operation Moshtarak (Dari for "Together" or "Joint"), also known as the Battle of Marjah, an International Security Assistance Force (ISAF) pacification offensive in the town of Marjah, Helmand Province, Afghanistan.  It involved a combined total of 15,000 Afghan, American, British, Canadian, Danish, and Estonian troops; constituting the largest joint operation of the War in Afghanistan up to that point.  The purpose of which, to remove the Taliban from Marja, eliminating the last Taliban stronghold in central Helmand Province.

Opium production in Afghanistan: Afghanistan's opium poppy production goes into more than 90% of heroin worldwide.  Afghanistan has been the world's greatest illicit opium producer, ahead of Burma (Myanmar), the "Golden Triangle", and Latin America since 1992, excluding the year 2001.  Afghanistan is the main producer of opium in the "Golden Crescent".  Opium production in Afghanistan has been on the rise since U.S. occupation started in 2001.  Based on UNODC data, opium poppy cultivation was more in each of the growing seasons in the periods between 2004 and 2007 than in any one year during Taliban rule.  More land is now used for opium in Afghanistan than is used for coca cultivation in Latin America.  In 2007, 93% of the "non-pharmaceutical-grade" opiates on the world market originated in Afghanistan.  This amounts to an export value of about $4 billion, with a quarter being earned by opium farmers and the rest going to district officials, insurgents, warlords, and drug traffickers.

Opium Nation: Opium Nation: Child Brides, Drug Lords, and One Woman's Journey Through Afghanistan is a 2011 book by Fariba Nawa.  The author travels throughout Afghanistan to talk with individuals part of the opium production in Afghanistan, centering on women's role in it.  Generally, reviewers felt that the book succeeded in its portrayal of Afghan culture and the impact of the opium trade on Afghans.

Wech Baghtu wedding party airstrike: The Wech Baghtu wedding party airstrike refers to the killing of 63 people including 37 Afghan civilians, mostly women and children, and 26 insurgents by a United States military airstrike on November 3, 2008.  The group was celebrating a wedding at a housing complex in the village of Wech Baghtu, a Taliban stronghold in the Shah Wali Kot District of Kandahar province, Afghanistan.

Opium licensing: Opium licensing is a policy instrument used to counter illegal drug cultivation and production.  It has been used in countries such as Turkey and India to curb illegal opium production.  The main mechanism used under opium licensing is a shift from cultivation and/or production for the illegal market towards legal uses such as the production of essential medicines such as morphine and codeine.

Opium production in Myanmar: Opium production in Myanmar (also known as "Burma") has historically been a major contributor to the county's gross domestic product (GDP).  Burma is the world's second largest producer of opium after Afghanistan, producing some 25% of the world's opium, and forms part of the Golden Triangle.  The opium industry was a monopoly during colonial times and has since been illegally operated by corrupt officials in the Burmese military and rebel fighters, primarily as the basis for heroin manufacture.

Makin, Pakistan: Makin or Makeen (Pashto: مکین‎ ) is a small town in South Waziristan, Pakistan, located on the Y-junction between Sararogha and Wana, just south of Razmak in North Waziristan.  It is mainly populated by members of the Mehsud tribe.  The Pakistani military has called it "the nerve center" of the Pakistani Taliban.  Just north of Makin is the village of China, and the Taliban stronghold of Ladha is a few kilometers to the south.

Siege of Kunduz: The Siege of Kunduz took place in 2001 during the War in Afghanistan.  After the fall of Mazar-i-Sharif on November 9, the focus of the Northern Alliance advance shifted towards the city of Kunduz, which was the last remaining Taliban stronghold in northern Afghanistan.

Helmand province campaign: The Helmand province campaign was a series of military operations conducted by the International Security Assistance Force (ISAF) forces against Taliban insurgents in the Helmand Province of Afghanistan.  Their objective was to control a province that was known to be a Taliban stronghold, and a center of opium production. <ref name="Gall/Wafa-NYT"> </ref>

Michael Alford (artist): Michael Alford (born 15 September 1958 in Cookham, England) is a British figurative painter whose work includes landscapes and cityscapes, figures, portraits and nudes.  Mostly self-taught, he has studied and the Slade and the Chelsea School of Art.  Early in his career he had an annual show at the Duncan Campbell Gallery in Mayfair and lived in Spain for extended period where the cost of living was reasonable.  He also worked as a muralist.  In 2010 he served as official War Artist to the 1st Battalion Grenadier Guards during their tour of Helmand, Afghanistan.  More recently he has painted nudes, cityscapes, a portrait of Vaughan Smith and completed a commission for the 1st Battalion Royal Irish Regiment.

Question: What did Michael Alford serve as, as part of the ISAF force against a known Taliban stronghold and center of opium production?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "role": {
      "type": "string",
      "description": "The specific role the person served in."
    },
    "military_unit": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the military unit."
        },
        "affiliation": {
          "type": "string",
          "description": "The larger force or alliance the unit was part of."
        }
      },
      "required": [
        "name",
        "affiliation"
      ],
      "additionalProperties": false
    },
    "location_of_service": {
      "type": "object",
      "properties": {
        "province": {
          "type": "string",
          "description": "The province where the service took place."
        },
        "country": {
          "type": "string",
          "description": "The country where the service took place."
        },
        "attributes": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key characteristics or descriptions of the location."
        }
      },
      "required": [
        "province",
        "country",
        "attributes"
      ],
      "additionalProperties": false
    },
    "year_of_service": {
      "type": "integer",
      "description": "The year the service took place."
    }
  },
  "required": [
    "person_name",
    "role",
    "military_unit",
    "location_of_service",
    "year_of_service"
  ],
  "additionalProperties": false
}
