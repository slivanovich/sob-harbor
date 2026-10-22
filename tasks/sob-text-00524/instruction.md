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
USNS Mission San Luis Obispo (T-AO-127): SS "Mission San Luis Obispo" was a Type T2-SE-A2 tanker built for the United States Maritime Commission during World War II.  After the war she was acquired by the United States Navy as USS "Mission San Luis Obispo" (AO-127).  Later the tanker transferred to the Military Sea Transportation Service as USNS "Mission San Luis Obispo" (T-AO-127).  A "Mission Buenaventura"-class oiler , she was named for Mission San Luís Obispo de Tolosa in San Luis Obispo, California.

Motel: A motel is a hotel designed for motorists and usually has a parking area for motor vehicles.  Entering dictionaries after World War II, the word "motel", coined as a portmanteau contraction of "motor hotel", originates from the Milestone Mo-Tel of San Luis Obispo, California (now called the Motel Inn of San Luis Obispo), which was built in 1925.  The term referred initially to a type of hotel consisting of a single building of connected rooms whose doors faced a parking lot and in some circumstances, a common area or a series of small cabins with common parking.  Motels are often individually owned, though motel chains do exist.

Skin cancer in horses: Skin cancer, or neoplasia, is the most common type of cancer diagnosed in horses, accounting for 45 to 80% of all cancers diagnosed.  Sarcoids are the most common type of skin neoplasm and are the most common type of cancer overall in horses.  Squamous-cell carcinoma is the second-most prevalent skin cancer, followed by melanoma.  Squamous-cell carcinoma and melanoma usually occur in horses greater than 9-years-old, while sarcoids commonly affect horses 3 to 6 years old.  Surgical biopsy is the method of choice for diagnosis of most equine skin cancers, but is contraindicated for cases of sarcoids.  Prognosis and treatment effectiveness varies based on type of cancer, degree of local tissue destruction, evidence of spread to other organs (metastasis) and location of the tumor.  Not all cancers metastasize and some can be cured or mitigated by surgical removal of the cancerous tissue or through use of chemotherapeutic drugs.

Calochortus simulans: Calochortus simulans is a California species of flowering plant in the lily family known by the common name San Luis Obispo mariposa lily, not to be confused with the San Luis mariposa lily "C. obispoensis".  It is native to San Luis Obispo County, California, and its range extends south into the northern part of Santa Barbara County.

Fortissimo (song): "Fortissimo" is a 1966 song brought to success by Rita Pavone.  The music was composed by Bruno Canfora, while the lyrics were written by director and screenwriter Lina Wertmüller, at the time a close collaborator of Pavone, after having directed her in the television miniseries "Il giornalino di Gian Burrasca" and in the musicarello film "Rita the Mosquito".  The arrangements of the song are by Luis Bacalov.

USNS Mission San Luis Rey (T-AO-128): SS "Mission San Luis Rey" was a Type T2-SE-A2 tanker built for the United States Maritime Commission during World War II.  After the war she was acquired by the United States Navy as USS "Mission San Luis Rey" (AO-128).  Later the tanker transferred to the Military Sea Transportation Service as USNS "Mission San Luis Rey" (T-AO-128).  She was a member of the "Mission Buenaventura"-class oiler and was named for Mission San Luis Rey de Francia, located in Oceanside, California.

Uterine cancer: Uterine cancer or womb cancer is any type of cancer that emerges from the tissue of the uterus.  It can refer to several types of cancer, with cervical cancer (arising from the lower portion of the uterus) being the most common type worldwide and the second most common cancer in women in developing countries.  Endometrial cancer (or cancer of the inner lining of the uterus) is the second most common type, and fourth most common cancer in women from developed countries.  Risk factors depend on specific type, but obesity, older age, and human papillomavirus infection add the greatest risk of developing uterine cancer.  Early on, there may be no symptoms, but irregular vaginal bleeding, pelvic pain or fullness may develop.  If caught early, most types of uterine cancer can be cured using surgical or medical methods.  When the cancer has extended beyond the uterine tissue, more advanced treatments including combinations of chemotherapy, radiation therapy, or surgery may be required.

Poa diaboli: Poa diaboli is a rare species of grass known by the common name Diablo Canyon bluegrass.  It is endemic to San Luis Obispo County, California, where it is known from about five occurrences in the San Luis Mountains near the coast.  The type specimen was collected in Montaña de Oro State Park and the grass was described as a new species in 2003.  The grass occurs on rugged mountaintops and north-facing slopes in thin soils covering shale rock within a few kilometers of the coastline.  Its habitat includes chaparral, oak woodland, coastal sage scrub, and Bishop pine forest.

Luis Bacalov: Luis Enríquez Bacalov (born 30 August 1933) is an Argentine-born Italian composer of film scores. Early on in his career, he composed scores for Spaghetti Western films.  In the early 1970s, he collaborated with Italian progressive rock bands.  Bacalov has been nominated twice for the Academy Award for Original Score, winning it in 1996 for "Il Postino".  Bacalov has composed significant works for chorus and orchestra.  Presently he is the artistic director of the "Orchestra della Magna Grecia" in Taranto, Italy.

San Luis Obispo County Search and Rescue: San Luis Obispo County Sheriff Search and Rescue is an all-volunteer organization in San Luis Obispo County within the county's Sheriff's office.  With approximately fifty active members year round, San Luis Obispo County's Search and Rescue (SLOSAR) responds to searches for missing people, evidence and other search requests in the county and on mutual aid calls anywhere in the state of California.  SLOSAR is a National Association of Search and Rescue (NASAR) Type II certified team able to handle the urban and wilderness searches below 7,000 feet in elevation.

Question: What type of industry does Fortissimo and  Luis Bacalohave in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_industry": {
      "type": "string",
      "description": "The industry that both entities have in common."
    },
    "industry_category": {
      "type": "string",
      "description": "A broader category for the identified common industry."
    },
    "entities_involved": {
      "type": "array",
      "description": "Details about each entity and its connection to the common industry.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "role": {
            "type": "string",
            "description": "The primary role or nature of the entity."
          },
          "specific_connection_to_film": {
            "type": "string",
            "description": "How this specific entity is connected to the film industry."
          }
        },
        "required": [
          "entity_name",
          "role",
          "specific_connection_to_film"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_industry",
    "industry_category",
    "entities_involved"
  ],
  "additionalProperties": false
}
