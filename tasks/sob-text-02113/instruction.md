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
Borzoi: The Borzoi ( , literally "fast"), also called the Russian wolfhound (Russian: Ру́сская псовая борзая ), is a breed of domestic dog ("Canis lupus familiaris").  Descended from dogs brought to Russia from central Asian countries, it is similar in shape to a greyhound, and is also a member of the sighthound family.

Texas Heeler: The Texas Heeler is a crossbred herding dog found mainly in Texas.  They are a cross between the Australian Cattle Dog, and the Australian Shepherd, but can be a cross between the ACD and the Border Collie.  They are bred mainly for their ability to work cattle.  Found mainly on ranches in the past, they are currently being enjoyed in dog sports such as agility, frisbee and Rally Obedience.

Entlebucher Mountain Dog: The Entlebucher Sennenhund or Entlebucher Mountain Dog is a medium-sized herding dog, it is the smallest of the four Sennenhunds, a dog type that includes four regional breeds.  The name Sennenhund refers to people called "Senn", herders in the Swiss Alps.  Entlebuch is a region in the canton of Lucerne in Switzerland.  The breed is also known in English as the Entelbuch Mountain Dog, Entelbucher Cattle Dog, and similar combinations.

Tail wagging by dogs: Tail wagging by dogs is the behavior of the dog observed as its tail moves back and forth in the same plane.  It is considered a social signal.  Tail wagging by dogs can be described by its vigorous movement or even just the slightest movement of the tip of its tail.  Other dogs wag their tail in a circular motion, and even when the tail is between their legs or the dog is on its back.  The behavior of a dog can not always be an indication its friendliness.  When a dog wags its tail, most people interpret this as the dog expressing happiness and friendliness.  Though indeed tail wagging can express these positive emotions, tail wagging is also an indication of fear, insecurity, challenging of dominance, establishing social relationships or a warning that the dog may bite.

Holodactylus africanus: Holodactylus africanus is a species of gecko that is commonly found in Eastern Africa.  The gecko has a big head, thin body, stumpy tail, and has tan and brown bands.  The adults are 3 and a half to four inches long.

Australian Cattle Dog: The Australian Cattle Dog (ACD), or simply Cattle Dog, is a breed of herding dog originally developed in Australia for droving cattle over long distances across rough terrain.  This breed is a medium-sized, short-coated dog that occurs in two main colour forms.  It has either brown or black hair distributed fairly evenly through a white coat, which gives the appearance of a "red" or "blue" dog.  It should not be confused with the Australian Shepherd, a similarly named but totally different breed.

Cão Fila de São Miguel: The Cão Fila de São Miguel (Portuguese: ] ) (frequently translated into English as the "São Miguel Cattle Dog" or "Cattle Dog of São Miguel Island", but other names, such as "Azores Cattle Dog", may be used) is a dog breed of molosser type originating on São Miguel Island in the Azores, an island chain which is one of the autonomous regions of Portugal.  The breed was originally used for working with cattle.

Halls Heeler: The Halls Heeler was a dog bred by Thomas Simpson Hall to herd cattle on the Hall family's extensive properties in north-western New South Wales in the 19th century.  On "Dartbrook Station", in the Upper Hunter Valley, Hall selectively crossed the offspring of Northumberland Drover's Dogs (Border Collie lineage) that he had imported, with progeny of dingoes that he had tamed.  By 1840 he had bred the type of dog that he needed to control cattle on the massive runs that his family owned, and until he died in 1870 few of these dogs were owned and used by anyone outside the Hall family and their workers.  However the death of Thomas Hall and the break-up of the Hall estate coincided with the development of the dog show, and an interest in breeding dogs to specific criteria or standards.  The Halls Heeler was further developed into two contemporary dog breeds the Australian Cattle Dog and the Australian Stumpy Tail Cattle Dog.  The name is spelled both with the possessive apostrophe, as Hall's Heeler, and without.

Argulus japonicus: Argulus japonicus, common name Japanese fishlouse or Japanese fish louse, is a species of crustacean in the family Argulidae, the fish lice.  This species is light brown in colour and may be between 4 and 9 mm long and 3 to 6 mm wide.  It has a stumpy tail, and is shaped somewhat like a round shield.

Australian Stumpy Tail Cattle Dog: The Australian Stumpy Tail Cattle Dog is a naturally bobtailed or tailless, medium-sized breed of Cattle Dog (not to be confused with the Australian Cattle Dog, aka "Queensland Heeler").  The Australian Stumpy Tail Cattle Dog was developed in Australia to herd cattle, and descends from crosses between European herding dogs and the Australian dingo.  The name is spelled both with hyphenation, as Australian Stumpy-Tail Cattle Dog, and without, and the shorter name Stump Tail Cattle Dog is also sometimes applied.

Question: Is the Australian Stumpy Tail Cattle Dog or the Borzoi most similar to a greyhound in appearance?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_subject_1": {
      "type": "object",
      "properties": {
        "breed_name": {
          "type": "string",
          "description": "The name of the first dog breed being compared."
        },
        "description_keywords": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key descriptive terms for the breed from the context."
        },
        "is_similar_to_greyhound": {
          "type": "boolean",
          "description": "Indicates if the context states this breed is similar to a greyhound."
        }
      },
      "required": [
        "breed_name",
        "description_keywords",
        "is_similar_to_greyhound"
      ],
      "additionalProperties": false
    },
    "comparison_subject_2": {
      "type": "object",
      "properties": {
        "breed_name": {
          "type": "string",
          "description": "The name of the second dog breed being compared."
        },
        "description_keywords": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key descriptive terms for the breed from the context."
        },
        "is_similar_to_greyhound": {
          "type": "boolean",
          "description": "Indicates if the context states this breed is similar to a greyhound."
        }
      },
      "required": [
        "breed_name",
        "description_keywords",
        "is_similar_to_greyhound"
      ],
      "additionalProperties": false
    },
    "most_similar_breed": {
      "type": "string",
      "description": "The name of the breed that is most similar to a greyhound based on the context."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why the chosen breed is most similar."
    }
  },
  "required": [
    "comparison_subject_1",
    "comparison_subject_2",
    "most_similar_breed",
    "reasoning"
  ],
  "additionalProperties": false
}
