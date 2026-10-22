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
Automatic test pattern generation: ATPG (acronym for both Automatic Test Pattern Generation and Automatic Test Pattern Generator) is an electronic design automation method/technology used to find an input (or test) sequence that, when applied to a digital circuit, enables automatic test equipment to distinguish between the correct circuit behavior and the faulty circuit behavior caused by defects.  The generated patterns are used to test semiconductor devices after manufacture, or to assist with determining the cause of failure (failure analysis).  The effectiveness of ATPG is measured by the number of modeled defects, or fault models, detectable and by the number of generated patterns.  These metrics generally indicate test quality (higher with more fault detections) and test application time (higher with more patterns).  ATPG efficiency is another important consideration that is influenced by the fault model under consideration, the type of circuit under test (full scan, synchronous sequential, or asynchronous sequential), the level of abstraction used to represent the circuit under test (gate, register-transfer, switch), and the required test quality.

Alex d'Arbeloff: Alexander Vladimir d'Arbeloff (December 21, 1927 – July 8, 2008) was the American co-founder of Teradyne, a multi-billion dollar Boston, Massachusetts-based manufacturer of automatic test equipment (ATE).

General Radio: General Radio Company (later, GenRad) was a broad-line manufacturer of electronic test equipment.  Started in Cambridge, Massachusetts in 1915 by Melville Eastham, the company moved to West Concord in the 1950s.  There, it became a major player in the automatic test equipment (ATE) business, manufacturing a line of testers for assembled printed circuit boards.  It also produced extensive lines of electrical component measuring equipment, sound and vibration measurement and RLC standards.

Automatic test equipment: Automatic test equipment or automated test equipment (ATE) is any apparatus that performs tests on a device, known as the device under test (DUT), equipment under test (EUT) or unit under test (UUT), using automation to quickly perform measurements and evaluate the test results.  An ATE can be a simple computer-controlled digital multimeter, or a complicated system containing dozens of complex test instruments (real or simulated electronic test equipment) capable of automatically testing and diagnosing faults in sophisticated electronic packaged parts or on wafer testing, including system on chips and integrated circuits.

Standard Test Data Format: Standard Test Data Format (STDF) is a proprietary file format for semiconductor test information originally developed by Teradyne, but it is now a de facto standard widely used throughout the semiconductor industry.  It is a commonly used format produced by automatic test equipment (ATE) platforms from companies such as LTX-Credence, Roos Instruments, Teradyne, Advantest, and others.

George Chamillard: George W. Chamillard (born 1939 in Needham, MA) is an American business executive who served as Chairman of the Board of Directors at Teradyne, a manufacturer of automatic test equipment for semiconductor devices, from 2000 to 2006.

Advantest: Advantest Corporation (株式会社アドバンテスト ) is a leading manufacturer of automatic test equipment (ATE) for the semiconductor industry, and a manufacturer of measuring instruments used in the design, production and maintenance of electronic systems including fiber optic and wireless communications equipment and digital consumer products.  Based in Tokyo, Advantest is a leading producer of Memory, SoC and RF test systems.  For the year ending March 31, 2017, the company reported a gain of ¥14.2 billion on revenues of ¥155.9 billion (US$1,398 million).  At March 31, 2010, the company lost ¥11.5 billion on revenues of ¥53.2 billion.

Verigy: Verigy Ltd is an Advantest Group company in the semiconductor automatic test equipment business.  The company existed as a business within Hewlett Packard before it was spun off in 2006 as a standalone company.  In 2010, Verigy was in the process of merging with LTX-Credence and on December 7, 2010 Advantest Japan made an all-cash offer for the company.  On July 4, 2011, after two reviews of the transaction by the Department of Justice the company announced that Advantest Corporation (, ) completed its acquisition of Verigy in an all-cash deal valued at $1.100 billion.  The resulting company is the largest manufacturer of semiconductor test equipment in the world.

Eagle Test Systems: Eagle Test Systems is a supplier of automatic test equipment (ATE) and operates as a business unit within the Teradyne Semiconductor Test Division.  Eagle's test equipment was designed to address volume production.  Customers, including semiconductor manufacturers and assembly and test subcontractors, use the products to test analog, a combination of digital and analog, known as mixed-signal, and radio frequency (RF) semiconductors.

Teradyne: Teradyne (), based in North Reading, Massachusetts in the United States, is a developer and supplier of automatic test equipment (ATE).  The company's divisions Semiconductor Test and Systems Test Group, are organized by the products they develop and deliver.  Teradyne's high-profile customers include Samsung, Qualcomm, Intel, Analog Devices, Texas Instruments and IBM.

Question: Eagle Test Systems is a supplier of automatic test equipment (ATE) and operates as a business unit within the Teradyne Semiconductor Test Division, Teradyne is based in North Reading, Massachusetts, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company whose location is being queried."
    },
    "parent_company_name": {
      "type": "string",
      "description": "The name of the parent company, if the queried company is a business unit."
    },
    "headquarters_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the company is based."
        },
        "state": {
          "type": "string",
          "description": "The state where the company is based."
        },
        "country": {
          "type": "string",
          "description": "The country where the company is based."
        }
      },
      "required": [
        "city",
        "state",
        "country"
      ],
      "additionalProperties": false
    },
    "country_of_headquarters": {
      "type": "string",
      "description": "The country where the company's headquarters is located."
    }
  },
  "required": [
    "company_name",
    "parent_company_name",
    "headquarters_location",
    "country_of_headquarters"
  ],
  "additionalProperties": false
}
