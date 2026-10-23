{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAirPort Extreme: The AirPort Extreme is a residential gateway product from Apple Inc. combining the functions of a router, network switch, wireless access point and NAS as well as varied other functions, and one of Apple's AirPort products.  The latest model, the 6th generation, supports 802.11ac networking in addition to older standards.  Versions of the same system with a built-in network-accessible hard drive are known as the AirPort Time Capsule.\n\nAirPort Express: The AirPort Express is a Wi-Fi base station product from Apple Inc., and is one of Apple's AirPort products.  While more compact and in some ways simpler than another Apple Wi-Fi base station, the AirPort Extreme, the Express offers audio output capability the Extreme lacks.  The AirPort Express was the first AirTunes (now called AirPlay) device to receive streamed audio from a computer running iTunes on the local network.\n\nWestinghouse Time Capsules: The Westinghouse Time Capsules are two time capsules prepared by the Westinghouse Electric & Manufacturing Company: \"Time Capsule I\" was created for the 1939 New York World's Fair and \"Time Capsule II\" was created for the 1964 New York World's Fair.  Both are buried 50 feet below Flushing Meadows–Corona Park, the site of both world's fairs; the 1965 capsule was placed ten feet north of the 1939 capsule.  The capsules are to be opened at the same time in the year 6939, five thousand years after the first capsule was sealed.\n\nA Message from Earth: A Message from Earth (AMFE) is a high-powered digital radio signal that was sent on 9 October 2008 towards Gliese 581c, a large terrestrial extrasolar planet orbiting within the Gliese 581 system.  The signal is a digital time capsule containing 501 messages that were selected through a competition on the social networking site Bebo.  The message was sent using the RT-70 radar telescope of Ukraine's State Space Agency.  The signal will reach the planet Gliese 581c in early 2029.  More than half a million people including celebrities and politicians participated in the AMFE project, which was the world's first digital time capsule where the content was selected by the public.\n\nInternational Time Capsule Society: The International Time Capsule Society (ITCS), based at Oglethorpe University in Atlanta, Georgia, is an organization established to promote the study of time capsules.  Since 1990, it has been documenting all types of time capsule projects worldwide.  In October 2016 its website reported that it is no longer active but continues to register time capsules.\n\nTime Capsule (Macau): Time Capsule (Portuguese: \"Cápsula do Tempo\" , ) is a time capsule that symbolizes the Portuguese government's witnessing and acknowledgement of China's promise to maintain Macau's level of autonomy for fifty years after the transfer of sovereignty.  The Time Capsule was closed and covered on 18 December 1999 and it is scheduled to be opened in 2049.  Currently, the Time Capsule is located in the Praça do Centro Cultural de Macau, which was the venue for the transference of sovereignty ceremony.\n\nYahoo! Time Capsule: The Yahoo! Time Capsule, a brainchild of Jonathan Harris, is a time capsule project by Yahoo! Inc. where users could contribute to a \"digital legacy\" of how life was in 2006.  The Time Capsule was originally intended to be beamed with a laser into space from a Mexican pyramid in an attempt to communicate with extraterrestrial life.  Open to contributions from October 10, 2006 to November 8, 2006, the Time Capsule also hoped to capture the thoughts and feelings of the world in 2006 as an exercise in electronic or \"digital anthropology\".  At the time of the closing of the capsule, the total number of submissions was 170,857.  The highest number of contributions, (32,910) came from the 20-29 age group.\n\nLove and Glory: Love and Glory (ISBN  ) is a 1983 novel by Robert B. Parker.  The story is told in the first person by Boone Adams.  It is a coming-of-age and love story.  There is explicit and implicit reference to and imitation of \"The Great Gatsby\".  Parker originally intended a combination novel and time capsule.  The time capsule sections, inter-chapter devices with baseball box scores, old ad copy, captions from LIFE magazine and popular song lyrics, were ultimately scrapped due to excessive permission fees.\n\nSamuel Adams and Paul Revere time capsule: The Samuel Adams and Paul Revere Time Capsule is a time capsule located in a cornerstone of the Massachusetts State House.  It is believed to have been buried in 1795 by then-Governor Samuel Adams and Paul Revere.  It is the oldest known time capsule in the United States.\n\nAirPort Time Capsule: The AirPort Time Capsule (previously known as just Time Capsule) is a wireless router sold by Apple Inc., featuring network-attached storage (NAS) and a residential gateway router, and is one of Apple's AirPort products.  They are, essentially, versions of the AirPort Extreme with an internal hard drive.  Apple describes it as a \"Backup Appliance\", designed to work in tandem with the Time Machine backup software utility introduced in Mac OS X 10.5.\n\nQuestion: What additional feature does the AirPort Time Capsule have over the Airport Extreme in the Apple network product line-up?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"product_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the product being described.\"\n    },\n    \"compared_product_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the product it is being compared against.\"\n    },\n    \"additional_feature\": {\n      \"type\": \"string\",\n      \"description\": \"The specific feature the product has that the compared product lacks.\"\n    },\n    \"feature_category\": {\n      \"type\": \"string\",\n      \"description\": \"The category of the additional feature (e.g., storage, audio).\"\n    },\n    \"manufacturer\": {\n      \"type\": \"string\",\n      \"description\": \"The manufacturer of the products.\"\n    }\n  },\n  \"required\": [\n    \"product_name\",\n    \"compared_product_name\",\n    \"additional_feature\",\n    \"feature_category\",\n    \"manufacturer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "product_name": {
        "type": "string",
        "description": "The name of the product being described."
      },
      "compared_product_name": {
        "type": "string",
        "description": "The name of the product it is being compared against."
      },
      "additional_feature": {
        "type": "string",
        "description": "The specific feature the product has that the compared product lacks."
      },
      "feature_category": {
        "type": "string",
        "description": "The category of the additional feature (e.g., storage, audio)."
      },
      "manufacturer": {
        "type": "string",
        "description": "The manufacturer of the products."
      }
    },
    "required": [
      "product_name",
      "compared_product_name",
      "additional_feature",
      "feature_category",
      "manufacturer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
