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
ISO 3166-1 alpha-2: ISO 3166-1 alpha-2 codes are two-letter country codes defined in ISO 3166-1, part of the ISO 3166 standard published by the International Organization for Standardization (ISO), to represent countries, dependent territories, and special areas of geographical interest.  They are the most widely used of the country codes published by ISO (the others being alpha-3 and numeric), and are used most prominently for the Internet's country code top-level domains (with a few exceptions).  They were first included as part of the ISO 3166 standard in its first edition in 1974.

ISO 3166-2:TW: ISO 3166-2:TW is the entry for Taiwan in ISO 3166-2, part of the ISO 3166 standard published by the International Organization for Standardization (ISO), which defines codes for the names of the principal subdivisions (e.g., provinces or states) of all countries coded in ISO 3166-1.  Due to the political status of Taiwan in the United Nations, the ISO 3166-1 full name is Taiwan, Province of China.

Svalbard and Jan Mayen: Svalbard and Jan Mayen (Norwegian: "Svalbard og Jan Mayen" , ISO 3166-1 alpha-2: SJ, ISO 3166-1 alpha-3: SJM, ISO 3166-1 numeric: 744) is a statistical designation defined by ISO 3166-1 of two parts of Norway under separate jurisdictions—Svalbard and Jan Mayen.  While the two are combined for the purposes of the International Organization for Standardization (ISO) category, they are not administratively related.  This has further resulted in the country code top-level domain . sj being issued for Svalbard and Jan Mayen, and .  The United Nations Statistics Division also uses this code, but has named it Svalbard and Jan Mayen Islands.

.tw: . tw is the Internet country code top-level domain (ccTLD) for Taiwan (Republic of China).  The domain name is based on the ISO 3166-1 alpha-2 country code .  The registry is maintained by TWNIC, a Taiwanese non-profit organization appointed by National Communication Commission (NCC) and ministry of transportation and communications ROC.  Since March 1, 2001, TWNIC has stopped allow itself to sign up new domain names directly, instead allowing new registration through its contracted reseller registrars.

ISO 3166-2:RU: ISO 3166-2:RU is the entry for Russia in ISO 3166-2, part of the ISO 3166 standard published by the International Organization for Standardization (ISO), which defines codes for some of the names of the principal subdivisions (e.g., provinces or states) of all countries coded in ISO 3166-1.  ISO 3166-2:RU contains no codes for the Russian-administered Republic of Crimea and Federal City of Sevastopol, which are internationally recognized as part of Ukraine and do have codes in .

ISO 3166-1 numeric: ISO 3166-1 numeric (or numeric-3) codes are three-digit country codes defined in ISO 3166-1, part of the ISO 3166 standard published by the International Organization for Standardization (ISO), to represent countries, dependent territories, and special areas of geographical interest.  They are similar to the three-digit country codes developed and maintained by the United Nations Statistics Division, from which they originate in its UN M.49 standard.  They were first included as part of the ISO 3166 standard in its second edition in 1981, but they were released by the United Nations Statistics Division since as early as 1970.

ISO 3166-1 alpha-3: ISO 3166-1 alpha-3 codes are three-letter country codes defined in ISO 3166-1, part of the ISO 3166 standard published by the International Organization for Standardization (ISO), to represent countries, dependent territories, and special areas of geographical interest.  They allow a better visual association between the codes and the country names than the two-letter alpha-2 codes (the third set of codes is numeric and hence offers no visual association).  They were first included as part of the ISO 3166 standard in its first edition in 1974.

ISO 3166-2:GB: ISO 3166-2:GB is the entry for the United Kingdom in ISO 3166-2, part of the ISO 3166 standard published by the International Organization for Standardization (ISO), which defines codes for the names of the principal subdivisions (e.g., provinces or states) of all countries coded in ISO 3166-1.  The codes and structures used are provided to the ISO by British Standards and the Office for National Statistics.

ISO 3166-2:SJ: ISO 3166-2:SJ is the entry for Svalbard and Jan Mayen in ISO 3166-2, part of the ISO 3166 standard published by the International Organization for Standardization (ISO).  The standard defines codes for names of principal subdivisions of all countries coded in ISO 3166-1.  Svalbard and Jan Mayen does not exist as an administrative region, but rather consists of two separate parts of Norway under separate jurisdictions—Svalbard and Jan Mayen.  Further subdivision for Svalbard and Jan Mayen occurs under Norway's entry, , namely NO-21 for Svalbard and NO-22 for Jan Mayen.  There are currently no ISO 3166-2 codes for Svalbard and Jan Mayen.

ISO 3166-1: ISO 3166-1 is part of the ISO 3166 standard published by the International Organization for Standardization (ISO), and defines codes for the names of countries, dependent territories, and special areas of geographical interest.  The official name of the standard is "Codes for the representation of names of countries and their subdivisions – Part 1: Country codes".  It defines three sets of country codes:

Question: .tw, is the Internet country code top-level domain (ccTLD) for Taiwan (Republic of China), the domain name is based on which codes are two-letter country codes defined in ISO 3166-1, part of the ISO 3166 standard published by the International Organization for Standardization (ISO), to represent countries, dependent territories, and special areas of geographical interest?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cctld": {
      "type": "string",
      "description": "The Internet country code top-level domain (ccTLD)."
    },
    "represented_entity": {
      "type": "string",
      "description": "The country or territory represented by the ccTLD."
    },
    "iso_code_details": {
      "type": "object",
      "properties": {
        "code_type": {
          "type": "string",
          "description": "The specific type of ISO 3166-1 code the ccTLD is based on."
        },
        "code_format_description": {
          "type": "string",
          "description": "A description of the code format (e.g., two-letter, three-letter, numeric)."
        },
        "standard_part": {
          "type": "string",
          "description": "The specific part of the ISO 3166 standard that defines the code."
        },
        "publishing_organization": {
          "type": "string",
          "description": "The organization that publishes the ISO standard."
        }
      },
      "required": [
        "code_type",
        "code_format_description",
        "standard_part",
        "publishing_organization"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "cctld",
    "represented_entity",
    "iso_code_details"
  ],
  "additionalProperties": false
}
