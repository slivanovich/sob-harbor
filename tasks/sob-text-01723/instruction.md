{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSecular state: A secular state is an idea pertaining to secularism, whereby a state is or purports to be officially neutral in matters of religion, supporting neither religion nor irreligion.  A secular state also claims to treat all its citizens equally regardless of religion, and claims to avoid preferential treatment for a citizen from a particular religion/nonreligion over other religions/nonreligion.  Secular states do not have a state religion (established religion) or equivalent, although the absence of a state religion does not necessarily mean that a state is fully secular; however, a true secular state should steadfastly maintain national governance without influence from religious factions and vice versa; i.e. Separation of church and state.\n\nChurch of Denmark: The Evangelical Lutheran Church in Denmark or National Church, sometimes called Church of Denmark (Danish: \"Den Danske Folkekirke\" or \"Folkekirken\" , literally: \"the People's Church\" or \"the National Church\"), is the established, state-supported church in Denmark.  The reigning monarch is the supreme secular authority in the church.  s of 01 2017 , 75.9% of the population of Denmark are members, though membership is voluntary.\n\nReligion in Greenland: The majority of the Greenlandic population is Christian and associates with the Church of Denmark, which is Protestant in classification and Lutheran in orientation.  The Church of Denmark is the established church through the Constitution of Denmark; this applies to all of the Kingdom of Denmark, except for the Faroe Islands, as the Church of the Faroe Islands became independent in 2007.  But traditional Inuit spiritual beliefs remain strong in many of Greenland's remote communities.\n\nEcclesiastical capital: The religious capital or ecclesiastical capital of a region is a place considered pre-eminent by the adherents of a particular religion within that region.  This is most often significant for the region's predominant religion or state religion, if any.  The administrative headquarters of an organised religion may be centralised in a particular location; for example, Rome for the Catholic Church, or Salt Lake City for The Church of Jesus Christ of Latter-day Saints.  In an episcopal church, the site of the cathedral of the primate bishop of an area may be considered its ecclesiastical capital; for example, Armagh is the seat of the primate of All Ireland in both the Catholic church and the Anglican church.  Other places may be considered religious capitals by being centres of learning, such as Qom for Shia Islam in Iran; or places of pilgrimage, such as Varanasi for Hinduism.\n\nMilitary of Greenland: The government of Greenland does not have control of Greenland's military or foreign affairs.  The defence of Greenland is the responsibility of Denmark.  However, following the November 2008 referendum on increased autonomy, which attracted significant popular support (72% turnout, 75% vote in favor), the governments of Greenland and Denmark have agreed to a 30-point package that will begin to give Greenland greater powers over defence and foreign affairs.\n\nGreenland in World War II: In 1940, Greenland was a Danish colony.  The fall of Denmark to German invasion in April 1940 left Greenland an unoccupied territory of an occupied nation, but under threat of seizure by Britain or Canada.  To forestall this, the United States acted to guarantee Greenland's position.  However, with the entrance of the United States into the war in December 1941, Greenland became a combatant.  During 1941-45 the United States established numerous and extensive facilities for air and sea traffic in Greenland, as well as radio beacons, radio stations, weather stations, ports, depots, artillery posts, and search-and-rescue stations.  The U.S. Coast Guard also provided a considerable portion of the civilian resupply task up and down both coasts.  Economically, Greenland traded successfully with the United States, Canada, and Portugal, which, supplemented by the cryolite exports, caused a reanimation and permanent realignment of the island's economy.\n\nPhenomenology of religion: The phenomenology of religion concerns the experiential aspect of religion, describing religious phenomena in terms consistent with the orientation of worshippers.  It views religion as made up of different components, and studies these components across religious traditions in order to gain some understanding of them.  The phenomenological approach to the study of religion owes its conceptualization and early development to Pierre Daniël Chantepie de la Saussaye (1848-1920), William Brede Kristensen (1867-1953) and Gerardus van der Leeuw (1890-1950).\n\nHate group: A hate group is a social group that advocates and practices hatred, hostility, or violence towards members of a race, ethnicity, nation, religion, gender, gender identity, sexual orientation or any other designated sector of society.  According to the United States Federal Bureau of Investigation (FBI), a hate group's \"primary purpose is to promote animosity, hostility, and malice against persons belonging to a race, religion, disability, sexual orientation, or ethnicity/national origin which differs from that of the members of the organization.\"\n\nHate speech laws in France: The hate speech laws in France are matters of both civil law and criminal law.  Those laws protect individuals and groups from being defamed or insulted because they belong or do not belong, in fact or in fancy, to an ethnicity, a nation, a race, a religion, a sex, or a sexual orientation, or because they have a handicap.  The laws forbid any communication which is intended to incite discrimination against, hatred of, or harm to, anyone because of his belonging or not belonging, in fact or in fancy, to an ethnicity, a nation, a race, a religion, a sex, or a sexual orientation, or because he or she has a handicap.\n\nChurch of Greenland: The Church of Greenland, consisting of the Diocese of Greenland is the official Lutheran church in Greenland under the leadership of the Bishop of Greenland, currently being Sofie Petersen.  The Church of Greenland is semi-independent from the Church of Denmark however it is still considered a diocese of the Church of Denmark.\n\nQuestion: Religion in Greenland and Church of Denmark are what religion by orientation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"religious_entities\": {\n      \"type\": \"array\",\n      \"description\": \"Information about the religious entities mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"entity_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the religious entity.\"\n          },\n          \"orientation\": {\n            \"type\": \"string\",\n            \"description\": \"The specific religious orientation of the entity.\"\n          },\n          \"classification\": {\n            \"type\": \"string\",\n            \"description\": \"The broader religious classification of the entity.\"\n          }\n        },\n        \"required\": [\n          \"entity_name\",\n          \"orientation\",\n          \"classification\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"shared_orientation\": {\n      \"type\": \"string\",\n      \"description\": \"The common religious orientation shared by all entities in the question.\"\n    },\n    \"is_state_supported_church_involved\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if any of the religious entities are state-supported churches.\"\n    }\n  },\n  \"required\": [\n    \"religious_entities\",\n    \"shared_orientation\",\n    \"is_state_supported_church_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "religious_entities": {
        "type": "array",
        "description": "Information about the religious entities mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "entity_name": {
              "type": "string",
              "description": "The name of the religious entity."
            },
            "orientation": {
              "type": "string",
              "description": "The specific religious orientation of the entity."
            },
            "classification": {
              "type": "string",
              "description": "The broader religious classification of the entity."
            }
          },
          "required": [
            "entity_name",
            "orientation",
            "classification"
          ],
          "additionalProperties": false
        }
      },
      "shared_orientation": {
        "type": "string",
        "description": "The common religious orientation shared by all entities in the question."
      },
      "is_state_supported_church_involved": {
        "type": "boolean",
        "description": "Indicates if any of the religious entities are state-supported churches."
      }
    },
    "required": [
      "religious_entities",
      "shared_orientation",
      "is_state_supported_church_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
