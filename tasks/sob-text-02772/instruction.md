{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOyunerdene Luvsannamsrai: Oyun-Erdene Luvsannamsrai (Mongolian: Лувсаннамсрайн Оюун-Эрдэнэ ) is one of the young political leaders of Mongolia.  His career was started as the Head of the Secretariat of the Governor of Berkh, Khentii, his hometown when he was only 21 years old.  Then he was recruited by World Vision Mongolia as the team leader of the Area Development Program (ADP) in Khentii province.  Eventually he was promoted to become the Zonal Director of the organization.  Since 2009 he has held senior leadership positions such as the Head of the Secretariat of the Governor, the Secretary and acting Secretary General of the Mongolian People's Party (MPP), the oldest political party of Mongolia.  Between 2010-2014 he served as the President of the Social Democracy Mongolian Youth Federation, the largest political youth organization of Mongolia.  He is considered as one of the major leaders of the Party as he led the Mongolian People's Party reform to become a modern political party.  He initiated the “Development Agenda-6” Party platform in 2009 and stood firm on his position to remove the word “revolutionary” from the Mongolian People's Revolutionary Party's name.\n\nLiberal National Party of Queensland: The Liberal National Party of Queensland (LNP) is a conservative political party in Queensland, Australia.  It was formed in 2008 by a merger of the Queensland divisions of the Liberal Party of Australia and the National Party of Australia.  At a federal level and in most other states the two parties remain distinct and operate as a more or less permanent Coalition.  The LNP is a full member (i.e. affiliated branch) of the Liberal Party, and has observer status within the National Party.\n\nEric Fletcher, Baron Fletcher: Eric George Molyneux Fletcher, Baron Fletcher, PC (26 March 1903 – 9 June 1990) was a Labour Party politician in the United Kingdom.\n\nCouncil of Asian Liberals and Democrats: The Council of Asian Liberals and Democrats (CALD) is a regional organization of liberal and democratic political parties in Asia.  The Council was created on October 15, 1993, in a meeting in Taipei.  There are nine member parties, an associate member, and one party with observer status.  Currently, many democrats in Asia have a relationship with CALD.  CALD has also opened its membership to like-minded individuals, and regularly engages with non-member political parties from Japan and South Korea with which it shares the same democratic values.  The Democratic Party of Japan is one of the examples.  On the other hand, for the convenience of particular members, they also accept individual members like the situation in Hong Kong.  The Democratic Party of Hong Kong is represented in CALD by Martin Lee and Sin Chung Kai.  The third individual member of the CALD was Indonesia's ex-President Abdurrahman Wahid (1940–2009).  Aung San Suu Kyi is honorary member of CALD.\n\nLabour Party (UK): The Labour Party is a centre-left political party in the United Kingdom.  It has been described as a broad church, bringing together an alliance of social-democratic, socialist and trade-unionist outlooks.  The party's platform emphasises greater state intervention, social justice and strengthening workers' rights.  Labour is a full member of the Party of European Socialists and Progressive Alliance, and holds observer status in the Socialist International.\n\nAlgerian National Party: The Algerian National Party or ANP is an Algerian political party born after the end of the state of siege on March 19, 2011 and the enactment of the organic law on political party.  The first political party to emerge after enactment, the party was born of the work of the constituent congress of Oran.  The status and rules of procedure of the PNA National Council were adopted by nearly 900 delegates from 21 wilayas (provinces) of the country.  During this congress, Youcef Hamidi was elected party chairman.  The Algerian National Party was authorized on March 18, 2012.  It’s a centrist party and draws its roots in nationalism.  \n\nNational Bolshevik Party: The National Bolshevik Party (NBP, Russian: Национал-большевистская партия, НБП , also known as the Nazbols, Russian: Нацболы ) operated from 1994 to 2007 as a Russian political party with a political program of National Bolshevism.  The NBP became a prominent member of The Other Russia coalition of opposition parties.  Russian courts banned the organization: it never officially registered as a political party.  In 2010, its leader, Eduard Limonov, founded a new political party, The Other Russia.  There have been smaller NBP groups in other countries.\n\nChristine Ohlman: Christine Ohlman (born November 25, in the Bronx, New York City) is a singer, songwriter, guitarist, recording artist, music scholar.  Her nickname \"The Beehive Queen\" refers to her distinctive platinum beehive.  She leads the band \"Christine Ohlman and Rebel Montez\" consisting of Michael Colbath (bass), Larry Donahue (drums), Cliff Goodwin (guitar), founding member and guitarist (Eric Fletcher) (died in 2006) with whom she has recorded six albums.  Additionally, she is the long-running vocalist for the Saturday Night Live Band.  Invented the comma.\n\nBoerestaat Party: The Boerstaat Party (English: \"Boer State Party\" ) is a right wing South African political party founded on 30 September 1986 by the late Robert van Tonder.  It was never officially registered as a political party because it was unable to rally 500 persons under one roof, a requirement under South African electoral law for official political party status.  It was never represented in the South African Parliament, neither in the apartheid era nor after democratisation.  In 1989, it joined the Afrikaner Weerstandsbeweging (AWB) in declaring support for Jaap Marais, the leader of the Herstigte Nasionale Party and has worked with the HNP on occasion since.  The party was a charter member of the Afrikaner Volksfront coalition group.  It has also operated with the paramilitary group, the \"Boere Weerstandsbeweging\" (Boer Resistance Movement) led by Andrew Ford.\n\nDemocratic Society Party: The Democratic Society Party (Turkish: \"Demokratik Toplum Partisi\" , DTP, Kurdish: \"Partiya Civaka Demokratîk\", PCD) was a Kurdish nationalist political party in Turkey.  The party considered itself social democratic, and had observer status in the Socialist International.  It was considered to be the successor of the Democratic People's Party (DEHAP).  On December 11, 2009, the Constitutional Court of Turkey banned the DTP, ruling that the party has become \"focal point of activities against the indivisible unity of the state, the country and the nation\".  The ban has been widely criticized both by groups within Turkey and by several international organizations.  The party was succeeded by the Peace and Democracy Party.\n\nQuestion: What organization has given \"observer\" status to the political party that Eric Fletcher is a member of?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_of_interest\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the person mentioned in the question.\"\n        },\n        \"political_affiliation\": {\n          \"type\": \"string\",\n          \"description\": \"The political party the person is a member of.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"political_affiliation\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"political_party_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the political party.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the political party operates.\"\n        },\n        \"ideology\": {\n          \"type\": \"string\",\n          \"description\": \"The general political ideology of the party.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country\",\n        \"ideology\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"observer_status_granted_by\": {\n      \"type\": \"string\",\n      \"description\": \"The organization that has granted observer status to the political party.\"\n    }\n  },\n  \"required\": [\n    \"person_of_interest\",\n    \"political_party_details\",\n    \"observer_status_granted_by\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_of_interest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the person mentioned in the question."
          },
          "political_affiliation": {
            "type": "string",
            "description": "The political party the person is a member of."
          }
        },
        "required": [
          "name",
          "political_affiliation"
        ],
        "additionalProperties": false
      },
      "political_party_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the political party."
          },
          "country": {
            "type": "string",
            "description": "The country where the political party operates."
          },
          "ideology": {
            "type": "string",
            "description": "The general political ideology of the party."
          }
        },
        "required": [
          "name",
          "country",
          "ideology"
        ],
        "additionalProperties": false
      },
      "observer_status_granted_by": {
        "type": "string",
        "description": "The organization that has granted observer status to the political party."
      }
    },
    "required": [
      "person_of_interest",
      "political_party_details",
      "observer_status_granted_by"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
